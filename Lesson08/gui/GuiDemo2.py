import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label = tkinter .Label(win, text='HI', fg='yellow',  bg='red', font=('Arial', 12))
label2 = tkinter .Label(win, text='Hallo')
label3 = tkinter .Label(win, text='123')
label4 = tkinter .Label(win, text='456')
label5 = tkinter .Label(win, text='789')
button6 = tkinter .Button(win, text='ooo')
button7 = tkinter .Button(win, text='ppp')
label.grid(column=0, row=0, padx=20, pady=20)
label2.grid(column=1, row=1)
label3.grid(column=2, row=2)
label4.grid(column=3, row=3)
label5.grid(column=4, row=4)
button6.grid(column=5, row=5)
button7.grid(column=6, row=6)

win.geometry('360x480')

win.mainloop()