
estudiantes = []

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción inválida. Por favor, elige un número entre 1 y 6.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def validar_nombre_estudiante(nombre):
    return nombre.strip() != ""

def validar_edad(edad_str):
    try:
        edad = int(edad_str)
        return edad > 0
    except ValueError:
        return False

def validar_nota(nota_str):
    try:
        nota = float(nota_str)
        return 1.0 <= nota <= 7.0
    except ValueError:
        return False

def agregar_estudiante(estudiantes):
    print("\n--- Agregar Estudiante ---")

    nombre = input("Ingrese el nombre completo del estudiante: ")
    if not validar_nombre_estudiante(nombre):
        print("Error: El nombre del estudiante no puede estar vacío ni solo espacios en blanco.")
        return

    edad_str = input("Ingrese la edad del estudiante (número entero > 0): ")
    if not validar_edad(edad_str):
        print("Error: La edad debe ser un número entero mayor que cero.")
        return
    edad = int(edad_str)

    nota_str = input("Ingrese la nota del estudiante (número decimal entre 1.0 y 7.0): ")
    if not validar_nota(nota_str):
        print("Error: La nota debe ser un número decimal entre 1.0 y 7.0 (incluidos).")
        return
    nota = float(nota_str)

    nuevo_estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False 
    }
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante '{nombre}' agregado con éxito.")

def buscar_estudiante(estudiantes, nombre_buscado):
    for i in range(len(estudiantes)):
        if estudiantes[i]["nombre"].lower() == nombre_buscado.lower():
            return i
    return -1

def eliminar_estudiante(estudiantes):
    print("\n--- Eliminar Estudiante ---")
    nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    indice = buscar_estudiante(estudiantes, nombre_a_eliminar)

    if indice != -1:
        estudiante_eliminado = estudiantes.pop(indice)
        print(f"Estudiante '{estudiante_eliminado['nombre']}' eliminado con éxito.")
    else:
        print(f"El estudiante '{nombre_a_eliminar}' no se encuentra registrado.")

def actualizar_estados(estudiantes):
    for estudiante in estudiantes:
        estudiante["aprobado"] = estudiante["nota"] >= 4.0

def mostrar_estudiantes(estudiantes):
    print("\n=== LISTA DE ESTUDIANTES ===")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    actualizar_estados(estudiantes)

    for estudiante in estudiantes:
        estado = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        print(f"Estado: {estado}")
        print("********************************************")

def main():
    print("Bienvenido al Sistema de Gestión de Estudiantes")

    while True:
        mostrar_menu()
        opcion = validar_opcion()

        if opcion == 1:
            agregar_estudiante(estudiantes)
        elif opcion == 2:
            print("\n--- Buscar Estudiante ---")
            nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ")
            indice = buscar_estudiante(estudiantes, nombre_buscado)
            if indice != -1:
                estudiante_encontrado = estudiantes[indice]
                print(f"Estudiante encontrado en la posición {indice + 1}:")
                print(f"  Nombre: {estudiante_encontrado['nombre']}")
                print(f"  Edad: {estudiante_encontrado['edad']}")
                print(f"  Nota: {estudiante_encontrado['nota']}")
                estado = "APROBADO" if estudiante_encontrado['aprobado'] else "REPROBADO"
                print(f"  Estado: {estado}")
            else:
                print(f"El estudiante '{nombre_buscado}' no se encuentra registrado.")
        elif opcion == 3:
            eliminar_estudiante(estudiantes)
        elif opcion == 4:
            actualizar_estados(estudiantes)
            print("Los estados de aprobación de todos los estudiantes han sido actualizados.")
        elif opcion == 5:
            mostrar_estudiantes(estudiantes)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


main()
