import socket
import select 
#using select


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#makes sure that the port can be reused 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

#list of users
clients= {}

print(f"Listening for connections on {IP}:{PORT}...")

def receive_messages(client_socket):
    try:
        #receving messages
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        #utf-8 is unicode transformation format HAHA
        message_length = int(message_header.decode('utf-8').strip())

        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:

        #if the user sends nothing or dcs
        return False

