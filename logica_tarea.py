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

def listar_tarea():
    if lista_tarea:
        sorted(lista_tarea,key= lambda fecha: fecha["Fecha Vencimiento"])
        for tarea in lista_tarea:
            ide = tarea.get("ID")
            titulo = tarea.get("Titulo")
            fecha_vencimiento = tarea.get("Fecha Vencimiento")
            prioridad = tarea.get("Prioridad")
            completado = "✔️" if tarea.get("Completado") else "❌"
            print(f"ID: {ide} | [{completado} {titulo} | ⏱️ {fecha_vencimiento} | Prioridad: {prioridad}]")

def buscar_tarea():
    pass

agregar_tarea()
listar_tarea()