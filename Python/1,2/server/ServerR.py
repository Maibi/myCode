import os
from socket import *
from collections import *
import string

size = 0
def File_check(path):

    if os.path.isfile(path) == True:
        return True
    else:
        return False




def File_length(file_name):
    f = open(file_name, "r")
    count = 0
    for l in f:
        count = count + 1
      #  print(l)
    f.close()
    size = count
    #print (size)
    return size

connection = False
while 1:

    if connection == False :
        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(("", serverPort))
        connection == True

    print "The server is reeady to recieve"



    while 1:


        message, clientAddress = serverSocket.recvfrom(2048) #name of file
        Check = File_check(message)
        #Check = File_check(path)
        print (clientAddress)
        IpAdress = str(clientAddress)
        if(Check == True):

            FileSize = File_length(message)
         # print(FileSize)
            serverSocket.sendto(str(Check), clientAddress) # true
            serverSocket.sendto(str(FileSize), clientAddress) # length of file
            f = open(message, "r")
            for l in f:
             #  print (l)
                serverSocket.sendto(l, clientAddress)

            f.close()
            print ("waiting")
            alterd, clientAddress = serverSocket.recvfrom(2048)
            print(alterd) #######
            print(clientAddress)
            print(IpAdress)

            if(alterd == "send" ):

                SizeofFile, clientAddress = serverSocket.recvfrom(2048)
                f = open(message, "w")
                for x in range(0, int(SizeofFile)):
                    FileChar, clientAddress = serverSocket.recvfrom(2048)
                    f.write(FileChar)
                f.close()

        else:
            serverSocket.sendto(str(Check), clientAddress)


