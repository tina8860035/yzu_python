import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label = tkinter .Label(win, text='HI')
label.pack(side=tkinter.LEFT)
label2 = tkinter .Label(win, text='Hallo')
label2.pack(side=tkinter.RIGHT)

win.geometry('360x480')

win.mainloop()