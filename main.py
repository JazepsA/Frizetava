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

pak1=Pakalpojums("Matu griezšana","PieManis","20%","15")
pak2=Pakalpojums("Uzacu un skropstu krāsošana ","Uzacu krāsošana ","25%")
pak3=Pakalpojums("Kosmētikas procedūras ","Higiēniskā sejas tīrīšana ","25%")

print(pak1.pakalpojumaId)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.pakalpojumaId)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.pakalpojumaId)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()