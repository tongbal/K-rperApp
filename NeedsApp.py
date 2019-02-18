from tkinter import *

root = Tk()
root.title("Körper Log App")
root.minsize(width=300, height=300)
root.maxsize(width=400, height=350)


theLabel = Label(root, text="Hunger")
theLabel.pack()
theLabel.place(x=10, y=0)
w = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w.pack()
w.place(x=10, y=20)

theLabel2 = Label(root, text="Komfort")
theLabel2.pack()
theLabel2.place(x=10, y=70)
w2 = Scale(root, from_=00, to=100, orient=HORIZONTAL)
w2.pack()
w2.place(x=10, y=90)

theLabel3 = Label(root, text="Bladder")
theLabel3.pack()
theLabel3.place(x=10, y=140)
w3 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w3.pack()
w3.place(x=10, y=160)

theLabel4 = Label(root, text="Energy")
theLabel4.pack()
theLabel4.place(x=10, y=210)
w4 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w4.pack()
w4.place(x=10, y=230)

theLabel5 = Label(root, text="Fun")
theLabel5.pack()
theLabel5.place(x=150, y=0)
w5 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w5.pack()
w5.place(x=150, y=20)

theLabel6 = Label(root, text="Social")
theLabel6.pack()
theLabel6.place(x=150, y=70)
w6 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w6.pack()
w6.place(x=150, y=90)

theLabel7 = Label(root, text="Hygiene")
theLabel7.pack()
theLabel7.place(x=150, y=140)
w7 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w7.pack()
w7.place(x=150, y=160)

theLabel8 = Label(root, text="Environment")
theLabel8.pack()
theLabel8.place(x=150, y=210)
w8 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
w8.pack()
w8.place(x=150, y=230)


root.mainloop()
