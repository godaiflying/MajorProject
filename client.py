import socket
import select
import errno 
#errno: To translate a numeric error code to an error message

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP,PORT))