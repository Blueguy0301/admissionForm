from PyQt6.QtGui import QIcon
from validation import validate
from textFieldNames import startUI,form1,form2
from PyQt6.QtWidgets import  QMainWindow,  QStackedWidget, QPushButton,QLineEdit,QFrame,QTextEdit,QCheckBox,QComboBox,QWidget
from PyQt6 import uic
resetObject = "reset"
nextObject = "next"
backObject = "back"
nextEnd = "nextEnd"
formFrame ="formFrame"
uiData = [startUI,form1,form2]
uiObjects = []
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Medical Records')
        self.setWindowIcon(QIcon("Screens/assets/lyceumLogo.png"))
        self.setGeometry(0, 00, 1024, 768)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget) 
        # List of UI file paths
        files = ['./Screens/mainWindow.ui', './Screens/form.ui', './Screens/form2.ui']
      
        for filePath in files:
            ui = uic.loadUi(filePath)
            uiObjects.append(ui)
            self.stacked_widget.addWidget(ui)
        for index, ui in enumerate(uiObjects):
            nextButton = ui.findChild(QPushButton, nextObject)
            if nextButton : nextButton.clicked.connect(self.next)
            reset_button = ui.findChild(QPushButton, resetObject)
            reset_button.clicked.connect(lambda checked, ui=ui: self.resetForm(ui))
            backButton = ui.findChild(QPushButton, backObject)
            backButton.clicked.connect(self.back)
            if index == len(uiObjects)-1:  
                nextButton = ui.findChild(QPushButton, nextEnd)
                nextButton.clicked.connect(self.retrieveAllData)
    def resetForm(self, ui):
        frame = ui.findChild(QFrame, formFrame)
        if frame is not None:
            # Iterate over the child widgets of the frame
            for widget in frame.findChildren(QLineEdit) + frame.findChildren(QTextEdit) + frame.findChildren(QCheckBox):
                if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                    # Clear the text of QLineEdit and QTextEdit widgets
                    widget.clear()
                if isinstance(widget, QCheckBox):
                    # Uncheck the checkboxes
                    widget.setChecked(False)
    def next(self):
        # Change the current index of the QStackedWidget
        current_index = self.stacked_widget.currentIndex()
        new_index = (current_index + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(new_index)
    def back(self):
        # Change the current index of the QStackedWidget
        current_index = self.stacked_widget.currentIndex()
        new_index = (current_index - 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(new_index)
    def retrieveAllData(self):
        all_data = {}
        indexes = [0,0]
        for index,ui in enumerate(uiObjects):
            indexes[0] = index
            for widget_name in uiData[index]:
                indexes[1] = index
                widget = ui.findChild(QWidget, widget_name)
                if widget:
                    if isinstance(widget, QCheckBox):
                        all_data[widget_name] = widget.isChecked()
                    elif isinstance(widget, QComboBox):
                        all_data[widget_name] = widget.currentText()
                    elif isinstance(widget, QLineEdit):
                        all_data[widget_name] = widget.text()
                else : print(f"{widget_name} NOT found")

        validate(all_data)
        # print(all_data)