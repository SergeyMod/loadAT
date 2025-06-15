from enum import Enum

class Links(Enum):
    HOST = 'https://www.kinopoisk.ru/'
    SEARCH = f'{HOST}s/'
    RESULT = f'{HOST}index.php'
    FILM = f'{HOST}film/'

    def __str__(self):
        return self.value
