import time

from otree import settings
from otree.api import *

from .image_utils import encode_image

doc = """
Real-effort tasks. The different tasks are available in task_matrix.py, task_transcription.py, etc.
You can delete the ones you don't need. 
"""


def get_task_module(player):
    """
    This function is only needed for demo mode, to demonstrate all the different versions.
    You can simplify it if you want.
    """
    from . import task_matrix, task_transcription, task_decoding, task_math

    session = player.session
    task = session.config.get("task")
    if task == "matrix":
        return task_matrix
    if task == "transcription":
        return task_transcription
    if task == "decoding":
        return task_decoding
    if task == "math":
        return task_math
    # default
    return task_math


class Constants(BaseConstants):
    name_in_url = "Math2"
    players_per_group = 2
    num_rounds = 1

    instructions_template = __name__ + "/instructions.html"
    captcha_length = 3


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        # initialize an empty dict to store how much they made in each app
        p.participant.app_payoffs = {}
    session = subsession.session
    session.past_groups = []
    template = dict(
        retry_delay=1.0, puzzle_delay=0, attempts_per_puzzle=1, max_iterations=None, max_math=10, max_math2=20, max_math4=40, max_decoding=5, max_decoding2=10, max_decoding4=20,
    )
    session.params = {}
    for param in template:
        session.params[param] = session.config.get(param, template[param])

def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session

    import itertools

    # this generates all possible pairs of waiting players
    # and checks if the group would be valid.
    for possible_group in itertools.combinations(waiting_players, 2):
        # use a set, so that we can easily compare even if order is different
        # e.g. {1, 2} == {2, 1}
        pair_ids = set(p.id_in_subsession for p in possible_group)
        # if this pair of players has not already been played
        #if pair_ids not in session.past_groups:
            # mark this group as used, so we don't repeat it in the next round.
            #session.past_groups.append(pair_ids)
            # in this function,
            # 'return' means we are creating a new group with this selected pair
        return possible_group

class Group(BaseGroup):
    num_correct = models.IntegerField(initial=0)


class Player(BasePlayer):
    iteration = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    num_correct = models.IntegerField(initial=0)
    num_failed = models.IntegerField(initial=0)
    num_g_correct = models.IntegerField(initial=0)
    potential_payoff = models.CurrencyField()

# puzzle-specific stuff


class Puzzle(ExtraModel):
    """A model to keep record of all generated puzzles"""

    player = models.Link(Player)
    iteration = models.IntegerField(initial=0)
    attempts = models.IntegerField(initial=0)
    timestamp = models.FloatField(initial=0)
    # can be either simple text, or a json-encoded definition of the puzzle, etc.
    text = models.LongStringField()
    # solution may be the same as text, if it's simply a transcription task
    solution = models.LongStringField()
    response = models.LongStringField()
    response_timestamp = models.FloatField()
    is_correct = models.BooleanField()


def generate_puzzle(player: Player) -> Puzzle:
    """Create new puzzle for a player"""
    task_module = get_task_module(player)
    fields = task_module.generate_puzzle_fields()
    player.iteration += 1
    return Puzzle.create(
        player=player, iteration=player.iteration, timestamp=time.time(), **fields
    )


def get_current_puzzle(player):
    puzzles = Puzzle.filter(player=player, iteration=player.iteration)
    if puzzles:
        [puzzle] = puzzles
        return puzzle


def encode_puzzle(puzzle: Puzzle):
    """Create data describing puzzle to send to client"""
    task_module = get_task_module(puzzle.player)  # noqa
    # generate image for the puzzle
    image = task_module.render_image(puzzle)
    data = encode_image(image)
    return dict(image=data)


def get_progress(player: Player):
    """Return current player progress"""
    return dict(
        num_trials=player.num_trials,
        num_correct=player.num_correct,
        num_incorrect=player.num_failed,
        group_correct=player.num_g_correct,
        iteration=player.iteration,
    )


