import requests

BASE_URL = "http://127.0.0.1:8000/api/items/"

def listar_items():
    r = requests.get(BASE_URL)
    print("GET LIST:", r.status_code)
    print(r.json(), "\n")

def crear_item():
    data = {"nombre": "Mouse", "descripcion": "Logitech MX Master 3"}
    r = requests.post(BASE_URL, json=data)
    print("POST (crear):", r.status_code)
    print(r.json(), "\n")
    return r.json().get("id")  # ID creado

def consultar_item(item_id):
    r = requests.get(BASE_URL + f"{item_id}/")
    print(f"GET ONE (id={item_id}):", r.status_code)
    print(r.json(), "\n")

def actualizar_item(item_id):
    data = {"nombre": "Mouse actualizado", "descripcion": "Logitech MX Master 3s"}
    r = requests.put(BASE_URL + f"{item_id}/", json=data)
    print(f"PUT (id={item_id}):", r.status_code)
    print(r.json(), "\n")

def borrar_item(item_id):
    r = requests.delete(BASE_URL + f"{item_id}/")
    print(f"DELETE (id={item_id}):", r.status_code, "\n")

if __name__ == "__main__":
    listar_items()
    nuevo_id = crear_item()
    consultar_item(nuevo_id)
    actualizar_item(nuevo_id)
    borrar_item(nuevo_id)
    listar_items()