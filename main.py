import os
try :
    import requests
except :
    os.system ('pip install requests')
os.system ('clear')
bin = input ("Enter Your Bin : ")
a = requests.get ("https://bin-checker.net/api/"+bin)
bank = a.json()
b1 = bank["scheme"]
b2 = bank["type"]
b3 = bank["level"]
b4 = bank["country"]["code"]
b5 = bank["country"]["name"]
b6 = bank["bank"]["name"]
b7 = bank["bank"]["website"]
b8 = bank["bank"]["phone"]
print ("NETWORK : "+b1)
print ("TYPE : "+b2)
print ("LEVEL : "+b3)
print ("COUNTRY CODE : "+b4)
print ("COUNTRY NAME : "+b5)
print ("BANK NAME : "+b6)
print ("WEBSITE : "+b7)
print ("PHONE : "+b8)

