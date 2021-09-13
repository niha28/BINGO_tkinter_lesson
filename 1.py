# tkinterを用いてウィンドウに文字を表示する

import tkinter

# tkinter本体
root = tkinter.Tk()
# GUIのタイトル
root.title("ラベルの表示")

# 表示するウィンドウの横縦幅，背景の色を設定
canvas = tkinter.Canvas(root, width=800, height=600, bg="red")
# ウィンドウを表示
# packは表示するだけ
canvas.pack()

# 表示する文字とフォント，大きさを設定
label = tkinter.Label(root, text="テスト",font=("Noto Sans CJK JP", 60))
# 文字を指定した場所に表示
# placeは場所を指定して表示
label.place(x=400, y=300)

# tkinterを実行
root.mainloop()

