from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'multiply_app'
    players_per_group = None
    num_rounds = 1
    factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    konfirmasi_token = models.FloatField()


# PAGES
class MyPage(Page):
    form_model = "player"
    form_fields = ["konfirmasi_token"]

page_sequence = [MyPage]
