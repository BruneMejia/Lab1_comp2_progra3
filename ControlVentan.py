from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget)
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

#Funcion para agragar la venta 
def venta():
    producto = entrada1.text()
    cantidad = entrada2.text()
    monto = entrada3.text()

    if producto and cantidad and monto:
        try:
            monto_float = float(monto)
            lista_ventas.addItem(f" #{cantidad} {producto}  ${monto_float:.2f}")
            entrada1.clear()
            entrada2.clear()
            entrada3.clear()
        except ValueError:
            QMessageBox.warning(ventana, "Error", "El monto debe ser un nmero valido.")
    else:
        QMessageBox.warning(ventana, "Error", "Por favor ingrese rl producto y monto.")


def eliminar():
    item = lista_ventas.currentItem()
    if item:
        lista_ventas.takeItem(lista_ventas.row(item))
    else:
        QMessageBox.warning(ventana, "Error", "Porfa seleccione una venta para eliminar.")


ventana = QWidget()
ventana.setWindowTitle("CONTROL DE VENTAS DE VERDURAS FM C:")

ventana.setGeometry(400,400,500,300)
#Icono
icono =QIcon("verduras.ico")
ventana.setWindowIcon(icono)

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

lista_ventas = QListWidget()
layout.addWidget(lista_ventas)

#boton
boton1 = QPushButton("Agregar venta")
boton1.clicked.connect(venta)
layout.addWidget(boton1)

boton2 = QPushButton("Eliminar venta")
boton2.clicked.connect(eliminar)
layout.addWidget(boton2)


ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())

 