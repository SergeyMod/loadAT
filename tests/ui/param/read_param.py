import json


class ReadParam:
    @staticmethod
    def get_param():
        with open('tests/ui/param/param.json', 'r', encoding='utf8') as f:
            return [(i['file_name'],
                     i['country'],
                     i['genre'])
                    for i in json.load(f)]
