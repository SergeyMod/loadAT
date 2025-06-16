import json


class ReadSettings:
    @staticmethod
    def get_settings():
        with open('conf/settings.json', 'r', encoding='utf8') as f:
            return json.load(f)
