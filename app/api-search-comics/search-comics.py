import requests
import hashlib
from dotenv import load_dotenv
"""from config.config import url_search_comic, ts
import os 
from config.keys import PRIVATE_KEY, PUBLIC_KEY"""
#Esta url nos sirve para buscar por id del comic
url_search_comic_id = "https://gateway.marvel.com:443/v1/public/comics/"
#Según se necesite, esta url nos sirve para buscar comics de la A-Z, por titulo especifico o
#para un comic que "empice con"
url_search_comic_title = "https://gateway.marvel.com:443/v1/public/comics?"
                        
ts = 1

hashed = hashlib.md5( (str(ts) + PRIVATE_KEY + PUBLIC_KEY ).encode('utf-8')).hexdigest()
#Busqueda por id de comic################
comic_id = 1
comic_string = "comicId="+ str(comic_id)
#########################################

#Busqueda por titulo de comic############
title = "Savage Spider-Man"
title_string = "title=" + title
#########################################

#Busqueda por titulo "empieza con" ######
title_starts_with = "Spi"
title_starts_with_string = "titleStartsWith=" +title_starts_with
######################################### 
ts_string = "ts=" + str(ts)
ts_string_1 = "&ts=" + str(ts)
public_key_string = "&apikey=" + PUBLIC_KEY
hashed_string = "&hash=" + str(hashed)
complement = ts_string_1 + public_key_string + hashed_string
complement_A_Z = ts_string + public_key_string + hashed_string
url_id = url_search_comic_id +  "2?"+ complement
url_title = url_search_comic_title + title_string + complement
url_starts_with = url_search_comic_title + title_starts_with_string + complement
url_all = url_search_comic_title + complement_A_Z
print("URL_ID:")
print(url_id)
print("URL TITLE:")
print(url_title)
print("URL STARTS WITH:")
print(url_starts_with)
print("URL A-Z")
print(url_all)

