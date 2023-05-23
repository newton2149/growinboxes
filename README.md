# GrowinBoxes

## Sensor Collection Application

### Run MongoDB Server using Docker


```
docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server
```

### Run FastAPI Application
```
uvicorn main:app --reload
```
