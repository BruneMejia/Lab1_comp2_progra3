# ControlVentan.py
#En esta parte empezamos haciendo la importación de librerías
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget)
from PyQt5.QtGui import QIcon
import sys
#Aquí se importan las librerías necesarias para crear la interfaz gráfica de usuario (GUI) utilizando PyQt5.
#En esta parte se crea la aplicación 
#Creacion de la aplicacion

app = QApplication(sys.argv)
#En esta parte se define la función para agregar una venta a la lista
#Funcion para agragar la venta 
def venta():
    producto = entrada1.text()
    cantidad = entrada2.text()
    monto = entrada3.text()
#En esta parte se valida que los campos no esten vacios ya que si lo estan se muestra un mensaje de error
    if producto and cantidad and monto:
        try:
#Se valida que el monto sea un número válido, si no lo es se muestra un mensaje de error
#En esta parte se convierte el monto a float para que se muestre con dos decimales
            monto_float = float(monto)
            lista_ventas.addItem(f" #{cantidad} {producto}  ${monto_float:.2f}")
            entrada1.clear()
            entrada2.clear()
            entrada3.clear()
        except ValueError:
#En esta parte se muestra un mensaje de error si el monto no es un número válido
            QMessageBox.warning(ventana, "Error", "El monto debe ser un nmero valido.")
    else:
        QMessageBox.warning(ventana, "Error", "Por favor ingrese rl producto y monto.")
#En esta parte se define la función para eliminar una venta de la lista
#Funcion para eliminar la venta
#En esta parte se valida que se haya seleccionado un item de la lista para eliminarlo, si no se muestra un mensaje de error
#Si esta seleccionado se elimina el item de la lista
def eliminar():
    item = lista_ventas.currentItem()
    if item:
        lista_ventas.takeItem(lista_ventas.row(item))
    else:
        QMessageBox.warning(ventana, "Error", "Porfa seleccione una venta para eliminar.")
#En esta parte se crea la ventana principal de la aplicación
#Creacion de la ventana
#Se define el título, tamaño e icono de la ventana
#Luego se crean los elementos de la interfaz (etiquetas, campos de entrada, botones y lista)
#Finalmente se muestra la ventana y se inicia el bucle de eventos de la aplicación
ventana = QWidget()
ventana.setWindowTitle("CONTROL DE VENTAS DE VERDURAS FM C:")
#Tamaño
ventana.setGeometry(400,400,500,300)
#Icono
icono =QIcon("verduras.ico")
ventana.setWindowIcon(icono)
#Elementos de la interfaz
layout = QVBoxLayout()
texto1 = QLabel("Producto")
entrada1 = QLineEdit()
texto2 = QLabel("Cantidad")
entrada2 = QLineEdit()
texto3 = QLabel("Monto")
entrada3 = QLineEdit()
texto4 = QLabel("Listado de productos:")
layout.addWidget(texto1)
layout.addWidget(entrada1)
layout.addWidget(texto2)
layout.addWidget(entrada2)
layout.addWidget(texto3)
layout.addWidget(entrada3)
layout.addWidget(texto4)
#Lista
lista_ventas = QListWidget()
layout.addWidget(lista_ventas)
#boton
boton1 = QPushButton("Agregar venta")
boton1.clicked.connect(venta)
layout.addWidget(boton1)
#boton para eliminar
#definicion del boton eliminar
#Se conecta el boton a la funcion eliminar
#Se agrega el boton al layout
boton2 = QPushButton("Eliminar venta")
boton2.clicked.connect(eliminar)
layout.addWidget(boton2)
#Mostrar la ventana
#Se establece el layout de la ventana
#Se muestra la ventana y se inicia el bucle de eventos
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())

 