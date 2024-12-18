import random

print("����� ���������� � ���� �� ����������!")

while True:
    print("�������� ������� ���������:")
    print("1 - �������")
    print("2 - �������")
    print("3 - �������")
    try:
        level = int(input("������� ����� ������ (1-3): "))
        if level in [1, 2, 3]:
            break
        print("������� ����� �� 1 �� 3.")
    except:
        print("������� ���������� �����.")

while True:
    try:
        questions = int(input("������� �������� �� ������ ������? "))
        if questions > 0:
            break
        print("������� ������������� �����.")
    except:
        print("������� ���������� �����.")

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

    if operation == '/' and num2 == 0:  # ����� �� ���� ������� �� ����
        num2 = 1

    if operation == '/':
        correct_answer = num1 // num2
    else:
        correct_answer = eval(f"{num1} {operation} {num2}")

    print(f"������ {i + 1}: {num1} {operation} {num2}")
    try:
        answer = int(input("��� �����: "))
        if answer == correct_answer:
            print("���������!")
            score += 1
        else:
            print(f"�����������! ���������� �����: {correct_answer}")
    except:
        print("������! �� ����� �� �����.")

print(f"�� ������ ��������� {score} �� {questions} ��������.")

