from tkinter import *
from math import floor


# смена цвета
background_color = "#ffd86e"
label_color = "#cbe882"
root = Tk()

root.minsize(500, 400)
root.title('Расчет зарплат')
root.configure(bg=background_color)
# просмотр списка работающих и просмотр их заработной платы, get_salaries
# список всех с их премиями и налогами, get_payable_salaries
# премии и налоги одного человека по фамилии, get_salaries_by_surname !lambda!
# добавить нового человека по фамилии и рассчитать всё для него. add_person
salaries = {
    'Фамилия1': 13000,
    'Фамилия2': 23000,
    'Фамилия3': 100000,
    'Фамилия4': 15000,
    'Фамилия5': 17000
}

calculate_percentage = lambda num, percent: floor((num/100) * percent)

def get_salaries(tax=False):
    listbox = Listbox(width=25,height=10, selectmode=EXTENDED)
    listbox.grid(row=5,column=0, padx=5, pady=5)
    if tax:
        [listbox.insert(0, f'{x} {get_payable_salaries(salaries[x])}') for x in salaries.keys()]
    else:
        [listbox.insert(0, f'{x} {salaries[x]}') for x in salaries.keys()]

def get_payable_salaries(salary, award_percent=10):
    MINIMUM_WAGE = 12_130
    if salary > MINIMUM_WAGE:
        PENSION_TAX = calculate_percentage(salary, 6)
        tax = calculate_percentage((salary - MINIMUM_WAGE - PENSION_TAX), 13) + calculate_percentage(salary, 1)
        award = calculate_percentage(salary, award_percent)
        return salary - tax + award
    else:
        print('Error - salary < MINIMUM_WAGE')

def add_person():
    if entry_salary.get() > 12_130:
        salaries[entry_surname.get()] = entry_salary.get()
        return get_salaries(tax=True)

get_salaries_by_surname = lambda : salary_by_surname.config(text=(get_payable_salaries(salaries[surname.get()])))

surname = StringVar()
surname.set(list(salaries.keys())[0])
entry_surname = StringVar()
entry_salary = IntVar()

OptionMenu(root, surname, *([x for x in salaries])).grid(row=0,column=0, sticky="w")
salary_by_surname = Label(text="", bg=label_color)
salary_by_surname.grid(row=0, column=1, sticky="w")

Button(text="Показать зарплату по фамилии", command=get_salaries_by_surname).grid(row=2,column=0)

Label(text='Фамилия', bg=label_color).grid(row=0, column=3, sticky='w')
Entry(textvariable=entry_surname).grid(row=0,column=4, padx=5, pady=5)
Label(text='Зарплата', bg=label_color).grid(row=1, column=3, sticky='w')
Entry(textvariable=entry_salary).grid(row=1,column=4, padx=5, pady=5)
Button(text="Добавить", command=add_person).grid(row=2,column=3)

listbox = Listbox(width=25,height=10, selectmode=EXTENDED)
listbox.grid(row=5,column=0, padx=5, pady=5)

Button(text="Показать зарплаты", command=get_salaries).grid(row=6,column=0)
Button(text="Показать зарплаты после налога и премий", command=lambda: get_salaries(tax=True)).grid(row=6,column=1)

root.mainloop()