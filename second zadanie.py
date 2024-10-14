Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> задание №2 для новичков. про ногти
SyntaxError: invalid character '№' (U+2116)
>>> Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]# Данные, которые у нас есть
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

average_visits_per_day = sum(Week) / 7# 1. Рассчитываем среднее количество посещений в день

total_visits = sum(Week) # 2. Рассчитываем общее количество посещений за неделю

total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))]) # 3. Рассчитываем общую выручку салона за неделю

revenue_per_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))} # 4. Рассчитываем выручку по каждому виду маникюра


average_revenue_per_day_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}# 5. Рассчитываем среднюю выручку в день по видам маникюра


print(f"Среднее количество посещений в день: {average_visits_per_day:.2f}")# 6. Выводим результаты
print(f"Общее количество посещений за неделю: {total_visits}")
print(f"Общая выручка салона за неделю: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"  {style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, average_revenue in average_revenue_per_day_per_style.items():
    print(f"  {style}: {average_revenue:.2f} руб.")

>>> Nail_style = ["Шеллак", "Френч", "Обычный лак", "Гель-лак", "Акрил"]# Данные, которые у нас есть
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

average_visits_per_day = sum(Week) / 7# 1. Рассчитываем среднее количество посещений в день

total_visits = sum(Week) # 2. Рассчитываем общее количество посещений за неделю

total_revenue = sum([Price[i] * Week[i] for i in range(len(Nail_style))]) # 3. Рассчитываем общую выручку салона за неделю

revenue_per_style = {Nail_style[i]: Price[i] * Week[i] for i in range(len(Nail_style))} # 4. Рассчитываем выручку по каждому виду маникюра


average_revenue_per_day_per_style = {style: revenue / 7 for style, revenue in revenue_per_style.items()}# 5. Рассчитываем среднюю выручку в день по видам маникюра


print(f"Среднее количество посещений в день: {average_visits_per_day:.2f}")# 6. Выводим результаты
print(f"Общее количество посещений за неделю: {total_visits}")
print(f"Общая выручка салона за неделю: {total_revenue} руб.")
print("Выручка по видам маникюра:")
for style, revenue in revenue_per_style.items():
    print(f"  {style}: {revenue} руб.")
print("Средняя выручка в день по видам маникюра:")
for style, average_revenue in average_revenue_per_day_per_style.items():
    print(f"  {style}: {average_revenue:.2f} руб.")