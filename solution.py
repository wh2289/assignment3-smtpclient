from socket import *
import base64


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Go NYU Cyber Fellows!"
    endmsg = "\r\n.\r\n"

    mailserver = ("mail.smtp2go.com", 2525)

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)


    recv = clientSocket.recv(1024).decode()
    print("Connection Requst:" + recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')


    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
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



    # Send RCPT TO command and handle server response.
    # Fill in start
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')