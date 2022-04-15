from operator import imod
import numpy as np
import folium
import phonenumbers
import os
from phonenumbers import carrier, geocoder
from phonenumbers.phonenumberutil import number_type
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv

config = load_dotenv(".env")

num = input("Insira o numero de telefone, não se esqueça do código do pais: ")

KEY_ENV = os.environ.get('KEY_ENV')

# Estado

ch_number = phonenumbers.parse(num)
yourLocation = geocoder.description_for_number(ch_number, "br")
print(yourLocation)

# Operadora

service_number = phonenumbers.parse(num)
print(carrier.name_for_number(service_number, "br"))

# Lat Long
geocoder = OpenCageGeocode(key=KEY_ENV)

query = str(yourLocation)
results = geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

# Salvar em HTML file

myMap.save("myLocation.html")
