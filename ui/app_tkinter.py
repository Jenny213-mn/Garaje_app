import tkinter as tk
from tkinter import messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Labels
        tk.Label(root, text="Placa").grid(row=0, column=0)
        tk.Label(root, text="Marca").grid(row=1, column=0)
        tk.Label(root, text="Propietario").grid(row=2, column=0)

        # Entradas
        self.entry_placa = tk.Entry(root)
        self.entry_marca = tk.Entry(root)
        self.entry_propietario = tk.Entry(root)

        self.entry_placa.grid(row=0, column=1)
        self.entry_marca.grid(row=1, column=1)
        self.entry_propietario.grid(row=2, column=1)

        # Botones
        btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=3, column=0)

        btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        btn_limpiar.grid(row=3, column=1)

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=4, column=0, columnspan=2)

    def agregar_vehiculo(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, propietario)
        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_lista()
        self.limpiar_campos()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for v in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, str(v))

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)