from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(("localhost",80))
server.listen()
print("socket is listening at 80")

connection,address=server.accept()
print("connected to client")

users=[]
def add_new_user(user_socket):
    new_socket, address = user_socket.accept()
    users.append(new_socket)
    print "A new user has joined"


def remove_user(user_socket):
    users.remove(user_socket)
    print "A user has left"

while True:
    data=input("server: ")
    connection.send(bytes(data,'utf-8'))
    print("data sent")

    if data == '0':
        break

    recieveData=connection.recv(1024).decode()
    print("client: ",recieveData)
     
    if recieveData == '0':
        break

connection.close()