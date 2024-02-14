#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Modificar:
    def __init__(self, master=None):
        # build Toplevel
        self.toplevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel.configure(height=200, width=200)
        self.toplevel.title("Adicionar/Modificar Exercício")
 
        frame1 = ttk.Frame(self.toplevel)
        frame1.configure(height=200, relief="sunken", width=200)

        ## Data/Date Label
        self.data_label = ttk.Label(frame1, name="data_label")
        self.data_label.configure(text='Data')
        self.data_label.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")

        ## Data/Date Entry
        self.date_entry = ttk.Entry(frame1, name="date_entry")
        self.date_entry.grid(column=1, padx=10, pady=10, row=0, sticky="nsew")

        ## Hora Inicio/Start Time Label
        self.inicio_label = ttk.Label(frame1, name="inicio_label")
        self.inicio_label.configure(text='Hora Início')
        self.inicio_label.grid(column=0, padx=10, pady=10, row=1, sticky="nsew")

        ## Hora Inicio/Start Time Entry
        self.inicio_entry = ttk.Entry(frame1, name="inicio_entry")
        self.inicio_entry.grid(column=1, padx=10, pady=10, row=1, sticky="nsew")

        ## Hora Fim/End Time Label
        self.fim_label = ttk.Label(frame1, name="fim_label")
        self.fim_label.configure(text='Hora de Fim')
        self.fim_label.grid(column=0, padx=10, pady=10, row=2, sticky="nsew")

        ## Hora Fim/End Time Entry
        self.fim_entry = ttk.Entry(frame1, name="fim_entry")
        self.fim_entry.grid(column=1, padx=10, pady=10, row=2, sticky="nsew")
        
        ## Tipo Exercicio/Exercise Type Label
        self.tipo_label = ttk.Label(frame1, name="tipo_label")
        self.tipo_label.configure(text='Tipo Exercício')
        self.tipo_label.grid(column=0, padx=10, pady=10, row=3, sticky="nsew")

        ## Tipo Exercicio/Exercise Type Entry
        self.tipo_entry = ttk.Entry(frame1, name="tipo_entry")
        self.tipo_entry.grid(column=1, padx=10, pady=10, row=3, sticky="nsew")

        ## Calorias/Calories Label
        self.caloria_label = ttk.Label(frame1, name="caloria_label")
        self.caloria_label.configure(text='Total Calorias')
        self.caloria_label.grid(column=0, padx=10, pady=10, row=4, sticky="nsew")

        ## Calorias/Calories Entry
        self.calorias_entry = ttk.Entry(frame1, name="calorias_entry")
        self.calorias_entry.grid(column=1, padx=10, pady=10, row=4)

        frame1.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        
        ## Button Frame
        frame2 = ttk.Frame(self.toplevel)
        frame2.configure(padding=10, width=200)

        ## OK Button
        self.ok_button = ttk.Button(frame2, name="ok_button")
        self.ok_button.configure(text='Ok')
        self.ok_button.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")

        ## Cancel Button
        self.cancel_button = ttk.Button(frame2, name="cancel_button")
        self.cancel_button.configure(text='Cancel')
        self.cancel_button.grid(column=0, padx=10, pady=10, row=1, sticky="nsew")

        frame2.grid(column=1, row=0)
        
        # Main widget
        self.mainwindow = self.toplevel

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = Modificar()
    app.run()