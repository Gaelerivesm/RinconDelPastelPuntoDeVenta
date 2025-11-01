# Inventario 
harina = 500
azucar = 300
huevos = 100
pasteles_chocolate = 10
pasteles_vainilla = 15


ejecutando = True
while ejecutando:
    print("\nMENÚ PRINCIPAL - RINCÓN DEL PASTEL")
    print("1. Registrar venta")
    print("2. Consultar inventario")
    print("3. Modo administrador")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nREGISTRO DE VENTA")
        print("1. Pastel de Chocolate")
        print("2. Pastel de Vainilla")
        tipo_pastel = input("Seleccione el pastel (1 o 2): ")

        if tipo_pastel == "1":
            if pasteles_chocolate > 0:
                pasteles_chocolate = pasteles_chocolate - 1
                print("Venta registrada. Gracias por su compra.")
            else:
                print("No hay pasteles de chocolate disponibles.")
        elif tipo_pastel == "2":
            if pasteles_vainilla > 0:
                pasteles_vainilla = pasteles_vainilla - 1
                print("Venta registrada. Gracias por su compra.")
            else:
                print("No hay pasteles de vainilla disponibles.")
        else:
            print("Opción inválida.")

    elif opcion == "2":
        print("\n--- INVENTARIO ---")
        print("Harina:", harina, "g")
        print("Azúcar:", azucar, "g")
        print("Huevos:", huevos)
        print("Pasteles de chocolate:", pasteles_chocolate)
        print("Pasteles de vainilla:", pasteles_vainilla)

        if harina < 200 or azucar < 200 or huevos < 5:
            print("Alerta: algún ingrediente está por agotarse.")

    elif opcion == "3":
        clave = input("Ingrese la clave de administrador: ")
        if clave == "admin123":
            print("Acceso permitido. Aquí se podrá modificar el inventario.")
            print("1. Agregar ingredientes")
            print("2. Agregar pasteles")
            admin_opcion = input("Seleccione una opción: ")

            if admin_opcion == "1":
                nueva_harina = int(input("Cantidad de harina a agregar (g): "))
                nueva_azucar = int(input("Cantidad de azúcar a agregar (g): "))
                nuevos_huevos = int(input("Cantidad de huevos a agregar: "))
                harina = harina + nueva_harina
                azucar = azucar + nueva_azucar
                huevos = huevos + nuevos_huevos
                print("Ingredientes actualizados.")
            elif admin_opcion == "2":
                nuevos_chocolate = int(input("Cantidad de pasteles de chocolate a agregar: "))
                nuevos_vainilla = int(input("Cantidad de pasteles de vainilla a agregar: "))
                pasteles_chocolate = pasteles_chocolate + nuevos_chocolate
                pasteles_vainilla = pasteles_vainilla + nuevos_vainilla
                print("Pasteles actualizados.")
            else:
                print("Opción inválida.")
        else:
            print("Acceso denegado. Solo el administrador puede acceder.")

    elif opcion == "4":
        print("Saliendo del sistema... Gracias.")
        ejecutando = False

    else:
        print("Opción no válida. Intente de nuevo.")