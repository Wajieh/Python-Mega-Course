import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton, QLineEdit
import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        birth_date  = QLabel ("DOB (MM/DD/YYYY): ")
        self.birth_date_line_edit = QLineEdit()

        calculate = QPushButton("Calculate Age")
        calculate.clicked.connect(self.calculate_age)
        self.output_label  = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(birth_date, 1, 0)
        grid.addWidget(self.birth_date_line_edit, 1, 1)
        grid.addWidget(calculate, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)  # ✅ Don't forget this!

    def calculate_age(self):
        try:
            current_year = datetime.datetime.now().year
            dob = self.birth_date_line_edit.text()
            yob = datetime.datetime.strptime(dob, "%m/%d/%Y").year
            age = current_year - yob
            name = self.name_line_edit.text()
            self.output_label.setText(f"{name} is {age} years old.")
        except ValueError:
            self.output_label.setText("Invalid date format. Use MM/DD/YYYY.")

app = QApplication(sys.argv)
age_calc = AgeCalculator()
age_calc.show()
sys.exit(app.exec())
