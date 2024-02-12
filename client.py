import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED" 
SERVER = "100.112.66.114"
ADDRESS = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS) # connecting to the server, rather than bind

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  # Pad the message length with spaces
    client.send(send_length)
    client.send(message)




send("Hello World!")
send("Hello Everyone!")
send("Hello Unos!")

send(DISCONNECT_MESSAGE)