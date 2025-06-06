import argparse
import json
from datetime import datetime

from src.event import TypeEvent, Event


class Run:
    input_file: str
    output_file: str
    list_event: list = []

    @classmethod
    def read_file(cls, file_name):
        with open(file_name, "r", encoding="utf8") as f:
            cls.list_event = [Event(date=i["date"],
                                    title=i["title"],
                                    type_event=TypeEvent(i["type_event"]),
                                    participants=i["participants"],
                                    place=i["place"]) for i in json.load(f)]
            return cls.list_event

    @staticmethod
    def group_data(list_event: list[Event]) -> dict:
        temp = {}
        for item in [i for i in list_event if i.type_event != TypeEvent.OTHER]:
            temp.setdefault(
                datetime.fromisoformat(item.date).date().isoformat(),
                []).append(item)
        for k in temp.keys():
            temp.get(k).sort(
                key=lambda event: datetime.fromisoformat(event.date))
        return temp

    @classmethod
    def write_file(cls, file_name, dict_events):
        with open(file_name, "w", encoding="utf8") as f:
            json.dump(
                {
                    key: [i.__dict__ for i in i_list]
                    for key, i_list in dict_events.items()
                },
                f, indent=2, default=str)

    @classmethod
    def parse_param(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-if', '--input_file',
            type=str,
            help='Путь до входного json файла',
            default='src/events.json')

        parser.add_argument(
            '-of', '--output_file',
            type=str,
            help='Путь до json файла для записи в него результата',
            default='src/output.json')
        args = parser.parse_args()
        cls.input_file = args.input_file
        cls.output_file = args.output_file

    @classmethod
    def run(cls):
        cls.parse_param()
        cls.read_file(cls.input_file)
        cls.write_file(cls.output_file, cls.group_data(cls.list_event))
