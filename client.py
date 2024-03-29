import socket
import select
import errno
import sys

#errno: To translate a numeric error code to an error message



HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))

#recv block set to false
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")
    #sending messages
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        #receive things
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            print("message recieved")
            if not len(username_header):
                print('Connection closed by server')
                sys.exit()
            
            #accually getting the username
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            #and message 
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            
            
            print(f"{username} > {message}")
    
    

    except IOError as e:
        #different computers use either EAGAIN or EWOULDBLOCK
        #Check for both and if one of them errors, that is expected meaning continue.
        # If different error code, something bad happened
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        #any other expection just exit
        print('general error', str(e))
        sys.exit()

    