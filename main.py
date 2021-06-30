num = [0, 1]
producto = ["Coca-cola", "Leche"]
inventario = [10, 13]
preciodc = [23, 43]
preciodv = [34, 50]
unive = [12, 2]
ventas = [1.1, 2]
ventast = None
cantidad = 2

print("Bienvenido a la lista de articulos de la tienda,")
print("Seleccione una de las siguientes opciones para realizar un cambio a la lista")

if cantidad <= 100:
    while True:
        print("1.- Agregar nuevo articulo")
        print("2.- Agregar compra (aumenta inventario)")
        print("3.- Ver listado")
        print("4.- Buscar ")
        print("5.- Agregar venta")
        print("6.- Eliminar ")
        print("7.- Ventas Totales ")
        print("0.- Salir ")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            num.append(cantidad-1)
            producto.append(input("Nombre del articulo: "))
            inventario.append(int(input("Numero de unidades: ")))
            preciodc.append(int(input("Precio de Compra: ")))
            preciodv.append((int(input("Precio de venta "))))
            unive.append(float(input("(float)Unidades vendidas ")))
            ventas.append(float(input("(float)Ventas totales del articulo")))
            cantidad += 1

            input("Enter para continual...")


        elif opcion == 2:
          d = int(input("ID del Articulo? "))
          b =int(input("Ingrese que se desea agregar al inventario "))

          inventario[d] = inventario[d] + b

          print(
              "ID={} - Nombre={} - Cantidad={} - P-Compra=${} - P-Venta=${} - Unidades vendidas={} - Ventas Totales2={}".format(
                  num[d], producto[d], inventario[d], preciodc[d], preciodv[d], unive[d], ventas[d]))

          input("Enter para continual...")


        elif opcion == 3:
            i = 0
            for i in range(cantidad):
                print("ID={} - Nombre={} - Cantidad={} - P-Compra=${} - P-Venta=${} - Unidades vendidas={} - Ventas Totales2={}" .format(
                    num[i], producto[i], inventario[i], preciodc[i], preciodv[i], unive[i], ventas[i]))

            input("Enter para continual...")

        elif opcion == 4:
            d = int(input("ID del Articulo? "))
            print(
                    "ID={} - Nombre={} - Cantidad={} - P-Compra=${} - P-Venta=${} - Unidades vendidas={} - Ventas Totales2={}".format(
                        num[d], producto[d], inventario[d], preciodc[d], preciodv[d], unive[d], ventas[d]))
            input("Enter para continual...")

        elif opcion == 5:
            d = None
            b = None
            d = int(input("ID del Articulo? "))
            b = int(input("Ingrese la cantidad vendida"))

            inventario[d] = inventario[d] - b
            unive[d] = unive[d] + b
            ventas[d] = ventas[d] + b

            print(
                "ID={} - Nombre={} - Cantidad={} - P-Compra=${} - P-Venta=${} - Unidades vendidas={} - Ventas Totales2={}".format(
                    num[d], producto[d], inventario[d], preciodc[d], preciodv[d], unive[d], ventas[d]))

            input("Enter para continual...")

        elif opcion == 6:
            d = None
            d = int(input("ID del Articulo? "))
            num.remove(num[d])
            producto.append(producto[d])
            inventario.append(inventario[d])
            preciodc.append(preciodc[d])
            preciodv.append(preciodv[d])
            unive.append(unive[d])
            ventas.append(ventas[d])

            input("Enter para continual...")

        elif opcion == 7:
            i = 0
            y = 0
            for i in range(cantidad):
                y = y + ventas[i]
            print("ventas totales = " + y)
            input("Enter para continual...")



        else:
            exit()



