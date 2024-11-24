# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QHBoxLayout, QWidget,QFrame,QApplication
# from qfluentwidgets import SubtitleLabel,setFont

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

# class MainWindow(QFrame):
#     def __init__(self,text:str, parent = None):
#         super().__init__(parent = parent)

#         self.lable = SubtitleLabel(text,self)
#         self.hBoxLayout = QHBoxLayout(self)

#         setFont(self.lable,20)
#         self.lable.setAlignment(Qt.AlignCenter)
#         self.hBoxLayout.addWidget(self.lable, 1,Qt.AlignCenter)

#         self.setObjectName(text.replace( ' ' , '-'))

# if __name__== '__main__':
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     w.show() 
#     app.exec()

dict = {"name":"dinesh",
        "age":19}

print(dict)
print(dict["name"])
print(dict["age"])

print(dict.keys())
print(dict.values())

new = dict["name"] = "vihaan"
print(new)

print(dict)


tup = (2,3,4,5,6,7,7,8,8,9)
print(tup)
print(type(tup))

set = set()
print(type(set))
















