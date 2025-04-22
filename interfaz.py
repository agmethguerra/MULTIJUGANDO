import tkinter as tk
from tkinter import messagebox
from juego import Juego

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Multijugando")
        self.root.geometry("800x600")
        self.root.configure(bg="#A64CA6")

        self.juego = Juego(tabla=15)
        self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()

        self.color_morado = "#A64CA6"
        self.color_titulo = "#6A1B6A"
        self.color_verde = "#28A745"
        self.color_hover_verde = "#1E7E34"
        self.color_amarillo = "#FFD700"
        self.color_hover_amarillo = "#FFC107"

        # ========= TÍTULO =========
        self.titulo_frame = tk.Frame(root, bg=self.color_titulo, height=60)
        self.titulo_frame.pack(fill=tk.X)

        self.lbl_titulo = tk.Label(self.titulo_frame, text="🧠 MULTIJUGANDO", font=("Helvetica", 18, "bold"),
                                   bg=self.color_titulo, fg="white")
        self.lbl_titulo.pack(pady=10)

        # ========= PUNTAJE FLOTANTE =========
        self.puntaje_frame = tk.Frame(root, bg="white", highlightthickness=0)
        self.puntaje_frame.place(x=20, y=80)

        self.lbl_puntaje = tk.Label(self.puntaje_frame, text="0", font=("Helvetica", 18, "bold"),
                                    bg="white", fg="black", padx=10, pady=5)
        self.lbl_puntaje.pack()
        self.puntaje_frame.config(highlightbackground="black", highlightthickness=2)

        # ========= PREGUNTA =========
        self.lbl_pregunta = tk.Label(root, text="", font=("Helvetica", 120, "bold"),
                                     bg=self.color_morado, fg="white")
        self.lbl_pregunta.pack(pady=60)

        # ========= INPUT + BOTÓN RESPONDER =========
        input_frame = tk.Frame(root, bg=self.color_morado)
        input_frame.pack(pady=10)

        self.entry_respuesta = tk.Entry(input_frame, font=("Helvetica", 14), width=4, justify="center",
                                        bg="white", fg="black", bd=0, relief="flat")
        self.entry_respuesta.pack(side=tk.LEFT, ipady=10, ipadx=5)

        self.btn_responder = tk.Label(input_frame, text="Responder", font=("Helvetica", 14, "bold"),
                                      bg=self.color_verde, fg="white", padx=20, pady=12, cursor="hand2")
        self.btn_responder.pack(side=tk.LEFT, padx=10)
        self.estilizar_boton(self.btn_responder, self.color_verde, self.color_hover_verde)

        # ========= BOTÓN REINICIAR =========
        self.btn_reiniciar = tk.Label(root, text="Reiniciar juego", font=("Helvetica", 14, "bold"),
                                      bg=self.color_amarillo, fg="white", padx=40, pady=15, cursor="hand2")
        self.btn_reiniciar.pack(pady=40)
        self.estilizar_boton(self.btn_reiniciar, self.color_amarillo, self.color_hover_amarillo)

        self.btn_responder.bind("<Button-1>", lambda e: self.verificar_respuesta())
        self.btn_reiniciar.bind("<Button-1>", lambda e: self.reiniciar_juego())

        self.mostrar_pregunta()

    def estilizar_boton(self, boton, color_normal, color_hover):
        boton.configure(relief="flat", bd=0)
        boton.bind("<Enter>", lambda e: boton.config(bg=color_hover))
        boton.bind("<Leave>", lambda e: boton.config(bg=color_normal))

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
                messagebox.showinfo("✅ Correcto", "¡Muy bien!")
            else:
                messagebox.showerror("❌ Incorrecto", f"La respuesta correcta era: {self.pregunta_actual.respuesta}")

            self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()
            self.entry_respuesta.delete(0, tk.END)
            self.lbl_puntaje.config(text=str(self.juego.puntaje))
            self.mostrar_pregunta()
        else:
            messagebox.showwarning("⚠️ Advertencia", "Por favor ingresa un número válido")

    def reiniciar_juego(self):
        self.juego = Juego(tabla=2)
        self.pregunta_actual = self.juego.preguntas.siguiente_pregunta()
        self.entry_respuesta.delete(0, tk.END)
        self.lbl_puntaje.config(text="0")
        self.btn_responder.config(state=tk.NORMAL)
        self.mostrar_pregunta()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
