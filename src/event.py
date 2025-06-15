from typing import List
from dataclasses import dataclass

from src.enum.type_event import TypeEvent


@dataclass()
class Event:
    date: str
    title: str
    type_event: TypeEvent
    participants: List[str]
    place: str

    def __eq__(self, other):
        if isinstance(other, Event):
            return (self.date == other.date
                    and self.title == other.title
                    and self.type_event == other.type_event
                    and self.participants == other.participants
                    and self.place == other.place)
        return False