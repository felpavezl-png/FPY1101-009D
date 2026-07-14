juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}


inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}



def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("====================================")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def validar_texto(texto):
    return texto.strip() != ""

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ['E', 'T', 'M']

def validar_multiplayer_input(respuesta):
    return respuesta.lower() in ['s', 'n']

def convertir_multiplayer(respuesta):
    return respuesta.lower() == 's'

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_stock(stock_str):
    try:
        stock = int(stock_str)
        return stock >= 0
    except ValueError:
        return False

def validar_codigo(codigo):
    return codigo.upper() not in juegos


def stock_plataforma(plataforma_buscada):
    total_stock = 0
    plataforma_buscada_lower = plataforma_buscada.lower()
    for codigo_juego, datos_juego in juegos.items():
        if datos_juego[1].lower() == plataforma_buscada_lower:
            if codigo_juego in inventario:
                total_stock += inventario[codigo_juego][1]
    print(f"El total de stock disponibles es: {total_stock}")


def busqueda_precio(p_min, p_max):
    juegos_encontrados = []
    for codigo_juego, datos_inventario in inventario.items():
        precio = datos_inventario[0]
        stock = datos_inventario[1]
        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[codigo_juego][0] 
            juegos_encontrados.append(f"{titulo}--{codigo_juego}")
    
    if not juegos_encontrados:
        print("No hay juegos en ese rango de precios.")
    else:
        juegos_encontrados.sort()
        print("Los juegos encontrados son:", juegos_encontrados)


def actualizar_precio(codigo, nuevo_precio):
    codigo_upper = codigo.upper()
    if codigo_upper in inventario:
        inventario[codigo_upper][0] = nuevo_precio
        return True
    return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    codigo_upper = codigo.upper()
    if codigo_upper in juegos:
        return False

    juegos[codigo_upper] = [titulo, plataforma, genero, clasificacion.upper(), multiplayer, editor]
    inventario[codigo_upper] = [precio, stock]
    return True


def eliminar_juego(codigo):
    codigo_upper = codigo.upper()
    if codigo_upper in juegos and codigo_upper in inventario:
        del juegos[codigo_upper]
        del inventario[codigo_upper]
        return True
    return False


def main():
    while True:
        mostrar_menu()
        opcion = validar_opcion()

        if opcion == 1:
            plataforma = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plataforma)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max= int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max)
                        break
                    else:
                        print("Los precios deben ser mayores o iguales a cero y el mínimo debe ser menor o igual al máximo.")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del juego: ")
                nuevo_precio_str = input("Ingrese nuevo precio: ")

                if not validar_precio(nuevo_precio_str):
                    print("Error: El precio debe ser un número entero mayor que cero.")
                else:
                    nuevo_precio = int(nuevo_precio_str)
                    if actualizar_precio(codigo, nuevo_precio):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ")
                if respuesta.lower() == 'n':
                    break
        elif opcion == 4:
            print("\n--- Agregar juego ---")
            codigo = input("Ingrese código del juego: ")
            if not validar_texto(codigo):
                print("Error: El código no puede estar vacío.")
                continue
            if not validar_codigo(codigo):
                print("Error: El código ya existe.")
                continue

            titulo = input("Ingrese título: ")
            if not validar_texto(titulo):
                print("Error: El título no puede estar vacío.")
                continue

            plataforma = input("Ingrese plataforma: ")
            if not validar_texto(plataforma):
                print("Error: La plataforma no puede estar vacía.")
                continue

            genero = input("Ingrese género: ")
            if not validar_texto(genero):
                print("Error: El género no puede estar vacío.")
                continue

            clasificacion = input("Ingrese clasificación (E, T o M): ")
            if not validar_clasificacion(clasificacion):
                print("Error: La clasificación debe ser 'E', 'T' o 'M'.")
                continue

            multiplayer_input = input("¿Es multiplayer? (s/n): ")
            if not validar_multiplayer_input(multiplayer_input):
                print("Error: La respuesta de multiplayer debe ser 's' o 'n'.")
                continue
            multiplayer = convertir_multiplayer(multiplayer_input)

            editor = input("Ingrese editor: ")
            if not validar_texto(editor):
                print("Error: El editor no puede estar vacío.")
                continue

            precio_str = input("Ingrese precio: ")
            if not validar_precio(precio_str):
                print("Error: El precio debe ser un número entero mayor que cero.")
                continue
            precio = int(precio_str)

            stock_str = input("Ingrese stock: ")
            if not validar_stock(stock_str):
                print("Error: El stock debe ser un número entero mayor o igual a cero.")
                continue
            stock = int(stock_str)
            
            if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
                print("Juego agregado")
            else:
                print("El código ya existe")

        elif opcion == 5:
            print("\n--- Eliminar juego ---")
            codigo = input("Ingrese el código del juego a eliminar: ")
            if eliminar_juego(codigo):
                print("Juego eliminado")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()