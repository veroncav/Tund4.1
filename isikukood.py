#ISIKUKOOD задание N1
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


#isikukood задание N2

def validate_length_and_digits(isikukood):
    """Проверка на длину и цифровой формат."""
    return len(isikukood) == 11 and isikukood.isdigit()


def validate_first_digit(isikukood):
    """Проверка первой цифры."""
    return isikukood[0] in '123456'


def calculate_control_number(isikukood):
    """Расчет контрольного числа."""
    weights_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    sum_1 = sum(int(isikukood[i]) * weights_1[i] for i in range(10))
    remainder_1 = sum_1 % 11
    
    if remainder_1 != 10:
        return remainder_1
    else:
        sum_2 = sum(int(isikukood[i]) * weights_2[i] for i in range(10))
        remainder_2 = sum_2 % 11
        return remainder_2 if remainder_2 != 10 else 0


def determine_birth_date(isikukood):
    """Определение даты рождения."""
    year = ('19' if isikukood[0] in '12' else '20' if isikukood[0] in '34' else '18') + isikukood[1:3]
    month = isikukood[3:5]
    day = isikukood[5:7]
    try:
        import datetime
        datetime.date(int(year), int(month), int(day))
        return day, month, year
    except ValueError:
        return None


def determine_gender(isikukood):
    """Определение пола."""
    return "мужчина" if int(isikukood[0]) % 2 == 1 else "женщина"


def determine_birth_place(isikukood):
    """Определение места рождения."""
    code_part = int(isikukood[7:10])
    if 1 <= code_part <= 10:
        return "Kuressaare Haigla"
    elif 11 <= code_part <= 19:
        return "Tartu Ülikooli Naistekliinik, Tartu"
    elif 21 <= code_part <= 220:
        return "Ida-Tallinna Keskhaigla, Pelgulinna sünнitusmaja"
    elif 221 <= code_part <= 270:
        return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= code_part <= 370:
        return "Maarjamõisa Kliinikum (Tartu)"
    elif 371 <= code_part <= 420:
        return "Narva Haigla"
    elif 421 <= code_part <= 470:
        return "Pärnu Haigla"
    elif 471 <= code_part <= 490:
        return "Pelgulinna Sünнitusmaja (Tallinn)"
    elif 491 <= code_part <= 520:
        return "Järvamaa Haigla (Paide)"
    elif 521 <= code_part <= 570:
        return "Rakvere, Tapa haigla"
    elif 571 <= code_part <= 600:
        return "Valga Haigla"
    elif 601 <= code_part <= 650:
        return "Viljandi Haigla"
    elif 651 <= code_part <= 700:
        return "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        return "Неизвестное место"


def process_isikukood(isikukood):
    """Основной процесс проверки личного кода."""
    if not validate_length_and_digits(isikukood):
        print("Некорректный код. Количество цифр должно быть 11. Попробуйте снова.")
        return False
    
    if not validate_first_digit(isikukood):
        print("Некорректный код. Первая цифра должна быть 1, 2, 3, 4, 5 или 6. Попробуйте снова.")
        return False
    
    birth_date = determine_birth_date(isikukood)
    if not birth_date:
        print("Некорректная дата рождения. Попробуйте снова.")
        return False
    
    control_number = calculate_control_number(isikukood)
    if int(isikukood[-1]) != control_number:
        print("Неверное контрольное число. Попробуйте снова.")
        return False
    
    gender = determine_gender(isikukood)
    day, month, year = birth_date
    birth_place = determine_birth_place(isikukood)
    print(f"Это {gender}, его/ее день рождения {day}.{month}.{year} и место рождения {birth_place}")
    
    return isikukood, gender, f"{day}.{month}.{year}", birth_place


def main():
    ikoodid = []  
    arvud = []  

    while True:
        isikukood = input("Введите личный код (или 'стоп' для завершения): ")
        if isikukood.lower() == 'стоп':
            break

        result = process_isikukood(isikukood)
        if result:
            ikoodid.append(result)
        else:
            arvud.append(isikukood)

    ikoodid.sort(key=lambda x: (x[1], x[0]))
    arvud.sort()

    print("\nПравильные коды:")
    for code in ikoodid:
        print(f"{code[0]}: {code[1]}, дата рождения: {code[2]}, место рождения: {code[3]}")

    print("\nНеправильные коды:")
    for code in arvud:
        print(code)

if __name__ == "__main__":
    main()



