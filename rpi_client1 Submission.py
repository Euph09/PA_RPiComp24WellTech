import re
import socket
import subprocess

command = "PATH_TO_R"
path = "PATH_TO_SCRIPT"
cmd = [command, path]

with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
    output = proc.stdout.read()

output = output.decode("utf-8")

data = re.findall(r'\".*?\"',output)[0]
print(f"The PM data is {data}")



s =socket.socket()

hostname='ENTER_IP'
port = 8000 # Port number

s.connect((hostname, port))
print("Connected to server")
s.send(data.encode())


