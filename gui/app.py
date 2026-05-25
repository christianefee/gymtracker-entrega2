import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modelos.ejercicios import EJERCICIOS
from logica.analizador import AnalizadorProgreso
from logica.recomendador import Recomendador
from logica.equilibrio import AnalizadorEquilibrio

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ARCHIVO_USUARIOS = "datos/usuarios.json"
ARCHIVO_SESIONES = "datos/sesiones.json"

def cargar(archivo):
    with open(archivo, "r") as f:
        return json.load(f)

def guardar(archivo, datos):
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=4)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GymTracker")
        self.geometry("860x560")
        self.resizable(False, False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._menu()
        self._pantalla_inicio()

    def _menu(self):
        panel = ctk.CTkFrame(self, width=170, corner_radius=0, fg_color="#1a1a2e")
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)

        ctk.CTkLabel(panel, text="GymTracker",
                     font=ctk.CTkFont(size=18, weight="bold"),
                     text_color="#4fc3f7").pack(pady=25)

        opciones = [
            ("🏠  Inicio",               self._pantalla_inicio),
            ("👤  Nuevo usuario",         self._pantalla_usuario),
            ("📋  Registrar sesion",      self._pantalla_sesion),
            ("📜  Historial",             self._pantalla_historial),
            ("📈  Analizar progreso",     self._pantalla_progreso),
            ("💡  Recomendacion",         self._pantalla_recomendacion),
            ("⚖️  Equilibrio muscular",   self._pantalla_equilibrio),
        ]

        for texto, cmd in opciones:
            ctk.CTkButton(panel, text=texto, command=cmd, anchor="w",
                          fg_color="transparent", hover_color="#16213e",
                          text_color="white", font=ctk.CTkFont(size=13)
                          ).pack(fill="x", padx=8, pady=2)

    def _limpiar(self):
        if hasattr(self, "panel"):
            self.panel.destroy()
        self.panel = ctk.CTkScrollableFrame(self, fg_color="#0f0f1a")
        self.panel.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

    def _titulo(self, texto):
        ctk.CTkLabel(self.panel, text=texto,
                     font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#4fc3f7").pack(pady=(10, 20))

    def _entrada(self, label, ancho=280):
        ctk.CTkLabel(self.panel, text=label, text_color="#aaaaaa").pack()
        e = ctk.CTkEntry(self.panel, width=ancho)
        e.pack(pady=3)
        return e

    def _boton(self, texto, cmd):
        ctk.CTkButton(self.panel, text=texto, command=cmd,
                      width=280, fg_color="#1565c0",
                      hover_color="#0d47a1").pack(pady=8)

    def _mensaje(self):
        lbl = ctk.CTkLabel(self.panel, text="", wraplength=400)
        lbl.pack(pady=5)
        return lbl

    # PANTALLAS

    def _pantalla_inicio(self):
        self._limpiar()
        ctk.CTkLabel(self.panel, text="Bienvenido a GymTracker",
                     font=ctk.CTkFont(size=24, weight="bold"),
                     text_color="#4fc3f7").pack(pady=60)
        ctk.CTkLabel(self.panel,
                     text="Registra tus entrenamientos y analiza tu progreso.",
                     text_color="#aaaaaa", font=ctk.CTkFont(size=14)).pack()

    def _pantalla_usuario(self):
        self._limpiar()
        self._titulo("Registrar usuario")
        nombre = self._entrada("Nombre")
        edad   = self._entrada("Edad")
        peso   = self._entrada("Peso (kg)")
        altura = self._entrada("Altura (cm)")
        ctk.CTkLabel(self.panel, text="Nivel", text_color="#aaaaaa").pack()
        nivel_var = ctk.StringVar(value="principiante")
        ctk.CTkOptionMenu(self.panel, values=["principiante", "promedio", "avanzado"],
                          variable=nivel_var, width=280).pack(pady=3)
        msg = self._mensaje()

        def guardar_usuario():
            u = cargar(ARCHIVO_USUARIOS)
            n = nombre.get().strip()
            if not n:
                msg.configure(text="El nombre no puede estar vacio.", text_color="red")
                return
            if n in u:
                msg.configure(text="El usuario ya existe.", text_color="orange")
                return
            u[n] = {"nombre": n, "edad": int(edad.get()), "peso": float(peso.get()),
                    "altura": float(altura.get()), "nivel": nivel_var.get()}
            guardar(ARCHIVO_USUARIOS, u)
            msg.configure(text=f"Usuario '{n}' registrado.", text_color="lightgreen")

        self._boton("Guardar", guardar_usuario)

    def _pantalla_sesion(self):
        self._limpiar()
        self._titulo("Registrar sesion")
        e_usuario = self._entrada("Usuario")
        e_sesion  = self._entrada("Nombre de la sesion")
        e_fecha   = self._entrada("Fecha (YYYY-MM-DD)")

        ctk.CTkLabel(self.panel, text="Ejercicio", text_color="#aaaaaa").pack()
        lista = list(EJERCICIOS.keys())
        ej_var = ctk.StringVar(value=lista[0])
        ctk.CTkOptionMenu(self.panel, values=lista, variable=ej_var, width=280).pack(pady=3)

        frame = ctk.CTkFrame(self.panel, fg_color="transparent")
        frame.pack()
        entradas = {}
        for i, (lbl, key) in enumerate([("Peso kg","peso"),("Series","series"),("Reps","reps")]):
            ctk.CTkLabel(frame, text=lbl, text_color="#aaaaaa").grid(row=0, column=i, padx=6)
            e = ctk.CTkEntry(frame, width=85)
            e.grid(row=1, column=i, padx=6, pady=3)
            entradas[key] = e

        caja = ctk.CTkTextbox(self.panel, width=420, height=90, state="disabled")
        caja.pack(pady=6)
        ejercicios = []
        msg = self._mensaje()

        def agregar():
            ej = ej_var.get()
            p, s, r = entradas["peso"].get(), entradas["series"].get(), entradas["reps"].get()
            if not all([p, s, r]):
                return
            musculo = EJERCICIOS[ej][0]
            ejercicios.append({"nombre": ej, "musculo": musculo, "peso": float(p),
                                "series": int(s), "repeticiones": int(r)})
            caja.configure(state="normal")
            caja.insert("end", f"{ej} | {musculo} | {p}kg | {s}x{r}\n")
            caja.configure(state="disabled")
            for e in entradas.values():
                e.delete(0, "end")

        def guardar_sesion():
            u = cargar(ARCHIVO_USUARIOS)
            usuario = e_usuario.get().strip()
            if usuario not in u:
                msg.configure(text="Usuario no encontrado.", text_color="red")
                return
            if not ejercicios:
                msg.configure(text="Agrega al menos un ejercicio.", text_color="red")
                return
            s = cargar(ARCHIVO_SESIONES)
            s.append({"usuario": usuario, "nombre": e_sesion.get(),
                      "fecha": e_fecha.get(), "ejercicios": ejercicios.copy()})
            guardar(ARCHIVO_SESIONES, s)
            msg.configure(text="Sesion guardada.", text_color="lightgreen")
            ejercicios.clear()
            caja.configure(state="normal")
            caja.delete("1.0", "end")
            caja.configure(state="disabled")

        ctk.CTkButton(self.panel, text="Agregar ejercicio", command=agregar,
                      width=280, fg_color="#2e7d32", hover_color="#1b5e20").pack(pady=4)
        self._boton("Guardar sesion", guardar_sesion)

    def _pantalla_historial(self):
        self._limpiar()
        self._titulo("Historial")
        e = self._entrada("Usuario")
        caja = ctk.CTkTextbox(self.panel, width=500, height=280, state="disabled")
        caja.pack(pady=8)

        def buscar():
            sesiones = [s for s in cargar(ARCHIVO_SESIONES) if s["usuario"] == e.get().strip()]
            caja.configure(state="normal")
            caja.delete("1.0", "end")
            if not sesiones:
                caja.insert("end", "No hay sesiones para este usuario.")
            else:
                for s in sesiones:
                    caja.insert("end", f"Sesion: {s['nombre']} | {s['fecha']}\n")
                    for ej in s["ejercicios"]:
                        caja.insert("end",
                            f"  - {ej['nombre']} | {ej['musculo']} | "
                            f"{ej['peso']}kg | {ej['series']}x{ej['repeticiones']}\n")
                    caja.insert("end", "\n")
            caja.configure(state="disabled")

        self._boton("Buscar", buscar)

    def _pantalla_progreso(self):
        self._limpiar()
        self._titulo("Analizar progreso")
        e_usuario = self._entrada("Usuario")
        lista = list(EJERCICIOS.keys())
        ej_var = ctk.StringVar(value=lista[0])
        ctk.CTkLabel(self.panel, text="Ejercicio", text_color="#aaaaaa").pack()
        ctk.CTkOptionMenu(self.panel, values=lista, variable=ej_var, width=280).pack(pady=3)
        msg = self._mensaje()

        def analizar():
            sesiones = [s for s in cargar(ARCHIVO_SESIONES)
                        if s["usuario"] == e_usuario.get().strip()]
            if not sesiones:
                msg.configure(text="No hay sesiones para este usuario.", text_color="red")
                return
            resultado = AnalizadorProgreso(sesiones).analizar(ej_var.get())
            msg.configure(text=resultado, text_color="white")

        self._boton("Analizar", analizar)

    def _pantalla_recomendacion(self):
        self._limpiar()
        self._titulo("Recomendacion")
        e_usuario = self._entrada("Usuario")
        lista = list(EJERCICIOS.keys())
        ej_var = ctk.StringVar(value=lista[0])
        ctk.CTkLabel(self.panel, text="Ejercicio", text_color="#aaaaaa").pack()
        ctk.CTkOptionMenu(self.panel, values=lista, variable=ej_var, width=280).pack(pady=3)
        msg = self._mensaje()

        def recomendar():
            usuarios = cargar(ARCHIVO_USUARIOS)
            nombre = e_usuario.get().strip()
            if nombre not in usuarios:
                msg.configure(text="Usuario no encontrado.", text_color="red")
                return
            sesiones = [s for s in cargar(ARCHIVO_SESIONES) if s["usuario"] == nombre]
            if not sesiones:
                msg.configure(text="No hay sesiones para este usuario.", text_color="red")
                return
            rec = Recomendador(sesiones, usuarios[nombre]["peso"], usuarios[nombre]["nivel"])
            msg.configure(text=rec.analizar(ej_var.get()), text_color="white")

        self._boton("Generar", recomendar)

    def _pantalla_equilibrio(self):
        self._limpiar()
        self._titulo("Equilibrio muscular")
        e_usuario = self._entrada("Usuario")
        msg = self._mensaje()
        frame_grafico = ctk.CTkFrame(self.panel, fg_color="transparent")
        frame_grafico.pack(fill="both", expand=True)

        def analizar():
            nombre = e_usuario.get().strip()
            sesiones = [s for s in cargar(ARCHIVO_SESIONES) if s["usuario"] == nombre]
            if not sesiones:
                msg.configure(text="No hay sesiones para este usuario.", text_color="red")
                return
            eq = AnalizadorEquilibrio(sesiones)
            dist = eq.calcular_distribucion()
            msg.configure(text=eq.analizar(), text_color="white")
            for w in frame_grafico.winfo_children():
                w.destroy()
            fig, ax = plt.subplots(figsize=(5, 3), facecolor="#0f0f1a")
            ax.set_facecolor("#0f0f1a")
            ax.bar(dist.keys(), dist.values(), color="#4fc3f7")
            ax.set_ylabel("%", color="white")
            ax.tick_params(colors="white")
            ax.set_title("Distribucion muscular", color="white")
            plt.xticks(rotation=30, ha="right")
            plt.tight_layout()
            canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            plt.close(fig)

        self._boton("Analizar", analizar)


if __name__ == "__main__":
    app = App()
    app.mainloop()