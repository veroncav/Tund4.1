import random

print("Добро пожаловать в тест по математике!")

while True:
    print("Выберите уровень сложности:")
    print("1 - простые")
    print("2 - средние")
    print("3 - сложные")
    try:
        level = int(input("Введите номер уровня (1-3): "))
        if level in [1, 2, 3]:
            break
        print("Введите число от 1 до 3.")
    except:
        print("Введите корректное число.")

while True:
    try:
        questions = int(input("Сколько примеров вы хотите решить? "))
        if questions > 0:
            break
        print("Введите положительное число.")
    except:
        print("Введите корректное число.")

score = 0

for i in range(questions):
    if level == 1:
        max_number = 10
        operations = ['+', '-']
    elif level == 2:
        max_number = 20
        operations = ['+', '-', '*']
    else:
        max_number = 50
        operations = ['+', '-', '*', '/']

    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    operation = random.choice(operations)

    if operation == '/' and num2 == 0:  # чтобы не было деления на ноль
        num2 = 1

    if operation == '/':
        correct_answer = num1 // num2
    else:
        correct_answer = eval(f"{num1} {operation} {num2}")

    print(f"Пример {i + 1}: {num1} {operation} {num2}")
    try:
        answer = int(input("Ваш ответ: "))
        if answer == correct_answer:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно! Правильный ответ: {correct_answer}")
    except:
        print("Ошибка! Вы ввели не число.")

print(f"Вы решили правильно {score} из {questions} примеров.")

