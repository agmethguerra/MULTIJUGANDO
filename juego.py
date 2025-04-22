import random
from lista import ListaPreguntas

class Juego:
    def __init__(self, tabla):
        self.tabla = tabla
        self.preguntas = ListaPreguntas()
        self.puntaje = 0
        self.generar_preguntas()

    def generar_preguntas(self):
        for i in range(1, 11):
            pregunta = f"{self.tabla} x {i}"
            respuesta = self.tabla * i
            self.preguntas.agregar_pregunta(pregunta, respuesta)

    def verificar_respuesta(self, pregunta_nodo, respuesta_usuario):
        if pregunta_nodo and int(respuesta_usuario) == pregunta_nodo.respuesta:
            self.puntaje += 1
            return True
        return False
