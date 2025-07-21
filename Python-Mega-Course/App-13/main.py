import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt6 App")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.show_message)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "Hello", "You clicked the button!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())

