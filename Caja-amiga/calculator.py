# imports -------------------------------
from guizero import App, Text, PushButton

# initialise variables ------------------
displayString = ''
a = False
b = False
result = 0
operator = ''
operatorFlag = False

# app -----------------------------------
app = App(title='MyCalc', layout='grid')
app.bg = '#000000'

# functions -----------------------------
def inputNumber(key):
    global displayString, operatorFlag
    if operatorFlag:
        displayString=''
        operatorFlag = False
    displayString = displayString + key
    display.value = displayString

def operatorKey(key):
    global a, operator, operatorFlag, displayString
    operator = key
    operatorFlag = True
    if not a:
        a = float(displayString)

def evaluate():
    global a, b, result, operator, displayString
    if not a and not b:
        return
    elif a and not b:
        b = float(displayString)    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a / b
    elif operator == 'x':
        result = a * b
    # stop decimal places appearing for whole numbers
    if result - int(result) == 0:
        result = int(result)
    displayString = str(result)
    display.value = displayString
    a = result
    
def allClear():
    global a, b, operator, result, displayString
    a = 0
    b = 0
    operator = ''
    result = 0
    displayString = ''
    display.value = '0'

def backspace():
    global displayString
    if len(displayString) > 1:
        displayString = displayString[:-1]
        display.value = displayString
    else:
        displayString = ''
        display.value = '0'
    
# layout & buttons ----------------------
display = Text(app, text='0', color='#FFFFFF', grid=[1,0,15,1])
display.text_size = 37

btn7 = PushButton(app, command=inputNumber, args=['7'], text='7', grid=[0,1])
btn8 = PushButton(app, command=inputNumber, args=['8'], text='8', grid=[1,1])
btn9 = PushButton(app, command=inputNumber, args=['9'], text='9', grid=[2,1])
btn4 = PushButton(app, command=inputNumber, args=['4'], text='4', grid=[0,2])
btn5 = PushButton(app, command=inputNumber, args=['5'], text='5', grid=[1,2])
btn6 = PushButton(app, command=inputNumber, args=['6'], text='6', grid=[2,2])
btn1 = PushButton(app, command=inputNumber, args=['1'], text='1', grid=[0,3])
btn2 = PushButton(app, command=inputNumber, args=['2'], text='2', grid=[1,3])
btn3 = PushButton(app, command=inputNumber, args=['3'], text='3', grid=[2,3])
btn0 = PushButton(app, command=inputNumber, args=['0'], text='0', grid=[1,4])
btnDec = PushButton(app, command=inputNumber, args=['.'], text=' .', grid=[2,4])

btnDiv = PushButton(app, command=operatorKey, args=['/'], text='÷', grid=[3,1])
btnMult = PushButton(app, command=operatorKey, args=['x'], text='x', grid=[3,2])
btnSub = PushButton(app, command=operatorKey, args=['-'], text='-', grid=[3,3])
btnAdd = PushButton(app, command=operatorKey, args=['+'], text='+', grid=[3,4])

btnEquals = PushButton(app, command=evaluate, text='=', grid=[4,4])
btnAC = PushButton(app, command=allClear, text='AC', grid=[4,1])
btnCE = PushButton(app, command=backspace, text='←', grid=[4,2])


# display app loop ------------------------------
app.display()