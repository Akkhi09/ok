import requests

url ='http://127.0.0.1:8000/celulares'

def pegar_celular(modelo):
    n = 0
    res = requests.get(url)
    celulares = res.json()
    if res.status_code == 200:
        for c in celulares:
        # print(c['modelo'])
            if modelo in c['modelo']:
                print(c['modelo'])
                n+=1
        print(f"A API fornece {n} celulares desse modelo")
    else:
        print("Erro: ", res.status_code, res.text)
pegar_celular("Galaxy")