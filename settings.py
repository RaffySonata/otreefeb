from os import environ


SESSION_CONFIGS = [
    dict(
        name="task_math",
        display_name="Math",
        num_demo_participants=1,
        app_sequence=["task_math"],
    ),
    dict(
        name="task_math2",
        display_name="Math 2 players",
        num_demo_participants=12,
        app_sequence=["task_math2"],
    ),
    dict(
        name="task_math4",
        display_name="Math 4 players",
        num_demo_participants=4,
        app_sequence=["task_math4"],
    ),
    dict(
        name="real_effort",
        display_name="Decoding",
        num_demo_participants=1,
        app_sequence=["real_effort"],
    ),
    dict(
        name="real_effort2",
        display_name="Decoding 2 Players",
        num_demo_participants=4,
        app_sequence=["real_effort2"],
    ),
    dict(
        name="real_effort4",
        display_name="Decoding 4 Players",
        num_demo_participants=4,
        app_sequence=["real_effort4"],
    ),
    dict(
        name="random",
        display_name="random",
        num_demo_participants=1,
        app_sequence=["token_random"],
    ),
    dict(
        name="pay_random",
        display_name="pay_random",
        num_demo_participants=1,
        app_sequence=["task_math", "real_effort", "token_random"],
    ),
    dict(
        name="Collective_Action",
        display_name="Collective_Action",
        num_demo_participants=4,
        app_sequence=["survey", "task_math", "real_effort", "task_math2", "real_effort2", "task_math4", "real_effort4", "token_random"],
    ),
    dict(
        name="Collective_Action_No_Phone",
        display_name="Collective_Action_No_Phone",
        num_demo_participants=1,
        app_sequence=["detect_mobile", "survey", "task_math", "real_effort", "token_random"],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']
ROOMS = [
    dict(
        name='Pilot_Experiment',
        display_name='Pilot_Experiment',
        participant_label_file='_rooms/econ101.txt',
        use_secure_urls=False
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['is_dropout',
                      'app_payoffs',
                      'expiry',
                      'finished_rounds',
                      'language',
                      'num_rounds',
                      'partner_history',
                      'past_group_id',
                      'progress',
                      'quiz_num_correct',
                      'selected_round',
                      'task_rounds',
                      'time_pressure',
                      'wait_page_arrival',
                      ]
SESSION_FIELDS = ['params',
                  'completions_by_treatment',
                  'past_groups',
                  'matrices',
                  'wait_for_ids',
                  'arrived_ids',
                  ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "Rp"
USE_POINTS = True

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_TITLE = "Real-effort tasks"
DEMO_PAGE_INTRO_HTML = """
Real-effort tasks (transcription, decoding, matrix, sliders, etc) 
"""

SECRET_KEY = "2015765205890"

# adjustments for testing
# generating session configs for all varieties of features
import sys


if sys.argv[1] == 'test':
    MAX_ITERATIONS = 10
    FREEZE_TIME = 0.1
    TRIAL_PAUSE = 0.2
    TRIAL_TIMEOUT = 0.3

    SESSION_CONFIGS = [
        dict(
            name=f"testing_sliders",
            num_demo_participants=1,
            app_sequence=['sliders'],
            trial_delay=TRIAL_PAUSE,
            retry_delay=FREEZE_TIME,
            num_sliders=3,
            attempts_per_slider=3,
        ),
    ]
    for task in ['decoding', 'matrix', 'transcription', 'task_math']:
        SESSION_CONFIGS.extend(
            [
                dict(
                    name=f"testing_{task}_defaults",
                    num_demo_participants=1,
                    app_sequence=['real_effort'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                ),
                dict(
                    name=f"testing_{task}_retrying",
                    num_demo_participants=1,
                    app_sequence=['real_effort'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    attempts_per_puzzle=MAX_ITERATIONS,
                ),
                dict(
                    name=f"testing_{task}_limited",
                    num_demo_participants=1,
                    app_sequence=['real_effort'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    max_iterations=MAX_ITERATIONS,
                ),
            ]
        )
