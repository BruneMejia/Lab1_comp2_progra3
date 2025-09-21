from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget)
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

#Funcion para el agragar la venta 
def venta():
    producto = entrada1.text()
    monto = entrada2.text()

    if producto and monto:
        try:
            monto_float = float(monto)
            lista_ventas.addItem(f"{producto}  ${monto_float:.2f}")
            entrada1.clear()
            entrada2.clear()
        except ValueError:
            QMessageBox.warning(ventana, "Error", "Monto debe ser un nmero valido.")
    else:
        QMessageBox.warning(ventana, "Error", "Por favor ingrese rl producto y monto.")



ventana = QWidget()
ventana.setWindowTitle("CONTROL DE VENTAS DE VERDURAS")

ventana.setGeometry(400,400,500,300)
#Icono
icono =QIcon("verduras.ico")
ventana.setWindowIcon(icono)

layout = QVBoxLayout()
texto1 = QLabel("Producto")
entrada1 = QLineEdit()
texto2 = QLabel("Monto")
entrada2 = QLineEdit()
layout.addWidget(texto1)
layout.addWidget(entrada1)
layout.addWidget(texto2)
layout.addWidget(entrada2)

lista_ventas = QListWidget()
layout.addWidget(lista_ventas)


#boton
boton1 = QPushButton("Agregar venta")
boton1.clicked.connect(venta)
layout.addWidget(boton1)



ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())

 