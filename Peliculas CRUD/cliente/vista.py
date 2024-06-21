import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas, listar_generos, listar_clasificaciones, listar_idiomas, listar_peliculas , guardar_peli, editar_peli, borrar_peli

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)

    #  niveles  #

    #principal

    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Consultas')
    barra.add_cascade(label='Acerca de..')
    barra.add_cascade(label='Ayuda')

    #submenu
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=580,height=420,bg="grey")
        self.root = root
        self.pack()
        self.id_peli = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)

        self.label_idiomas = tk.Label(self, text="Idioma: ")
        self.label_idiomas.config(font=('Arial', 12, 'bold'))
        self.label_idiomas.grid(row=0, column=3, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=('Arial',12,'bold'))
        self.label_duracion.grid(row= 1, column=0,padx=10,pady=10)

        self.label_genero = tk.Label(self, text="Genero: ")
        self.label_genero.config(font=('Arial',12,'bold'))
        self.label_genero.grid(row= 2, column=0,padx=10,pady=10)

        self.label_clasificacion = tk.Label(self, text="Clasificacion: ")
        self.label_clasificacion.config(font=('Arial', 12, 'bold'))
        self.label_clasificacion.grid(row=2, column=3, padx=10, pady=10)
    
    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled',font=('Arial',12))
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10, columnspan='2')

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.duracion)
        self.entry_duracion.config(width=50, state='disabled',font=('Arial',12))
        self.entry_duracion.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')


        #aca limpiamos la lista de tuplas que nos retorna la funcion
        x = listar_generos()
        print(x)
        y = []
        for i in x:
            y.append(i[1])
        print(y)

        #concatenemos el nuevo array
        self.generos = ['Seleccione uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25, state='disabled',font=('Arial',12))
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 2, column=1,padx=5,pady=5, columnspan='2')


        m = listar_clasificaciones()
        h = []
        for l in m:
            h.append(l[1])
        print(m)
        # concatenemos el nuevo array
        self.clasificaciones = ['Seleccione uno'] + h
        self.entry_clasificacion = ttk.Combobox(self, state="readonly")
        self.entry_clasificacion['values'] = self.clasificaciones
        self.entry_clasificacion.current(0)
        self.entry_clasificacion.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_clasificacion.bind("<<ComboboxSelected>>")
        self.entry_clasificacion.grid(row=2, column=4, padx=5, pady=5, columnspan='2')


        e = listar_idiomas()
        j = []
        for g in e:
            j.append(g[1])
        print(e)
        # concatenemos el nuevo array
        self.idiomas = ['Seleccione uno'] + j
        self.entry_idiomas = ttk.Combobox(self, state="readonly")
        self.entry_idiomas['values'] = self.idiomas
        self.entry_idiomas.current(0)
        self.entry_idiomas.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_idiomas.bind("<<ComboboxSelected>>")
        self.entry_idiomas.grid(row=0, column=4, padx=5, pady=5, columnspan='2')

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 3, column=0,padx=10,pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row= 3, column=1,padx=10,pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row= 3, column=2, padx=10,pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_idiomas.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_clasificacion.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_genero.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.duracion.set('')
        self.id_peli = None #reseteanis el id luego de eliminar
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current(),
            self.entry_clasificacion.current(),
            self.entry_idiomas.current()
        )

        if self.id_peli == None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    def mostrar_tabla(self):
        self.lista_p = listar_peliculas()
        print(listar_peliculas())
        self.lista_p.reverse() #para invertir el orden
        self.tabla = ttk.Treeview(self, columns=('Nombre','Duración','Clasificacion','Genero','Idioma'))
        self.tabla.grid(row=4,column=0,columnspan=6)

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=6,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Duración')
        self.tabla.heading('#3',text='Clasificacion')
        self.tabla.heading('#4', text='Genero')
        self.tabla.heading('#5', text='Idioma')
       
        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0], values = (p[1],p[2],p[4],p[6],p[5]))

        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 5, column=0,padx=10,pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 5, column=1,padx=10,pady=10)

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']

            self.nombre_peli_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.clasificacion_peli_e = self.tabla.item(self.tabla.selection())['values'][3]
            self.idioma_peli_e = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli_e)
            self.duracion.set(self.dura_peli_e)
            self.entry_genero.current(self.generos.index(self.gene_peli_e))
            self.entry_clasificacion.current(self.clasificacion.index(self.clasificacion_peli_e))
            self.entry_idioma.current(self.idioma.index(self.idioma_peli_e))
        except:
            pass
    
    def eliminar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            borrar_peli(int(self.id_peli))
            self.mostrar_tabla()
            self.id_peli = None #reseteanis el id luego de eliminar
        except:
            pass