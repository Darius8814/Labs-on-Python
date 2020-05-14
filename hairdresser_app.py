from tkinter import *

background_color = "#ffd86e"
label_color = "#cbe882"
root = Tk()

root.minsize(900, 800)
root.title('Приложение для парикмахерской')
root.configure(bg=background_color)

clients = {'Жмышенко': [['07.01.2020', 'Стрижка и укладка', 1000], ['05.03.2020', 'Стрижка бороды', 1500]],
            'Халимов': [['10.04.2020', 'Укладка', 800]]}

# создание записи для нового клиента и добавлениt информации о клиенте
surname = StringVar()
surname_to_delete = StringVar()
surname_to_find = StringVar()
date = StringVar()
date_to_find = StringVar()
service = StringVar()
price = IntVar()
dropdown_key = StringVar(root)


# dropdown_key.set(list(clients.keys())[0])
dropdown_value = StringVar(root)

variables = [('Фамилия', surname), ('Дата', date), ('Услуга', service), ('Цена', price)]
variables2 = [('Поиск по фамилии', surname_to_find), ('Поиск по дате', date_to_find)]
def create_form(*attributes):
    label, var, row_count = attributes
    Label(text=label, bg=label_color).grid(row=row_count, column=0, sticky='w')
    Entry(textvariable=var).grid(row=row_count,column=1, padx=5, pady=5)

def add_client(update=False):
    try:
        key = surname.get()
        value = [x.get() for x in [date, service, price]]
        if update:
            clients[key].append(value)
        else:
            clients[key] = [value]
    except Exception as e:
        print(f'Error - {e}')

def delete_client(value=None):
    key = surname_to_delete.get()
    if value:
        key = dropdown_key.get()
        value = eval(value.replace('(', '[').replace(')', ']'))
        print(value)
        if value in clients[key]:
            clients[key].remove(value)
        else:
            print(f'There is no {value} in Clients')
    else:
        try:
            clients.pop(key)
        except:
            print(f'There is no {key} in the Clients')

def update_dropdown(event):
    OptionMenu(root, dropdown_key, *([y for y in clients])).grid(row=2,column=3, padx=5, pady=5)
    if clients[dropdown_key.get()]:     
        OptionMenu(root, dropdown_value, *([x for x in clients[dropdown_key.get()]])).grid(row=2,column=4, padx=5, pady=5)
    else:
        OptionMenu(root, dropdown_value, ' ').grid(row=2,column=4, padx=5, pady=5)

update_button = Button(text="Обновить записи")
update_button.bind('<ButtonRelease-1>', update_dropdown)
update_button.grid(row=3,column=4, padx=5, pady=5, sticky="e")
Button(text="Удалить запись", command=lambda: delete_client(dropdown_value.get())).grid(row=3,column=3, padx=5, pady=5, sticky="e")


row_count = 0
for label, var in variables:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Добавить клиента", command=add_client).grid(row=6,column=0, padx=5, pady=5, sticky="e")
Button(text="Добавить значение клиенту", command=lambda: add_client(update=True)).grid(row=6,column=1, padx=5, pady=5, sticky="e")

Label(text=variables[0][0], bg=label_color).grid(row=0, column=3, sticky='w')
Entry(textvariable=surname_to_delete).grid(row=0,column=4, padx=5, pady=5)
Button(text="Удалить клиента", command=delete_client).grid(row=1,column=4, padx=5, pady=5, sticky="e")

row_count = 7
for label, var in variables2:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Найти", command=add_client).grid(row=10,column=0, padx=5, pady=5, sticky="e")


root.mainloop()