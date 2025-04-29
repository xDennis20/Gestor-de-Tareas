from logica_tarea import agregar_tarea,listar_tarea,buscar_tarea

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
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            salir = True

menu()