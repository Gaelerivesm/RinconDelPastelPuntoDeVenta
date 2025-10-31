# Esqueleto Rincón del Pastel 

harina = 500
azucar = 300
huevos = 100
pasteles_chocolate = 10
pasteles_vainilla = 15

print("BIENVENIDOS AL MENÚ PRINCIPAL DE RINCÓN DEL PASTEL") 

print("1. Registrar venta")
print("2. Consultar inventario")
print("3. Modo administrador")
print("4. Salir")
accion= input(print("Opcion deseada: "))

if accion == 2: 
    print("\n--- INVENTARIO ---")
    print("Harina:", harina, "g")
    print("Azúcar:", azucar, "g")
    print("Huevos:", huevos)
    print("Pasteles de chocolate:", pasteles_chocolate)
    print("Pasteles de vainilla:", pasteles_vainilla)
    
    # Alerta si ingredientes están bajos
    if harina < 200 or azucar < 200 or huevos < 5:
        print("Alerta: algún ingrediente está por agotarse.")

if accion == 1:
 print("\nREGISTRO DE VENTA")
 print("1. Pastel de Chocolate")
 print("2. Pastel de Vainilla")
    
opcion = input("Seleccione el pastel (1 o 2): ")
    
    # Validación básica de stock (Regla 1)
if opcion == "1":
    if pasteles_chocolate > 0:
            pasteles_chocolate -= 1  # Regla 2
            print("Venta registrada. Gracias por su compra.")
    else:
            print("No hay pasteles de chocolate disponibles.")
elif opcion == "2":
        if pasteles_vainilla > 0:
            pasteles_vainilla -= 1
            print("Venta registrada. Gracias por su compra.")
        else:
            print("No hay pasteles de vainilla disponibles.")
else:
        print("Opción inválida.")

# modo_administrador
clave = input("Ingrese la clave de administrador: ")
if clave == "admin123":
        print("Acceso permitido. Aquí se podrá agregar o modificar inventario.")
else:
        print("Acceso denegado. Solo el administrador puede acceder")

ejecutando = True
while ejecutando:
    print("mostrar_menu")
    opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
            registrar_venta()
    elif opcion == "2":
            consultar_inventario()
    elif opcion == "3":
            print("modo_administrador")
    elif opcion == "4":
            print("Saliendo del sistema... ¡Gracias!")
            ejecutando = False
    else:
            print("Opción no válida, intente de nuevo.")