from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, BaseSettings
import datetime
from typing import List


class Settings(BaseSettings):
    eventCounter = 0


class EventIn(BaseModel):
    date: str
    event: str


class EventOut(BaseModel):
    id: int
    event: str
    date: str
    dateAdded: str


app = FastAPI()
settings = Settings()
eventsList = []


@app.put("/events/", status_code=200, response_model=EventOut)
def add_event(eventIn: EventIn):
    try:
        datetime.datetime.strptime(eventIn.date, "%Y-%m-%d")
    except:
        raise HTTPException(status_code=400, detail="Invalid date format")
    eventId = settings.eventCounter
    eventAdded = str(datetime.date.today())

    eventCreated = EventOut(
        id=eventId, event=eventIn.event, date=eventIn.date, dateAdded=eventAdded
    )

    eventsList.append(eventCreated)
    settings.eventCounter += 1

    return eventCreated


@app.get("/", status_code=200)
def root():
    print("test")
    return {"start": "1970-01-01"}


@app.post(path="/method", status_code=201)
def get_post():
    return {"method": "POST"}


daysDict = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
    7: "sunday",
}


@app.get(path="/day/", status_code=200)
def get_day(name: str, number: int):
    if name != None and number != None:
        if name not in daysDict.values():
            raise HTTPException(status_code=400, detail="Invalid day name")
        elif number not in daysDict.keys():
            raise HTTPException(status_code=400, detail="Invalid day name")
        elif name == daysDict.get(number):
            status_code = 200
            return daysDict[number]
        elif name != daysDict.get(number):
            raise HTTPException(status_code=400, detail="Day doesn't match the number")
    else:
        raise HTTPException(
            status_code=400, detail="Parameters name and number can't be empty"
        )
