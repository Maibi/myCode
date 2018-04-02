from socket import *
from collections import *
import string
import os

size = 0


def Prime_file():
    if (os.path.isfile("primes.dat") == False):

        f = open("primes.dat", "w")

        # f = open("primes.dat", "a")

        for p in range(2, 1000):
            print p
            for i in range(2, p):
                #print p
                if p % i == 0:
                    break
            else:
                f.write(str(p) + '\n')

        print "finished"
        f.close()


def File_length():
    f = open("primes.dat", "r")
    countr = 0
    for l in f:
        countr = countr + 1
        # print(l)
    f.close()
    size = countr

    return size


def Request_Prime(Reqnum):
    k = int(File_length())

    i = 0
    f = open("primes.dat", "r")
    Newf = open("reqprimes.dat", "w")
    print("this is i: " + str(i))
    print("this is k :" + str(k))

    print("this is Requm" + str(Reqnum))
    for l in f:


        if i >= (k - Reqnum):
            Newf.write(l)
            print("this is l :" + l)
        i = i + 1
    Newf.close()
    f.close()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

Prime_file()
print "The server is reeady to recieve"

while 1:

    message, clientAddress = serverSocket.recvfrom(2048)

    modifiedMessage = File_length()
    Request_Prime(int(message))
    Newf = open("reqprimes.dat", "r")
    print ("Num req =" + message)
    print ("Lenght : " + str(modifiedMessage))
    for l in Newf:
        serverSocket.sendto(l, clientAddress)

    Newf.close()
