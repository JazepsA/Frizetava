import itertools
import datetime
from datetime import time

class Pakalpojums:

    Pakalpojuma_kategorija =""
    Pakalpojuma_nosaukums =""
    Pakalpojuma_atlaide =""
    Pakalpojuma_cena =0 


    id_iter= itertools.count()
    def __init__(self,pak_kat=None,pak_nos=None,pak_atl=None,pak_cena=10):
        self.pakalpojumaId=next(self.id_iter)+1
        self.pakalpojumaKategorija=pak_kat
        self.pakalpojumaNosaukums=pak_nos
        self.pakalpojumaAtlaide=pak_atl
        self.pakalpojumaCenaStunda=pak_cena
        self.laiksPieejams=True
    
    def __repr__(self):
        if self.pakalpojumaKategorija: return self.pak_kat
        elif self.pakalpojumaNosaukums: return self.pak_nos
        elif self.pakalpojumaAtlaide: return self.pak_atl
        elif self.pakalpojumaCenaStunda: return self.pak_cena
        return''
    
    def Pakalpojuma_info(self):
        return [
            self.pakalpojumaKategorija,self.pakalpojumaNosaukums,
            self.pakalpojumaAtlaide,self.pakalpojumaCenaStunda
        ]
    
    def Pakalpojuma_info_print(self):
        print("Pakalpojuma kategorija: "+ str(self.pakalpojumaKategorija))
        print("Pakalpojuma nosaukums: " + str(self.pakalpojumaNosaukums))
        print("Pakalpojuma atlaide: "+ str(self.pakalpojumaAtlaide))
        print("Pakalpojuma cena par stundu: " + str(self.pakalpojumaCenaStunda))
        print("Laiks pieejams: " + str(self.laiksPieejams) + "\n")

class Klients:
    Klienta_vards=""
    Klienta_uzvards=""
    Klienta_PK=""
    Klienta_tel_numurs=0

    id_iter_kl=itertools.count()

    def __init__(self,_vards,_uzvards,_pk,_tel_numurs):
        self.klientaId=next(self.id_iter_kl) + 1
        self.klientaVards=_vards
        self.klientaUzvards=_uzvards
        self.klientaPK= _pk
        self.klientaTelNumurs=_tel_numurs

    def Klientu_info(self):
        return [
            self.klientaVards,self.klientaUzvards,
            self.Klienta_PK,self.klientaTelNumurs
        ]

    def Klientu_info_print(self):
        print("Klienta vārds: "+ str(self.klientaVards))
        print("Klienta uzvārds: " + str(self.klientaUzvards))
        print("Klienta personas kods : "+ str(self.klientaPK))
        print("Klienta Tel. numurs : " + str(self.klientaTelNumurs))
 

class Izmantosana:
    Pakalpojuma_sakuma_laiks = 0
    Pakalpojuma_beigu_laiks = 0 
    Pakalpojuma_datums = 0
    Izmantosanas_cena_stunda = 10
    id_Pakalpojums = 0
    id_Klients = 0
    Izmantosana_id = 0

    id_iter_izmantosana = itertools.count()


    def Cena_kopa(self):
        kopeja_cena = self.Izmantosanas_cena_stunda * ((
            (self.Pakalpojuma_beigu_laiks - self.Pakalpojuma_sakuma_laiks)))
        return kopeja_cena
    
    def Izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks:" + str(self.Pakalpojuma_sakuma_laiks))
        print("Pakalpojuma beigu laiks : " + str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojuma id : " + str(self.id_Pakalpojums))
        print("Klienta id : "+ str(self.id_Klients))
        print("Pakalpojuma cena stunda,EUR : "+ str(self.Izmantosanas_cena_stunda) + "\n")


pak1=Pakalpojums("Matu griezšana","PieManis","20%","15")
pak2=Pakalpojums("Uzacu un skropstu krāsošana ","Uzacu krāsošana ","25%")
pak3=Pakalpojums("Kosmētikas procedūras ","Higiēniskā sejas tīrīšana ","25%")

kli1=Klients("Nikita","Arbuzov","430921-12314","12345578")
kli2=Klients("Dainis","Bernans","130915-64314","16754653")
kli3=Klients("Hubs","Diks","111021-79314","85662343")



#info par pakalpojumiem
print(pak1.pakalpojumaId)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.pakalpojumaId)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.pakalpojumaId)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()

#info par klientiem
print(kli1.klientaId)
kli1.Klientu_info()
kli1.Klientu_info_print()
print(kli2.klientaId)
kli2.Klientu_info()
kli2.Klientu_info_print()
print(kli3.klientaId)
kli3.Klientu_info()
kli3.Klientu_info_print()

