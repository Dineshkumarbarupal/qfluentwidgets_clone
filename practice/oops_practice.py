import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget,QFrame,QApplication
from qfluentwidgets import SubtitleLabel,setFont


# class Student:
#     name = "vihaan"        # class attributes
#     age = 19
#     def __init__(self, name, age=19):
#         self.name = name    # object attributes
#         self.age = age
#         print("hello how are you brother, this is a cundtructor.")

# stu1 = Student("dinesh")
# print(stu1.name)
# print(stu1.age)

class MainWindow(QFrame):
    def __init__(self,text:str, parent = None):
        super().__init__(parent = parent)

        self.lable = SubtitleLabel(text,self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.lable,20)
        self.lable.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.lable, 1,Qt.AlignCenter)

        self.setObjectName(text.replace( ' ' , '-'))

        

if __name__== '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show() 
    app.exec()