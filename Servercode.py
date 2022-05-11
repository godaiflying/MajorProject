import socket
from threading import Thread


#the ip address
#create a TCP socket
#list all conected clients' sockets 
#make the  all port resuable
#bind the socket to the address we specified

serverhost = "0.0.0.0"
serverport = 5002 #the tcp port number
separator_token = "<SEP>" #seperate client name

client_sockets = set()
s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((serverhost, serverport))

s.listen(5)

print(f"[*] Listening as {serverhost}:{serverport}")


def listening(cs):
    #create a fucntion that listenst for messages using the cs socket
    #whenever a message is receved bordcast it to the rest of the clients 


    while True: 
        try:
            #look for messages
            msg = cs.recv(1024).decode()

        except Exception as e:
            #if the client is disconnected DELETE IT 
        
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
            
        for client_socket in client_sockets:
                client_socket.send(msg.encode())

while True:

    #keep listening for new connections
    #add connected clients to connected sockets
    #start a new thread that listens for each message
    #make a thread daemon beacuse it runs in the background apparently and is good !!
    #then start the thread

    client_sockets, client_address = s.accept()

    print(f"[+] {client_address} connected.")

    client_sockets.add(client_sockets)

    t = Thread(target = listening, args=(client_sockets,))

    t.daemon = True

    t.start()

# close server socket

for cs in client_sockets:
    cs.close()

s.close()
