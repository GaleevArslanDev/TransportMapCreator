from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import webbrowser

data = ""

root = Tk()
root.title("Создатель маршрутов внутригородского общественного транспорта")
root.geometry("850x600")
root.resizable(False, False)

def about_click():
    messagebox.showinfo("О программе", "Программа TransportMapCreator создана в 2024 году в г.Казани для расчета транспортных маршрутов города")

def help_click():
    webbrowser.open('https://vk.com', new=2)

def create_click():
    filepath = filedialog.asksaveasfilename(defaultextension="tm", initialfile="new.tm", filetypes=[("Transport Map files", "*.tm")], confirmoverwrite=True)
    if filepath != "":
        text = "12345"
        with open(filepath, "w") as file:
            file.write(text)

def save_click():
    filepath = filedialog.asksaveasfilename(defaultextension="tm", initialfile="new.tm", filetypes=[("Transport Map files", "*.tm")], confirmoverwrite=True)
    if filepath != "":
        with open(filepath, "w") as file:
            global data
            file.write(data)

def open_click():
    filepath = filedialog.askopenfilename(defaultextension="tm", filetypes=[("Transport Map files", "*.tm")])
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            global data
            data = text
            # text_editor.delete("1.0", END)
            # text_editor.insert("1.0", text)

main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Создать", command=create_click)
file_menu.add_command(label="Сохранить", command=save_click())
file_menu.add_command(label="Открыть", command=open_click)
file_menu.add_separator()
file_menu.add_command(label="Выход")

area_menu = Menu(tearoff=0)
area_menu.add_cascade(label="Жилой")
area_menu.add_cascade(label="Рабочий")

tools_menu = Menu(tearoff=0)
tools_menu.add_cascade(label="Район", menu=area_menu)
tools_menu.add_cascade(label="Остановка")
tools_menu.add_cascade(label="Маршрут")

help_menu = Menu(tearoff=0)
help_menu.add_cascade(label="О программе", command=about_click)
help_menu.add_cascade(label="Помощь", command=help_click)

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Инструменты", menu=tools_menu)
main_menu.add_cascade(label="Справка", menu=help_menu)

root.config(menu=main_menu)
root.mainloop()
