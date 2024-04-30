
import requests,json

#url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"
url="https://opendata.aemet.es/opendata/api/observacion/convencional/todas"
metadatos="https://opendata.aemet.es/opendata/sh/55c2971b"
datos="https://opendata.aemet.es/opendata/sh/97e2876e"
#url="https://opendata.aemet.es/opendata/api/prediccion/especifica/montaña/pasada/area/{cat1}"
querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZXJyYW5sbGFmQGdtYWlsLmNvbSIsImp0aSI6IjU5MmRlYjBmLTA2MjMtNGZhYy1iNWI5LWFiZjk2NzEwYzY3ZSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzEzNTE4ODYxLCJ1c2VySWQiOiI1OTJkZWIwZi0wNjIzLTRmYWMtYjViOS1hYmY5NjcxMGM2N2UiLCJyb2xlIjoiIn0.I2J4_IZg2j9pGax016oMnfzaRGN98rG9N1VC2cO69A0"}

headers = {
    'cache-control': "no-cache"
    }

#response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.request("GET", datos, headers=headers, params=querystring)
#print(response.text)

diccionario_respuesta = response.json()
#print(f"Repositorios totales: {diccionario_respuesta['total_count']}")
print(diccionario_respuesta)
fichero_legible = 'metadatos_aemet_legible.json'

with open(fichero_legible, 'w') as f:
          json.dump(diccionario_respuesta,f,indent=4)


