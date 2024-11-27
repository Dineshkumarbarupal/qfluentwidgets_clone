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

# dict = {"name":"dinesh",
#         "age":19}

# print(dict)
# print(dict["name"])
# print(dict["age"])

# print(dict.keys())
# print(dict.values())

# new = dict["name"] = "vihaan"
# print(new)

# print(dict)

# tup = (2,3,4,5,6,7,7,8,8,9)
# print(tup)
# print(type(tup))

# set = set()
# print(type(set))

# class Main_Window:
#     def __init__(self):
#         print("Hi, How are you brother.")
        
# window = Main_Window()

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(second):
    print(f"Sleeping time {second} seconds.")
    time.sleep(second)
    return second
    
# func(4)
# func(3)
# func(1)

time1 = time.perf_counter()    
t1 = threading.Thread(target= func, args= [4])
t2 = threading.Thread(target= func, args= [3])
t3 = threading.Thread(target= func, args= [1])
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

time2 = time.perf_counter()
print(time2 - time1)

def polling():
   with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(func , 4)
    # future2 = executor.submit(func , 3)
    # future3 = executor.submit(func , 1)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())

    l = [3, 5, 1, 2]
    results = executor.map(func,l)
    for result in results:
      print(result)

polling()











