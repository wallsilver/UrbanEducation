from tkinter import filedialog
import tkinter
import os

def file_select():
    filename = filedialog.askopenfilename(initialdir='.', title='Выберете файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x140')
window.resizable(False, False)
window.configure(bg='lightgreen')
text = tkinter.Label(window, text='Файл:', height=5, width=50, background='silver')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=30, height=3, text='Выбрать файл',  background='silver',
                               command=file_select)
button_select.grid(column=1, row=2)
window.mainloop()
