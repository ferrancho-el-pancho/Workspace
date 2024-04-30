import requests

# Realiza una llada a la API y guarda la respuesta.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
cabeceras = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=cabeceras)
print(f"Código de estado: {r.status_code}")


# Almacena en una variable la respuesta de la API.
diccionario_respuesta = r.json()
#print(f"Repositorios totales: {diccionario_respuesta['total_count']}")
print(diccionario_respuesta)

# Explora informacion sobre los repositorios.
diccionarios_repositorio = diccionario_respuesta['items']
#print(f"Repositories returned: {len(diccionarios_repositorio)}")


'''
print("\nInformación seleccionada sobre cada repositorio:")
for diccionario_repo in diccionarios_repositorio:
    print(f"Name: {diccionario_repo['name']}")
    print(f"Owner: {diccionario_repo['owner']['login']}")
    print(f"Stars: {diccionario_repo['stargazers_count']}")
    print(f"Repository: {diccionario_repo['html_url']}")
    print(f"Created: {diccionario_repo['created_at']}")
    print(f"Updated: {diccionario_repo['updated_at']}")
    print(f"Description: {diccionario_repo['description']}")
'''