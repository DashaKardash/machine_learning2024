Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> Задание №1. Про утят
SyntaxError: invalid character '№' (U+2116)
>>> import re
from collections import Counter

# 1. Определяем функцию, которая принимает текст и анализирует частоту появления каждого слова
def analyze_text_frequency(text):
    # 2. Приводим текст к нижнему регистру и убираем знаки препинания с помощью регулярного выражения
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # 3. Разбиваем текст на слова, используя метод split(), который разбивает строку по пробелам
    words = cleaned_text.split()
    
    # 4. Используем Counter из модуля collections для подсчета частоты каждого слова
    word_count = Counter(words)
    
    # 5. Сортируем слова по частоте в порядке убывания, а если частота одинаковая — по алфавиту
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # 6. Выводим каждое слово и его частоту
    for word, count in sorted_word_count:
        print(f'{word}: {count}')

# 7. Входной текст, который будем анализировать
text = """На шагающих утят быть похожими хотят,
Быть похожими хотят не зря, не зря.
Можно хвостик отряхнуть и пуститься в дальний путь
И пуститься в дальний путь, крича "кря-кря".
И природа хороша, и погода хороша,
Нет, не зря поет душа, не зря, не зря.
Даже толстый бегемот, неуклюжий бегемот
От утят не отстает, кряхтит "кря-кря"."""

# 8. Вызываем функцию с текстом
analyze_text_frequency(text)

SyntaxError: multiple statements found while compiling a single statement
>>> 