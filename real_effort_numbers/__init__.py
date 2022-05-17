import random
import time

from otree.api import *


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_numbers'
    players_per_group = None
    num_rounds = 10
    payment_per_round = 1


class Player(BasePlayer):
    number_entered1 = models.FloatField()
    sum_of_of_numbers1 = models.FloatField()

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

# FUNCTIONS
# PAGES
class AddNumbers(Page):
        timeout_seconds = 60
        form_model = "player"
        form_fields = ["number_entered1"]

        @staticmethod
        def vars_for_template(player: Player):
            number1 = random.randint(1, 9)
            number2 = random.randint(1, 9)
            number3 = random.randint(1, 9)
            type = random.randint(0, 7)

            if type == 0:
                player.sum_of_of_numbers1 = round((number1 * number2 + number3), 2)
                question = "{} * {} + {}".format(number1, number2, number3)
            elif type == 1:
                player.sum_of_of_numbers1 = round((number1 * number2 - number3), 2)
                question = "{} * {} - {}".format(number1, number2, number3)
            elif type == 2:
                player.sum_of_of_numbers1 = round((number1 + number2 * number3), 2)
                question = "{} + {} * {}".format(number1, number2, number3)
            elif type == 3:
                player.sum_of_of_numbers1 = round((number1 - number2 * number3), 2)
                question = "{} - {} * {}".format(number1, number2, number3)
            elif type == 4:
                player.sum_of_of_numbers1 = round((number1 / number2 + number3), 2)
                question = "{} / {} + {}".format(number1, number2, number3)
            elif type == 5:
                player.sum_of_of_numbers1 = round((number1 / number2 - number3), 2)
                question = "{} / {} - {}".format(number1, number2, number3)
            elif type == 6:
                player.sum_of_of_numbers1 = round((number1 + number2 / number3), 2)
                question = "{} + {} / {}".format(number1, number2, number3)
            elif type == 7:
                player.sum_of_of_numbers1 = round((number1 - number2 / number3), 2)
                question = "{} - {} / {}".format(number1, number2, number3)
            return {
                "number1": number1,
                "number2": number2,
                "number3": number3,
                "question": question,
            }

        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            if player.sum_of_of_numbers1 == player.number_entered1:
                player.payoff = Constants.payment_per_round

class Results(Page):
    pass


class CombinedResults(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds
    @staticmethod
    def vars_for_template(player: Player):
        all_players = player.in_all_rounds()
        combined_payoff = 0
        for player in all_players:
            combined_payoff += player.payoff
        return {"combined_payoff": combined_payoff}


page_sequence = [AddNumbers, Results, CombinedResults]
