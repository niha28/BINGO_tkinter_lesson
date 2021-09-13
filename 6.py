# リアルタイム処理とキー入力を同時に行う

import tkinter
from typing import KeysView

# 押されたキーを保存するための変数key
key = 0

# キーが押されたときに実行
# 押されたキーを変数keyに保存
def key_down(e):
    global key
    key = e.keysym

# "ずっと"実行される
# ラベルをkeyに変更
def main():
    label["text"] = key
    root.after(100, main)

root = tkinter.Tk()
root.title("リアルタイムキー入力")

root.bind("<KeyPress>", key_down)

label = tkinter.Label()
label.pack()

main()
root.mainloop()