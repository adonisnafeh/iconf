"""
Django settings files used for testing purposes
"""

import iconf

config = iconf.get(["SECRET_KEY"], path='iconf/tests/configs.json')
DJANGO_SETTINGS_VAR1 = "DJANGO_SETTINGS_VAR1"
DJANGO_SETTINGS_VAR2 = "DJANGO_SETTINGS_VAR2"
SECRET_KEY = config['SECRET_KEY']
