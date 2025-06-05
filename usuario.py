class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)

    def mostrar_tareas(self):
        print(f"Tareas de {self.nombre}:")
        for tarea in self.tareas_asignadas:
            print(tarea)
