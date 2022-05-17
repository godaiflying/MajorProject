from http import client
from pydoc import cli
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




#receive all messages for all of client sockets then
#send all messages out to client sockets

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_messages(client_socket)
            
            if user is False:
                continue
            
            sockets_list.append(client_socket)
            clients[clients] = user
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")

        else:
            message = receive_messages(notified_socket)
                #if client dc then there is no point checking weather they have sent messages
            if message is False: 
                print(f"Close connection from : {clients[notified_socket]['data'].decode['utf-8']}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

                continue

            user = clients[notified_socket]
                #printing the message
            print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            

            #broadcast message to all people but the sender
            for client_socket in client:
                if client_socket != notified_socket:
                    client_socket.send(user['header']+ user['data'] + message['header'] + message['data'])

    #watching socket excpetions
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]