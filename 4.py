# 関数を繰り返し実行する

import tkinter

# 時間をカウントする変数tmrの宣言
tmr = 0

# 繰り返し処理される関数
def count_up():
    # グローバル関数を定義
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    # 1000ms後関数を実行
    root.after(1000, count_up)

root = tkinter.Tk()
root.title("タイマー")

label = tkinter.Label()
label.pack()

# 1000ms後関数を実行
root.after(1000, count_up)

root.mainloop()
