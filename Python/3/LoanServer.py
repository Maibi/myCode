from socket import *
from collections import *
import string


montlypay = 0

def LoanCalculator(intrest, num ,LAmount):
    intrest_rate = float(intrest)
    numYears = float(num)
    LoanAmount= float(LAmount)
    print (intrest_rate)
    totalpay = LoanAmount + (LoanAmount * (intrest_rate/100))
    montlypay = totalpay / int(12*(numYears))

    return montlypay

def dispMsg(montly,numYers):
     m = int(montly) * int((12*(int(numYers))))
     return(m)


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print "The server is reeady to recieve"
while 1:

    #countr = 0
    message, clientAddress = serverSocket.recvfrom(2048)
    message2, clientAddress = serverSocket.recvfrom(2048)
    message3, clientAddress = serverSocket.recvfrom(2048)

    LoanAmount = LoanCalculator(message, message2, message3)
    month = dispMsg(LoanAmount, message2)
    #modifiedMessage = str(dispMsg(LoanAmount))
    serverSocket.sendto("Monthly pay :"+str(LoanAmount), clientAddress)
    serverSocket.sendto("Total pay : "+str(month), clientAddress)



