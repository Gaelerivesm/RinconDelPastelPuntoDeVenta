import csv
from datetime import datetime

archivo_ingredientes = "ingredientes.csv"
archivo_pasteles = "pasteles.csv"
archivo_pedidos = "pedidos.csv"

# ======= INVENTARIO =======
ingredientes = {}
pedidos = []
pasteles = {}

    #================ Guardar en archivo csv =============
def guardar_ingredientes():
    with open(archivo_ingredientes, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "cantidad", "costo"])
        for nombre, datos in ingredientes.items():
            writer.writerow([nombre, datos["cantidad"], datos["costo"]])

def cargar_ingredientes():
    try:
        with open(archivo_ingredientes, "r") as f:
            reader = csv.DictReader(f)
            ingredientes.clear()
            for row in reader:
                ingredientes[row["nombre"]] = {
                    "cantidad": int(row["cantidad"]),
                    "costo": float(row["costo"])
                }
    except FileNotFoundError:
        return

def guardar_pasteles():
    with open(archivo_pasteles, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "ingredientes", "ganancia"])
        for nombre, datos in pasteles.items():
            ing_str = ";".join(f"{k}:{v}" for k, v in datos["ingredientes"].items())
            writer.writerow([nombre, ing_str, datos["ganancia"]])

def cargar_pasteles():
    try:
        with open(archivo_pasteles, "r") as f:
            reader = csv.DictReader(f)
            pasteles.clear()
            for row in reader:
                ingredientes_usados = {}
                if row["ingredientes"]:
                    for parte in row["ingredientes"].split(";"):
                        k, v = parte.split(":")
                        ingredientes_usados[k] = int(v)

                pasteles[row["nombre"]] = {
                    "ingredientes": ingredientes_usados,
                    "ganancia": float(row["ganancia"])
                }
    except FileNotFoundError:
        return
    
def guardar_pedidos():
    with open(archivo_pedidos, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["cliente", "pastel", "cantidad", "total", "pago", "fecha"])
        for p in pedidos:
            writer.writerow([
                p["cliente"],
                p["pastel"],
                p["cantidad"],
                p["total"],
                p["pago"],
                p["fecha"].isoformat()
            ])

def cargar_pedidos():
    try:
        with open(archivo_pedidos, "r") as f:
            reader = csv.DictReader(f)
            pedidos.clear()
            for row in reader:
                try:
                    fecha = datetime.fromisoformat(row["fecha"])
                except:
                    fecha = row["fecha"]
                pedidos.append({
                    "cliente": row["cliente"],
                    "pastel": row["pastel"],
                    "cantidad": int(row["cantidad"]),
                    "total": float(row["total"]),
                    "pago": row["pago"],
                    "fecha": fecha
                })
    except FileNotFoundError:
        return


    # ====== FUNCIONES EN INGREDIENTES ======
def agregar_ingrediente():
    nombre = input("Nombre del ingrediente: ").strip()
    if nombre in ingredientes:
        print("El ingrediente ya existe.")
        return
    cantidad = int(input("Cantidad inicial (enteros): "))
    costo = float(input("Costo por unidad (número): "))
    ingredientes[nombre] = {"cantidad": cantidad, "costo": costo}
    guardar_ingredientes()

def modificar_ingrediente():
    nombre = input("Nombre del ingrediente a modificar: ").strip()
    if nombre not in ingredientes:
        print("El ingrediente no existe.")
        return
    entrada = int(input("Nueva cantidad (deja en blanco para no cambiar): "))
    entrada = int(input("Nuevo costo (deja en blanco para no cambiar): "))
    ingredientes[nombre]["costo"] = float(entrada)
    guardar_ingredientes()
    print("Ingrediente modificado.")

def eliminar_ingrediente():
    nombre = input("Nombre del ingrediente a eliminar: ").strip()
    if nombre not in ingredientes:
        print("El ingrediente no existe.")
        return
    del ingredientes[nombre]
    guardar_ingredientes()
    print("Ingrediente eliminado.")


## Esto de aca es para ingresar ingredientes en la parte de agregar pastel##

def pedir_ingredientes_para_pastel():
    print("Introduce los ingredientes uno por uno.")
    print("Usa el formato: nombre cantidad")
    print("Ejemplo: harina 2")
    print("Cuando termines, deja vacío y presiona ENTER.")

    ingredientes_usados = {}

    while True:
        linea = input("Ingrediente: ").strip()

        if linea == "":
            break

        partes = linea.split()

        if len(partes) != 2:
            print("Formato inválido. Usa: nombre cantidad")
            continue

        nombre_ing = partes[0]

        try:
            cantidad_ing = int(partes[1])
        except:
            print("La cantidad debe ser un número.")
            continue

        ingredientes_usados[nombre_ing] = cantidad_ing

    return ingredientes_usados

    # ======= PASTELES =======
def agregar_pastel():
    nombre = input("Introduce el nombre del pastel a agregar")
    if nombre in pasteles:
        print("Ese pastel ya existe.")
        return

    ingredientes_usados = pedir_ingredientes_para_pastel()
    ganancia = int(input("Introduce la ganancia"))
    pasteles[nombre] = {"ingredientes": ingredientes_usados, "ganancia": ganancia}

    guardar_pasteles()
    print("Pastel agregado.")

