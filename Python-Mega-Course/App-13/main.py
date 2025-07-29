from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
     QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, \
     QVBoxLayout, QComboBox, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import datetime, sys, sqlite3

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


<<<<<<< HEAD
=======

>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(600,600)
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_stu_section = QAction(QIcon("icons/add.png"),"Add Student", self)
        add_stu_section.triggered.connect(self.insert)
        file_menu_item.addAction(add_stu_section)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        search_section = QAction(QIcon("icons/search.png"),"Search", self)
        search_section.triggered.connect(self.search)
        edit_menu_item.addAction(search_section)


        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile Contact"))
        self.setCentralWidget(self.table)

<<<<<<< HEAD
    #     #Toolbar
    #     toolbar = QToolBar()
    #     toolbar.setMovable(True)
    #     self.addToolBar(toolbar)
    #     toolbar.addAction(add_stu_section)
    #     toolbar.addAction(search_section)

    #     #status bar
    #     statusbar = QStatusBar()
    #     self.setStatusBar(statusbar)

    #     #Click Detection
    #     self.table.cellClicked.connect(self.cell_clicked)


    # def cell_clicked(self):
    #     edit_button = QPushButton("Edit Record")
    #     edit_button.clicked.connect(self.edit)

    #     delete_button = QPushButton("Delete Record")
    #     delete_button.clicked.connect(self.delete)

    #     self.statusBar().addWidget(edit_button)
    #     self.statusBar().addWidget(delete_button)
=======
        #Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_stu_section)
        toolbar.addAction(search_section)

        #status bar
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        #Click Detection
        self.table.cellClicked.connect(self.clicked)


    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        self.statusBar.addWidget(edit_button)
>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c

    def load_data(self):    
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num,col_num, QTableWidgetItem(str(data)))
        connection.close()

<<<<<<< HEAD
#     # def insert(self):
#     #     dialog = InsertDialog()
#     #     dialog.exec()
 
#     # def search(self):
#     #     dialog = SearchDialog()
#     #     dialog.exec()
    
#     # def edit(self):...

#     # def delette(self):...

# class EditDialog(QDialog):
#     pass
=======
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()
 
    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def load_data(self):
    
    def edit(self):

    def delette(self):

class EditDialog(QDialog):
    pass
>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedWidth(300)
        self.setFixedHeight(600)
        
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Bio", "Phy", "Che"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.phone_num = QLineEdit()
        self.phone_num.setPlaceholderText("Phone #")
        layout.addWidget(self.phone_num)

        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text() 
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.phone_num.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name,course,mobile) VALUES (?,?,?)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
<<<<<<< HEAD
        main_window.load_data()
=======
        age_calc.load_data()
>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c

class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Search Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit(self)
        self.student_name.setPlaceholderText('Enter student name')
        layout.addWidget(self.student_name)

        self.button = QPushButton('Search', self)
        self.button.clicked.connect(self.search)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        row = list(result)
        print(row)
<<<<<<< HEAD
        items = main_window.table.findItems("John Smith", Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)
=======
        items = age_calc.table.findItems("John Smith", Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            age_calc.table.item(item.row(), 1).setSelected(True)
>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c

        cursor.close()
        connection.close()


app = QApplication(sys.argv)
# age_calc = AgeCalculator()
<<<<<<< HEAD
main_window = MainWindow()
main_window.show()
main_window.load_data()
=======
age_calc = MainWindow()
age_calc.show()
age_calc.load_data()
>>>>>>> b79e84cf1b0d3d6700d5b9b7c6e900344d67688c
sys.exit(app.exec())
