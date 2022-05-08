from os import environ

SESSION_CONFIGS = [
     dict(
         name='real_effort_numbers',
         app_sequence=['real_effort_numbers'],
         num_demo_participants=1,
     ),
    dict(
         name='count_words',
         app_sequence=['count_words'],
         num_demo_participants=1,
     ),
    dict(
         name='Collective_Action_Test',
         app_sequence=['survey', 'real_effort_numbers', 'count_words'],
         num_demo_participants=1,
     ),
    dict(
        name='Welcome',
        app_sequence=['survey'],
        num_demo_participants=1,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3170777934544'
