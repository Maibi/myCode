from socket import *


def File_length(file_name):
    f = open(file_name, "r")
    count = 0
    for l in f:
        count = count + 1
       # print(l)
    f.close()
    size = count
  #  print (size)
    return size

serverName = "Localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
connection = True
while 1:

    if(connection == True):
        serverName = ""
        serverPort = 12000
        clientSocket = socket(AF_INET, SOCK_DGRAM)


        FileName = raw_input("Input Name of file: ")
        #FileName ="/home/ernest/PycharmProjects/25.txt"
        #FileName2 = "25.txt"
        clientSocket.sendto( FileName, (serverName, serverPort))
        #wait for response
        Response, serverAddress = clientSocket.recvfrom(2048)
        print(Response)
        if(Response == str(True)):
            LenthofFile, serverAddress = clientSocket.recvfrom(2048)
            print(LenthofFile)
            f = open(FileName, "w")
            for x in range(0, int(LenthofFile)):
                FileChar, serverAddress = clientSocket.recvfrom(2048)
                f.write(FileChar)
            f.close()

            print("file recieved")
            Reply = raw_input("Type send to return file: ")
            SizeOfFile = File_length(FileName)

            if(Reply == "send"):
                #print(Reply)
                clientSocket.sendto(Reply, (serverName, serverPort))
                clientSocket.sendto(str(SizeOfFile), (serverName, serverPort))
                f = open(FileName, "r")
                for l in f:
                    clientSocket.sendto(l, (serverName, serverPort))
                    print("Sending")

        else:
            print("File not found")
    else:
        print("Waiting for connection")



clientSocket.close();
