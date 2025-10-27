import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=500, width=800)

shape1 = myCanvas.create_oval(200, 250, 300, 350, fill="blue")
shape2= myCanvas.create_polygon(10, 10, 30, 50, 100, 200, fill="green", outline="blue")
shape3= myCanvas.create_arc(50, 50, 150, 150, start=0, extent=90, style=tkinter.ARC, outline="black", width=2)


xx=yy=3
def move_shape():
    global xx, yy
    myCanvas.move(shape1, xx, yy)
    (x1, y1, x2, y2)=myCanvas.coords(shape1)

    if x1 <= 0 or x2 >= 800:
        xx = -xx
    if y1 <= 0 or x2 >= 500:
        yy = -yy
    myCanvas.after(30, move_shape())


myCanvas.after(10, move_shape())
myCanvas.pack()
root.mainloop()