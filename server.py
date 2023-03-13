import socket

host = "localhost"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(1)

print("The server is up and running, so it is listening to clients requests")

conn, address = sock.accept()

message = "Hey there, I have a message for you"

conn.send(message.encode())

conn.close()
