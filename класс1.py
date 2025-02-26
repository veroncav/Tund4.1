from random import *
def failist_to_dict(f:str) :
riik_pealinn={}#sõnastik {"Riik":"Pealinn"}
pealinn_riik={}#sõnastik {"Pealinn":"Riik"}
riigid=[] #järjend, kus talletakse riigide nimetused
file=open(f,'r',encoding="utf-8-sig")
for line in file:
  k, v=line.strip.split('-') #k-võti, v-väärtus
  riik_pealinn[k]=v #täidame riik_pealinn
  pealinn_riik[v]=k #täidame pealinn_riik
  rigid.append(k)
file.close()
return riik_pealinn, pealinn_riik,riigid
#käivitame loodud funktsion
riik_pealinn, pealinn_riik,riigid=failist_to_dict
("rigid_pealinnad.txt)

# Словарь европейских стран и их столиц
capitals = {
Вот список стран и их столиц на эстонском языке:

"Albaania": "Tirana"
"Andorra": "Andorra-la-Vella"
"Austria": "Viin"
"Belgia": "Brüssel"
"Bulgaaria": "Sofia"
"Horvaatia": "Zagreb"
"Küpros": "Nikosia"
 "Tšehhi": "Praha"
"Taani": "Kopenhaagen"
 "Eesti": "Tallinn"
 "Soome": "Helsingi"
 "Prantsusmaa": "Pariis"
 "Saksamaa": "Berliin"
 "Kreeka": "Ateena"
 "Ungari": "Budapest"
 "Islandi": "Reykjavik"
 "Iirimaa": "Dublin"
 "Itaalia": "Rooma"
 "Läti": "Riia"
 "Liechtenstein": "Vaduz"
 "Leedu": "Vilniuse"
 "Luxemburg": "Luxemburg"
 "Malta": "Vallettta"
 "Monaco": "Monaco"
 "Montenegro": "Podgorica"
 "Madalmaad": "Amsterdam"
 "Põhja-Makedoonia": "Skopje"
 "Norra": "Oslo"
 "Poola": "Varssavi"
 "Portugali": "Lissabon"
 "Rumeenia": "Bukarest"
 "San Marino": "San Marino"
 "Serbia": "Belgrad"
 "Slovakkia": "Bratislava"
 "Sloveenia": "Ljubljana"
 "Hispaania": "Madrid"
 "Rootsi": "Stockholm"
 "Šveits": "Bern"
 "Vatikani": "Vatikani"
 "Suurbritannia": "London"
}

def find_capital():
    country = entry.get().strip()
    if country in capitals:
        result_label.config(text=f"Столица {country}: {capitals[country]}")
    else:
        add_new_entry(country)

def find_country():
    capital = entry.get().strip()
    for country, cap in capitals.items():
        if cap == capital:
            result_label.config(text=f"Страна {capital}: {country}")
            return
    add_new_entry(capital, is_country=False)

def add_new_entry(name, is_country=True):
    msg = "Введите столицу" if is_country else "Введите страну"
    pair = simpledialog.askstring("Добавление", f"{msg} для {name}:")
    if pair:
        if is_country:
            capitals[name] = pair
        else:
            capitals[pair] = name
        messagebox.showinfo("Добавлено", f"Добавлена пара: {name} - {pair}")

def edit_entry():
    country = simpledialog.askstring("Редактирование", "Введите название страны:")
    if country in capitals:
        new_capital = simpledialog.askstring("Редактирование", f"Введите новую столицу для {country}:")
        if new_capital:
            capitals[country] = new_capital
            messagebox.showinfo("Обновлено", f"Столица {country} изменена на {new_capital}")
    else:
        messagebox.showwarning("Ошибка", "Страна не найдена!")

def quiz():
    correct = 0
    questions = random.sample(list(capitals.items()), min(5, len(capitals)))
    for country, capital in questions:
        answer = simpledialog.askstring("Викторина", f"Введите столицу страны {country}:")
        if answer and answer.strip().lower() == capital.lower():
            correct += 1
    score = (correct / len(questions)) * 100
    messagebox.showinfo("Результат", f"Вы ответили правильно на {score:.2f}% вопросов")

root = tk.Tk()
root.title("Страны и столицы")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn_find_capital = tk.Button(root, text="Найти столицу", command=find_capital)
btn_find_capital.pack()

btn_find_country = tk.Button(root, text="Найти страну", command=find_country)
btn_find_country.pack()

btn_edit = tk.Button(root, text="Редактировать", command=edit_entry)
btn_edit.pack()

btn_quiz = tk.Button(root, text="Проверить знания", command=quiz)
btn_quiz.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()




