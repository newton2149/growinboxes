from fastapi import APIRouter
from database.config import db
from models.sensorData import SensorData

router = APIRouter()


@router.post("/sensor")
def post_sensor(req: SensorData):
    data = {
        "metadata": {"sensorId": req.sensorId, "type": req.type},
        "timestamp": req.timeStamp,
        "temp": req.val
    }
    db['sensor-data'].insert_one(data)
    return {
        "body":"success"
    }