def modificar_pastel():
    nombre = input("Introduce el nombre del pastel a modificar")
    if nombre not in pasteles:
        print("Ese pastel no existe.")
        return
    
    print(f"\nModificando pastel: {nombre}")
    print("Ingredientes actuales:")
    for ing, cant in pasteles[nombre]["ingredientes"].items():
        print(f" - {ing}: {cant}")

    print("\n¿Quieres modificar los ingredientes?")
    print("1 = Sí")
    print("ENTER = No (dejar igual)")
    op = input("Opción: ").strip()

    if op == "1":
        print("\nIntroduce los nuevos ingredientes:")
        nuevos_ing = pedir_ingredientes_para_pastel()
        pasteles[nombre]["ingredientes"] = nuevos_ing
        print("Ingredientes actualizados.")
    
    print(f"\nGanancia actual: {pasteles[nombre]['ganancia']}")
    nueva_g = input("Nueva ganancia (ENTER para dejar igual): ").strip()

    if nueva_g != "":
        try:
            pasteles[nombre]["ganancia"] = float(nueva_g)
            print("Ganancia actualizada.")
        except:
            print("Ganancia inválida, no se modificó.")

    guardar_pasteles()
    print("\nPastel modificado correctamente.")

def eliminar_pastel():
    nombre = input("Introduce el nombre del pastel a eliminar: ")
    if nombre not in pasteles:
        print("No existe ese pastel.")
        return
    del pasteles[nombre]
    guardar_pasteles()
    print("Pastel eliminado.")

    # ======= CALCULAR PRECIO =======
def calcular_precio_pastel():
    nombre_pastel = input("Introduce el nombre del pastel a calcular: ")
    pastel = pasteles[nombre_pastel]
    costo_total = 0
    for ing, cant in pastel["ingredientes"].items():
        costo_total += ingredientes[ing]["costo"] * cant
    precio_final = costo_total * (1 + pastel["ganancia"])
    precio_final *= 1.16  # IVA
    return precio_final
def calcular_precio_pastelel(nombre_pastel):
    pastel = pasteles[nombre_pastel]
    costo_total = 0
    for ing, cant in pastel["ingredientes"].items():
        costo_total += ingredientes[ing]["costo"] * cant
    precio_final = costo_total * (1 + pastel["ganancia"])
    precio_final *= 1.16  # IVA
    return precio_final

    # ======= REGISTRO DE PEDIDOS =======
def registrar_pedido():
    cliente = input("Cliente: ")
    tipo_pastel = input("Pastel: ")
    cantidad = int(input("Cantidad: "))
    metodo_pago = input("Método de pago: ")
    if tipo_pastel not in pasteles:
        print("Ese pastel no existe.")
        return
    for ing, cant in pasteles[tipo_pastel]["ingredientes"].items():
        if ingredientes[ing]["cantidad"] < cant * cantidad:
            print("Ingrediente insuficiente:", ing)
            return
    for ing, cant in pasteles[tipo_pastel]["ingredientes"].items():
        ingredientes[ing]["cantidad"] -= cant * cantidad
    total = calcular_precio_pastelel(tipo_pastel) * cantidad
    pedidos.append({
        "cliente": cliente,
        "pastel": tipo_pastel,
        "cantidad": cantidad,
        "total": total,
        "pago": metodo_pago,
        "fecha": datetime.now()
    })
    guardar_ingredientes()
    guardar_pedidos()
    print("cliente: ", cliente,"\npastel: ", tipo_pastel,"\ncantidad: ", cantidad,"\ntotal: ", total,"\nMetodo de pago: ", metodo_pago,"\nfecha: ", datetime.now())

# ======= CONSULTAS =======
def mostrar_inventario():
    print("Inventario:")
    for ing, datos in ingredientes.items():
        print(f"{ing}: {datos['cantidad']} unidades, costo {datos['costo']}")

def mostrar_pedidos():
    print("Pedidos registrados:")
    for p in pedidos:
        print(f"{p['fecha']} - Cliente: {p['cliente']} - {p['cantidad']}x {p['pastel']} - Total: {p['total']}")

def mostrar_pasteles():
    print("\n--- Pasteles ---")
    for nombre, datos in pasteles.items():
        ing_str = ", ".join(f"{k}:{v}" for k, v in datos["ingredientes"].items())
        print(f"{nombre} -> {ing_str} | ganancia: {datos['ganancia']}")

cargar_ingredientes()
cargar_pasteles()
cargar_pedidos()
#Estas van a ser las opciones a elegir en el codigo final
while True:
    print("==== Menú Pastelería ====")
    print("1) Mostrar inventario")
    print("2) Agregar ingrediente")
    print("3) Modificar ingrediente")
    print("4) Eliminar ingrediente")
    print("5) Mostrar pasteles")
    print("6) Agregar pastel")
    print("7) Modificar pastel")
    print("8) Eliminar pastel")
    print("9) Registrar pedido")
    print("10) Mostrar pedidos")
    print("11) Calcular precio (1 unidad)")
    print("0) Guardar y salir")
    opcion = input("Elige una opción: ")