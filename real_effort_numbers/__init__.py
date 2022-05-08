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
    num_rounds = 2
    payment_per_round = 10


class Player(BasePlayer):
    number_entered1 = models.FloatField()
    number_entered2 = models.FloatField()
    number_entered3 = models.FloatField()
    number_entered4 = models.FloatField()
    number_entered5 = models.FloatField()
    number_entered6 = models.FloatField()
    number_entered7 = models.FloatField()
    number_entered8 = models.FloatField()
    number_entered9 = models.FloatField()
    number_entered10 = models.FloatField()
    sum_of_of_numbers1 = models.FloatField()
    sum_of_of_numbers2 = models.FloatField()
    sum_of_of_numbers3 = models.FloatField()
    sum_of_of_numbers4 = models.FloatField()
    sum_of_of_numbers5 = models.FloatField()
    sum_of_of_numbers6 = models.FloatField()
    sum_of_of_numbers7 = models.FloatField()
    sum_of_of_numbers8 = models.FloatField()
    sum_of_of_numbers9 = models.FloatField()
    sum_of_of_numbers10 = models.FloatField()



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass




# FUNCTIONS
# PAGES
class AddNumbers(Page):
    timeout_seconds = 60
    form_model = "player"
    form_fields = ["number_entered1", "number_entered2", "number_entered3", "number_entered4", "number_entered5", "number_entered6", "number_entered7", "number_entered8", "number_entered9", "number_entered10"]
    @staticmethod
    def vars_for_template(player: Player):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 9)
        num5 = random.randint(1, 9)
        num6 = random.randint(1, 9)
        num7 = random.randint(1, 9)
        num8 = random.randint(1, 9)
        num9 = random.randint(1, 9)
        num10 = random.randint(1, 9)
        num11 = random.randint(1, 9)
        num12 = random.randint(1, 9)
        num13 = random.randint(1, 9)
        num14 = random.randint(1, 9)
        num15 = random.randint(1, 9)
        num16 = random.randint(1, 9)
        num17 = random.randint(1, 9)
        num18 = random.randint(1, 9)
        num19 = random.randint(1, 9)
        num20 = random.randint(1, 9)
        num21 = random.randint(1, 9)
        num22 = random.randint(1, 9)
        num23 = random.randint(1, 9)
        num24 = random.randint(1, 9)
        num25 = random.randint(1, 9)
        num26 = random.randint(1, 9)
        num27 = random.randint(1, 9)
        num28 = random.randint(1, 9)
        num29 = random.randint(1, 9)
        num30 = random.randint(1, 9)

        player.sum_of_of_numbers1 = round((num1 * num2 + num3), 2)
        player.sum_of_of_numbers2 = round((num4 * num5 - num6), 2)
        player.sum_of_of_numbers3 = round((num7 / num8 + num9), 2)
        player.sum_of_of_numbers4 = round((num10 / num11 - num12), 2)
        player.sum_of_of_numbers5 = round((num13 * num14 + num15), 2)
        player.sum_of_of_numbers6 = round((num16 * num17 - num18), 2)
        player.sum_of_of_numbers7 = round((num19 / num20 + num21), 2)
        player.sum_of_of_numbers8 = round((num22 / num23 - num24), 2)
        player.sum_of_of_numbers9 = round((num25 * num26 + num27), 2)
        player.sum_of_of_numbers10 = round((num28 / num29 + num30), 2)
        return {
            "num1": num1,
            "num2": num2,
            "num3": num3,
            "num4": num4,
            "num5": num5,
            "num6": num6,
            "num7": num7,
            "num8": num8,
            "num9": num9,
            "num10": num10,
            "num11": num11,
            "num12": num12,
            "num13": num13,
            "num14": num14,
            "num15": num15,
            "num16": num16,
            "num17": num17,
            "num18": num18,
            "num19": num19,
            "num20": num20,
            "num21": num21,
            "num22": num22,
            "num23": num23,
            "num24": num24,
            "num25": num25,
            "num26": num26,
            "num27": num27,
            "num28": num28,
            "num29": num29,
            "num30": num30,
        }
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.sum_of_of_numbers1 == player.number_entered1 and player.sum_of_of_numbers2 == player.number_entered2 and player.sum_of_of_numbers3 == player.number_entered3 and player.sum_of_of_numbers4 == player.number_entered4 and player.sum_of_of_numbers5 == player.number_entered5 and player.sum_of_of_numbers6 == player.number_entered6 and player.sum_of_of_numbers7 == player.number_entered7 and player.sum_of_of_numbers8 == player.number_entered8 and player.sum_of_of_numbers9 == player.number_entered9 and player.sum_of_of_numbers10 == player.number_entered10:
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
