import socket
import threading # preventing the blocking of other clients entering into the system

HEADER = 64 # first message of bytes to the server to be intentionally limiting?
'''potential concern is because this is a fixed length'''
PORT = 5050 # >4000 is inactive but there are 10,000
# using an unused port of the rotuer to create a server on this computer
SERVER = socket.gethostbyname(socket.gethostname()) # getting the ip address for the computer
ADDRESS = (SERVER, PORT) # making everything into a simple line to understand
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED" 
# when recieving this message, we can close and disconnect the client safely from the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle_client(connection, address): # handling the individual distribution bewteen 1 server and 1 client
    print(f"[SERVER] NEW CONNECTION : {address} connected.")

    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT).strip()
        # blocking line of code until we recieve a msg from our client
        if message_length:
            message_length = int(message_length)
            message = connection.recv(HEADER).decode(FORMAT)

            if message == DISCONNECT_MESSAGE:
                connected = False
            # print(f"[SERVER] [{address}] sent a message : {message}")
            print(f"[{address}] : {message}")

    connection.close()

def start():
    server.listen() # handle new connections and disturb where they need to go
    print(f"[SERVER] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept() # will wait for a new connection to occur
            # address - what address and port it came from
            # connection - store an actual object that will allows to send information back to that connection
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start() # making a copy of handle_client to handle each client as they come with each other
        print(f"[SERVER] ACTIVE CONNECTIONS : {threading.activeCount() - 1}")
            # start counts as 1 as well, so -1

print("[SERVER] Starting server...")
start()