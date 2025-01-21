ikoodid = []  # Список правильных кодов
arvud = []  # Список неправильных кодов

while True:
    isikukood = input("Введите личный код (или 'стоп' для завершения): ")

    if isikukood.lower() == 'стоп':
        break

    
    if len(isikukood) != 11 or not isikukood.isdigit() or isikukood[0] not in '123456':
        print("Некорректный код. Попробуйте снова.")
        arvud.append(isikukood)
        continue

    year = ('19' if isikukood[0] in '12' else '20' if isikukood[0] in '34' else '18') + isikukood[1:3]
    month = isikukood[3:5]
    day = isikukood[5:7]

    try:
        import datetime
        datetime.date(int(year), int(month), int(day))  
    except ValueError:
        print("Некорректная дата рождения. Попробуйте снова.")
        arvud.append(isikukood)
        continue

    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    sum_1 = 0
    for i in range(10):
        sum_1 += int(isikukood[i]) * weights_1[i]
    
    remainder_1 = sum_1 % 11
    
    if remainder_1 != 10:
        control_number = remainder_1
    else:
        sum_2 = 0
        for i in range(10):
            sum_2 += int(isikukood[i]) * weights_2[i]
        
        remainder_2 = sum_2 % 11
        
        if remainder_2 != 10:
            control_number = remainder_2
        else:
            control_number = 0
    
   
    if int(isikukood[-1]) != control_number:
        print("Неверное контрольное число. Попробуйте снова.")
        arvud.append(isikukood)
        continue

  
    gender = "мужчина" if int(isikukood[0]) % 2 == 1 else "женщина"
    birth_date = f"{day}.{month}.{year}"

    ikoodid.append((isikukood, gender, birth_date))
    print(f"Это {gender}, его/ее день рождения {birth_date}")


ikoodid.sort(key=lambda x: (x[1], x[0]))  
arvud.sort()


print("\nПравильные коды:")
for code in ikoodid:
    print(f"{code[0]}: {code[1]}, дата рождения: {code[2]}")
print("\nНеправильные коды:")
for code in arvud:
    print(code)




