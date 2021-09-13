# ボタンでテキストの中身を変える

import tkinter

# ボタンを押したら実行される関数
def click_btn():
    # ボタンのテキストを爆発に変える
    button["text"] = "bakuhatu"
    # キャンバスの背景を赤に変える
    canvas["bg"] = "red"

root = tkinter.Tk()
root.title("爆破スイッチ")

canvas = tkinter.Canvas(root, width=800, height=600, bg="skyblue")
canvas.pack()

label = tkinter.Label(root, text="bakudan", font=("DejaVu Sans Mono",60))
label.place(x=200, y=100)

# ボタンの文字，フォント，大きさを設定
# ボタンを押したら実行される関数を設定
button = tkinter.Button(root, text="osunayo", font=("DejaVu Sans Mono",60), command=click_btn)
# ボタンを指定の場所に表示
button.place(x=200, y=300)

root.mainloop()

