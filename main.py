from tarea import Tarea
from gestor import GestorTareas
from usuario import Usuario

def menu():
    gestor = GestorTareas()
    usuarios = {}

    while True:
        print("\n--- MENÚ ---")
        print("1. Crear usuario")
        print("2. Crear tarea")
        print("3. Asignar tarea a usuario")
        print("4. Ver tareas de usuario")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            usuarios[nombre] = Usuario(nombre)

        elif opcion == "2":
            nombre = input("Nombre de la tarea: ")
            desc = input("Descripción: ")
            tarea = Tarea(nombre, desc)
            gestor.agregar_tarea(tarea)

        elif opcion == "3":
            usuario_nombre = input("Nombre del usuario: ")
            tarea_nombre = input("Nombre de la tarea: ")
            tarea = next((t for t in gestor.tareas if t.nombre == tarea_nombre), None)
            if tarea and usuario_nombre in usuarios:
                usuarios[usuario_nombre].asignar_tarea(tarea)
            else:
                print("Usuario o tarea no encontrada.")

        elif opcion == "4":
            nombre = input("Nombre del usuario: ")
            if nombre in usuarios:
                usuarios[nombre].mostrar_tareas()
            else:
                print("Usuario no encontrado.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
