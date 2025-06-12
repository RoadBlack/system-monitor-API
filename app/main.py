from fastapi import FastAPI 
from dataclasses import dataclass  
import psutil
import datetime
import json    
app = FastAPI()

#T

@dataclass 
class systemInfo():
        cpu: float
        ram: float
        disk: float
        date: datetime.datetime


@app.get("/")
async def main():
    return("znajdujesz sie w glownym katalogu, wpisz /health aby zobaczyc czy dziala serwer")

@app.get('/stats', response_model=systemInfo)
async def getItems():
    cpu_stats = psutil.cpu_percent()
    ram_stats = psutil.virtual_memory().percent
    disk_stats = psutil.disk_usage('/').percent
    server_date = datetime.datetime.now()
    return{
        "cpu": cpu_stats,
        "ram": ram_stats,
        "disk": disk_stats,
        "date": server_date,     
    }

@app.get('/health')
async def getItems():
    cpu_stats = psutil.cpu_percent()
    ram_stats = psutil.virtual_memory().percent
    disk_stats = psutil.disk_usage('/').percent
    server_date = datetime.datetime.now()
    if(cpu_stats < 0):
        return{"msg":"Wystapil problem z cpu"}
    elif(ram_stats < 0):
        return{"msg":"wystapil problem z ramem"}
    elif(disk_stats < 0):
        return{"msg":"wystapil problem z Dyskiem"}
    elif(server_date is None):
        return{"msg":"wystapil problem z Data"}
    else:
        return{"msg": "OK"}
