from socket import *
from random import sample
import re
import datetime
import threading
from math import *
import sys
from math import pi
from math import sqrt

RE = re.compile(' +')
serverName = '127.0.0.1'
serverPort = 13000

def IPADDRESS():
    ip = gethostbyname(gethostname())
    return str(ip)


def PORT(addr):
    return addr[1]
def COUNT(string):
    consonants = 0
    vowels = 0
    gjatesia = len(string)
    if(gjatesia<=128):
        for i in string:
            if not (
                    i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or ord(
                    i) >= 32 and ord(i) <= 64 or ord(i) >= 91 and ord(i) <= 96 or ord(i) >= 123 and ord(i) <= 126):
                consonants = consonants + 1
            elif i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or ord(
                    i) >= 32 and ord(i) <= 64 or ord(i) >= 91 and ord(i) <= 96 or ord(i) >= 123 and ord(i) <= 126:
                vowels = vowels + 1

        return ( 'Teksti i pranuar permban ' + str(vowels) + ' zanore dhe ' + str(consonants) + ' bashketingellore' )
    else:
        print("Mesazhi eshte me i gjate se 128 karaktere")
def REVERSE(string):
    stringlength = len(string) # llogarit gjatesine e stringut
    slicedString = string[stringlength :: -1]

    return slicedString
def PALINDROME(string):
    string = string.replace(" ", "")  # ktu nese ka naj hapesire e hjek psh ramush aga shumar hahahaahahahhahahah
    reverse = string[::-1]  # qikjo e kthen stringun mrapsht
    if (string == reverse):
        return 'Teksti i dhene eshte palindrom'
    return 'Teksti i dhene nuk eshte palindrom'


def TIME():
   return(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
def GAME():
  list1 = range(1,35)
  sorted_list=sample(list1,5)
  sorted_list.sort()
  return sorted_list


def GCF(numri1, numri2):
    if numri1 > numri2:
        numri1, numri2 = numri2, numri1

    for x in range(numri1, 0, -1):
        if numri1 % x == 0 and numri2 % x == 0:
            return x

def CONVERT(opt,num):
    if opt.lower() == 'cmtofeet':
        cm=round(0.03281,2)
        ft=int(num)*cm
        return round(ft,2)
    elif opt.lower() == 'feettocm':
        ft=round(30.48,2)
        cm=int(num)*ft
        return round(cm,2)
    elif opt.lower() == 'kmtomiles':
        km = round(0.62137,2)
        miles = int(num)*km
        return round(miles,2)
    elif opt.lower() == 'milestokm':
        miles = round(1.60934, 2)
        km = int(num) * miles
        return round(km,2)

    else:
        print("Please choose a method and enter an integer!")

def GUESSING(guess_word):
    secret_word = "GIRAFFE"
    if guess_word.upper() != secret_word:
        return("Wrong guess, YOU LOSE!")
    else:
        return("YOU WIN!")

def GET_MIDDLE(s):
    print(s)
    x = len(s)
    y = int(x/2)
    if x%2==0:
        return s[y-1:y+1]
    else:
        return s[y:y+1]


def check_if(data,addr):
    while True:
        if data.upper() == 'EXIT':
            break
        elif data.upper() == 'IPADDRESS':
            return ("IP Adresa e klientit eshte: " + IPADDRESS())
        elif data.upper() == 'PORT':
            return ("Klienti eshte duke perdorur portin: " + str(PORT(addr)))
        elif re.match('(COUNT) ([A-Z]+)', data.upper()):
            ndarja = data.split(' ')
            # print(ndarja)
            send_payload = " ".join(ndarja[1:len(ndarja)])
            print(send_payload)
            return COUNT(send_payload)
        elif re.match('(REVERSE) ([A-Z]+)', data.upper()):
            ndarja1 = data.lower()
            ndarja = ndarja1[7:len(data)]
            return (REVERSE(ndarja))
        elif re.match('(PALINDROME) ([A-Z]+)', data.upper()):
            ndarja1= data.lower()
            ndarja = ndarja1[10:len(data)]
            return (PALINDROME(ndarja))
        elif data.upper() == 'TIME':
            return (TIME())
        elif data.upper() == 'GAME':
            return ("5 numrat e rastesishem: " + str(GAME()))
        elif re.match('(GCF) [0-9]+', data.upper()):
            ndarja = data.lower().split(' ')
            numri1 = int(ndarja[1])
            numri2 = int(ndarja[2])
            return(GCF(numri1,numri2))
        elif re.match('(CONVERT) ([A-Z]+) [0-9]+', data.upper()):
            ndarja = (data.lower()).split()
            # print(ndarja)
            if ndarja[1] == 'cmtofeet' or ndarja[1] == 'feettocm' or ndarja[1] == 'kmtomiles' or \
                ndarja[1] == 'milestokm':
                konverto = CONVERT(ndarja[1], ndarja[2])
                return (konverto)
            else:
                return ('')
        elif re.match("(GUESSING) ([A-Z]+)",data.upper()):
            ndarja = data.split(' ')
            return(GUESSING(str(ndarja[1])))
        elif re.match("(GET_MIDDLE) [A-Z]+",data.upper()):
            ndarja = data.split(' ')
            # print(ndarja)
            return(GET_MIDDLE(str(ndarja[1:(len(ndarja))])))
        else:
            return('Nuk u gjend metoda')




def client_thread(conn, addr):
    print('Lidhja juaj me serverin u realizua...')
    while True:
        dataOfClient = conn.recv(128)
        data = dataOfClient.decode('utf-8')
        print(data)
        if not data:
            break
        dataOfServer = check_if(data)
        print(dataOfServer)
        if dataOfServer!='':
            conn.sendall(str(dataOfServer).encode('UTF-8'))
        else:
            conn.sendall("Pergjigjja nuk mund te gjendet".encode('UTF-8'))

try:
    serverSocket = socket(AF_INET, SOCK_DGRAM)
except socket.error as error:
    print(error)
    sys.exit(0)
print("Soketa u krijua me sukses!")

try:
    serverSocket.bind((serverName, serverPort))
    print('Serveri eshte startuar ne localhost ne portin ' + str(serverPort))
except socket.error as error:
    print(error)
    sys.exit(0)

# serverSocket.listen(5)
# print('Serveri eshte i gatshem te pranoj kerkesa')

while 1:
     print('Lidhja juaj me serverin u realizua...')
     while True:
         dataOfClient,addr = serverSocket.recvfrom(128)
         data = dataOfClient.decode('utf-8')
         print(data)
         if not data:
             break
         dataOfServer = check_if(data,addr)
         print(dataOfServer)
         if dataOfServer != '':
             serverSocket.sendto(str(dataOfServer).encode('UTF-8'),addr)
         else:
             serverSocket.sendto("Pergjigjja nuk mund te gjendet".encode('UTF-8'),addr)
#     connectionSocket, addr = serverSocket.accept()
#     threading._start_new_thread(client_thread, (connectionSocket, addr))