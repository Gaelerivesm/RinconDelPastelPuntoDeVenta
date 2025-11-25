# Esqueleto Rincón del Pastel
# FALTAN SEPARADORES ENTRE SECCIONES, PERO TODO FUNCIONA BIEN
harina = 500
azucar = 300
huevos = 100
pasteles_chocolate = 10
pasteles_vainilla = 15

while True:
    print("BIENVENIDOS AL MENÚ PRINCIPAL DE RINCÓN DEL PASTEL")
    print("1. Registrar venta")
    print("2. Consultar inventario")
    print("3. Modo administrador")
    print("4. Salir")
    accion = input("Opción deseada: ")

    if accion == "2":
        print("\n--- INVENTARIO ---")
        print("Harina:", harina, "g")
        print("Azúcar:", azucar, "g")
        print("Huevos:", huevos)
        print("Pasteles de chocolate:", pasteles_chocolate)
        print("Pasteles de vainilla:", pasteles_vainilla)
        if harina < 200 or azucar < 200 or huevos < 5:
            print("Alerta: algún ingrediente está por agotarse.")

    elif accion == "1":
        while True:
            print("\nREGISTRO DE VENTA")
            print("1. Pastel de Chocolate")
            print("2. Pastel de Vainilla")
            opcion = input("Seleccione el pastel (1 o 2): ")
            if opcion == "1":
                if pasteles_chocolate > 0:
                    pasteles_chocolate -= 1
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
            break

    elif accion == "3":
        while True:
            clave = input("Ingrese la clave de administrador: ")
            if clave == "python123":
                print("Acceso permitido. Aquí se podrá agregar o modificar inventario.")
                while True:
                    print("¿Qué quieres hacer?")
                    print("1. Agregar")
                    print("2. Modificar")
                    print("3. Eliminar")
                    print("4. Salir")
                    admin = input("Opción deseada: ")

                    if admin == "1":
                        print("\n--- AGREGAR AL INVENTARIO ---")
                        print("1. Harina")
                        print("2. Azúcar")
                        print("3. Huevos")
                        print("4. Pasteles de chocolate")
                        print("5. Pasteles de vainilla")
                        opcion_add = input("Seleccione el ingrediente o producto: ")

                        if opcion_add == "1":
                            cantidad = int(input("¿Cuántos gramos de harina agregarás?: "))
                            harina += cantidad
                            print("Se agregaron", cantidad, "g de harina.")
                        elif opcion_add == "2":
                            cantidad = int(input("¿Cuántos gramos de azúcar agregarás?: "))
                            azucar += cantidad
                            print("Se agregaron", cantidad, "g de azúcar.")
                        elif opcion_add == "3":
                            cantidad = int(input("¿Cuántos huevos agregarás?: "))
                            huevos += cantidad
                            print("Se agregaron", cantidad, "huevos.")
                        elif opcion_add == "4":
                            cantidad = int(input("¿Cuántos pasteles de chocolate agregarás?: "))
                            pasteles_chocolate += cantidad
                            print("Se agregaron", cantidad, "pasteles de chocolate.")
                        elif opcion_add == "5":
                            cantidad = int(input("¿Cuántos pasteles de vainilla agregarás?: "))
                            pasteles_vainilla += cantidad
                            print("Se agregaron", cantidad, "pasteles de vainilla.")

                    elif admin == "2":
                        print("\n--- INVENTARIO ---")
                        print("1. Harina:", harina, "g")
                        print("2. Azúcar:", azucar, "g")
                        print("3. Huevos:", huevos)
                        print("4. Pasteles de chocolate:", pasteles_chocolate)
                        print("5. Pasteles de vainilla:", pasteles_vainilla)
                        opcionadmin = input("Opción deseada: ")
                        if opcionadmin == "1":
                            harina = int(input("¿Cuántos gramos de harina quedan?: "))
                        elif opcionadmin == "2":
                            azucar = int(input("¿Cuántos gramos de azúcar quedan?: "))
                        elif opcionadmin == "3":
                            huevos = int(input("¿Cuántos huevos quedan?: "))
                        elif opcionadmin == "4":
                            pasteles_chocolate = int(input("¿Cuántos pasteles de chocolate quedan?: "))
                        elif opcionadmin == "5":
                            pasteles_vainilla = int(input("¿Cuántos pasteles de vainilla quedan?: "))

                    elif admin == "3":
                        print("\n--- ELIMINAR DEL INVENTARIO ---")
                        print("1. Harina")
                        print("2. Azúcar")
                        print("3. Huevos")
                        print("4. Pasteles de chocolate")
                        print("5. Pasteles de vainilla")
                        opcion_del = input("Seleccione el ingrediente o producto a eliminar: ")

                        if opcion_del == "1":
                                cantidad = int(input("¿Cuántos gramos de harina eliminarás?: "))
                                if cantidad <= harina:
                                        harina -= cantidad
                                else:
                                        print("No hay suficiente harina. Se elimina todo lo disponible.")
                                        harina = 0
                                print("Quedan", harina, "g de harina.")

                        elif opcion_del == "2":
                                cantidad = int(input("¿Cuántos gramos de azúcar eliminarás?: "))
                                if cantidad <= azucar:
                                        azucar -= cantidad
                                else:
                                        print("No hay suficiente azúcar. Se elimina todo lo disponible.")
                                        azucar = 0
                                        print("Quedan", azucar, "g de azúcar.")

                        elif opcion_del == "3":
                                cantidad = int(input("¿Cuántos huevos eliminarás?: "))
                                if cantidad <= huevos:
                                        huevos -= cantidad
                                else:
                                        print("No hay suficientes huevos. Se elimina todo lo disponible.")
                                        huevos = 0
                                print("Quedan", huevos, "huevos.")

                        elif opcion_del == "4":
                                cantidad = int(input("¿Cuántos pasteles de chocolate eliminarás?: "))
                                if cantidad <= pasteles_chocolate:
                                        pasteles_chocolate -= cantidad
                                else:
                                        print("No hay suficientes pasteles de chocolate. Se elimina todo lo disponible.")
                                        pasteles_chocolate = 0
                                print("Quedan", pasteles_chocolate, "pasteles de chocolate.")

                        elif opcion_del == "5":
                                cantidad = int(input("¿Cuántos pasteles de vainilla eliminarás?: "))
                                if cantidad <= pasteles_vainilla:
                                        pasteles_vainilla -= cantidad
                                else:
                                        print("No hay suficientes pasteles de vainilla. Se elimina todo lo disponible.")
                                        pasteles_vainilla = 0
                                print("Quedan", pasteles_vainilla, "pasteles de vainilla.")


                    elif admin == "4":
                        break
                break
            else:
                print("Acceso denegado. Solo el administrador puede acceder.")

    elif accion == "4":
        print("Programa finalizado, muchas gracias por utilizar.")
        break
