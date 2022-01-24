import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Controlador

app = Controlador.Controlador()

ventana = tk.Tk()
ventana.title("Biblioteca")

#### Vista productos ####
ttk.Label(ventana, text ="Productos").grid(column=0, row=0, columnspan=2)
ttk.Label(ventana, text ="Usuarios").grid(column=2, row=0, columnspan=2)
ttk.Label(ventana, text ="Empleados").grid(column=4, row=0, columnspan=2)

ttk.Label(ventana, text ="Precio").grid(column=0, row=1)
precio = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=precio).grid(column=1, row=1)

ttk.Label(ventana, text ="Cantidad").grid(column=0, row=2)
cantidad = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=cantidad).grid(column=1, row=2)

ttk.Label(ventana, text ="Marca").grid(column=0, row=3)
marca = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=marca).grid(column=1, row=3)

ttk.Label(ventana, text ="Caducidad").grid(column=0, row=4)
caducidad = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=caducidad).grid(column=1, row=4)

ttk.Label(ventana, text ="Nombre").grid(column=0, row=5)
nombre = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=nombre).grid(column=1, row=5)

ttk.Label(ventana, text ="Codigo").grid(column=0, row=6)
codigo = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=codigo).grid(column=1, row=6)

#### Vista Usuarios ####

ttk.Label(ventana, text ="Nombre").grid(column=2, row=1)
nombreu = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=nombreu).grid(column=3, row=1)

ttk.Label(ventana, text ="Apellido").grid(column=2, row=2)
apellidou = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=apellidou).grid(column=3, row=2)

ttk.Label(ventana, text ="Edad").grid(column=2, row=3)
edadu = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=edadu).grid(column=3, row=3)

ttk.Label(ventana, text ="Documento").grid(column=2, row=4)
documentou = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=documentou).grid(column=3, row=4)

ttk.Label(ventana, text ="Contraseña").grid(column=2, row=5)
contraseñau = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=contraseñau).grid(column=3, row=5)


#### Vista Empleados ####

ttk.Label(ventana, text ="Nombre").grid(column=4, row=1)
nombree = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=nombree).grid(column=5, row=1)

ttk.Label(ventana, text ="Apellido").grid(column=4, row=2)
apellidoe = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=apellidoe).grid(column=5, row=2)

ttk.Label(ventana, text ="Edad").grid(column=4, row=3)
edade = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=edade).grid(column=5, row=3)

ttk.Label(ventana, text ="Puesto").grid(column=4, row=4)
puesto = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=puesto).grid(column=5, row=4)

ttk.Label(ventana, text ="Documento").grid(column=4, row=5)
documentoe = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=documentoe).grid(column=5, row=5)

ttk.Label(ventana, text ="Contraseña").grid(column=4, row=6)
contraseñae = tk.StringVar()
ttk.Entry(ventana, width = 20, textvariable=contraseñae).grid(column=5, row=6)



ttk.Label(ventana, text ="Para operar sobre un producto ingrese su código.").grid(column=0, row=9, columnspan=2)
ttk.Label(ventana, text ="Para operar sobre un usuario ingrese su documento.").grid(column=2, row=9, columnspan=2)
ttk.Label(ventana, text ="Para operar sobre un empleado ingrese su documento.").grid(column=4, row=9, columnspan=2)




#### Ingresar datos ####


def IngresarClick():
    if app.operaciones(precio, cantidad, marca, nombre, caducidad, codigo, 1) == 0:
        messagebox.showinfo("Mensaje", "Ingreso exitoso")
    else:
        messagebox.showerror("Mensaje", "Hubo un problema")
ttk.Button(ventana, text ="Ingresar", command=IngresarClick).grid(column=0, row = 7)

def IngresarClickU():
    if app.operacionesu(nombreu, apellidou, edadu, documentou, contraseñau, 1) == 0:
        messagebox.showinfo("Mensaje", "Ingreso exitoso")
    else:
        messagebox.showerror("Mensaje", "Hubo un problema")
