from datetime import datetime
from typing import List,Dict

lista_tarea: List[Dict] = []

def validar_fecha(fecha_str: str) -> bool:
    try:
        datetime.strptime(fecha_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False

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
        for tarea_listar in lista_tarea:
            ide = tarea_listar.get("ID")
            titulo = tarea_listar.get("Titulo")
            fecha_vencimiento = tarea_listar.get("Fecha Vencimiento")
            prioridad = tarea_listar.get("Prioridad")
            completado = "✔️" if tarea_listar.get("Completado") else "❌"
            print(f"ID: {ide} | [{completado} {titulo} | ⏱️ {fecha_vencimiento} | Prioridad: {prioridad}]")

def buscar_tarea() -> None:
    palabra_buscar = input("Buscar palabra: ").lower()
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
        for tareas in lista_resultado:
            ide_resultado = tareas.get("ID")
            titulo_resultado = tareas.get("Titulo")
            fecha_vencimiento_resultado = tareas.get("Fecha Vencimiento")
            prioridad_resultado = tareas.get("Prioridad")
            completado_resultado = "✔️" if tareas.get("Completado") else "❌"
            print(f"ID: {ide_resultado} | [{completado_resultado} {titulo_resultado} | ⏱️ {fecha_vencimiento_resultado} | Prioridad: {prioridad_resultado}]")
    else:
        print("No se encontraron tareas con esa palabra clave")

