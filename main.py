from fastapi import FastAPI 
import psutil
import datetime
import json    
app = FastAPI()

#T


class systemInfo():
    def __init__(self,cpu,ram,disk,date):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.date = date
        


@app.get("/")
async def main():
    return("znajdujesz sie w glownym katalogu, wpisz /health aby zobaczyc czy dziala serwer")

@app.get('/stats')
async def getItems():
    cpu_stats = psutil.cpu_percent()
    ram_stats = psutil.virtual_memory().percent
    disk_stats = psutil.disk_usage('/').percent
    server_date = datetime.datetime.now()
    return(systemInfo(cpu_stats,ram_stats,disk_stats,server_date))

@app.get('/health')
async def getItems():
    cpu_stats = psutil.cpu_percent()
    ram_stats = psutil.virtual_memory().percent
    disk_stats = psutil.disk_usage('/').percent
    server_date = datetime.datetime.now()
    if(cpu_stats < 0):
        return("Wystapil problem z cpu")
    elif(ram_stats < 0):
        return("wystapil problem z ramem")
    elif(disk_stats < 0):
        return("wystapil problem z Dyskiem")
    elif(server_date is None):
        return("wystapil problem z Data")
    else:
        return("OK")
