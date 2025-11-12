import tkinter as tk

top = tk.Tk()
top.geometry("500x500")
text_Box = tk.Text(top, width=35, height=2)
text_Box.place(x=50, y=50)

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
class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append((text_Box.get(1.0, "end-1c")))

    def pop(self):
        self.element.pop()

    def display(self):
        print("Elements in Stack:")
        for i in self.element:
            print(i)


s = None
q= None
i = 1
x=1
stacks = {}
queues = {}


def show(n):
    global q
    global s
    global i
    global x
    if n == "Create Stack":
        name = "s" + str(i)
        stacks[name] = Stack()
        s = stacks[name]
        print("Created new stack:", name)
        i += 1
    elif n == "Push":
        if s:
            s.push()
            text_Box
            print("Element pushed")
        else:
            print("First, make a stack")
    elif n == "Pop":
        if s:
            s.pop()
            print("Element popped")
        else:
            print("First, make a stack")
    elif n == "Display":
        if s:
            s.display()
        else:
            print("First, make a stack")

    elif n == "Create Queue":
        name = "q" + str(x)
        queues[name] = Queue()
        q = queues[name]
        print("Created new queue:", name)
        x += 1
    elif n == "Enqueue":
        if q:
            q.enqueue()
            print("Element added to end of queue")
        else:
            print("First, make a queue")
    elif n == "Dequeue":
        if q:
            q.dequeue()
            print("Element removed from front of queue")
        else:
            print("First, make a queue")
    elif n == "Display":
        if q:
            q.display()
        else:
            print("First, make a queue")



B1 = tk.Button(top, text="Create Stack", width=10, height=4, command=lambda: show("Create Stack"))
B1.place(x=50, y=100)

B2 = tk.Button(top, text="Push", width=10, height=4, command=lambda: show("Push"))
B2.place(x=150, y=100)

B3 = tk.Button(top, text="Pop", width=10, height=4, command=lambda: show("Pop"))
B3.place(x=250, y=100)

B4 = tk.Button(top, text="Display", width=10, height=4, command=lambda: show("Display"))
B4.place(x=350, y=100)

B5 = tk.Button(top, text="Create Queue", width=10, height=4, command=lambda: show("Create Queue"))
B5.place(x=50, y=200)

B6 = tk.Button(top, text="Enqueue", width=10, height=4, command=lambda: show("Enqueue"))
B6.place(x=150, y=200)

B7 = tk.Button(top, text="Dequeue", width=10, height=4, command=lambda: show("Dequeue"))
B7.place(x=250, y=200)

B8 = tk.Button(top, text="Display", width=10, height=4, command=lambda: show("Display"))
B8.place(x=350, y=200)

top.mainloop()
