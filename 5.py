# キー入力を受け付ける

import tkinter

key = 0

# 押されたキーをprintする
def key_down(e):
    global key
    # 変数keyに押されたキーコードを代入
    key = e.keycode
    print("KEY:"+str(key))

root = tkinter.Tk()

root.title("キーボード入力")

# キーが押されたときにkey_downを実行
# bind("イベント", イベント発生時に実行する関数名)
root.bind("<KeyPress>", key_down)

root.mainloop()