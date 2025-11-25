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
