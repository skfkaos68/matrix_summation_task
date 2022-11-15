from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

EXTENSION_APPS = [
    # 'minimum',
    # 'auctionone',
    'realefforttask',
    # 'double_auction'
]

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    # {
    #     'name': 'minimum_ret',
    #     'display_name': 'Simple RET example',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['minimum'],
    #
    # },
    {
        'name': 'realefforttask',
        'display_name': 'Real Effort Task - 2 matrices',
        'num_demo_participants': 1,
        'app_sequence': ['realefforttask'],
        'task': 'TwoMatrices',
        'task_params': {'difficulty': 5},
    },
    # {
    #     'name': 'realefforttask2',
    #     'display_name': 'Real Effort Task - sum of N numbers',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['realefforttask'],
    #     'task': 'SumNumbers',
    #     'task_params': {'num_digits': 4,
    #                     'digits_range': [50, 99]},
    # },
    #
    # {
    #     'name': 'realefforttask3',
    #     'display_name': 'Real Effort Task - count 0s',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['realefforttask'],
    #     'task': 'CountZeroes',
    #     'task_params': {'num_rows': 5,
    #                     'num_columns': 10,
    #                     # 'value_to_count': 1,
    #                     # 'selection_set': [0, 1, 2],
    #                     },
    # },
    {
        'name': 'realefforttask4',
        'display_name': 'Real Effort Task - Decoding',
        'num_demo_participants': 1,
        'app_sequence': ['realefforttask'],
        'task': 'Decoding',
        'task_params': {'dict_length': 10, 'task_len': 5},
    },
    # {
    #     'name': 'auctionone',
    #     'display_name': 'One sided auction and RET',
    #     'num_demo_participants': 3,
    #     'app_sequence': ['auctionone'],
    #
    # },
    # {
    #     'name': 'double_auction',
    #     'display_name': 'Double auction',
    #     'num_demo_participants': 3,
    #     'app_sequence': ['double_auction'],
    #     'num_sellers': 1,
    #     'num_buyers': 2,
    #     'units_per_seller': 4,
    #     'units_per_buyer': 4,
    #     'time_per_round': 300,
    #     'multiple_unit_trading': False,
    #     'seller_cost_lb': 1,
    #     'seller_cost_ub': 10,
    #     'buyer_value_lb': 1,
    #     'buyer_value_ub': 10,
    #     'endowment_lb': 10,
    #     'endowment_ub': 50,
    # },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '%&w(ic-c^8avzg9833mspr)3uyvm5p9ce4y%iv$n@6@d9f9b-u'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
