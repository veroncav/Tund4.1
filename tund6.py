#Ulesanne 1

N = int(input("������� �����? "))
max_num = -float('inf')
for _ in range(N):
    num = int(input())
    if num > max_num:
        max_num = num
print("������������:", max_num)N = int(input("������� �����? "))
max_num = -float('inf')
for _ in range(N):
    num = int(input())
    if num > max_num:
        max_num = num
print("������������:", max_num)


#Ulesanne 2


while True:
    num = int(input())
    if num == 0:
        break
    print(77 if num == 13 else num)


#Ulesanne 3


dist = 10
total = 0
for _ in range(7):
    total += dist
    dist *= 1.1
print("�����:", round(total, 2))


#Ulesanne 4

M = int(input("����� �����: "))
while M > 0:
    piece = int(input("�������: "))
    if piece > M:
        if input("������ �������? (��/���): ") == "��":
            print("�������:", M)
            break
    else:
        M -= piece
print("����� �����������")


#Ulesanne 5

while True:
    a = float(input("a: "))
    b = float(input("b: "))
    h = float(input("h: "))
    print("�������:", (a + b) * h / 2)
    if input("���? (��/���): ") != "��":
        break


#Ulesanne 6

num = int(input("�����: "))
print("�������" if num % 3 == 0 else "�� �������")
#111