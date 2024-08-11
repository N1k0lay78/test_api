from time import time

import requests

HOST = "127.0.0.1:5000"

r = requests.post(f"http://{HOST}/post_time", json={"time": time()})
if r.status_code == 200:
    print(f"SUCCESS SEND. server answer: {r.json()['answer']}")
else:
    print(f"UNSUCCESSFUL SEND. server error: {r.status_code}")

r = requests.get(f"http://{HOST}/get_time")
if r.status_code == 200:
    print(f"SUCCESS SEND. server answer time: {r.json()['time']}")
else:
    print(f"UNSUCCESSFUL SEND. server error: {r.status_code}")