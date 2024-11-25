import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer,QEventLoop
from gui.main_window import Window  # Import your FluentWindow class
from gui.splash_screen import Splashscreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()  # Instantiate your main window
    splash = Splashscreen(window)
    splash.show()
     
    QTimer.singleShot(3000, lambda:(
        splash.splashScreen.finish(),
        window.show()
    ))

    sys.exit(app.exec_())  # Start the event loop




