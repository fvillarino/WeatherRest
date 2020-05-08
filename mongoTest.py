import pymongo 
import pprint
from AVWXRequest import CallMETAR

mongo_uri = "mongodb://localhost:27017/"  
client = pymongo.MongoClient(mongo_uri)

print(client.list_database_names())

WeatherMessageDB = client.WeatherMessage

print(WeatherMessageDB.list_collection_names())

MetarTable = WeatherMessageDB.metar

for metar in MetarTable.find():
    print(metar)

#Insertar nuevo Metar
response_json = CallMETAR('SAEZ')
new_metar = {'airport':'SAEZ',
             'METAR' : response_json['sanitized'] }
#insert = MetarTable.insert(new_metar)
MetarTable.insert(response_json)

for metar in MetarTable.find():
    print(metar)

