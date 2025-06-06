from src.run import Run

if __name__ == '__main__':
    Run.run()



# Генерация events.json
# import json
# if __name__ == "__main__":
#     with open("src/events.json", "w", encoding="utf-8") as f:
#         count_events = 1000
#         events = [RandomEvent.random_event() for _ in range(count_events)]
#         json.dump([i.__dict__ for i in events], f, indent=2, default=str)