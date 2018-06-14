from pymongo import MongoClient
import os
import json
import PyPDF2
import ast

client = MongoClient()
client.drop_database("dogs")
db = client.dogs
col = db.Dogs
col.drop

#TODO: czyszczenie kolekcji przed dodaniem, col.delete() albo coś takiego
#TODO: graficzna reprezentacja wynikow np. Flask

rootdir = 'data\\fci\dump'

for subdir, dirs, files in os.walk(rootdir): 
    data = {}
    for file in files: 
        if file.endswith('.json'):
            with open(subdir+'\\'+file) as data_file:
                dataform = str(data_file).strip("'<>() ").replace('\'', '\"')
                datas = json.load(data_file)
                data["info"] = datas
        else:
            pdfFileObj = open(subdir+'\\'+file,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            dict = {}
            for page in pdfReader.pages:
                test = page.extractText().split("\n \n")
                for string in test:
                    if ":"  in string:
                        splitted = string.replace('.','').replace('\n','').strip().split(":")
                        dict[splitted[0]] = splitted[1]
            #t = json.dumps(dict)
            data["pdf"] = dict
    col.insert_one(data)
    print(str(subdir) +"\n")
#TODO: parsowanie PDF i wrzucanie go do bazy danych do Dogs. JSON musi miec pole nowe.
print(col.find())

# {
#   "info":
#       {
#         "country": "GREAT BRITAIN",
#         "name": "ENGLISH POINTER",
#         "pdf": "http://www.fci.be/Nomenclature/Standards/001g07-en.pdf",
#         "refid": "1",
#         "section": "British and Irish Pointers and Setters",
#         "thumb": "http://www.fci.be/Nomenclature/Illustrations/001g07.jpg",
#         "url": "http://www.fci.be/en/nomenclature/ENGLISH-POINTER-1.html"         
#       },

#   "pdf": 
#       {
#         "pole1" : "abc",
#         "pole2" : "abc",
#         "pole3" : "abc",
#       }
#}

