questions = [
    "Как вас зовут?",
    "Сколько вам лет?",
    "Где вы живёте?",
    "Какой у вас любимый язык программирования?",
    "Чем вы занимаетесь (учёба/работа)?"
]

answers = []
print("Пожалуйста, ответьте на следующие вопросы:\n")

for question in questions:
    answer = input(question + " ")
    answers.append(answer)

from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"анкета_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as file:
    for q, a in zip(questions, answers):
        file.write(f"{q}\nОтвет: {a}\n\n")

print(f"\nСпасибо за заполнение анкеты! Ваши ответы сохранены в файле: {filename}")
