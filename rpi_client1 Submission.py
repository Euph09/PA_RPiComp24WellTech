import re
import socket
import subprocess

#Gather data from R for outdoor air quality
command = "PATH_TO_R"
path = "PATH_TO_SCRIPT"
cmd = [command, path]

#Execute command to run R script
with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
    output = proc.stdout.read()

#R output is encoded, so decode
output = output.decode("utf-8")

#Extract data we want
data = re.findall(r'\".*?\"',output)[0]
print(f"The PM data is {data}")


#Send data over to RPi, via sockets
s =socket.socket()

hostname='ENTER_IP'
port = 8000 # Port number

s.connect((hostname, port))
print("Connected to server")
s.send(data.encode())


