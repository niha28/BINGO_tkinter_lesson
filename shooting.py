import tkinter

# 入力されたキーを保存する変数key
key = ""

cx = 250
cy = 350
rx = 250
ry = 50
tx = 200
ty = 100
# キーが押された時に実行
def key_down(e):
    global key
    key = e.keysym
# キーが放された時に実行
def key_up(e):
    global key
    key = ""

def main():
    pass()

root = tkinter.Tk()
root.title("シューティング")

canvas = tkinter.Canvas(width=600, height=400, bg="lightblue")
canvas.pack()

fatcat = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/tutrial/images/pet_fat_cat.png")
fatcat = fatcat.subsample(7, 7)
canvas.create_image(cx, cy, image=fatcat, tag="cat")

ramen = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/tutrial/images/food_cup_ramen_syouyu.png")
ramen = ramen.subsample(7, 7)
canvas.create_image(rx, ry, image=ramen, tag="enemy")

tikin = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/tutrial/images/food_salad_chicken.png")
tikin = tikin.subsample(7, 7)
canvas.create_image(tx, ty, image=tikin, tag="item")


root.mainloop()