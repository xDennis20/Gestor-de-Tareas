from logica_tarea import agregar_tarea,listar_tarea,buscar_tarea,filtrar_tarea_por_prioridad,tareas_vencidas,marcar_completada,eliminar_tarea

def menu():
    opcion = 0
    salir = False
    while not salir:
        print("""
    📚 Gestor de Tareas 
    1. Agregar tarea
    2. Ver tareas
    3. Buscar tarea
    4. Filtrar por prioridad
    5. Mostrar vencidas
    6. Marcar como completada
    7. Eliminar tarea
    8. Guardar y salir
        """)
        try:
            opcion = int(input("Escoga una opcion (1-8): "))
        except ValueError:
            print("\n ¡Por favor coloque un valor entero!")
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            listar_tarea()
        elif opcion == 3:
            buscar_tarea()
        elif opcion == 4:
            filtrar_tarea_por_prioridad()
        elif opcion == 5:
            tareas_vencidas()
        elif opcion == 6:
            marcar_completada()
        elif opcion == 7:
            eliminar_tarea()
        elif opcion == 8:
            salir = True

menu()