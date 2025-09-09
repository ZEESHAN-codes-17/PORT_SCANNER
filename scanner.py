
import socket

print("welcome to routine port scanner")

host = input("enter your IP/HOST: ")
start = int(input("enter your starting point: "))
end = int(input("enter your ending point: "))

for port in range(start, end+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    result = sock.connect_ex((host, port))

    if result == 0:
        print(f'port is opened {port}')
    else:
        print(f'port is closed {port}')

    sock.close()         