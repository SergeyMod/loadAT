from datetime import datetime
from pydantic import BaseModel, Field


class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str = Field(default_factory=lambda: datetime.now().isoformat())
    status: str
    complete: bool