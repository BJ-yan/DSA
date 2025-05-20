import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.108.88', 8000))

client_socket.send("hello, itheima")

recv_bytes = client_socket.recv(1024)
recv_data = recv_bytes.decode(encoding = 'utf-8')

print(f"客户端收到{recv_data}")