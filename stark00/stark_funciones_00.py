# 1
def obtener_nombre(diccionario: dict) -> str:
    return diccionario["nombre"]

def imprimir_dato(dato: str):
    print(dato)

def stark_imprimir_nombres_heroes(lista: list):
    if len(lista) > 0:
        for e_lista in lista:
            nombre = obtener_nombre(e_lista)
            imprimir_dato(nombre)

# 2
def obtener_nombre_y_dato(diccionario: dict, dato: str):
    nombre_dato = "Nombre {0} | {1} {2}".format(diccionario["nombre"], dato.capitalize(), diccionario[dato])
    print(nombre_dato)

# 3
def calcular_max(lista: list, key: str):
    max_heroe = max(lista, key=lambda x: x[key])
    return max_heroe

# 4
def calcular_min(lista: list, key: str):
    min_heroe = min(lista, key=lambda x: x[key])
    return min_heroe

def stark_calcular_imprimir_heroe(lista: list, estado: str, key: str):
    if estado == "max":
        maxmin = calcular_max(lista, key)
    elif estado == "min":
        maxmin = calcular_min(lista, key)
    else:
        return

    print("Superhéroe: {0} | {1} {2}".format(maxmin["nombre"], key, maxmin[key]))

def es_dict(diccionario: dict) -> bool:
    return isinstance(diccionario, dict) and bool(diccionario)

# 5
def contador(lista: list):
    return len(lista)

def sumar_dato_heroe(lista: list, key: str):
    acu_key = sum(hero[key] for hero in lista if es_dict(hero))
    return acu_key

def calcular_promedio(lista: list, key: str):
    if not lista:
        return -1
    acu_key = sumar_dato_heroe(lista, key)
    con_key = contador(lista)
    return acu_key / con_key

def stark_calcular_imprimir_promedio_altura(lista: list, key: str):
    promedio = calcular_promedio(lista, key)
    imprimir_dato(promedio)

# 6
def imprimir_menu():
    print("Menú de opciones:\n1. Superhéroe más alto\n2. Superhéroe más bajo\n3. Promedio de altura\n4. Superhéroe más pesado\n5. Superhéroe menos pesado\n6. Salir")

def validar_entero(string: str):
    return string.isdigit()

def stark_menu_principal():
    while True:
        imprimir_menu()
        opcion = input("Opción: ")
        if validar_entero(opcion):
            return int(opcion)

# 7
def stark_marvel_app(lista: list):
    stark_normalizar_datos(lista)
    stark_imprimir_nombres_heroes(lista)
    while True:
        opcion = stark_menu_principal()
        if opcion == 1:
            stark_calcular_imprimir_heroe(lista, "max", "altura")
        elif opcion == 2:
            stark_calcular_imprimir_heroe(lista, "min", "altura")
        elif opcion == 3:
            stark_calcular_imprimir_promedio_altura(lista, "altura")
        elif opcion == 4:
            stark_calcular_imprimir_heroe(lista, "max", "peso")
        elif opcion == 5:
            stark_calcular_imprimir_heroe(lista, "min", "peso")
        elif opcion == 6:
            break

def stark_normalizar_datos(lista):
    for e_lista in lista:
        e_lista["altura"] = float(e_lista["altura"])
        e_lista["peso"] = float(e_lista["peso"])
    print("Datos normalizados")

# 01 A y B
def imprimir_heroes(lista: list, estado: str):
    for e_lista in lista:
        if e_lista["genero"] == estado:
            print(e_lista["nombre"])

def calcular_maximo_minimo(lista: list, estado: str, clave: str, genero: str):
    filtro = [heroe for heroe in lista if heroe["genero"] == genero]
    if not filtro:
        return -1

    minmax = max(filtro, key=lambda x: x[clave]) if estado == "max" else min(filtro, key=lambda x: x[clave])
    return minmax

def imprimir_superheroe(lista: list, estado: str, clave: str, genero: str):
    minmax = calcular_maximo_minimo(lista, estado, clave, genero)
    if minmax != -1:
        print("Superhéroe {0}: {1} | {2} {3}".format(genero, minmax["nombre"], clave, minmax[clave]))
