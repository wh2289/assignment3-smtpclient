from socket import *



def smtp_client(port=1025, mailserver ='127.0.0.1'):

    msg = "\r\n Go NYU Cyber Fellows!"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect("127.0.0.1",1025)


    recv = clientSocket.recv(1024).decode()
    print("Connection Requst:" + recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')


    helloCommand = 'HELLO Alice\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    mailFrom = "Mail From: <networking@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print(" Mail From: " + recv2)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    rcptto = "Rcpt To : <recipient@gmail.com> \r\n"
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024)
    print("Rcpt To: " + recv3)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    data = "Data \r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024)
    print("Data: " + recv4)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    message = raw_input("Enter message: ")

    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    clientSocket.send("Quit\r\n".encode())
    message = clientSocket.recv(1024)
    print(message)
    clientSocket.close()



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')