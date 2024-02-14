#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class GuiApp:
    def __init__(self, master=None):
        # Main window
        self.window = tk.Tk(master)
        self.window.configure(height=200, width=200)
        self.window.title("Gestor de Exercício")
        frame_1 = ttk.Frame(self.window)
        frame_1.configure(height=400, relief="sunken", width=600)
        frame_1_1 = ttk.Frame(frame_1)
        frame_1_1.configure(height=200, width=200)

        ## Carregar/Load Button
        self.load_button = ttk.Button(frame_1_1, name="load_button")
        self.load_button.configure(text='Carregar')
        self.load_button.grid(column=0, padx=10, pady=30, row=0, sticky="nsew")

        ## Adicionar/Add Button
        self.add_button = ttk.Button(frame_1_1, name="add_button")
        self.add_button.configure(text='Adicionar')
        self.add_button.grid(column=0, padx=10, row=1, sticky="nsew")

        ## Modificar/Modify Button
        self.modify_button = ttk.Button(frame_1_1, name="modify_button")
        self.modify_button.configure(text='Modificar')
        self.modify_button.grid(
            column=0,
            padx=10,
            pady=10,
            row=2,
            sticky="nsew")
        
        ## Eliminar/Delete Button
        self.delete_button = ttk.Button(frame_1_1, name="delete_button")
        self.delete_button.configure(text='Eliminar')
        self.delete_button.grid(column=0, padx=10, row=3, sticky="nsew")

        frame_1_1.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        frame_1_2 = ttk.Frame(frame_1)
        frame_1_2.configure(height=200, width=200)

        ## Filtrar Frame
        self.filter_frame = ttk.Labelframe(frame_1_2, name="filter_frame")
        self.filter_frame.configure(height=200, text='Filtrar', width=200)
        frame_1_3 = ttk.Frame(self.filter_frame)
        frame_1_3.configure(height=200, width=200)

        ## Filtrar Label
        self.month_label = ttk.Label(frame_1_3, name="month_label")
        self.month_label.configure(text='Mês')
        self.month_label.grid(column=0, row=0, sticky="nsew")

        ## Filtrar Combobox
        self.month_combobox = ttk.Combobox(frame_1_3, name="month_combobox")
        self.month_combobox.grid(
            column=1,
            padx=10,
            pady=10,
            row=0,
            sticky="nsew")
        frame_1_3.grid(column=0, columnspan=2, padx=10, row=0)

        ##Aplicar/Apply Button
        self.apply_button = ttk.Button(self.filter_frame, name="apply_button")
        self.apply_button.configure(text='Aplicar')
        self.apply_button.grid(
            column=0,
            columnspan=2,
            padx=40,
            pady=10,
            row=2,
            sticky="nsew")
        

        self.filter_frame.grid(
            column=0,
            padx=10,
            pady=10,
            row=0,
            sticky="nsew")
        frame_1_2.grid(column=1, padx=10, pady=10, row=0, sticky="nsew")
        frame_1.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")


        ## Treeview Frame
        frame2 = ttk.Frame(self.window)
        frame2.configure(height=200, relief="sunken", width=200)
        
        ## Treeview
        self.data_treeview = ttk.Treeview(frame2, name="data_treeview")
        self.data_treeview.configure(selectmode="browse")
        self.data_treeview.grid(
            column=0,
            padx=10,
            pady=10,
            row=0,
            sticky="nsew")
        frame2.grid(column=0, padx=10, pady=10, row=1, sticky="nsew")
        frame2.columnconfigure(0, weight=1)


        ## Estatistica Frame
        frame3 = ttk.Frame(self.window)
        frame3.configure(height=200, width=200)

        ## Numero de exercicios Label
        self.exercicios_label = ttk.Label(frame3, name="exercicios_label")
        self.exercicios_label.configure(text='Número de exercícios: ')
        self.exercicios_label.grid(column=0, row=0)
        
        ## Duracao Media Label
        self.minutos_label = ttk.Label(frame3, name="minutos_label")
        self.minutos_label.configure(text='Duração média: ')
        self.minutos_label.grid(column=1, row=0)
        
        ## Total Calorias Label
        self.calorias_label = ttk.Label(frame3, name="calorias_label")
        self.calorias_label.configure(text='Total de calorias: ')
        self.calorias_label.grid(column=2, row=0)
        
        frame3.grid(column=0, row=2, sticky="nsew")

        # Main widget
        self.mainwindow = self.window

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run()