def play_game(player: Player, message: dict):
    """Main game workflow
    Implemented as reactive scheme: receive message from vrowser, react, respond.

    Generic game workflow, from server point of view:
    - receive: {'type': 'load'} -- empty message means page loaded
    - check if it's game start or page refresh midgame
    - respond: {'type': 'status', 'progress': ...}
    - respond: {'type': 'status', 'progress': ..., 'puzzle': data} -- in case of midgame page reload

    - receive: {'type': 'next'} -- request for a next/first puzzle
    - generate new puzzle
    - respond: {'type': 'puzzle', 'puzzle': data}

    - receive: {'type': 'answer', 'answer': ...} -- user answered the puzzle
    - check if the answer is correct
    - respond: {'type': 'feedback', 'is_correct': true|false, 'retries_left': ...} -- feedback to the answer

    If allowed by config `attempts_pre_puzzle`, client can send more 'answer' messages
    When done solving, client should explicitely request next puzzle by sending 'next' message

    Field 'progress' is added to all server responses to indicate it on page.

    To indicate max_iteration exhausted in response to 'next' server returns 'status' message with iterations_left=0
    """
    session = player.session
    my_id = player.id_in_group
    params = session.params
    task_module = get_task_module(player)

    now = time.time()
    # the current puzzle or none
    current = get_current_puzzle(player)

    message_type = message['type']

    # page loaded
    if message_type == 'load':
        p = get_progress(player)
        if current:
            return {
                my_id: dict(type='status', progress=p, puzzle=encode_puzzle(current))
            }
        else:
            return {my_id: dict(type='status', progress=p)}

    if message_type == "cheat" and settings.DEBUG:
        return {my_id: dict(type='solution', solution=current.solution)}

    # client requested new puzzle
    if message_type == "next":
        if current is not None:
            if current.response is None:
                raise RuntimeError("trying to skip over unsolved puzzle")
            if now < current.timestamp + params["puzzle_delay"]:
                raise RuntimeError("retrying too fast")
            if player.num_g_correct == params['max_math2'] or player.num_g_correct == params['max_math2'] + 1:
                return {
                    my_id: dict(
                        type='status', progress=get_progress(player), iterations_left=0
                    )
                }
        # generate new puzzle
        z = generate_puzzle(player)
        p = get_progress(player)
        return {my_id: dict(type='puzzle', puzzle=encode_puzzle(z), progress=p)}

    # client gives an answer to current puzzle
    if message_type == "answer":
        if current is None:
            raise RuntimeError("trying to answer no puzzle")

        if current.response is not None:  # it's a retry
            if current.attempts >= params["attempts_per_puzzle"]:
                raise RuntimeError("no more attempts allowed")
            if now < current.response_timestamp + params["retry_delay"]:
                raise RuntimeError("retrying too fast")

            # undo last updation of player progress
            player.num_trials -= 1
            if current.is_correct:
                player.num_correct -= 1
            else:
                player.num_failed -= 1

        # check answer
        answer = message["answer"]

        if answer == "" or answer is None:
            raise ValueError("bogus answer")

        current.response = answer
        current.is_correct = task_module.is_correct(answer, current)
        current.response_timestamp = now
        current.attempts += 1

        # update player progress
        if current.is_correct:
            player.num_correct += 1
        else:
            player.num_failed += 1
        player.num_trials += 1
        group = player.group
        players = group.get_players()
        player.num_g_correct = sum([p.num_correct for p in players])


        retries_left = params["attempts_per_puzzle"] - current.attempts
        p = get_progress(player)
        return {
            my_id: dict(
                type='feedback',
                is_correct=current.is_correct,
                retries_left=retries_left,
                progress=p,
            )
        }

    raise RuntimeError("unrecognized message from client")



class Game(Page):
    timeout_seconds = 60

    live_method = play_game

    @staticmethod
    def js_vars(player: Player):
        return dict(params=player.session.params)

    @staticmethod
    def vars_for_template(player: Player):
        task_module = get_task_module(player)
        return dict(DEBUG=settings.DEBUG,
                    input_type=task_module.INPUT_TYPE,
                    placeholder=task_module.INPUT_HINT,
                    partner=player.get_others_in_group()[0])
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        # if it's the last round
        if player.round_number == Constants.num_rounds:
            random_round = random.randint(1, Constants.num_rounds)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            if player_in_selected_round.num_g_correct > 19:
                player.potential_payoff = 12.5
            else:
                player.potential_payoff = 0
            potential_payoff = player.potential_payoff
            # __name__ is a magic variable that contains the name of the current app
            participant.app_payoffs[__name__] = potential_payoff

class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        players = group.get_players()
        group.num_correct = sum([p.num_correct for p in players])

class WaitPage1(WaitPage):
    group_by_arrival_time = True
    body_text = "Harap menunggu pasangan main Anda"

class Results(Page):
    pass


page_sequence = [WaitPage1, Game, ResultsWaitPage, Results]
