from otree.api import *


doc = """
App where we choose the app to be paid
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_app3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    app_to_pay1 = models.StringField()
    app_to_pay2 = models.StringField()
    app_to_pay3 = models.StringField()
    konfirmasi_token = models.IntegerField()
    payoff1 = models.FloatField(initial=0)
    payoff2 = models.FloatField(initial=0)
    payoff3 = models.FloatField(initial=0)
    convert = models.FloatField(initial=0)
    convert2 = models.FloatField(initial=0)
    convert3 = models.FloatField(initial=0)
    convert4 = models.FloatField(initial=0)

# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["konfirmasi_token"]

class PayRandomApp(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        # print('participant.app_payoffs is', participant.app_payoffs)

        apps = [
            'task_math',
            'real_effort',
        ]
        app_to_pay1 = random.choice(apps)
        player.payoff1 = participant.app_payoffs[app_to_pay1]
        if app_to_pay1 == 'task_math':
            player.app_to_pay1 = 'operasi angka'
        else:
            player.app_to_pay1 = 'penguraian kode'
        player.convert = player.payoff1 * 1500

        apps2 = [
            'task_math2',
            'real_effort2',
        ]
        app_to_pay2 = random.choice(apps2)
        player.payoff2 = participant.app_payoffs[app_to_pay2]
        if app_to_pay2 == 'task_math2':
            player.app_to_pay2 = 'operasi angka'
        else:
            player.app_to_pay2 = 'penguraian kode'
        player.convert2 = player.payoff2 * 1500

        apps3 = [
            'task_math4',
            'real_effort4',
        ]
        app_to_pay3 = random.choice(apps3)
        player.payoff3 = participant.app_payoffs[app_to_pay3]
        if app_to_pay3 == 'task_math4':
            player.app_to_pay3 = 'operasi angka'
        else:
            player.app_to_pay3 = 'penguraian kode'
        player.convert3 = player.payoff3 * 1500
        participant.payoff = player.payoff1 + player.payoff2 + player.payoff3
        player.convert4 = participant.payoff * 1500 + 10000



class Results(Page):
    pass


page_sequence = [PayRandomApp, Results]
