import random

number = random.randint(1, 100)
print("Я загадал число от 1 до 100.")
answer = input("Оно чётное? (да/нет): ").strip().lower()

is_even = (number % 2 == 0)

if (answer == "да" and is_even) or (answer == "нет" and not is_even):
    print(f"Правильно! Загаданное число: {number}")
else:
    print(f"Неправильно! Загаданное число: {number}")
    
