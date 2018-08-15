import tkinter

root = tkinter.Tk()

hi_there = tkinter.Label(
root,
text = "Hi, there!",
bg = "gray",
fg = "white"
)

hi_there.pack(fill=tkinter.BOTH, expand=True)

my_name = tkinter.Label(root, text="My name is Yang")
my_name.pack()
root.mainloop()
