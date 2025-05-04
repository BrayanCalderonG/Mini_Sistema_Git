from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        nueva_tarea = Tarea(nombre, descripcion)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        else:
            return False

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        for i, tarea in enumerate(self.tareas):
            estado = "✅" if tarea.completada else "❌"
            print(f"{i}. {tarea.nombre} - {tarea.descripcion} [{estado}]")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            return True
        else:
            return False