ttk.Button(ventana, text ="Ingresar", command=IngresarClickU).grid(column=2, row = 7)

def IngresarClickE():
    if app.operacionese(nombree, apellidoe, edade, puesto, documentoe, contraseñae, 1) == 0:
        messagebox.showinfo("Mensaje", "Ingreso exitoso")
    else:
        messagebox.showerror("Mensaje", "Hubo un problema")
ttk.Button(ventana, text ="Ingresar", command=IngresarClickE).grid(column=4, row = 7)


#### Modificar datos ####

def ModificarClick():
    if app.operaciones(precio, cantidad, marca, nombre, caducidad,codigo,2) == 0:
        messagebox.showinfo("Informacion", "Modificacion exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")

ttk.Button(ventana, text ="Modificar", command=ModificarClick).grid(column=1, row = 7)

def ModificarClickU():
    if app.operacionesu(nombreu, apellidou, edadu, documentou, contraseñau,2) == 0:
        messagebox.showinfo("Informacion", "Modificacion exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")

ttk.Button(ventana, text ="Modificar", command=ModificarClickU).grid(column=3, row = 7)

def ModificarClickE():
    if app.operacionese(nombree, apellidoe, edade, puesto, documentoe, contraseñae,2) == 0:
        messagebox.showinfo("Informacion", "Modificacion exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Modificar", command=ModificarClickE).grid(column=5, row = 7)



#### Borrar datos ####
def BorrarClick():
    if app.operaciones("", "", "", "", "",codigo,3) == 0:
        messagebox.showinfo("Informacion", "Borrado exitoso")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Borrar", command=BorrarClick).grid(column=0, row = 8)

def BorrarClickU():
    if app.operacionesu("", "", "", documentou, "",3) == 0:
        messagebox.showinfo("Informacion", "Borrado exitoso")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Borrar", command=BorrarClickU).grid(column=2, row = 8)

def BorrarClickE():
    if app.operacionese("", "", "", "",documentoe, "",3) == 0:
        messagebox.showinfo("Informacion", "Borrado exitoso")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Borrar", command=BorrarClickE).grid(column=4, row = 8)



#### Consultar DB ####


def ConsultarClick():
    if app.operaciones("", "", "", "", "",codigo,4) == 0:
        precio.set(str(app.ListaResultado[0]))
        cantidad.set(str(app.ListaResultado[1]))
        marca.set(str(app.ListaResultado[2]))
        nombre.set(str(app.ListaResultado[3]))
        caducidad.set(str(app.ListaResultado[4]))
        messagebox.showinfo("Informacion", "Consulta exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")

ttk.Button(ventana, text ="Consultar", command=ConsultarClick).grid(column=1, row = 8)


def ConsultarClickU():
    if app.operacionesu("", "", "",documentou,"", 4) == 0:
        nombreu.set(str(app.ListaResultadou[0]))
        apellidou.set(str(app.ListaResultadou[1]))
        edadu.set(str(app.ListaResultadou[2]))
        contraseñau.set(str(app.ListaResultadou[3]))
        messagebox.showinfo("Informacion", "Consulta exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Consultar", command=ConsultarClickU).grid(column=3, row = 8)

def ConsultarClickE():
    if app.operacionese("", "", "", "",documentoe, "",4) == 0:
        nombree.set(str(app.ListaResultadoe[0]))
        apellidoe.set(str(app.ListaResultadoe[1]))
        edade.set(str(app.ListaResultadoe[2]))
        puesto.set(str(app.ListaResultadoe[3]))
        contraseñae.set(str(app.ListaResultadoe[4]))
        messagebox.showinfo("Informacion", "Consulta exitosa")
    else:
        messagebox.showerror("Informacion", "Hubo un problema")
ttk.Button(ventana, text ="Consultar", command=ConsultarClickE).grid(column=5, row = 8)

ventana.mainloop()