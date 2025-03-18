import re
import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def detect_language(name):
    """Определяет язык имени: русский или английский"""
    if re.search("[а-яА-Я]", name) and re.search("[a-zA-Z]", name):
        return None  # Смешанные буквы — ошибка
    elif re.search("[а-яА-Я]", name):
        return "ru"
    elif re.search("[a-zA-Z]", name):
        return "en"
    else:
        return None

def get_name_number(name):
    """Вычисляет число имени по нумерологии"""
    name = name.lower()

    ru_dict = {
        'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 6, 'ж': 8, 'з': 9,
        'и': 1, 'й': 1, 'к': 3, 'л': 4, 'м': 5, 'н': 6, 'о': 7, 'п': 8, 'р': 9,
        'с': 1, 'т': 2, 'у': 3, 'ф': 4, 'х': 5, 'ц': 6, 'ч': 7, 'ш': 8, 'щ': 9,
        'ъ': 0, 'ы': 1, 'ь': 2, 'э': 3, 'ю': 4, 'я': 5
    }
    
    en_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    }
    
    lang = detect_language(name)
    if lang is None:
        return "Ошибка: используйте только русский или только английский алфавит."

    num_dict = ru_dict if lang == "ru" else en_dict

    total = sum(num_dict[char] for char in name if char in num_dict)

    while total > 9:
        total = sum(int(digit) for digit in str(total))

    return total

def get_number_description(number):
    """Описание значений чисел"""
    descriptions = {
        1: "1 — Лидер, амбициозность, уверенность.",
        2: "2 — Дипломатия, гармония, чуткость.",
        3: "3 — Творчество, оптимизм, общительность.",
        4: "4 — Практичность, стабильность, упорство.",
        5: "5 — Свобода, приключения, энергия.",
        6: "6 — Ответственность, любовь, забота.",
        7: "7 — Аналитика, интеллект, духовность.",
        8: "8 — Власть, успех, материальный достаток.",
        9: "9 — Доброта, мудрость, альтруизм."
    }
    return descriptions.get(number, "Нет описания для этого числа.")

def send_email(email, name, number, description):
    """Отправляет результаты на почту"""
    sender_email = "veronika1999.v@gmail.com"  # Замените на ваш email
    sender_password = "40Ve9Ro10"  # Замените на ваш пароль

    subject = "Результат расчёта числа имени"
    body = f"Имя: {name}\nЧисло имени: {number}\nОписание: {description}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        messagebox.showinfo("Успех", "Результаты отправлены на вашу почту!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось отправить email: {e}")

def calculate():
    """Функция обработки ввода и вывода результата"""
    name = entry_name.get().strip()
    email = entry_email.get().strip()

    if not name:
        messagebox.showerror("Ошибка", "Введите имя")
        return
    if not email:
        messagebox.showerror("Ошибка", "Введите email")
        return
    if re.search("[0-9]", name):
        messagebox.showerror("Ошибка", "Имя не должно содержать цифр")
        return
    
    result = get_name_number(name)

    if isinstance(result, str):  # Ошибка
        messagebox.showerror("Ошибка", result)
        return

    description = get_number_description(result)
    label_result.config(text=f"Число имени: {result}\n{description}")

    # Отправляем результаты на почту
    send_email(email, name, result, description)

# --- Создание GUI ---
root = tk.Tk()
root.title("Расчёт числа имени")
root.geometry("400x400")
root.configure(bg="#f0f0f0")  # Светло-серый фон

# Ввод имени
label_name = tk.Label(root, text="Введите имя:", bg="#f0f0f0", font=("Arial", 12))
label_name.pack(pady=5)

entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

# Ввод email
label_email = tk.Label(root, text="Введите ваш email:", bg="#f0f0f0", font=("Arial", 12))
label_email.pack(pady=5)

entry_email = tk.Entry(root, font=("Arial", 12))
entry_email.pack(pady=5)

# Кнопка для расчета
button_calculate = tk.Button(root, text="Рассчитать и отправить", command=calculate, font=("Arial", 12), bg="#4CAF50", fg="white")
button_calculate.pack(pady=10)

# Область для вывода результата
label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12), wraplength=300)
label_result.pack(pady=5)

root.mainloop()