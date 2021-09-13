# キーボードでキャラクターを動かす

import tkinter

# 入力されたキーを保存する変数key
key = ""
# キーが押された時に実行
def key_down(e):
    global key
    key = e.keysym
# キーが放された時に実行
def key_up(e):
    global key
    key = ""

# キャラクターの初期位置
cx = 400
cy = 300

# キーの押されたボタンによって画像の座標を変更
def main():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Right":
        cx = cx + 20
    if key == "Left":
        cx = cx - 20
    # cx,cyに画像を移動
    canvas.coords("neko", cx, cy)
    root.after(100, main)

root = tkinter.Tk()

root.title("キャラクター移動")

root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tkinter.Canvas(width=800, height=600, bg="lightgreen")
canvas.pack()

# 画像を読み込み
img = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/py_samples/Chapter8/mimi.png")
# 画像を表示
canvas.create_image(cx, cy, image=img, tag="neko")

main()
root.mainloop()