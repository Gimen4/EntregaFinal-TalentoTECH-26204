# Importar librería dataset
import dataset

# Conexión a la base de datos SQLite 
miBase = dataset.connect("sqlite:///productos.db")
tabla_productos = miBase["Productos"]

# ****** Defino funciones ******
def mostrar_productos():
    """ Obtiene y muestra todos los productos almacenados en la base de datos."""
    print("\n****** Productos en stock ******")
  
    if len(tabla_productos) == 0:
        print("No hay productos cargados en el stock.")
        return

    for producto in tabla_productos:
        print(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: $ {producto['precio']} | Categoría: {producto['categoria']}")

        
 def agregar_producto():
    """ Valida e inserta un nuevo producto en la base de datos."""
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    categoria = input("Ingrese la categoría del producto: ").strip().capitalize()
    
   # Validar que el campo nombre y categoría no queden vacíos
    if nombre == "" or categoria == "":
        print("¡ERROR! El nombre y la categoría no pueden estar vacíos.")
        return
    
   # Validar precio
    try:
        precio = int(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("¡ERROR! El precio debe ser mayor a 0.")
            return
          
        # Agrega el registro y guarda los cambios automáticamente
        agregar = {"nombre": nombre, "precio": precio, "categoría": categoria}
        tabla_productos.insert(agregar)
        print(f"¡El producto '{nombre}' se guardó correctamente en la base de datos!")
        mostrar_producto()   
    except ValueError:
        print("¡ERROR! Debe ingresar un número válido para el precio.")


def buscar_producto():
    """ Busca productos por ID."""
    buscar = input("Ingrese el id del producto a buscar: ").strip()
      
    if buscar == "":
        print("¡ERROR! Debe ingresar el id a buscar.")
        return
      
    try:
      encontrado = tabla_productos.find_one(id = buscar)
      
      print("\n**** Resultados de búsqueda *****")    
      if encontrado:
        print(f"ID: {encontrado['id']} | Nombre: {encontrado['nombre']} | Precio: $ {encontrado['precio']} | Categoría: {encontrado['categoria']}")
       else:
            print("No se encontró ningún producto con ese ID.")
           
    except ValueError:
        print("¡ERROR! El ID debe ser un número entero.")


def eliminar_producto():
    """ Muestra los productos y elimina el producto seleccionado según su ID."""
    if len(tabla_productos) == 0:
        print("El stock está vacío. No hay productos para eliminar.")
        return
    
    print("\n*** Productos actuales ***")      
    mostrar_producto()
  
    try:
        id_eliminar = int(input("\nIngrese el número de ID del producto a eliminar: ").strip())

        # Verificamos si existe un registro con ese ID antes de borrarlo
        producto_a_borrar = tabla_productos.find_one(id = id_eliminar)

        if producto_a_borrar:
            tabla_productos.delete(id = id_eliminar)
            print(f"¡El producto '{producto_a_borrar['nombre']}' se eliminó con éxito!\n")
            mostrar_productos()
        else:
            print("¡ERROR! No existe ningún producto con ese ID.")
    except ValueError:
        print("¡ERROR! Debe ingresar un número entero válido.")
      

# ***************************************************************************************************************************************
# ****** PROGRAMA PRINCIPAL ******
while True:
  print("\n*** Menú de opciones ***\n")
  opciones = input("A - Agregar producto\nB - Buscar producto por ID\nE - Eliminar producto por ID\nM - Mostrar productos\nS - Salir\n").strip().upper()

  match opciones:
    case "A":
      agregar_producto()
    case "B":
      buscar_producto()
    case "E":
      eliminar_producto()
    case "M":
      mostrar_productos()
    case "S":
      print("Saliendo del programa... ¡Hasta luego!")
      break
    case _:
      print("Opción no válida. Por favor, elija A, B, E, M o S.")
   
