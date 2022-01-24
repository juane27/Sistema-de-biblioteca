import mysql.connector

class ModeloProductos:

    def __init__ (self):
        self.precio = ""
        self.cantidad = ""
        self.marca = ""
        self.nombre = ""
        self.caducidad = ""

        try:
            self.instancia = mysql.connector.connect(host="localhost", user="root", password="root", database="Biblioteca")
            self.puntero = self.instancia.cursor()
        except:        
            print("Error de conexion")

    def ingresarDB(self, precio, cantidad, marca, nombre, caducidad, codigo):
        sql = "INSERT INTO productos (precio, cantidad, marca, nombre, caducidad, codigo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (precio, cantidad, marca, nombre, caducidad, codigo)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def modificarDB (self, precio, cantidad, marca, nombre, caducidad, codigo):
        sql = "UPDATE productos SET precio = %s, cantidad = %s, marca = %s, nombre = %s, caducidad = %s WHERE codigo = %s"
        valores = (precio, cantidad, marca, nombre, caducidad, codigo)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def eliminarDB (self, codigo):
        sql = "DELETE FROM productos WHERE codigo ='" + codigo + "'"

        try:
            self.puntero.execute(sql)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def consultarDB (self, codigo):
        sql = "SELECT precio, cantidad, marca, nombre, caducidad FROM productos WHERE codigo ='" + codigo + "'"

        try:
            self.puntero.execute(sql)
            resultado = self.puntero.fetchall()
            for x in resultado:
                self.precio = x[0]
                self.cantidad = x[1]
                self.marca = x[2]
                self.nombre = x[3]
                self.caducidad = x[4]
        except:
            raise Exception("No se pudo ejecutar")

    def __del__(self):
        self.instancia.close()


###### CLASE USUARIOS ######

class ModeloUsuarios:

    def __init__ (self):
        self.nombreu = ""
        self.apellidou = ""
        self.edadu = ""
        self.documentou = ""
        self.contraseñau = ""

        try:
            self.instancia = mysql.connector.connect(host="localhost", user="root", password="root", database="Biblioteca")
            self.puntero = self.instancia.cursor()
        except:        
            print("Error de conexion")

    def ingresarDB(self, nombreu, apellidou, edadu, documentou, contraseñau):
        sql = "INSERT INTO usuarios (nombre, apellido, edad, documento, contraseña) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombreu, apellidou, edadu, documentou, contraseñau)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def modificarDB (self, nombreu, apellidou, edadu, documentou, contraseñau):
        sql = "UPDATE usuarios SET nombre = %s, apellido = %s, edad = %s, documento = %s, contraseña = %s WHERE documento ='" + documentou + "'"
        valores = (nombreu, apellidou, edadu, documentou, contraseñau)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def eliminarDB (self, documentou):
        sql = "DELETE FROM usuarios WHERE documento ='" + documentou + "'"

        try:
            self.puntero.execute(sql)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def consultarDB (self, documentou):
        sql = "SELECT nombre, apellido, edad, contraseña FROM usuarios WHERE documento ='" + documentou + "'"

        try:
            self.puntero.execute(sql)
            resultado = self.puntero.fetchall()
            for x in resultado:
                self.nombreu = x[0]
                self.apellidou = x[1]
                self.edadu = x[2]
                self.contraseñau = x[3]
        except:
            raise Exception("No se pudo ejecutar")

    def __del__(self):
        self.instancia.close()

###### CLASE Empleados ######

class ModeloEmpleados:

    def __init__ (self):
        self.nombree2 = ""
        self.apellidoe2 = ""
        self.edade2 = ""
        self.puesto2 = ""
        self.documentoe2 = ""
        self.contraseñae2 = ""

        try:
            self.instancia = mysql.connector.connect(host="localhost", user="root", password="root", database="Biblioteca")
            self.puntero = self.instancia.cursor()
        except:        
            print("Error de conexion")

    def ingresarDB(self, nombree, apellidoe, edade, puesto, documentoe, contraseñae):
        sql = "INSERT INTO empleados (nombre, apellido, edad, puesto, documento, contraseña) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombree, apellidoe, edade, puesto, documentoe, contraseñae)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def modificarDB (self, nombree, apellidoe, edade, puesto, documentoe, contraseñae):
        sql = "UPDATE empleados SET nombre = %s, apellido = %s, edad = %s, puesto = %s, documento = %s, contraseña = %s WHERE documento ='" + documentoe + "'"
        valores = (nombree, apellidoe, edade, puesto, documentoe, contraseñae)

        try:
            self.puntero.execute(sql, valores)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def eliminarDB (self, documentoe):
        sql = "DELETE FROM empleados WHERE documento ='" + documentoe + "'"

        try:
            self.puntero.execute(sql)
            self.instancia.commit()
        except:
            raise Exception("No se pudo ejecutar")

    def consultarDB (self, documentoe):
        sql = "SELECT nombre, apellido, edad, puesto, contraseña FROM empleados WHERE documento ='" + documentoe + "'"

        try:
            self.puntero.execute(sql)
            resultado = self.puntero.fetchall()
            for x in resultado:
                self.nombree = x[0]
                self.apellidoe = x[1]
                self.edade = x[2]
                self.puesto = x[3]
                self.contraseñae = x[4]
        except:
            raise Exception("No se pudo ejecutar")

    def __del__(self):
        self.instancia.close()

