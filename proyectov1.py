import tkinter as tk

class Interfaz:
    def _init_(self):
        self.nombres = []  

    def registro(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("500x200")
        self.ventana.title("VENTANA DE REGISTRO")

        etiqueta = tk.Label(self.ventana, text="Ingrese su nombre")
        etiqueta.pack()

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        boton = tk.Button(self.ventana, text="Registrar", command=self.guardar_nombre)
        boton.pack()

        self.ventana.mainloop()

    def guardar_nombre(self):
        nombre = self.entrada.get()
        if nombre:
            self.nombres.append(nombre)
            print("Nombre registrado:", nombre)
            self.entrada.delete(0, tk.END)
        else:
            print("No se ingresó ningún nombre.")

        if nombre == "_main_":
         app = Interfaz()
         app.registro()