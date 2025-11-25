# ======= INVENTARIO =======
ingredientes = {
    "harina": {"cantidad": 10, "costo": 12},
    "azucar": {"cantidad": 8, "costo": 10},
    "huevo": {"cantidad": 30, "costo": 2}
}

pasteles = {
    "Chocolate": {
        "ingredientes": {"harina": 2, "azucar": 1, "huevo": 3},
        "ganancia": 0.30
    }
}
# ======= PEDIDOS =======
pedidos = []

# ====== FUNCIONES EN INGREDIENTES ======
def agregar_ingrediente(nombre, cantidad, costo):
    if nombre in ingredientes:
        print("El ingrediente ya existe.")
        return
    ingredientes[nombre] = {"cantidad": cantidad, "costo": costo}
    print("Ingrediente agregado.")

def modificar_ingrediente(nombre, nueva_cantidad=None, nuevo_costo=None):
    if nombre not in ingredientes:
        print("El ingrediente no existe.")
        return
    if nueva_cantidad is not None:
        ingredientes[nombre]["cantidad"] = nueva_cantidad
    if nuevo_costo is not None:
        ingredientes[nombre]["costo"] = nuevo_costo
    print("Ingrediente modificado.")

def eliminar_ingrediente(nombre):
    if nombre not in ingredientes:
        print("El ingrediente no existe.")
        return
    del ingredientes[nombre]
    print("Ingrediente eliminado.")

# ======= PASTELES =======
def agregar_pastel(nombre, ingredientes_usados, ganancia):
    if nombre in pasteles:
        print("Ese pastel ya existe.")
        return
    pasteles[nombre] = {"ingredientes": ingredientes_usados, "ganancia": ganancia}
    print("Pastel agregado.")

def modificar_pastel(nombre, nuevos_ingredientes=None, nueva_ganancia=None):
    if nombre not in pasteles:
        print("Ese pastel no existe.")
        return
    if nuevos_ingredientes is not None:
        pasteles[nombre]["ingredientes"] = nuevos_ingredientes
    if nueva_ganancia is not None:
        pasteles[nombre]["ganancia"] = nueva_ganancia
    print("Pastel modificado.")

def eliminar_pastel(nombre):
    if nombre not in pasteles:
        print("Ese pastel no existe.")
        return
    del pasteles[nombre]
    print("Pastel eliminado.")

# ======= CALCULAR PRECIO =======
def calcular_precio_pastel(nombre_pastel):
    pastel = pasteles[nombre_pastel]
    costo_total = 0
    for ing, cant in pastel["ingredientes"].items():
        costo_total += ingredientes[ing]["costo"] * cant
    precio_final = costo_total * (1 + pastel["ganancia"])
    precio_final *= 1.16  # IVA
    return precio_final

# ======= REGISTRO DE PEDIDOS =======
from datetime import datetime

def registrar_pedido(cliente, tipo_pastel, cantidad, metodo_pago):
    if tipo_pastel not in pasteles:
        print("Ese pastel no existe.")
        return
    for ing, cant in pasteles[tipo_pastel]["ingredientes"].items():
        if ingredientes[ing]["cantidad"] < cant * cantidad:
            print("Ingrediente insuficiente:", ing)
            return
    for ing, cant in pasteles[tipo_pastel]["ingredientes"].items():
        ingredientes[ing]["cantidad"] -= cant * cantidad
    total = calcular_precio_pastel(tipo_pastel) * cantidad
    pedidos.append({
        "cliente": cliente,
        "pastel": tipo_pastel,
        "cantidad": cantidad,
        "total": total,
        "pago": metodo_pago,
        "fecha": datetime.now()
    })
    print("Pedido registrado. Total:", total)

