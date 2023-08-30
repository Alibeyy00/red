import requests
from bs4 import BeautifulSoup
import random
import string
import sys
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import warnings

# ------- SSL hata ayıklaması için
# Yani konsoldan gizlemek için 
def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)


sys.stderr = open('/dev/null', 'w')


print("""
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|""")
print("")

print("                        ENZA")

print("    Gemiler battı diye")

print("     Acırmı denizin canı..")
print("")



print("Created By TG: @dark_enza")
print("")



print("RedBull eSIM İnternet Generator")
print("")





device_id = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) for _ in range(5))  # Rastgele bir deviceId oluştur
kullan = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  # Rastgele bir isim oluştur (6 karakter)



eposta = input("[@]Eposta Gir: ")
print("[#]Şifre: zsezsert55")





url = "https://wndr.azurewebsites.net/api/v1/auth/registration/email"
headers = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "X-Device-ID": device_id,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}


data = {
    "deviceId": device_id,
    "name":  name ,
    "email": eposta,
    "password": "zsezsert55"
}
response = requests.post(url, headers=headers, json=data)

try:
	sonuc = response.json() == {}
	print("[+]Eposta Eklendi 🟢")
except:
	print("[-]Başarısız Admine ulaş TG: @dark_enza")
	raise SystemExit()

print("\n[•]Epostaya Git Ve Bağlantıyı Doğrula\n")
onay = input("Doğruladıysan Enter'e Bas: ")


if onay == "":
	print("Diğer Adıma Geçili")
else:
	print("Hata tekrar dene")

url2 = "https://wndr.azurewebsites.net/api/v1/auth/login/email"
headers2 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "X-Device-ID": device_id,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}

data2 = {
    "email": eposta,
    "password": "zsezsert55"
}

response2 = requests.post(url2, headers=headers2, json=data2)
sonuc2 = response2.json()
try:
	sonuc2 = response2.json()["accessToken"]
	print("[+]Token Çekildi 🟢")
except:
	print("[-]Token Çekilemedi Tekrar Dene🔴")
	raise SystemExit()






url3 = "https://wndr.azurewebsites.net/api/v1/packages/subscriber"
headers3 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "Authorization": "Bearer " + sonuc2,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "X-Device-ID": device_id,
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}
response3 = requests.post(url3, headers=headers3)
sonuc3 = response3.json()["subscriber_reference"]



url4 = f"https://wndr.azurewebsites.net/api/v1/packages/subscriber/{sonuc3}"
headers4 = {
        "X-Device-Model": "iPhone13,2",
        "Connection": "keep-alive",
        "Authorization": "Bearer " + sonuc2,
        "X-Device-Type": "iOS",
        "X-Accept-Version": "1.1",
        "X-Device-ID": device_id,
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "X-App-Version": "1.3.0",
        "Host": "wndr.azurewebsites.net",
        "Accept-Language": "en",
        "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
        "Accept": "*/*"
    }

response4 = requests.get(url4, headers=headers4)
sonuc4 = response4.json()


urlpromo = "https://wndr.azurewebsites.net/api/v1/promoCodes/assign"


promo_data = {"promocode": "TRAVELDEALZ"}
response_promo = requests.patch(urlpromo, headers=headers3, json=promo_data)

if response_promo.json() == {}:
	print("[+]1GB Eklendi")
else:
	print("[-]İnternet Eklenemedi")




time.sleep(5)
satın_al = "https://wndr.azurewebsites.net/api/v1/packages/order-free-package"

satınal_data = {"packageId": "mDFiwArRhFsEJVhTEd_XU"}
satınal = requests.post(satın_al, headers=headers3, json=satınal_data)
sonucc = satınal.json()

if sonucc == {}:
	print("[+]Paket Aktiflendi ")
else:
	print("[-]Paket Aktiflenmedi")



if 'simcard' in sonuc4 and 'smdp_address' in sonuc4['simcard'] and 'matching_id' in sonuc4['simcard']:
	smdp_address = sonuc4['simcard']['smdp_address']
	matching_id = sonuc4['simcard']['matching_id']
	print("")
	print("SM+DP:")
	print(smdp_address)
	print("")
	print("Etkinleştirme kodu:")
	print(matching_id)
	print("")
	print("Dark Enza Bol kullanımlar diler..")

