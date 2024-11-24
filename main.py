import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import Window  # Import your FluentWindow class
from gui.splash_screen import Splashscreen


if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = Splashscreen()
    splash.show()
    window = Window()  # Instantiate your main window
    window.show()

    splash.finish()
    sys.exit(app.exec_())  # Start the event loop
