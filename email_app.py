import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

drafts_file = "drafts.json"
attachments = []

def load_drafts():
    if os.path.exists(drafts_file):
        with open(drafts_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_draft():
    draft = {
        "email": email_entry.get(),
        "subject": subject_entry.get(),
        "message": message_text.get("1.0", tk.END).strip(),
        "attachments": attachments.copy()
    }
    drafts.append(draft)
    with open(drafts_file, "w", encoding="utf-8") as file:
        json.dump(drafts, file, indent=4, ensure_ascii=False)
    messagebox.showinfo("Черновик", "Черновик сохранен!")

def view_draft():
    if drafts:
        draft = drafts[-1]
        email_entry.delete(0, tk.END)
        email_entry.insert(0, draft["email"])
        subject_entry.delete(0, tk.END)
        subject_entry.insert(0, draft["subject"])
        message_text.delete("1.0", tk.END)
        message_text.insert("1.0", draft["message"])
        global attachments
        attachments = draft.get("attachments", [])
        update_attachments_label()
    else:
        messagebox.showinfo("Черновик", "Черновиков нет!")

def preview_email():
    email = email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    attachment_info = "\n".join([f"Приложение: {os.path.basename(f)}" for f in attachments])
    preview_text = f"To: {email}\nSubject: {subject}\n\n{message}\n\n{attachment_info}"
    messagebox.showinfo("Предпросмотр письма", preview_text)

def clear_fields():
    email_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)
    global attachments
    attachments = []
    update_attachments_label()

def add_attachment():
    file_paths = filedialog.askopenfilenames(title="Выберите файлы для прикрепления")
    if file_paths:
        attachments.extend(file_paths)
        update_attachments_label()

def remove_attachments():
    global attachments
    attachments = []
    update_attachments_label()

def update_attachments_label():
    if attachments:
        text = f"Прикреплено файлов: {len(attachments)}"
        if len(attachments) == 1:
            text += f" ({os.path.basename(attachments[0])})"
        attachments_label.config(text=text)
    else:
        attachments_label.config(text="Нет прикрепленных файлов")

def send_email():
    sender_email = "veronika1999.v@gmail.com"  # Replace with your email
    sender_password = ""      # Replace with your password
    receiver_email = email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END).strip()

    if not receiver_email:
        messagebox.showerror("Ошибка", "Введите адрес получателя!")
        return

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Add attachments
        for file_path in attachments:
            attachment = open(file_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
            msg.attach(part)
            attachment.close()

        # Connect to SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        messagebox.showinfo("Отправка", "Письмо успешно отправлено!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Ошибка отправки", f"Не удалось отправить письмо:\n{str(e)}")

drafts = load_drafts()

# Создание окна
root = tk.Tk()
root.title("E-kiri")
root.geometry("600x500")
root.configure(bg="#F3E5AB")  # Пастельный бежевый

frame = tk.Frame(root, bg="#FDFD96")  # Пастельный желтый
frame.pack(padx=10, pady=10, fill="both", expand=True)

font_style = ("Helvetica", 12, "bold")

# Email field
tk.Label(frame, text="EMAIL:", bg="#B5EAD7", fg="#4A4A4A", font=font_style, width=10).grid(row=0, column=0, sticky="w", padx=5, pady=2)
email_entry = tk.Entry(frame, width=45, font=("Helvetica", 12))
email_entry.grid(row=0, column=1, padx=5, pady=2)

# Subject field
tk.Label(frame, text="TEEMA:", bg="#FFDAC1", fg="#4A4A4A", font=font_style, width=10).grid(row=1, column=0, sticky="w", padx=5, pady=2)
subject_entry = tk.Entry(frame, width=45, font=("Helvetica", 12))
subject_entry.grid(row=1, column=1, padx=5, pady=2)

# Message field
tk.Label(frame, text="KIRI:", bg="#FFABAB", fg="#4A4A4A", font=font_style, width=10).grid(row=2, column=0, sticky="w", padx=5, pady=2)
message_text = tk.Text(frame, height=8, width=45, font=("Helvetica", 12))
message_text.grid(row=2, column=1, padx=5, pady=2)

# Attachments
attachments_label = tk.Label(frame, text="Нет прикрепленных файлов", bg="#E2F0CB", fg="#4A4A4A", font=("Helvetica", 10))
attachments_label.grid(row=3, column=1, sticky="w", padx=5, pady=2)

# Buttons
add_attachment_btn = tk.Button(frame, text="LISA FAIL", bg="#C7CEEA", fg="black", font=font_style, command=add_attachment)
add_attachment_btn.grid(row=4, column=0, pady=5, padx=5, sticky="ew")

remove_attachments_btn = tk.Button(frame, text="EEMALDA FAILID", bg="#FF9AA2", fg="black", font=font_style, command=remove_attachments)
remove_attachments_btn.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

save_draft_btn = tk.Button(frame, text="SALVESTA MUSTAND", bg="#A2C3E8", fg="black", font=font_style, command=save_draft)
save_draft_btn.grid(row=5, column=0, pady=5, padx=5, sticky="ew")

view_draft_btn = tk.Button(frame, text="AVA MUSTAND", bg="#D4A5A5", fg="black", font=font_style, command=view_draft)
view_draft_btn.grid(row=5, column=1, pady=5, padx=5, sticky="ew")

preview_btn = tk.Button(frame, text="EELVAADE", bg="#B9FBC0", fg="black", font=font_style, command=preview_email)
preview_btn.grid(row=6, column=0, pady=5, padx=5, sticky="ew")

send_btn = tk.Button(frame, text="SAADA", bg="#F7A399", fg="black", font=font_style, command=send_email)
send_btn.grid(row=6, column=1, pady=5, padx=5, sticky="ew")

clear_btn = tk.Button(frame, text="PUHASTA", bg="#E5D4EF", fg="black", font=font_style, command=clear_fields)
clear_btn.grid(row=7, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

root.mainloop()