# Ddos
This is a Ddos Atacker???

# How Run it
need virtual machine or vps with different ip 
suggest : Ubuntu Server 24
clone repository :
```git clone https://github.com/shayanghad0/Ddos/```
then open ```main.py``` file
must change thease on lines 5 6
```python
target_ip = "104.21.88.251"  # Replace with the target IP
target_port = 80           # Replace with the target port
```
and this on line 19
```python
for i in range(500):  # High number of threads for stronger effect
```
then run project just this
```py/python/py3/python3 main.py```
if print ```attack is started``` your ddos is started
