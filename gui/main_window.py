import sys
from PyQt5.QtWidgets import QFrame,QHBoxLayout,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from qfluentwidgets import NavigationItemPosition, Fluentwindow, SubtitleLabel, setFont
from qfluentwidgets import FluentIcon as FIF
from widgets.basic_input.button.button import ToolButtonDemo

class Widget(QFrame):

    def __init__(self, text: str= "Default text", parent=None):
        super().__init__(parent=parent)
        # self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        # setFont(self.label, 24)
        # self.label.setAlignment(Qt.AlignCenter)
        # self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)

        # Must set a globally unique object name for the sub-interface
        self.setObjectName( "Default text")
        
class Window(Fluentwindow):
    """ Main Interface """

    def __init__(self):
        super().__init__()

        self.buttons = ToolButtonDemo()

        # Create sub-interfaces, when actually using, replace Widget with your own sub-interface
        self.homeInterface = Widget(self)
        self.musicInterface = Widget(self)
        self.videoInterface = Widget(self)
        self.settingInterface = Widget(self)
        self.albumInterface = Widget(self)
        self.albumInterface1 = Widget(self)

        self.homeInterface.hBoxLayout.addWidget(self.buttons,Qt.AlignCenter)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music library')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, 'Video library')

        self.navigationInterface.addSeparator()

        self.addSubInterface(self.albumInterface, FIF.ALBUM, 'Albums', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.albumInterface1, FIF.ALBUM, 'Album 1', parent=self.albumInterface)

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

    def initWindow(self):
        self.resize(900, 700)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()







