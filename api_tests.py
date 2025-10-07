import requests

BASE_URL = "http://127.0.0.1:8000/api/items/"

def print_result(title, response):
    status = "Correcto!" if response.status_code in [200, 201, 204] else "Fallido!"
    print(f"{status} {title} -> Status: {response.status_code}")
    if response.text:
        try:
            print(response.json(), "\n")
        except Exception:
            print(response.text, "\n")

def listar_items():
    r = requests.get(BASE_URL)
    print_result("GET LIST (listar_items)", r)

def crear_item():
    data = {"nombre": "Mouse", "descripcion": "Logitech MX Master 3"}
    r = requests.post(BASE_URL, json=data)
    print_result("POST (crear_item)", r)
    return r.json().get("id") if r.status_code == 201 else None

def consultar_item(item_id):
    r = requests.get(BASE_URL + f"{item_id}/")
    print_result(f"GET ONE (consultar_item id={item_id})", r)

def actualizar_item(item_id):
    data = {"nombre": "Mouse actualizado", "descripcion": "Logitech MX Master 3s"}
    r = requests.put(BASE_URL + f"{item_id}/", json=data)
    print_result(f"PUT (actualizar_item id={item_id})", r)

def actualizar_parcial(item_id):
    data = {"descripcion": "Actualizado parcialmente con PATCH"}
    r = requests.patch(BASE_URL + f"{item_id}/", json=data)
    print_result(f"PATCH (actualizar_parcial id={item_id})", r)

def borrar_item(item_id):
    r = requests.delete(BASE_URL + f"{item_id}/")
    print_result(f"DELETE (borrar_item id={item_id})", r)

if __name__ == "__main__":
    print("Iniciando pruebas de API REST\n")

    listar_items()
    nuevo_id = crear_item()

    if nuevo_id:
        consultar_item(nuevo_id)
        actualizar_item(nuevo_id)
        actualizar_parcial(nuevo_id)
        borrar_item(nuevo_id)

    listar_items()

    print("Pruebas finalizadas")
