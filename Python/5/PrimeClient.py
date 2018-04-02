from socket import *

serverName = "Localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    NumPrimes = raw_input("Input Number of Last Primes: ")


    clientSocket.sendto(NumPrimes, (serverName, serverPort))
    print ("NUmREq = " + NumPrimes)
    for x in range(0, int(NumPrimes)):
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print modifiedMessage


clientSocket.close();