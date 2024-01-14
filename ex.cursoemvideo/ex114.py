#Tentei com webbrowser
#Tentei com requests
import requests

try:    
    site = requests.get("https://g1.globo.com/")
except:
    print('Site nao acessivel')
else:
    print('Site acessivel')
