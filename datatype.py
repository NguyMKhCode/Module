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
    def __init__(converter, data, customMessage, customErrorMessage):
        converter.data = data
        converter.customMess = customMessage
        converter.customMessError = customErrorMessage

    def convertToInt(converter):
        try:
            int(converter.data)
            if converter.customMess == None or converter.customMess == False:
                print("Done convert")
            elif converter.customMess:
                print(converter.customMess)
            converter.data = int
            return converter.data
        except ValueError:
            if converter.customMessError == None or converter.customMessError == False:
                print("Cannot convert")
            elif converter.customMessError:
                print(converter.customMessError)

    def convertToStr(converter):
        try:
            str(converter.data)
            if converter.customMess == None or converter.customMess == False:
                print("Done convert")
            elif converter.customMess:
                print(converter.customMess)
            converter.data = str
            return converter.data
        except ValueError:
            if converter.customMessError == None or converter.customMessError == False:
                print("Cannot convert")
            elif converter.customMessError:
                print(converter.customMessError)
        
    def convertToFloat(converter):
        try:
            float(converter.data)
            if converter.customMess == None or converter.customMess == False:
                print("Done convert")
            elif converter.customMess:
                print(converter.customMess)
            converter.data = float
            return converter.data
        except ValueError:
            if converter.customMessError == None or converter.customMessError == False:
                print("Cannot convert")
            elif converter.customMessError:
                print(converter.customMessError)


#Note: If you wish to make customMess or customMessError become False, please do "customMess=None" or "CustomMessError=None"
#Also note: Convert module is broken. Don't trust any thing it said. 