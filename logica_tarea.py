from datetime import datetime, date, timedelta
from typing import List,Dict
import csv

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

def tareas_vencidas() -> None:
    fecha_actual = date.today()
    lista_tareas_vencidas = []
    for tarea in lista_tarea:
        if tarea.get("Fecha Vencimiento") < fecha_actual and not tarea.get("Completado"):
            lista_tareas_vencidas.append(tarea)
    if lista_tareas_vencidas:
        mostrar_tarea(lista_tareas_vencidas)
    else:
        print("🎉 No hay tareas vencidas. ¡Estás al día!")

def marcar_completada():
    id_usuario = 0
    try:
        id_usuario = int(input("Ingrese el ID de la tarea que busca completar: ").strip())
    except ValueError:
        print("Ingrese un valor entero por favor")
    encontrado = False
    for tarea in lista_tarea:
        if tarea.get("ID") == id_usuario:
            encontrado = True
            if not tarea.get("Completado"):
                tarea["Completado"] = True
                print("Fue marcado exitosamente")
            else:
                print("La tarea ya estaba marcada")
            break
    if not encontrado:
        print("El ID que ingreso no encontro ninguna tarea")

def eliminar_tarea():
    id_usuario = 0
    try:
        id_usuario = int(input("Ingrese el ID de la tarea que desea eliminar: ").strip())
    except ValueError:
        print("Por favor Ingrese un valor entero")
    encontrado = False
    for indice, tarea in enumerate(lista_tarea):
        if tarea.get("ID") == id_usuario:
            encontrado = True
            del lista_tarea[indice]
    if not encontrado:
        print("El ID que ingreso no encontro ninguna tarea")

def guardar_tarea():
    lista_nombres = ["ID", "Titulo", "Descripcion", "Fecha Vencimiento", "Prioridad", "Completado"]
    with open("Tareas.csv","a",newline= "") as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=lista_nombres)
        for tarea in lista_tarea:
            copia_de_las_tareas = tarea.copy()
            copia_de_las_tareas["Fecha Vencimiento"] = str(copia_de_las_tareas["Fecha Vencimiento"]) #Esto es para transformar las fechas que esten formato date y transforamar string
            escritor.writerow(copia_de_las_tareas)

    print("Tarea Guardada Con Exito 🎉")

def cargar_tareas():
    with open("Tareas.csv","r",newline= "") as archivo:
        tareas = csv.DictReader(archivo)
        for tarea in tareas:
            copia_tareas = tarea.copy()
            copia_tareas["ID"] = int(copia_tareas["ID"])
            copia_tareas["Completado"] = True if copia_tareas["Completado"] == "True" else False
            copia_tareas["Fecha Vencimiento"] = datetime.strptime(copia_tareas["Fecha Vencimiento"],"%Y-%m-%d").date()
            lista_tarea.append(copia_tareas)

def recordatorio_de_tareas():
    fecha_actual = date.today()
    fecha_manana = fecha_actual + timedelta(days=1)
    lista_vencidas = []
    lista_vencen_manana = []
    with open("Tareas.csv","r",newline= "") as archivo:
        tareas = csv.DictReader(archivo)
        for tarea in tareas:
            copiar_tareas = tarea.copy()
            fecha = copiar_tareas.get("Fecha Vencimiento")
            fecha_vencimiento = datetime.strptime(fecha, "%Y-%m-%d").date()
            if fecha_vencimiento < fecha_actual:
                lista_vencidas.append(copiar_tareas)
            if fecha_vencimiento == fecha_manana:
                lista_vencen_manana.append(copiar_tareas)
    if lista_vencidas:
        print("⚠️ Tareas vencidas:")
        mostrar_tarea(lista_vencidas)
    else:
        print("🎉 No hay tareas vencidas. ¡Estás al día!")
    if lista_vencen_manana:
        print("📅 Tareas que vencen mañana:")
        mostrar_tarea(lista_vencen_manana)
    else:
        print("🎉 No hay tareas para mañana.")