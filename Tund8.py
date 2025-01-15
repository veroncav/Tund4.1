#Praktiline töö 1: Sõne ja järjesti funktsioonidaktiline töö 1: Sõne ja järjesti funktsioonid


# Pyhton. Cписки

# Список продуктов в магазине
products = ["Хлеб", "Молоко", "Яблоки", "Масло", "Сыр"]
cart = []  # Корзина покупок

while True:
    # Меню
    print("\n1. Посмотреть продукты")
    print("2. Добавить в корзину")
    print("3. Удалить из корзины")
    print("4. Показать корзину")
    print("5. Сортировать корзину")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":  # Посмотреть продукты
        print("\nДоступные товары:")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")

    elif choice == "2":  # Добавить в корзину
        product = input("\nВведите название товара для добавления: ")
        if product in products:
            cart.append(product)  # Добавление в корзину
          


# Функции и методы строк 10 примеров с комментариями


# #1
# s="blueberry, strawberry, rasberry"
# result=s.replace("rasberry","cranberry") #Заменила в списке "rasberry" на "cranberry"
# print(result)

# #2
# s = "Monkey"
# result = s.isalpha()  # Проверяю состоит ли строка только из букв
# print(result)  

# #3
# s = "45657"
# result = s.isdigit()  # Проверяю состоит ли строка только из цифр
# print(result)  

# #4
# s = "kodutoo"
# result = s.capitalize()  # Преобразую первую букву строки в верхний регистр, остальные в нижний и получаем "Kodutoo"
# print(result) 

# #5
# s = "new year"
# result = s.upper() # Преобразую строку в верхний регистр и получаем "NEW YEAR"
# print(result)  

# #6
# S1 = "Merry"
# S2 = "Christmas"
# result = S1 + " " + S2  # Объединяю строки S1 и S2 с пробелом между ними и получаем "Merry Christmas"
# print(result)


# #7
# S1 = "Happy "
# result = S1 * 3  # Повторяею строку S1 3 раза и получаем " Happy Happy Happy "
# print(result)  

# #8
# s = "Your Nickname!"
# result = s[5:13]  # Извлекаем подстроку с 5-го по 13-й символ и получаем "Nickname"
# print(result)  

# #9
# s = "banana, apple, banana, carrot, banana"
# result = s.count("banana")  # Считаю количество раз слово "banana" встречается в строке и получаем 3
# print(result) 

# #10
# s = "   Veronika   "
# result = s.strip()  # Удаляем лишние пробелы с начала и конца строки и получаем "Veronika"
# print(result)  