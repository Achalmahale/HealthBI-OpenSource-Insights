from fastapi import FastAPI
import uvicorn
#run cleaning.py
from cleaning import clean_data
import pandas as pd

app = FastAPI()

STEPS = pd.read_csv("Data/com.samsung.shealth.tracker.pedometer_day_summary.csv", skiprows=1, header=0)
HEART_RATE = pd.read_csv("Data/com.samsung.shealth.tracker.heart_rate.csv", skiprows=1, header=0)
SLEEP = pd.read_csv("Data/com.samsung.health.sleep_stage.csv", skiprows=1, header=0)
STRESS = pd.read_csv("Data/com.samsung.shealth.stress.csv", skiprows=1, header=0)
WEIGHT = pd.read_csv("Data/com.samsung.health.weight.csv", skiprows=1, header=0)
ACTIVITY_SUMMARY = pd.read_csv("Data/com.samsung.shealth.activity.day_summary.csv", skiprows=1, header=0)

print(HEART_RATE.head())

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)