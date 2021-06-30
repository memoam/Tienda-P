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
        print("1.- Agregar compra (aumenta inventario)")
        print("2.- Ver listado")
        print("3.- Buscar ")
        print("2.- Agregar venta")
        print("2.- Eliminar ")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            num.append(cantidad-1)
            producto.append(input("Nombre del articulo: "))
            inventario.append(int(input("Numero de unidades: ")))
            preciodc.append(int(input("Precio de Compra: ")))
            preciodv.append((int(input("Precio de venta "))))
            unive.append(int(input("Unidades vendidas ")))
            ventas.append(float(input("(float)Ventas totales del articulo")))
            cantidad += 1


        else:
            print(producto)
