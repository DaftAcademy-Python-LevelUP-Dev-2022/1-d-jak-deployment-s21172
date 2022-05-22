from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/", status_code = 200)
def root():
    print ("test")
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

@app.get(path="/day/", status_code = 200)
def get_day(name:str, number:int):
	if name!=None and number!=None:
		if name not in daysDict.values():
			raise HTTPException(status_code=400, detail="Invalid day name")
		elif number not in daysDict.keys():
			raise HTTPException(status_code=400, detail="Invalid day name")
		elif name==daysDict.get(number):
			status_code=200
			return daysDict[number]
		elif name!=daysDict.get(number):
			status_code=400
			return daysDict[number]
	else:
		raise HTTPException(status_code=400, detail="Parameters name and number can't be empty")
		
	
	 
	
	