from tkinter import *

root = Tk()
root.resizable(False, False)
root.config(bg='grey')
style = 'consolas 18'

ishora = ''
raqam0 = ''  # 12


def cal(num):
    num1 = entry.get()
    entry.delete(0, END)
    entry.insert(0, num1 + num)


def equal():
    raqam = entry.get()
    entry.delete(0, END)
    if ishora == 'plus':
        entry.insert(0, str(int(raqam0) + int(raqam)))
    elif ishora == 'minus':
        entry.insert(0, str(int(raqam0) - int(raqam)))


def equal_1():
    raqam_1 = entry.get()
    entry.delete(0, END)
    if ishora == 'kopaytiruv':
        entry.insert(0, str(int(raqam0) * int(raqam_1)))
    elif ishora == 'boluv':
        entry.insert(0, str(int(raqam0) / int(raqam_1)))


def plus():
    global ishora, raqam0
    ishora = "plus"
    raqam0 = entry.get()
    entry.delete(0, END)


def minus():
    global ishora, raqam0
    ishora = "minus"
    raqam0 = entry.get()
    entry.delete(0, END)


def kopaytiruv():
    global ishora, raqam0
    ishora = "kopaytiruv"
    raqam0 = entry.get()
    entry.delete(0, END)


def boluv():
    global ishora, raqam0
    ishora = "boluv"
    raqam0 = entry.get()
    entry.delete(0, END)


entry = Entry(root, font='consolas 20', width=18)
btnC = Button(root, text="C", font=style, width=4, command=lambda: entry.delete(0, END))
btnP = Button(root, text="<", font=style, width=4, command=lambda: entry.delete(len(entry.get()) - 1, END))
btn_bol = Button(root, text='/', font=style, width=4, command=boluv)
btn_kop = Button(root, text='*', font=style, width=4, command=kopaytiruv)
btn_puls = Button(root, text='+', font=style, width=4, height=3, command=plus)
btn_mins = Button(root, text='-', font=style, width=4, command=minus)
btn_equal = Button(root, text='=', font=style, width=10, command=equal)

btn1 = Button(root, text='1', font=style, width=4, command=lambda: cal("1"))
btn2 = Button(root, text='2', font=style, width=4, command=lambda: cal("2"))
btn3 = Button(root, text='3', font=style, width=4, command=lambda: cal("3"))
btn4 = Button(root, text='4', font=style, width=4, command=lambda: cal("4"))
btn5 = Button(root, text='5', font=style, width=4, command=lambda: cal("5"))
btn6 = Button(root, text='6', font=style, width=4, command=lambda: cal("6"))
btn7 = Button(root, text='7', font=style, width=4, command=lambda: cal("7"))
btn8 = Button(root, text='8', font=style, width=4, command=lambda: cal("8"))
btn9 = Button(root, text='9', font=style, width=4, command=lambda: cal("9"))
btn0 = Button(root, text='0', font=style, width=4, command=lambda: cal("0"))
btn00 = Button(root, text='00', font=style, width=4, command=lambda: cal("00"))

# entry
entry.grid(row=0, column=0, columnspan=4, padx=2, pady=4)
# c, p, /, *
btnC.grid(row=1, column=0, padx=2, pady=2)
btnP.grid(row=1, column=1, padx=2, pady=2)
btn_bol.grid(row=1, column=2, padx=2, pady=2)
btn_kop.grid(row=1, column=3, padx=2, pady=2)
# 7, 8, 9, -
btn7.grid(row=2, column=0, padx=2, pady=2)
btn8.grid(row=2, column=1, padx=2, pady=2)
btn9.grid(row=2, column=2, padx=2, pady=2)
btn_mins.grid(row=2, column=3, padx=2, pady=2)
# 4, 5, 6, +
btn4.grid(row=3, column=0, padx=2, pady=2)
btn5.grid(row=3, column=1, padx=2, pady=2)
btn6.grid(row=3, column=2, padx=2, pady=2)
btn_puls.grid(row=3, column=3, rowspan=2, padx=2, pady=2)
# 1, 2, 3
btn1.grid(row=4, column=0, padx=2, pady=2)
btn2.grid(row=4, column=1, padx=2, pady=2)
btn3.grid(row=4, column=2, padx=2, pady=2)
# 0, 00, =
btn0.grid(row=5, column=0, padx=2, pady=2)
btn00.grid(row=5, column=1, padx=2, pady=2)
btn_equal.grid(row=5, column=2, columnspan=2, padx=2, pady=2)

root.bind("<BackSpace>", lambda e: entry.delete(len(entry.get()) - 1, END))
root.bind('<space>', lambda event: cal(' 00'))
root.bind('<Escape>', lambda event: quit())

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


class setKey:
    def __init__(self):
        self.number = None

    def init(self, number: str):
        self.number = number
        root.bind(number, lambda e: cal(number))


for i in numbers:
    setKey()

root.mainloop()
