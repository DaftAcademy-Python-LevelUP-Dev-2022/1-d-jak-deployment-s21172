from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code = 200)
def root():
    print ("test")
    return {"start": "1970-01-01"}