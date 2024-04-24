from tkinter import *
import qrcode

root = Tk()
root.title("QR Code Generator")
root.geometry("1000x550")
root.config(bg="black")
root.resizable(False, False)

#icon image
image_icon=PhotoImage(file="aryan.png")
root.iconphoto(False,image_icon)


def generate():
    name = title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qr codes/"+ str(name)+".png")

    global Image
    Image=PhotoImage(file="Qr codes/"+ str(name)+".png")
    image_view.config(image=Image)

image_view=Label(root,bg="black")
image_view.pack(padx=50,pady=10,side=RIGHT)


Label(root, text="Title", fg="white", bg="black", font=15).place(x=50, y=170)
title = Entry(root, width=15, font="Arial 15")
title.place(x=50, y=200)

entry = Entry(root, font="arial 15", width=28)
entry.place(x=50, y=250)
Button(root, text="Generate Code", width=20, height=2, bg="black",
       fg="white", command=generate).place(x=50, y=300)

root.mainloop()
