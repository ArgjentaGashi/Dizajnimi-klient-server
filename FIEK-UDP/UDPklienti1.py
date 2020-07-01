from socket import *
import sys
import re
serverName = input('Jepni emrin e serverit: ')
if serverName == '':
    serverName = 'localhost'
    print(serverName)
elif serverName == 'localhost':
    print(serverName)
port = input('Jepni portin: ')
if port == '':
    port = 13000
    print(port)
elif port == '13000':
    port = 13000
    print(port)




def check_if(var):
    while True:
        if var.upper() == 'EXIT':
            break
        elif var.upper()=='IPADDRESS':
            return ('IPADDRESS')
        elif var.upper()=='PORT':
            return ('PORT')
        elif var.upper()=='COUNT':
            fjala=input("Teksti? ")
            if fjala!='':
                payload=var.upper()+" "+fjala
                return (payload)
            else:
                print('Ju nuk keni dhene ndonje tekst.')
        elif var.upper() == 'REVERSE':
            fjala = input("Teksti? ")
            if fjala.lower()!='':
                payload=var.upper()+" "+fjala.lower()
                return(payload)
            else:
                print('Ju nuk keni dhene ndonje tekst')
        elif var.upper() == 'PALINDROME':
            fjala = input("Teksti?")
            if fjala.lower()!= '':
                payload = var.upper()+" "+fjala.lower()
                return (payload)
            else:
                print('Ju nuk keni dhene ndonje tekst')
        elif var.upper()=='TIME':
            return('TIME')
        elif var.upper()=='GAME':
            return('GAME')
        elif var.upper() == 'GCF':
            print('Shkruani dy numra: ')
            numri1 = input('Numri i pare: ')
            numri2 = input('Numri i dyte: ')
            faktori = var+" "+numri1+" "+numri2
            return faktori
        elif var.upper()=='CONVERT':
            print('Zgjedhni konvertimin qe doni te beni: \ncmToFeet \nfeetToCm \nkmToMiles \nmilesToKm ')
            konvertimi_i_zgjedhur=input("Zgjedhja juaj: ")
            if konvertimi_i_zgjedhur.lower()=='cmtofeet' or konvertimi_i_zgjedhur.lower()=='feettocm' or konvertimi_i_zgjedhur.lower()=='kmtomiles' or konvertimi_i_zgjedhur.lower()=='milestokm':
                vlera_e_dhene=input("Jepni vleren qe doni te konvertoni: ")
                if re.match('[0-9]+',vlera_e_dhene):
                   konverto = var+" "+konvertimi_i_zgjedhur+" "+vlera_e_dhene
                   return konverto
                else:
                   print("Vlera e kthyer duhet te jete numer i plote")

                   return('')
            else:
                print("Nje opsion i tille nuk egziston")
                return('')
        elif var.upper() == "GUESSING":
            fjala = input("Jepni fjalen per te qelluar fjalen sekrete: ")
            if fjala != " ":
                payload = var.upper() + " " + fjala
                return(payload)
            else:
                print("Nuk keni dhene tekst! ")
        elif var.upper() == "GET_MIDDLE":
            fjala = input("Jepni fjalen per metoden GET_MIDDLE: ")
            if fjala!='':
                payload = var.upper() + " " +fjala
                return(payload)
            else:
                return('Nuk keni dhene fjale!')


        else:
            return('Nuk eshte gjetur')




try:
    s = socket(AF_INET,SOCK_DGRAM)
    # s.connect((serverName, port))
    #r = s.recv(128)
    #print(r.decode("utf-8"))
    #print('Ju lutem zgjedhni njeren nga metodat.\nPer IPADRES shkruaj --> IPADRES \nPer numer te portit --> NUMRIIPORTIT \nPer bashketingellore -->BASHKETINGELLORE Tekstin (Psh. BASHKETINGELLORE buba e dajve)\nPer printim --> PRINTIMI tekstin (Psh. PRINTO Ky eshte nje paragraf)\nPer hot --> EMRIIKOMPJUTERIT \nPer kohen --> KOHA \nPer lojen --> LOJA \nPer konvertim --> KONVERTIMI \nPer FIBONACCI -->FIBONACCI Numri (Psh.FIBONACCI 7) \nPer radhitje te fjalise--> RADHITJA teksti (RADHITJA esh3te emri1 2im 4aurora - numri tregon renditjen e fjales ne fjali) \nPer shkronjen unike ne fjale --> UNIKENERADHITJE Teksti (UNIKENERADHITJE aaabbbbbsssdddaa ->absda)')
    while 1:
        var = input('Zgjedhni nje nga funksionet: IPADDRESS, PORT, COUNT, REVERSE,  PALINDROME, TIME, GAME, GCF, CONVERT, GUSEEING, GET MIDDLE\n')
        checked_datum = check_if(var)
        if checked_datum != '' and checked_datum.upper()!="EXIT":
            # s.sendall(checked_datum.encode("UTF-8"))
            s.sendto(str(checked_datum).encode(), (serverName,port))
            # data = s.recv(128)
            data,address= s.recvfrom(128)
            print(data.decode("utf-8"))
        else:
            break
    s.close()
except:
    print("Error404: Server not found!")