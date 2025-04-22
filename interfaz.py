import tkinter as tk
from tkinter import messagebox
from juego import Juego

class Aplicacion:
    def __init__(self,root):
        self.root = root
        self.root.title("MULTIJUGANDO")
        self.root.geometry("400x300")
        self.juego = Juego(tabla=2) #esto permite al usuario elegir la tabla
        
        self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()
        
        #etiqueta titulo
        self.titulo = tk.Label(root, text="Multiplicando y Jugando", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=10)
        
        # Pregunta
        self.lbl_pregunta = tk.Label(root, text="", font=("Arial", 14))
        self.lbl_pregunta.pack()

        # Campo de respuesta
        self.entry_respuesta = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry_respuesta.pack(pady=10)

        # Botón responder
        self.btn_responder = tk.Button(root, text="Responder", command=self.verificar_respuesta)
        self.btn_responder.pack(pady=5)

        # Puntaje
        self.lbl_puntaje = tk.Label(root, text="Puntaje: 0", font=("Arial", 12))
        self.lbl_puntaje.pack()

        # Reiniciar
        self.btn_reiniciar = tk.Button(root, text="Reiniciar Juego", command=self.reiniciar_juego)
        self.btn_reiniciar.pack(pady=5)

        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        if self.pregunta_actual:
            self.lbl_pregunta.config(text=self.pregunta_actual.pregunta)
        else:
            messagebox.showinfo("Juego terminado", f"¡Felicitaciones! Tu puntaje fue: {self.juego.puntaje}")
            self.btn_responder.config(state=tk.DISABLED)
    
    def verificar_respuesta(self):
        respuesta = self.entry_respuesta.get()
        if respuesta.isdigit():
            correcta = self.juego.verificar_respuesta(self.pregunta_actual, int(respuesta))
            if correcta:
                messagebox.showinfo("Correcto", "¡Muy bien!")
            else:
                messagebox.showerror("Incorrecto", f"La respuesta correcta era: {self.pregunta_actual.respuesta}")
            
            # Avanzar a la siguiente pregunta
            self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()
            self.entry_respuesta.delete(0, tk.END)
            self.lbl_puntaje.config(text=f"Puntaje: {self.juego.puntaje}")
            self.mostrar_pregunta()
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa un número válido")

    def reiniciar_juego(self):
        self.juego = Juego(tabla=2)
        self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()
        self.btn_responder.config(state=tk.NORMAL)
        self.entry_respuesta.delete(0, tk.END)
        self.lbl_puntaje.config(text="Puntaje: 0")
        self.mostrar_pregunta()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()