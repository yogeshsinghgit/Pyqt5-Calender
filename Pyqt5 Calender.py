# PyQt5 : Dynamic Coding
# Calender Script ....

# importing libraries
from PyQt5.QtWidgets import QMainWindow,QCalendarWidget,QApplication
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Dynamic Coding")
        # setting geometry
        self.setGeometry(100, 100, 400, 250)
        self.setFixedSize(400,250)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()

        # method for components
    def UiComponents(self):
        # creating a QCalendarWidget object
        self.calendar = QCalendarWidget(self)

        # setting geometry to the calender
        self.calendar.setGeometry(0, 0, 400, 250)
        # setting style sheet // change the color of calender if you want ..
        self.calendar.setStyleSheet("background : cyan;")
        # ensuring paint event
        self.calendar.repaint()

    # create pyqt5 app

App = QApplication(sys.argv)
# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())