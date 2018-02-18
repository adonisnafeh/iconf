import unittest
import os
import pip
import appconf

ENVIRONMENT_VAR1 = 'ENVIRONMENT_VAR1'
ENVIRONMENT_VAR2 = 'ENVIRONMENT_VAR2'
JSON_VAR1 = 'JSON_VAR1'
JSON_VAR2 = 'JSON_VAR2'
DJANGO_SETTINGS_VAR1 = 'DJANGO_SETTINGS_VAR1'
DJANGO_SETTINGS_VAR2 = 'DJANGO_SETTINGS_VAR2'
CONFIGS_PATH = 'appconf/tests/configs.json'
DJANGO_SETTINGS_PATH = 'appconf.tests.settings'


class AppConfTest(unittest.TestCase):
    def test_environment_conf(self):
        """get variables from environment variables"""
        os.environ['ENVIRONMENT_VAR1'] = ENVIRONMENT_VAR1
        os.environ['ENVIRONMENT_VAR2'] = ENVIRONMENT_VAR2

        configs = appconf.get(['ENVIRONMENT_VAR1',
                               'ENVIRONMENT_VAR2',
                               'MISSING_VARIABLE'])

        self.assertEqual(configs['ENVIRONMENT_VAR1'],
                         os.environ['ENVIRONMENT_VAR1'])
        self.assertEqual(configs['ENVIRONMENT_VAR2'],
                         os.environ['ENVIRONMENT_VAR2'])
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def test_json_partial_conf(self):
        """get keys from json file"""
        configs = appconf.get(['JSON_VAR1',
                               'JSON_VAR2',
                               'MISSING_VARIABLE'], CONFIGS_PATH)

        self.assertEqual(configs['JSON_VAR1'], JSON_VAR1)
        self.assertEqual(configs['JSON_VAR2'], JSON_VAR2)
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def test_json_full_conf(self):
        """get all keys from json file"""
        configs = appconf.get(path=CONFIGS_PATH)

        self.assertEqual(configs['JSON_VAR1'], JSON_VAR1)
        self.assertEqual(configs['JSON_VAR2'], JSON_VAR2)

    def test_environment_json_conf(self):
        """get settings from environment variables and/or json file"""
        os.environ['ENVIRONMENT_VAR1'] = ENVIRONMENT_VAR1

        configs = appconf.get(['JSON_VAR1',
                               'JSON_VAR2',
                               'ENVIRONMENT_VAR1',
                               'MISSING_VARIABLE'], CONFIGS_PATH)

        self.assertEqual(configs['JSON_VAR1'], JSON_VAR1)
        self.assertEqual(configs['JSON_VAR2'], JSON_VAR2)
        self.assertEqual(configs['ENVIRONMENT_VAR1'],
                         os.environ['ENVIRONMENT_VAR1'])
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def test_environment_missing_json_conf(self):
        """get settings from environment variables and/or json file"""
        os.environ['ENVIRONMENT_VAR1'] = ENVIRONMENT_VAR1

        configs = appconf.get(['JSON_VAR1',
                               'ENVIRONMENT_VAR1',
                               'MISSING_VARIABLE'], 'missing_file.json')

        self.assertEqual(configs['JSON_VAR1'], None)
        self.assertEqual(configs['ENVIRONMENT_VAR1'],
                         os.environ['ENVIRONMENT_VAR1'])
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def test_bad_parameters(self):
        with self.assertRaises(Exception):
            appconf.get()
        with self.assertRaises(Exception):
            appconf.get('test')


class DjangoAppConfTest(unittest.TestCase):
    def test_environment_django_conf(self):
        """
        get variables from environment variables and/or django settings
        """
        pip.main(['install', 'django==1.8'])

        os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_PATH
        os.environ['ENVIRONMENT_VAR1'] = ENVIRONMENT_VAR1

        configs = appconf.get(['ENVIRONMENT_VAR1',
                               'DJANGO_SETTINGS_VAR1',
                               'DJANGO_SETTINGS_VAR2',
                               'MISSING_VARIABLE'])

        self.assertEqual(configs['ENVIRONMENT_VAR1'], ENVIRONMENT_VAR1)
        self.assertEqual(configs['DJANGO_SETTINGS_VAR1'], DJANGO_SETTINGS_VAR1)
        self.assertEqual(configs['DJANGO_SETTINGS_VAR2'], DJANGO_SETTINGS_VAR2)
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def test_environment_json_django_conf(self):
        """
        get variables from environment variables and/or json files
        and/or django settings
        """
        pip.main(['install', 'django==1.8'])

        os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_PATH
        os.environ['ENVIRONMENT_VAR1'] = ENVIRONMENT_VAR1
        os.environ['ENVIRONMENT_VAR2'] = ENVIRONMENT_VAR2

        configs = appconf.get(['ENVIRONMENT_VAR1',
                               'ENVIRONMENT_VAR2',
                               'DJANGO_SETTINGS_VAR1',
                               'DJANGO_SETTINGS_VAR2',
                               'JSON_VAR1',
                               'JSON_VAR2',
                               'MISSING_VARIABLE'], CONFIGS_PATH)

        self.assertEqual(configs['ENVIRONMENT_VAR1'], ENVIRONMENT_VAR1)
        self.assertEqual(configs['ENVIRONMENT_VAR2'], ENVIRONMENT_VAR2)
        self.assertEqual(configs['DJANGO_SETTINGS_VAR1'], DJANGO_SETTINGS_VAR1)
        self.assertEqual(configs['DJANGO_SETTINGS_VAR2'], DJANGO_SETTINGS_VAR2)
        self.assertEqual(configs['JSON_VAR1'], JSON_VAR1)
        self.assertEqual(configs['JSON_VAR2'], JSON_VAR2)
        self.assertEqual(configs['MISSING_VARIABLE'], None)

    def tearDown(self):
        pip.main(['uninstall', 'django', '-y'])
