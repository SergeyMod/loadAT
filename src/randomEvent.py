import random
from string import ascii_letters, digits
from datetime import datetime, timezone, timedelta

from faker import Faker

from src.event import Event
from src.enum.type_event import TypeEvent


class RandomEvent:

    @classmethod
    def random_event(cls, range_date: list[str] = None) -> Event:
        date: str = cls.__random_datetime_with_timezone(range_date)
        type_event: TypeEvent = random.choice(list(TypeEvent))
        title: str = cls.__generate_event_name()
        participants: list = [Faker().first_name() for _ in
                              range(random.randint(0, 10))]
        place: str = cls.__random_place()
        return Event(
            date=date,
            type_event=type_event,
            title=title,
            participants=participants,
            place=place)

    @staticmethod
    def random_string(max_len=20) -> str:
        length = random.randint(1, max_len)
        return ''.join(random.choices(ascii_letters + digits, k=length))

    @classmethod
    def __generate_event_name(cls) -> str:
        words = []
        while True:
            word = cls.random_string(20)
            if len(' '.join(words + [word])) > 100:
                break
            words.append(word)
        return ' '.join(words)

    @classmethod
    def __random_place(cls) -> str:
        choice = random.choice(["zoom",
                                "telegram",
                                "address"])
        if choice in ["zoom",
                      "telegram"]:
            return choice
        return cls.random_string(30)

    @staticmethod
    def __random_datetime_with_timezone(range_date=None) -> str:
        if range_date is None:
            range_date = ['2020-05-20', '2020-05-22']
        formats = ['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%Y/%m/%d',
                   '%d.%m.%Y']
        start_date, end_date = None, None
        for fmt in formats:
            try:
                start_date, end_date = [datetime.strptime(i, fmt)
                                        for i in range_date]
            except ValueError:
                continue
        if not start_date or not end_date:
            raise ValueError(f"Не удалось распознать дату")
        delta = end_date - start_date
        random_seconds = random.randint(0, int(delta.total_seconds()))
        dt = start_date + timedelta(seconds=random_seconds)
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)

        dt.replace(hour=random_hour,
                   minute=random_minute)
        tz = timezone(timedelta(hours=random.choice([-5, 0, 3, 5, 9])))
        dt.astimezone(tz)
        return dt.isoformat()
