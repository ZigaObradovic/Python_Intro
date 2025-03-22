import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(700, 200, 500, 500)
        self.setWindowIcon(QIcon("GUI/IMG_1193.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #278f3f;""background-color: #ebe9b5;""font-weight: bold;""font-style: italic;""text-decoration: underline;")

        #label.setAlignment(Qt.AlignBottom) # VERTICALY BOTTOM
        #label.setAlignment(Qt.AlignTop) # VERTICALY TOP
        #label.setAlignment(Qt.AlignVCenter) # VERTICALY CENTER
        #label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        #label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        #label.setAlignment(Qt.AlignLeft) # HORIZONTALLY Left
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # SKUPAJ
        label.setAlignment(Qt.AlignCenter)

        label2 = QLabel(self)
        label2.setGeometry(0, 100, 250, 250)

        pixmap = QPixmap("GUI/IMG_1193.jpg")

        label2.setPixmap(pixmap)
        label2.setScaledContents(True)
        label2.setGeometry((self.width() - label2.width())//2, (self.height() - label2.height())//2, label2.width(), label2.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()