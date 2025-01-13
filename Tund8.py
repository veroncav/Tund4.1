#Praktiline töö 1: Sõne ja järjesti funktsioonidaktiline töö 1: Sõne ja järjesti funktsioonid


# Pyhton. Cписки

# Список продуктов в магазине
products = ["Хлеб", "Молоко", "Яблоки", "Масло", "Сыр"]

# Функция для отображения меню
def display_menu():
    print("\n1. Посмотреть продукты")
    print("2. Добавить в корзину")
    print("3. Удалить из корзины")
    print("4. Показать корзину")
    print("5. Выйти")

# Основная функция программы
def shopping():
    cart = []  # Корзина покупок
    while True:
        display_menu()  # Показываем меню
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\nДоступные товары:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product}")

        elif choice == "2":
            product = input("\nВведите название товара для добавления: ")
            if product in products:
                cart.append(product)  # Добавление в корзину
                print(f"{product} добавлен в корзину.")
            else:
                print("Товар не найден.")

        elif choice == "3":
            print("\nТовары в корзине:")
            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")
            try:
                idx = int(input("\nВведите номер товара для удаления: ")) - 1
                removed_item = cart.pop(idx)  # Удаление из корзины
                print(f"{removed_item} удален из корзины.")
            except (ValueError, IndexError):
                print("Неверный номер товара.")

        elif choice == "4":
            print("\nТовары в корзине:")
            for item in cart:
                print(f"- {item}")

      
        elif choice == "5":
            print("\nСпасибо за покупку!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

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