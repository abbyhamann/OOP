import tkinter as tk
top = tk()
top.geometry("500x500")
class Queue:
    def __init__(self):
        self.element = []
    def enqueue(self):
        textBox = tk.Text(top, width=35, height=2)
        x = textBox.get(1.0, "end-1c")
        self.element.append(x)
    def dequeue(self):
        self.element.remove(self.element[0])
    def display(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)

var = "q"
i=1
def show(n):
    if n == "Create Queue":
        var = "q" + i
        var = Queue()
        i += 1
    elif n =="Enqueue":
        q = input("Enter queue name:")
        var.enqueue()
    elif n == "Dequeue":
        q = input("Enter queue name:")
        q.dequeue()
    elif n == "Display":
        q = input("Enter queue name:")
        q.display()



B1 = tk.Button(top, text="Create Queue", width=10, height=4, command=lambda: show("Create Queue"))
B1.place(x=100, y=150)

B2 = tk.Button(top, text="Enqueue", width=10, height=4, command=lambda: show("Enqueue"))
B2.place(x=200, y=150)

B3 = tk.Button(top, text="Dequeue", width=10, height=4, command=lambda: show("Dequeue"))
B3.place(x=300, y=150)

B4 = tk.Button(top, text="Display", width=10, height=4, command=lambda: show("Display"))
B4.place(x=100, y=200)


