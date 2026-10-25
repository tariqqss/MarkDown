# 1. Типи даних
name = "Tariqq"
age = 17
height = 1.73
skills = ["Python", "Git", "HTML"]
student_info = {"name": name, "age": age}
coordinates = (50.45, 30.52)
unique_numbers = {1, 2, 3, 3, 2}

print("Типи даних:")
print(f"Ім'я: {name} ({type(name)})")
print(f"Вік: {age} ({type(age)})")
print(f"Навички: {skills}")
print(f"Унікальні числа: {unique_numbers}\n")

# 2. Вбудовані константи та зарезервовані слова
print("Константи та зарезервовані слова:")
print(f"Константи: {True}, {False}, {None}")
import keyword
print(f"Зарезервовані слова (перші 5): {keyword.kwlist[:5]}\n")

# 3. Вбудовані функції
numbers = [10, 5, 20, 15]
print("Вбудовані функції:")
print(f"Довжина списку: {len(numbers)}")
print(f"Максимальне значення: {max(numbers)}")
print(f"Сума елементів: {sum(numbers)}\n")

# 4. Цикли
print("Цикли:")
fruits = ["яблуко", "банан", "груша"]
for idx, fruit in enumerate(fruits, 1):
    print(f"{idx}. {fruit}")

count = 3
while count > 0:
    print(f"Зворотний відлік: {count}")
    count -= 1
print()

# 5. Розгалуження
print("Розгалуження:")
num = 7
if num % 2 == 0:
    print(f"Число {num} є парним")
else:
    print(f"Число {num} є непарним\n")

# 6. Обробка винятків try-except-finally
print("Обробка винятків:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Перехоплено помилку: {e}")
finally:
    print("Блок finally виконано успішно\n")

# 7. Контекстний менеджер with
print("Контекстний менеджер:")
try:
    with open("README.md", "r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        print(f"Перший рядок файлу README.md: {first_line}")
except FileNotFoundError:
    print("Файл README.md не знайдено, але з'єднання закрито коректно.")
print()

# 8. Лямбда-функції
print("Лямбда-функції:")
square = lambda x: x ** 2
greet = lambda user: f"Привіт, {user}!"

print(f"Квадрат числа 5: {square(5)}")
print(greet("Tariqq"))