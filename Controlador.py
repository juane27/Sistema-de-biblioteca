import Modelo

class Controlador:

    def __init__(self):
        self.BD = Modelo.ModeloProductos()
        self.BD1 = Modelo.ModeloUsuarios()
        self.BD2 = Modelo.ModeloEmpleados()
        self.ListaResultado = []
        self.ListaResultadou = []
        self.ListaResultadoe = []

    def operaciones(self, precio, cantidad, marca, nombre, caducidad, codigo, operacion):
        if operacion == 1:
            try:
                self.BD.ingresarDB(precio.get(), cantidad.get(), marca.get(), nombre.get(), caducidad.get(), codigo.get())
                return 0
            except:
                return -1
        elif operacion == 2:
            try:
                self.BD.modificarDB(precio.get(), cantidad.get(), marca.get(), nombre.get(), caducidad.get(), codigo.get())
                return 0
            except:
                return -1
        elif operacion == 3:
            print(type(codigo))
            try:
                self.BD.eliminarDB(codigo.get())
                return 0
            except:
                return -1
        elif operacion == 4:
            try:
                self.BD.consultarDB(codigo.get())
                self.ListaResultado.append(self.BD.precio)
                self.ListaResultado.append(self.BD.cantidad)
                self.ListaResultado.append(self.BD.marca)
                self.ListaResultado.append(self.BD.nombre)
                self.ListaResultado.append(self.BD.caducidad)
                return 0
            except:
                return -1


    def operacionesu(self, nombreu, apellidou, edadu, documentou, contraseñau, operacion):
        if operacion == 1:
            print(type(documentou))
            try:
                self.BD1.ingresarDB(nombreu.get(), apellidou.get(), edadu.get(), documentou.get(), contraseñau.get())
                return 0
            except:
                return -1
        elif operacion == 2:
            try:
                self.BD1.modificarDB(nombreu.get(), apellidou.get(), edadu.get(), documentou.get(), contraseñau.get())
                return 0
            except:
                return -1
        elif operacion == 3:
            try:
                self.BD1.eliminarDB(documentou.get())
                return 0
            except:
                return -1
        elif operacion == 4:
            try:
                self.BD1.consultarDB(documentou.get())
                self.ListaResultadou.append(self.BD1.nombreu)
                self.ListaResultadou.append(self.BD1.apellidou)
                self.ListaResultadou.append(self.BD1.edadu)
                self.ListaResultadou.append(self.BD1.contraseñau)
                return 0
            except:
                return -1





    def operacionese(self, nombree, apellidoe, edade, puesto, documentoe, contraseñae, operacion):
        if operacion == 1:
            try:
                self.BD2.ingresarDB(nombree.get(), apellidoe.get(), edade.get(), puesto.get(), documentoe.get(), contraseñae.get())
                return 0
            except:
                return -1
        elif operacion == 2:
            try:
                self.BD2.modificarDB(nombree.get(), apellidoe.get(), edade.get(), puesto.get(), documentoe.get(), contraseñae.get())
                return 0
            except:
                return -1
        elif operacion == 3:
            try:
                self.BD2.eliminarDB(documentoe.get())
                return 0
            except:
                return -1
        elif operacion == 4:
            try:
                self.BD2.consultarDB(documentoe.get())
                print('controlador')
                print(self.BD2.nombree)
                self.ListaResultadoe.append(self.BD2.nombree)
                self.ListaResultadoe.append(self.BD2.apellidoe)
                self.ListaResultadoe.append(self.BD2.edade)
                self.ListaResultadoe.append(self.BD2.puesto)
                self.ListaResultadoe.append(self.BD2.contraseñae)
                return 0
            except:
                return -1