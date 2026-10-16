from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")


upload = image.open("App BG.jfif")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=100, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    hg="light blue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    MsgBox = messagebox.showinfo(
        def topwin():)

top = Toplevel()
top.title("Denominations Calculator")
top.configure(bg="light grey")
top.geometry("600x350+50+50")
label = Label(top, text="Enter total amount", bg="light grey")
entry = Entry(top)
