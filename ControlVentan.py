from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox)
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("CONTROL DE VENTAS DE VERDURAS")

ventana.setGeometry(500,500,500,400)

ventana.show()
sys.exit(app.exec_())