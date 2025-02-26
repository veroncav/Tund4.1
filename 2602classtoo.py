import tkinter as tk
from tkinter import filedialog

def send_email():
    email = email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    print(f"Отправка письма:\nEmail: {email}\nТема: {subject}\nСообщение: {message}")
def add_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        print(f"Выбрано изображение: {file_path}")

root = tk.Tk()
root.title("E-kirja saatmine")  
root.geometry("400x300")  
root.configure(bg="green")  

frame = tk.Frame(root, bg="white")
frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame, text="EMAIL:", bg="green", fg="white", width=10).grid(row=0, column=0, sticky="w", padx=5, pady=2)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame, text="TEEMA:", bg="green", fg="white", width=10).grid(row=1, column=0, sticky="w", padx=5, pady=2)
subject_entry = tk.Entry(frame, width=30)
subject_entry.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame, text="KIRI:", bg="green", fg="white", width=10).grid(row=2, column=0, sticky="w", padx=5, pady=2)
message_text = tk.Text(frame, height=5, width=30)
message_text.grid(row=2, column=1, padx=5, pady=2)

add_image_btn = tk.Button(frame, text="LISA PILT", bg="green", fg="white", command=add_image)
add_image_btn.grid(row=5, column=0, pady=5, padx=5, sticky="ew")

send_btn = tk.Button(frame, text="SAADA", bg="green", fg="white", command=send_email)
send_btn.grid(row=5, column=1, pady=5, padx=5, sticky="ew")

root.mainloop()
