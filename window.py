from PyQt6.QtWidgets import QMessageBox

def err():
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setText("Программа крайне чуствительна, скорее всего ваш аудиофайл имеет плохое качетсво")
    error.show()