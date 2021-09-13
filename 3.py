# テキストを入出力する

import tkinter

# entryのテキストを受け取ってボタンに表示
def click_btn():
    txt = entry.get()
    button["text"] = txt

# textに文字を追加
def click_btn2():
    text.insert(tkinter.END, "You're filled with determination.")

root = tkinter.Tk()
root.title("テキスト入力")
root.geometry("400x600")

# 文字入力を作成
entry = tkinter.Entry(width=20)
entry.pack()

# click_btnが実行
button = tkinter.Button(text="get_text", command=click_btn)
button.pack()

button2 = tkinter.Button(text="inter_text", command=click_btn2)
button2.pack()

# 複数行の文字入力を作成
text = tkinter.Text()
text.pack()

root.mainloop()