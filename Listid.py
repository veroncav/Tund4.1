# #1
# from curses.ascii import isdigit
# import string
# vokaali=['a','e','i','o','u','y','ä','ö']
# konsonanti="qwertzuiopšõüasdfghjklõäöüxcvbnm"
# markid=string.punctuation #!@#$%^&^*()_+{}|:"<>?[]\;',./
# v=k=m=t=0
# while True:
#     v=k=m=t=0
#     text=input("Sisesta tekst:").lower()
#     if text.isdigit():
#        break
#    else:
#        tekst_list=list(text)
#        print(tekst_list)
#        for that in tekst_list:
#            if that in vokaali:
#                v+=1
#            elif that in konsonanti:
#                k+=1
#            elif that in markid:
#                m+=1
#            else: that==" ": 
#                t+=1
# print("Vokaali: ",v)
# print("Konsonanti: ",k)
# print("Märkid: ",m)
# print("Tühikuid: ",t)

#2
# vanused=[]
# for i in range(7):
#     vanus=int(input(f"{i+1}.Sisesta vanus:"))
#     vanused.append(vanus)
#     print("Sisestatud vanused")
#     print(max(vanused))
#     print(min(vanused))
#     print(sum(vanused)/len(vanused))


# nimed=[]
# for i in range(5):
#     nimi=input(f"{i+1}.Sisesta nimi:")
#     nimed.append(nimi)
#     print("Enne sorteerimist")
#     print(nimed)
#     nimed.sort()
#     print("Sorteerimise parast")
#     print(f"Viimasena lisatud nimi on:{nimi}") #{nimi[4]}, {nimed[-1]}
#     v=input("Kas muudame nimeid?:").lower()
#     if v=="jah":
#         v=input("Nimi voi positsoon: N/P").upper()
#         if v=="P":
#             print("Sisesta nimi asukoht")

#             else
#             print("Sisesta nimi")
#             uus_nimi=input("Uus nimi")
#             v=nimed.index(uus_nimi)
#             nimed[v]=uus_nimi
#             print(nimed)
# dublta=list(set(nimed))
# print(dublta)


# #dublikatid 2

# dublta=[]
# for nimi in nimed:
#    if nimi 
# print("Mitte korduv loetelu 2.variant")
# dublta.append(nimi)
# print("Mitte korduv loetelu 2.variant")
# print(dublta)


#3
# from asyncio import AbstractEventLoop


# Vartused=[11,24,5,68,17]
# read=int(input("Reade kogus:"))
# for i in range(read):
#    arv=int(input("Arv:"))
#    Vartused.append(arv)
#     print(Vartused)
# s=input("Sumbol:")
# for vartus in Vartused:
#     print(vartus*s)

#     print()

#4
postiindeks = input("Postiindeks: ")

if not (postiindeks.isdigit() and len(postiindeks) == 5):
    print("Vale postiindeks.")
else:
    indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
 while 1:
        try:
            postiindeks=int(input("Sisesta postiindeks:"))
            if len(str(postiindeks))==5:
                break
            else
                print("On vaja 5 sumbolid")
         except:
                print("!!!")
 print("Postiindeksi analuus:")
 index_list=list(str(postiindeks)) #"1","2","3"
 s1=int(index_list[0]) #!
 print(f"Postindeks {postiindex} on {indexid[s1-1]} piirkond")


