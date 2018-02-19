import json
import os


def get(keys=None, path=None):
    if not keys and not path:
        raise Exception("please set the keys or path argument")

    if keys and not isinstance(keys, list):
        raise Exception("keys argument must be a list")

    json_data = {}
    if path:
        try:
            with open(path, 'r') as f:
                json_data = json.load(f)
        except IOError:
            pass

    if json_data and not keys:
        return json_data

    configs = {key: None for key in keys}

    try:
        from django.conf import settings as dj_settings
    except ImportError:
        dj_settings = None

    for key in keys:
        if key in os.environ:
            configs.update({key: os.environ[key]})
        elif key in json_data:
            configs.update({key: json_data[key]})
        elif dj_settings and hasattr(dj_settings, key):
            configs.update({key: getattr(dj_settings, key)})

    return configs
