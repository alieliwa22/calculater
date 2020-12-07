import tkinter as tk
root = tk.Tk()
root.title("Calculater")
expretion = ""

# Functions


def add(value):
    global expretion
    expretion += value
    results.config(text=expretion)


def clear():
    global expretion
    expretion = ""
    results.config(text="")


def calculate():
    global expretion
    result = ""
    if expretion != "":
        try:
            result = eval(expretion)
            expretion = str(result)
        except:
            result = "Error"
            expretion = ""
    results.config(text=result)


# GUI
results = tk.Label(root, text="")
results.grid(row=0, column=0, columnspan=4)
# buttons
b1 = tk.Button(root, text="1", width=3, command=lambda: add("1"))
b1.grid(row=1, column=0)

b2 = tk.Button(root, text="2", width=3, command=lambda: add("2"))
b2.grid(row=1, column=1)

b3 = tk.Button(root, text="3", width=3, command=lambda: add("3"))
b3.grid(row=1, column=2)

div = tk.Button(root, text="/", width=3, command=lambda: add("/"))
div.grid(row=1, column=3)

b4 = tk.Button(root, text="4", width=3, command=lambda: add("4"))
b4.grid(row=2, column=0)

b5 = tk.Button(root, text="5", width=3, command=lambda: add("5"))
b5.grid(row=2, column=1)

b6 = tk.Button(root, text="6", width=3, command=lambda: add("6"))
b6.grid(row=2, column=2)

mul = tk.Button(root, text="*", width=3, command=lambda: add("*"))
mul.grid(row=2, column=3)

b7 = tk.Button(root, text="7", width=3, command=lambda: add("7"))
b7.grid(row=3, column=0)

b8 = tk.Button(root, text="8", width=3, command=lambda: add("8"))
b8.grid(row=3, column=1)

b9 = tk.Button(root, text="9", width=3, command=lambda: add("9"))
b9.grid(row=3, column=2)

plus = tk.Button(root, text="+", width=3, command=lambda: add("+"))
plus.grid(row=3, column=3)

bc = tk.Button(root, text="C", width=3, command=lambda: clear())
bc.grid(row=4, column=0)

b0 = tk.Button(root, text="0", width=3, command=lambda: add("0"))
b0.grid(row=4, column=1)

bdot = tk.Button(root, text=".", width=3, command=lambda: add("."))
bdot.grid(row=4, column=2)

sub = tk.Button(root, text="-", width=3, command=lambda: add("-"))
sub.grid(row=4, column=3)

equl = tk.Button(root, text="=", width=16, command=lambda: calculate())
equl.grid(row=5, column=0, columnspan=4)


root.mainloop()
