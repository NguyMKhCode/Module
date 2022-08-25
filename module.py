class Checker:

    def __init__(check, data, customMessage, customMessageError):
        check.data = data
        check.customMessage = customMessage
        check.customMessage2 = customMessageError
        pass
        
    
    
    def CheckInt(check):
        try:
            int(check.data)
            if check.customMessage == None or check.customMessage == False:
                print("True")
            elif check.customMessage:
                print(check.customMessage)
            check.data = True
            return check.data
        except ValueError:
            if check.customMessage2 == None or check.customMessage2 == False:
                print("False")
            if check.customMessage2:
                print(check.customMessage2)
            check.data = False
            return check.data
    
    def CheckStr(check):
        if type(check.data) == str:
            if check.customMessage == None or check.customMessage == False:
                print("True")
            elif check.customMessage:
                print(check.customMessage)
            check.data = True
            return check.data
        else:
            if check.customMessage2 == None or check.customMessage2 == False:
                print("False")
            elif check.customMessage2:
                print(check.customMessage2)
            check.data = False
            return check.data
    
    def CheckFloat(check):
        if type(check.data) == float:
            if check.customMessage == None or check.customMessage == False:
                print("True")
            elif check.customMessage:
                print(check.customMessage)
            check.data = True
            return check.data
        else:
            if check.customMessage2 == None or check.customMessage2 == False:
                print("False")
            elif check.customMessage2:
                print(check.customMessage2)
            check.data = False
            return check.data

class Convert:
    def __init__(converter, data,):
        converter.data = data


    def convertToInt(converter):
        try:
            converter = int(converter.data)
            return converter
        except ValueError:
            converter.CheckStr = isinstance(converter.data,str)
            if converter.CheckStr is True:
                raise ValueError("Cannot convert string (str) to interger (int)")

    def convertToStr(converter):
        try:
            converter = str(converter.data)
            return converter
        except ValueError:
            converter.CheckInt = isinstance(converter.data, int)
            if converter.CheckInt is True:
                raise ValueError("Cannot convert interger (int) to string (str)")
        
    def convertToFloat(converter):
        try:
            converter = float(converter.data)
            return converter
        except ValueError:
            if converter.CheckStr is True:
                raise("Cannot convert string (str) to float")


#Note: If you wish to make customMess or customMessError become False, please do "customMess=None" or "CustomMessError=None"
#Convert module now fixed!