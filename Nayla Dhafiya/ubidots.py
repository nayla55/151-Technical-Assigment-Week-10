import time
import requests
import math
import random

TOKEN = "BBFF-H1ojzeIEgioOKEPg8bR75zuo1qf6Kl"  
DEVICE_LABEL = "project" 
VARIABLE_1 = "temperature"  
VARIABLE_2 = "kelembaban"  
VARIABLE_3 = "led control"
VARIABLE_4 = "kecepatan"
VARIABLE_5 = "position"  


def build_payload(variable_1, variable_2, variable_3, variable_4, variable_5):
    # menambahkan nilai values yang akan dikirimkan
    value_1 = random.randint(-5, 50)
    value_2 = random.randint(20, 85)
    value_3 = random.randint(0, 1)
    value_4 = random.randint(0, 180)

    # menambahkan gps pada ubidots
    lat = random.randrange(34, 36, 1) + \
        random.randrange(1, 1000, 1) / 1000.0
    lng = random.randrange(-83, -87, -1) + \
        random.randrange(1, 1000, 1) / 1000.0
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3,
               variable_4: value_4,
               variable_5: {"value": 1, "context": {"lat": lat, "lng": lng}}}

    return payload


def post_request(payload):
    # request HTTP
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(VARIABLE_1, VARIABLE_2, VARIABLE_3, VARIABLE_4, VARIABLE_5)
    print("[INFO] mengirimkan data")
    post_request(payload)
    print("[INFO] selesai")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
