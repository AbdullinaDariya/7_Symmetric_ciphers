# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:36:30 2019

@author: 181416
"""

def encrypt(key, str):
    sp1=[]
    sp2=[]
    for i in str:
        sp1.append((ord(i)+key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    shifr=''.join(sp2)   
    return shifr 

def decrypt(key, shifr):
    sp1=[]
    sp2=[]
    for i in shifr:
        sp1.append((ord(i)-key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    str=''.join(sp2)   
    return str

def hack(shifr):
    kol_vhod=[]
    for i in range(len(shifr)):
        kol_vhod.append([shifr.count(shifr[i]),shifr[i]])
        max=0
        for j in range(len(kol_vhod)):
            if kol_vhod[j][0] > max:
                max=kol_vhod[j][0]
                elmax=kol_vhod[j][1]
    key=ord(elmax)-ord(' ')%256
    sp1=[]
    sp2=[]
    for i in shifr:
        sp1.append((ord(i)-key)%256) 
    for i in range(len(sp1)):
        sp2.append(chr(sp1[i]))
    str=''.join(sp2)   
    return str
 
msg="be mime and it is all i want "
k=int(input("Введите ключ: "))
rez=encrypt(k,msg)
sh=decrypt(k,rez)
print(msg, "-Исходное")
print(rez, "-Закодированное")
print(sh, "-Раскодированное")

#введи мне предложение зашифрованное и я расшифрую без ключа
slovo=input("Введите зашифрованное предложение: ")
r=hack(slovo)
print("Я расшифровала его: ", r)