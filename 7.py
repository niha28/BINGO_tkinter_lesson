# 画像を表示する

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

# "ずっと"実行される関数
def main():
    if key == "space":
        # 画像を表示する
        # (x座標, y座標, image=表示する画像, tag="タグ")
        canvas.create_image(200, 300, image=img, tag="neko")
    else:
        canvas.delete("neko")
    root.after(100, main)

root = tkinter.Tk()
root.title("キャラクター表示")

# キーが押されたとき，放されたときの実行する関数を指定
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

canvas = tkinter.Canvas(width=400, height=600, bg="lightblue")
canvas.pack()

# 表示する画像を読み込む
img = tkinter.PhotoImage(file="/mnt/c/Users/niha2/Documents/projects/pygame/py_samples/Chapter8/mimi.png")

main()
root.mainloop()

