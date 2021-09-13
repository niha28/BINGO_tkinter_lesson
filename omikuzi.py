import random
import tkinter
from PIL import Image, ImageTk

def omikuzi():
    l = ["大吉", "中吉", "末吉", "小吉"]
    label["text"]=random.choice(l)
    label.update()

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)

canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

img = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/tutrial/images/pet_fat_cat.png")
img = img.subsample(7, 7)
canvas.create_image(200, 300, image=img)

label = tkinter.Label(root, text="??", font=("DejaVu Sans Mono", 120))
label.place(x=380, y=60)

button = tkinter.Button(root, text="おみくじを引く", font=("DejaVu Sans Mono", 36), command=omikuzi, fg="skyblue")
button.place(x=360, y=400)

root.mainloop()