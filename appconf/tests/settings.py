"""
Django settings files used for testing purposes
"""

import appconf

config = appconf.get(["SECRET_KEY"], path='appconf/tests/configs.json')
DJANGO_SETTINGS_VAR1 = "DJANGO_SETTINGS_VAR1"
DJANGO_SETTINGS_VAR2 = "DJANGO_SETTINGS_VAR2"
SECRET_KEY = config['SECRET_KEY']
