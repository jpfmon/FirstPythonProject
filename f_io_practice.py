import os
import shutil

import send2trash

f = open("practice.text","w+")

f.write("First text to a file")

f.close()

print(os.getcwd())
print(os.listdir())
print("**************")
print(os.listdir("D:\\UDEMY\\PythonForBeginners"))

shutil.move('practice.text', "D:\\UDEMY\\PythonForBeginners\\FirstPythonProject\\DestinationFolder\\")

print(os.listdir("D:\\UDEMY\\PythonForBeginners\\FirstPythonProject\\DestinationFolder"))

# send2trash.send2trash("D:\\UDEMY\\PythonForBeginners\\FirstPythonProject\\DestinationFolder\\practice.text")
