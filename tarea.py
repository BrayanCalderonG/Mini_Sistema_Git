# tarea.py

class Tarea:
    def __init__(self, nombre, descripcion):
        """
        Constructor de la clase Tarea.
        Inicializa una tarea con nombre, descripción y estado de completada en False.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Representación en texto de la tarea.
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {estado}"
