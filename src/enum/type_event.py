from enum import Enum


class TypeEvent(Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"

    def __str__(self):
        return self.value
