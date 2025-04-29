from datetime import datetime
from typing import List,Dict

lista_tarea: List[Dict] = []

def validar_fecha(fecha_str: str) -> bool:
    try:
        datetime.strptime(fecha_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def mostrar_tarea(tareas: list[Dict]) -> None:
    for tarea in tareas:
        ide = tarea.get("ID")
        titulo = tarea.get("Titulo")
        fecha_vencimiento = tarea.get("Fecha Vencimiento")
        prioridad = tarea.get("Prioridad")
        completado = "✔️" if tarea.get("Completado") else "❌"
        print(f"ID: {ide} | [{completado} {titulo} | ⏱️ {fecha_vencimiento} | Prioridad: {prioridad}]")

def agregar_tarea() -> None:
    titulo = input("Ingrese el Titulo de la tarea: ").strip()
    descripcion = input("Ingrese la descripcion de la tarea: ").strip()
    while True:
        fecha_str = input("Ingrese la fecha: ").strip()
        if validar_fecha(fecha_str):
            fecha_vencimiento = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            break
        else:
            print("Fecha no valida intente de nuevo")
    prioridad_validas = {"alta","media","baja"}
    while True:
        prioridad = input("Coloque la Prioridad de la tarea (Alta,Media,Baja): ").lower().strip()
        if prioridad in prioridad_validas:
            break
        else:
                print("Prioridad no reconocida, ingrese de nuevo porfavor")

    lista_tarea.append({
        "ID": len(lista_tarea) + 1,
        "Titulo": titulo,
        "Descripcion": descripcion,
        "Fecha Vencimiento": fecha_vencimiento,
        "Prioridad": prioridad,
        "Completado": False
    })
    print("✅ ¡Tarea agregada con exito!")

def listar_tarea() -> None:
    if lista_tarea:
        sorted(lista_tarea,key= lambda fecha: fecha["Fecha Vencimiento"])
        mostrar_tarea(lista_tarea)

def buscar_tarea() -> None:
    palabra_buscar = input("Buscar palabra: ").lower().strip()
    contador = 0
    lista_resultado = []
    for tarea in lista_tarea:
        titulo = tarea.get("Titulo")
        descripcion = tarea.get("Descripcion")
        titulo = titulo.lower()
        descripcion = descripcion.lower()
        if palabra_buscar in titulo or palabra_buscar in descripcion:
            contador +=1
            lista_resultado.append(tarea)
    if lista_resultado:
        print(f"Se encontro {contador} tareas:")
        mostrar_tarea(lista_resultado)
    else:
        print("No se encontraron tareas con esa palabra clave")

def filtrar_tarea_por_prioridad() -> None:
    prioridad_usuario = input("Ingrese la prioridad de las tareas que desea ver: ").strip().lower()
    lista_filtrado_prioridad = []
    for buscar_prioridad in lista_tarea:
        prioridad = buscar_prioridad.get("Prioridad")
        if prioridad_usuario == prioridad:
            lista_filtrado_prioridad.append(buscar_prioridad)
    if lista_filtrado_prioridad:
        mostrar_tarea(lista_filtrado_prioridad)
    else:
        print("No hay tareas con esa prioridad")

