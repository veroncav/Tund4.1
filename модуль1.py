Anastassia, [2/12/2025 10:41 AM]
from string import *
from time import sleep
from os import path, remove, system
from tkinter import simpledialog as sd
from gtts import *

def registreerimine(kasutajad:list,paroolid:list)->any:
    """Kirjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        r??gimine("Sinu kasutajanimi on "+nimi,"et")
                        r??gimine("Sinu salas?na on "+parool,"et")
                    break
                else:
                    r??gimine("N?rk salas?na!","et")
                    print("N?rk salas?na!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    #mail=sd.askstring("Kirjuta oma e-posti!","Kuhu saada kirja?")
    #email(mail)
    return kasutajad, paroolid
def r??gimine(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on j?rjendis kasutajad
        Salas?na on paroolide j?rjendis
        Nimi ja salas?na indeksid on v?rdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool=input("Sisesta salas?na: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break                   
                except:
                    print("Vale nimi v?i salas?na!")
                    if p==5: 
                        print("Proovi uuesti 10 sek p?rast")
                        for i in range(10):
                            sleep(1)
                            print(f"On j??nud {10-i} sek")
        else:
            print("Kasutajat pole")
def nimi_v?i_parooli_muurmine(list_:list):
    """
    """
    muutuja=input("Vana nimi v?i parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi v?i parool: ")
        list_[indeks]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    j?rjend=[]
    for rida in f:
        j?rjend.append(rida.strip())
    f.close()
    return j?rjend
def kirjuta_failisse(fail:str,j?rjend=[]):
    """Salvestame tekst failisse
    """
    #n=int(input("Mitu: "))
    #for i in range(n):
    #    j?rjend.append(input(f"{i+1}. s?na: "))
    f=open(fail,'w',encoding="utf-8")
    for element in j?rjend:
        f.write(element+"\n")
    f.close()
def ?mber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'a')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:

Anastassia, [2/12/2025 10:41 AM]
print(f"Fail {failinimi} puudub")
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    
        #k,v=line.strip().split(":")
        #kus_vas[k]=v
        
    fail.close()
    return kus,vas #,kus_vas

import smtplib,ssl
from email.message import EmailMessage
def saada_kiri(nimi:str, parool:str):
    kellele=input("Kellele: ")
    kiri="Sa oled registreeritud. Sinu kasutajanimi on"+nimi+", sinu salasona on "+parool
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="veronika1999.v@gmail.com"
    password="12345"
    context=ssl.ceate_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="E-kiri saatmine" #from entry
    msg['From']="Veronika Vanitseva"
    msg['To']=kellele
