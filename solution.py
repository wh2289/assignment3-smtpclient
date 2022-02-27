from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Go NYU Cyber Fellows!"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print("Connection Requst:" + recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    helloCommand = 'HELLO Alice\r\n'
    clientSocket.send(helloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    mailFrom = "MAIL FROM: <networking@gmail.com> \r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print("MAIL FROM:" +recv2)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    rcptto = "RCPT TO: <recipient@gmail.com> \r\n"
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print("RCPT TO: " + recv3)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    data = "DATA \r\n"
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print("DATA: " + recv4)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    message = raw_input("Enter message: ")

    mailMessageEnd = '\r\n.\r\n'
    clientSocket.send(message + mailMessageEnd)
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    clientSocket.send("QUIT\r\n".encode())
    message=clientSocket.recv(1024)
    print(message)
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
