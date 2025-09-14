import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette
from PyQt5.QtCore import Qt

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Number generator")
        self.setWindowIcon(QIcon("1722485002-0.jpg"))

        #число для генерации
        self.number = QLabel(str(random.randint(1, 10)), self)
        self.number.setGeometry(0, 100, 500, 100)
        self.number.setFont(QFont("Arial", 50))
        self.number.setAlignment(Qt.AlignHCenter)

        #создание кнопки генерации
        self.btn = QPushButton("Generate!", self)
        self.btn.resize(100, 50)
        self.btn.move(200, 300)
        self.btn.setFont(QFont("Arial", 14))
        self.btn.setStyleSheet("color:black;"
                               "background-color:yellow;"
                               "font-weight:bold")
        self.btn.clicked.connect(self.generateNumber)

        #название
        label = QLabel("Random number", self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 500, 100 )
        label.setAlignment( Qt.AlignHCenter | Qt.AlignTop)

        #выбор числа от
        self.spbFrom = QSpinBox(self)
        self.spbFrom.move(120, 230)
        self.spbFrom.setPrefix("From ")
        self.spbFrom.setRange(0, 10000)
        self.spbFrom.setWrapping(True)

        #выбор числа до
        self.spbTo = QSpinBox(self)
        self.spbTo.move(300, 230)
        self.spbTo.setPrefix("To ")
        self.spbTo.setRange(0, 10000)
        self.spbTo.setWrapping(True)

    #обработчик событий при нажатии кнопки
    def generateNumber(self):
        newNumber = random.randint(self.spbFrom.value(), self.spbTo.value())
        self.number.setText(str(newNumber))

    #обработчик событий при выходе
    def closeEvent(self, event):
        exit = QMessageBox.question(self, "Exit", "Are you sure you wanna leave?", QMessageBox.Yes | QMessageBox.No)
        if exit == QMessageBox.Yes:
            event.accept()
        elif exit == QMessageBox.No:
            event.ignore()

#головная функция программы
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()