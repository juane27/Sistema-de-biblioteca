import mysql.connector

base_datos = mysql.connector.connect(host="localhost", user="root", password="root")



puntero = base_datos.cursor()

puntero.execute("CREATE DATABASE Biblioteca")

base_datos = mysql.connector.connect(host="localhost", user="root", password="root", database="Biblioteca")

puntero = base_datos.cursor()

puntero.execute("CREATE TABLE productos (precio decimal(6,2), cantidad smallint, marca varchar(50), nombre varchar(120), caducidad varchar(5), codigo varchar(3))")

puntero.execute("CREATE TABLE usuarios (nombre varchar(20), apellido varchar(20), edad smallint, documento varchar(20), contraseña varchar(30))")

puntero.execute("CREATE TABLE empleados (nombre varchar(20), apellido varchar(20), edad smallint, puesto varchar(30), documento varchar(20), contraseña varchar(30))")