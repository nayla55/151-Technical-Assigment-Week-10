import time 
import requests 
import math
import random 

TOKEN = "BBFF-H1ojzeIEgioOKEPg8bR75zuo1qf6Kl"
DEVICE_LABEL = "node_raspi"
VARIABLE_1 = "kecepatan"
VARIABLE_2 = "kelembaban"

def build_payload(variable_1,variable_2):
    nilai_kecepatan = random.randint(35,45)
    nilai_kelembaban = random.randint(95,105)
    payload = {variable_1:nilai_kecepatan, variable_2:nilai_kelembaban}
    return payload

def kirim_data(payload):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url,DEVICE_LABEL)
    headers = {"X-Auth-Token":TOKEN,"Content-Type":"application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts<=5:
        req = requests.post(url=url,headers=headers,json=payload)
        status = req.status_code
        attempts +=1
        time.sleep(1)
    
    print(req.status_code, req.json())
    
    if status>=400:
        print("Ada Error")
        return False
    print("berhasil")
    return True

def main():
    payload = build_payload(VARIABLE_1,VARIABLE_2)
    print("mencoba mengirim data")
    kirim_data(payload)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
    
    
    


