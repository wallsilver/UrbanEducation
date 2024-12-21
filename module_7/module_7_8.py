import time
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import os.path

def on_click():
    messagebox.showinfo(select_directory)

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        selected_directory_label.config(text=f"выбран каталог: {directory}")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_dir = f'{directory}\{file}'
                filepath = os.path.join(file)
                filetime = os.path.getmtime(file_dir)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                filesize = os.path.getsize(file_dir)
                parent_dir = os.path.dirname(directory)
                messagebox.showinfo('',
                    f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    else:
        selected_directory_label.config(text="Каталог не выбран")

# Создание окна
window = tk.Tk()
window.title('Проводник')
window.geometry('350x140')
window.resizable(False, False)
window.configure(bg='lightgreen')

# Создание надписи в окне
selected_directory_label = tk.Label(window, text="Каталог не выбран")
selected_directory_label.pack(pady=40)

# Создание кнопки выбора
select_button = tk.Button(window, text="Выберите каталог", command=select_directory)
select_button.pack()

# Run the tkinter main loop
window.mainloop()