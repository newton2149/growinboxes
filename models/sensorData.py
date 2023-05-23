from pydantic import BaseModel
from datetime import datetime


class SensorData(BaseModel):
    sensorId: int
    type: str
    timeStamp: datetime = datetime.now()
    val : int
