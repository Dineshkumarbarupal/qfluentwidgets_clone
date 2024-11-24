# coding:utf-8
import sys
from PyQt5.QtCore import Qt, QEventLoop, QTimer, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import SplashScreen
from qframelesswindow import FramelessWindow
class Splashscreen(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle('PyQt-Fluent-Widgets')
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))

        # Create splash screen and show window
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(102, 102))
        self.splashScreen.show()

        # Simulate loading delay
        self.createSubInterface()

        # Close splash screen
        # Pass the main window object (e.g., window) to the finish method
        self.splashScreen.finish(self)  # Here, pass `self` which refers to the Splashscreen, not the main window

    def createSubInterface(self):
        loop = QEventLoop(self)
        QTimer.singleShot(3000, loop.quit)  # Simulate 3 seconds of loading
        loop.exec()
