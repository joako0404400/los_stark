def normalizar_datos(lista):
    for heroe in lista:
        heroe["altura"] = float(heroe.get("altura", 0))
        heroe["peso"] = float(heroe.get("peso", 0))
        heroe["fuerza"] = float(heroe.get("fuerza", 0))

def filtrar_superheroes(lista, genero):
    return [heroe for heroe in lista if heroe["genero"] == genero]

def encontrar_extremo(lista, clave, genero, maximo=True):
    filtro_genero = filtrar_superheroes(lista, genero)
    if not filtro_genero:
        return None
    return max(filtro_genero, key=lambda x: x[clave]) if maximo else min(filtro_genero, key=lambda x: x[clave])

def calcular_promedio(lista, clave, genero):
    filtro_genero = filtrar_superheroes(lista, genero)
    if not filtro_genero:
        return 0
    total = sum(heroe[clave] for heroe in filtro_genero)
    return total / len(filtro_genero)

def imprimir_promedio(lista, clave, genero):
    promedio = calcular_promedio(lista, clave, genero)
    print(f"Promedio de {clave}: {promedio:.2f}")

def contar_tipos(lista, clave):
    contador_tipos = {}
    for heroe in lista:
        tipo = heroe[clave].capitalize()
        contador_tipos[tipo] = contador_tipos.get(tipo, 0) + 1

    for tipo, cantidad in contador_tipos.items():
        if tipo == " ":
            print(f"No hay información sobre {clave.replace('_', ' de ')}")
        else:
            print(f"Hay {cantidad} superhéroes con {clave.replace('_', ' de ').capitalize()} {tipo}")

def listar_superheroes_por_tipo(lista, clave):
    for heroe in lista:
        print(f"Superhéroe: {heroe['nombre']} | {clave.replace('_', ' de ').capitalize()}: {heroe[clave]}")

def stark_marvel_app(lista):
    normalizar_datos(lista)
    
    while True:
        print("Menu de opciones:")
        print("1. Mostrar héroes masculinos")
        print("2. Mostrar héroes femeninos")
        print("3. Superhéroe masculino más alto")
        print("4. Superhéroe femenino más alto")
        print("5. Superhéroe masculino más bajo")
        print("6. Superhéroe femenino más bajo")
        print("7. Altura promedio masculinos")
        print("8. Altura promedio femeninos")
        print("9. ¿Cuántos superhéroes tienen cada color de ojos?")
        print("10. ¿Cuántos superhéroes tienen cada color de pelo?")
        print("11. ¿Cuántos superhéroes tienen cada tipo de inteligencia?")
        print("12. Superhéroes por color de ojos")
        print("13. Superhéroes por color de pelo")
        print("14. Superhéroes por tipo de inteligencia")
        print("15. Salir")
        
        opcion = int(input("Opción: "))
        
        if opcion == 1:
            imprimir_heroes(lista, "M")
        elif opcion == 2:
            imprimir_heroes(lista, "F")
        elif opcion == 3:
            imprimir_superheroe(lista, "max", "altura", "M")
        elif opcion == 4:
            imprimir_superheroe(lista, "max", "altura", "F")
        elif opcion == 5:
            imprimir_superheroe(lista, "min", "altura", "M")
        elif opcion == 6:
            imprimir_superheroe(lista, "min", "altura", "F")
        elif opcion == 7:
            imprimir_promedio(lista, "altura", "M")
        elif opcion == 8:
            imprimir_promedio(lista, "altura", "F")
        elif opcion == 9:
            contar_tipos(lista, "color_ojos")
        elif opcion == 10:
            contar_tipos(lista, "color_pelo")
        elif opcion == 11:
            contar_tipos(lista, "inteligencia")
        elif opcion == 12:
            listar_superheroes_por_tipo(lista, "color_ojos")
        elif opcion == 13:
            listar_superheroes_por_tipo(lista, "color_pelo")
        elif opcion == 14:
            listar_superheroes_por_tipo(lista, "inteligencia")
        elif opcion == 15:
            break