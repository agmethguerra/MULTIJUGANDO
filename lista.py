class NodoPregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.siguiente = None

class ListaPreguntas:
    def __init__(self):
        self.primero = None
        self.actual = None

    def agregar_pregunta(self, pregunta, respuesta):
        nuevo = NodoPregunta(pregunta, respuesta)
        if not self.primero:
            self.primero = nuevo
            self.actual = nuevo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo

    def siguiente_pregunta(self):
        if self.actual:
            pregunta = self.actual
            self.actual = self.actual.siguiente
            return pregunta
        return None

    def reiniciar(self):
        self.actual = self.primero
