from datetime import datetime

class Payloads:
    _date = datetime.now().isoformat()
    create_order = {
          "id": 1,
          "petId": 0,
          "quantity": 0,
          "shipDate": _date,
          "status": "placed",
          "complete": "true"
}