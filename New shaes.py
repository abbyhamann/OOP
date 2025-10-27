import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=500, width=800)
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