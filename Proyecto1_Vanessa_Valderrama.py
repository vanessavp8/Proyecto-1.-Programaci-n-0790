print("Bienvenido a la Ferretería de Vanessa. A continuación te mostraremos el menú.")
# Definimos productos en el inventario con su nombre, categoría, cantidad en stock y precio.
producto_1 = ["Esmeril", "Herramientas", 13, 129]
producto_2 = ["Taladro", "Herramientas", 18, 99.50]
producto_3 = ["Set de destornilladores", "Herramientas", 23, 12]
producto_4 = ["Grifería para fregadero", "Plomería", 15, 23.90]
producto_5 = ["Filtro purificador de agua", "Plomería", 12, 22.00]
producto_6 = ["Válvula de bronce", "Plomería", 7, 15.00]
producto_7 = ["Toma corriente", "Hogar", 32, 3.50]
producto_8 = ["Bombillos Led", "Hogar", 24, 1.59]
producto_9 = ["Cerraduras", "Hogar", 17, 9.90]

# Definimos del inventario de la Ferretería de Vanessa como una lista que contiene todos los productos.
inventario_ferreteria = [producto_1, producto_2, producto_3, producto_4, producto_5, producto_6, producto_7, producto_8, producto_9]

# Imprimimos el menú del inventario para que el usuario seleccione la opción deseada.
while True:
    print("°°°°MENÚ DE INVENTARIO DE FERRETERÍA VANESSA°°°°")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Mostrar Inventario")
    print("6. Salir")

    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    if opcion == 1:
 # Agregar producto
        nombre_producto = input("Nombre del producto: ")
        categoria_producto = input("Categoría a la que pertenece el producto (Herramientas, Plomería u Hogar): ")
        cantidad_producto = int(input("Cantidad del producto que hay en stock: "))
        precio_producto = float(input("Precio del producto: "))
        nuevo_producto = [nombre_producto, categoria_producto, cantidad_producto, precio_producto]
        inventario_ferreteria.append(nuevo_producto)
        print("Su producto fue agregado al inventario.")

    elif opcion == 2:
# Eliminar producto
        producto_a_eliminar = input("Ingrese el producto que desea eliminar: ").lower()
        for producto in inventario_ferreteria:
            if producto[0].lower() == producto_a_eliminar:
                inventario_ferreteria.remove(producto)
                print("Se eliminó correctamente el producto.")
                break
        else:
            print("El producto ingresado no se encontró en el inventario.")

    elif opcion == 3:
 # Buscar producto
        producto_a_buscar = input("Ingrese el nombre o la categoría del producto que desea buscar: ").lower()
        resultados = []
        for producto in inventario_ferreteria:
            if producto_a_buscar in [producto[0].lower(), producto[1].lower()]:
                resultados.append(producto)

        if resultados:
            print("Resultados de la búsqueda:")
            for producto in resultados:
                print("Nombre: " + producto[0])
                print("Categoría: " + producto[1])
                print("Cantidad: " + str(producto[2]))
                print("Precio: " + str(producto[3]))
                print("-----------------------------")
        else:
            print("No se encontraron productos que coincidan con la búsqueda.")

    elif opcion == 4:
# Actualizar producto
        producto_a_actualizar = input("Ingrese el nombre del producto que desea actualizar: ").lower()
        for producto in inventario_ferreteria:
            if producto[0].lower() == producto_a_actualizar:
                cantidad = int(input("Ingrese la nueva cantidad en stock del producto: "))
                precio = float(input("Ingrese el nuevo precio del producto: "))
                producto[2] = cantidad
                producto[3] = precio
                print("El producto ha sido actualizado en el inventario.")
                break
        else:
            print("El producto no existe en el inventario.")

    elif opcion == 5:
# Mostrar inventario
        print("Inventario de la Ferretería de Vanessa:")
        for producto in inventario_ferreteria:
            print("Nombre: " + producto[0])
            print("Categoría: " + producto[1])
            print("Cantidad: " + str(producto[2]))
            print("Precio: " + str(producto[3]))

    elif opcion == 6:
        # Salir del programa
        print("Gracias por visitar la Ferretería de Vanessa. Esperamos que haya disfrutado de nuestros servicios.")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
#Append método que permite agregar un elemento al final de la lista.
#Lower convierte una cadena de caracteres a minuscula 
#Use el while true para crear un bucle infinito, de tal forma que se siguera repitiendo hasta que el usuario ingrese algo indebido y lo corte
        