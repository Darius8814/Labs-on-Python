from tkinter import *

# смена цвета
background_color = "#ffd86e"
label_color = "#cbe882"
root = Tk()
# размеры окна
root.minsize(700, 400)
root.title('Приложение для парикмахерской')
root.configure(bg=background_color)
# список переменных: фамилия и поиск по фамилии, дата поиска, сервис, цена, клавиша дропа
surname = StringVar()
surname_to_delete = StringVar()
surname_to_find = StringVar()
date = StringVar()
date_to_find = StringVar()
service = StringVar()
price = IntVar()
dropdown_key = StringVar(root)
# !!!.set() отвечает за стандартное
dropdown_key.set('Фамилия')
dropdown_value = StringVar(root)
dropdown_value.set('Услуга')

variables = [('Фамилия', surname), ('Дата', date), ('Услуга', service), ('Цена', price)]
variables2 = [('Поиск по фамилии', surname_to_find), ('Поиск по дате', date_to_find)]

# Создание кнопок Label - Entry
def create_form(*attributes):
    # атрибуты с неограниченным количеством аргументов,
    label, var, row_count = attributes
    Label(text=label, bg=label_color).grid(row=row_count, column=0, sticky='w')
    Entry(textvariable=var).grid(row=row_count,column=1, padx=5, pady=5)

# Цикл, в котором создается первая форма
row_count = 0
for label, var in variables:
    create_form(label, var, row_count)
    row_count += 1

# Кнопки добавления
Button(text="Добавить клиента").grid(row=4,column=0, padx=5, pady=5, sticky="e")
Button(text="Добавить значение клиенту").grid(row=4,column=1, padx=5, pady=5, sticky="e")

# Кнопки удаления
Label(text=variables[0][0], bg=label_color).grid(row=0, column=3, sticky='w')
Entry(textvariable=surname_to_delete).grid(row=0,column=4, padx=5, pady=5)
Button(text="Удалить клиента").grid(row=1,column=4, padx=5, pady=5, sticky="e")

# Цикл, в котором создается вторая форма
row_count = 5
for label, var in variables2:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Найти").grid(row=10,column=0, padx=5, pady=5, sticky="e")
# Выпадающие списки
OptionMenu(root, dropdown_key, '').grid(row=2,column=3, padx=5, pady=5)
OptionMenu(root, dropdown_value, '').grid(row=2,column=4, padx=5, pady=5)
Button(text="Удалить запись").grid(row=3,column=3, padx=5, pady=5, sticky="e")

# Поле вывода клиентов за сутки
Label(text="Клиенты за сутки", bg=label_color).grid(row=4, column=4, sticky='e')
Button(text="Показать").grid(row=5,column=4, padx=5, pady=5, sticky="e")

root.mainloop()