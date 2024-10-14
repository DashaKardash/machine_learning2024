Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> Итоговое задание для новичков
SyntaxError: invalid syntax
>>> import csv
import json
from datetime import datetime

employees = [    # Данные сотрудников в виде списка словарей
    {"ФИО": "Иванов Иван Иванович", "Должность": "Менеджер", "Дата найма": "22.10.2013", "Оклад": 250000},
    {"ФИО": "Сорокина Екатерина Матвеевна", "Должность": "Аналитик", "Дата найма": "12.03.2020", "Оклад": 75000},
    {"ФИО": "Струков Иван Сергеевич", "Должность": "Старший программист", "Дата найма": "23.04.2012", "Оклад": 150000},
    {"ФИО": "Корнеева Анна Игоревна", "Должность": "Ведущий программист", "Дата найма": "22.02.2015", "Оклад": 120000},
    {"ФИО": "Старчиков Сергей Анатольевич", "Должность": "Младший программист", "Дата найма": "12.11.2021", "Оклад": 50000},
    {"ФИО": "Бутенко Артем Андреевич", "Должность": "Архитектор", "Дата найма": "12.02.2010", "Оклад": 200000},
    {"ФИО": "Савченко Алина Сергеевна", "Должность": "Старший аналитик", "Дата найма": "13.04.2016", "Оклад": 100000},
]

def calculate_programmer_bonus(employees):   # Функция для расчёта премии программистам на День программиста
    bonuses = []
    for employee in employees:
        if "программист" in employee["Должность"].lower():
            bonus = employee["Оклад"] * 0.03
            bonuses.append({"ФИО": employee["ФИО"], "Премия": bonus})
    return bonuses

def calculate_gender_bonus(employees):     # Функция для расчёта премии к 23 февраля и 8 марта

    bonuses = []
    for employee in employees:
        if employee["ФИО"].split()[1].endswith("а"):  # Женское имя
            bonus = 2000
            bonuses.append({"ФИО": employee["ФИО"], "Премия": bonus, "Праздник": "8 марта"})
        else:  # Мужское имя
            bonus = 2000
            bonuses.append({"ФИО": employee["ФИО"], "Премия": bonus, "Праздник": "23 февраля"})
    return bonuses

def calculate_salary_indexation(employees):  # Функция для расчёта индексации зарплат
    indexed_salaries = []
    current_date = datetime.now()
    for employee in employees:
        hire_date = datetime.strptime(employee["Дата найма"], "%d.%m.%Y")
        years_worked = (current_date - hire_date).days // 365
        indexation_rate = 0.07 if years_worked > 10 else 0.05
        new_salary = employee["Оклад"] * (1 + indexation_rate)
        indexed_salaries.append({"ФИО": employee["ФИО"], "Новая зарплата": new_salary})
    return indexed_salaries

def vacation_schedule(employees): # Функция для составления графика отпусков
    eligible_for_vacation = []
    current_date = datetime.now()
    for employee in employees:
        hire_date = datetime.strptime(employee["Дата найма"], "%d.%m.%Y")
        months_worked = (current_date - hire_date).days // 30
        if months_worked > 6:
            eligible_for_vacation.append(employee)
    return eligible_for_vacation

def write_to_csv(data, filename):  # Функция для записи данных в CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

def write_to_json(data, filename):  # Функция для записи данных в JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

programmer_bonuses = calculate_programmer_bonus(employees)  # Примеры использования функций
gender_bonuses = calculate_gender_bonus(employees)
indexed_employees = calculate_salary_indexation(employees)
vacation_list = vacation_schedule(employees)

write_to_csv(employees, 'employees.csv') # Запись данных в файлы
write_to_json(employees, 'employees.json')

print("Премии программистам ко Дню программиста:") # Вывод результатов
for bonus in programmer_bonuses:
    print(f"{bonus['ФИО']}: премия составляет {bonus['Премия']} рублей.")

print("\nПремии по гендерным праздникам:")
for bonus in gender_bonuses:
    print(f"{bonus['ФИО']}: премия к {bonus['Праздник']} составляет {bonus['Премия']} рублей.")

print("\nИндексация зарплат:")
for emp in indexed_employees:
    print(f"{emp['ФИО']}: новая зарплата составляет {emp['Новая зарплата']} рублей.")

print("\nСотрудники, включенные в график отпусков:")
for emp in vacation_list:
    print(f"{emp['ФИО']} включен(а) в график отпусков.")


SyntaxError: multiple statements found while compiling a single statement
>>> 