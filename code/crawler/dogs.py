from pymongo import MongoClient
import os
import json

client = MongoClient()
db = client.dogs
col = db.Dogs


#TODO: czyszczenie kolekcji przed dodaniem, col.delete() albo coś takiego
#TODO: graficzna reprezentacja wynikow np. Flask

rootdir = 'data\\fci\dump'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.json'):
            with open(subdir+'\\'+file) as data_file:
                data = json.load(data_file)
                col.insert_one(data)
#TODO: parsowanie PDF i wrzucanie go do bazy danych do Dogs. JSON musi miec pole nowe.
print(col.find())

# {
#   "country": "GREAT BRITAIN",
#   "name": "ENGLISH POINTER",
#   "pdf": "http://www.fci.be/Nomenclature/Standards/001g07-en.pdf",
#   "refid": "1",
#   "section": "British and Irish Pointers and Setters",
#   "thumb": "http://www.fci.be/Nomenclature/Illustrations/001g07.jpg",
#   "url": "http://www.fci.be/en/nomenclature/ENGLISH-POINTER-1.html",
#   "pdf": {
#         "pole1" : "abc",
#         "pole2" : "abc",
#         "pole3" : "abc",
#   }
# }


