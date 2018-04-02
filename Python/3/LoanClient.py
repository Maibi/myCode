from socket import *

serverName = "Localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    InterstRate = raw_input("Input Annual Interest Rate: ")
    Duration = raw_input("Input Number of Years: ")
    Amount = raw_input("Input Loan Amount: ")

    clientSocket.sendto(InterstRate, (serverName, serverPort))
    clientSocket.sendto(Duration, (serverName, serverPort))
    clientSocket.sendto(Amount, (serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    modifiedMessage2, serverAddress = clientSocket.recvfrom(2048)

    print modifiedMessage
    print modifiedMessage2
clientSocket.close();
