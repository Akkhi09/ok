import requests

url ='http://127.0.0.1:8000/celulares/Samsung'

def pegar_celular(modelo):
    n = 0
    res = requests.get(url)
    celulares = res.json()
    if res.status_code == 200:
        for c in celulares:
        # print(c['modelo'])
            if modelo.lower() in c['modelo'].lower():
                print(c['modelo'])
                res.content
                n+=1
        print(f"A API fornece {n} celulares desse modelo: {modelo.lower()}.")
    else:
        print("Erro: ", res.status_code, res.text)
#pegar_celular("Redmi")
res = requests.get(url)
for e in res.json():
    print(e['modelo'])