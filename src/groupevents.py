import json
from datetime import datetime

from src.event import Event
from src.enum.type_event import TypeEvent
from src.parse_param import parse_param


class GroupEvents:

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r", encoding="utf8") as f:
            return [Event(date=i["date"],
                          title=i["title"],
                          type_event=TypeEvent(i["type_event"]),
                          participants=i["participants"],
                          place=i["place"]) for i in json.load(f)]

    @staticmethod
    def sorted_(dict_event: dict[str: list[Event]]):
        for k in dict_event.keys():
            dict_event.get(k).sort(
                key=lambda event: datetime.fromisoformat(event.date))

    @staticmethod
    def filter_(list_event: list[Event]):
        return [i for i in list_event if i.type_event != TypeEvent.OTHER]

    @staticmethod
    def group_data(list_event: list[Event]) -> dict:
        temp = {}
        for item in list_event:
            temp.setdefault(
                datetime.fromisoformat(item.date).date().isoformat(),
                []).append(item)
        return temp

    @staticmethod
    def write_file(file_name, dict_events):
        with open(file_name, "w", encoding="utf8") as f:
            json.dump(
                {
                    key: [i.__dict__ for i in i_list]
                    for key, i_list in dict_events.items()
                },
                f, indent=2, default=str)

    def run(self):
        input_file, output_file = parse_param()
        list_event = self.read_file(input_file)
        dict_events = self.group_data(self.filter_(list_event))
        self.sorted_(dict_events)
        self.write_file(output_file, dict_events)
