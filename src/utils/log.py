import datetime
import os

def log(message):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists("out"):
        os.makedirs("out")

    with open("out/log.txt", "a") as f:
        f.write(f"{timestamp} - {message}\n")
