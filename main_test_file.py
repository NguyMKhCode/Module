
from datatype import *
import time

Input = input("Type anything here: ")

InputToModule = Convert(Input, customErrorMessage=False, customMessage=False)

Input2 = input("What kind of data-type do you want to convert?: ")
if Input2 == 'int':
    InputToModule.convertToInt()
elif Input2 == 'float':
    InputToModule.convertToFloat()
elif Input2 == 'str':
    InputToModule.convertToStr()
else:
    print("none.")

print("Interger data-base boolean:")
print(isinstance(Input, int))
print("Float data-base boolean:")
print(isinstance(Input, float))
print("String data-base boolean:")
print(isinstance(Input,str))

time.sleep(999999)
time.sleep(999999)
time.sleep(999999)