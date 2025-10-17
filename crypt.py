import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def launch_app():
    def encrypt_message():
        msg = message_entry.get()
        try:
            shift = int(key_entry.get())
            encrypted = encrypt(msg, shift)
            result_var.set(f"Encrypted: {encrypted}")
        except:
            messagebox.showerror("Invalid", "Shift must be an integer.")

    def decrypt_message():
        msg = message_entry.get()
        try:
            shift = int(key_entry.get())
            decrypted = decrypt(msg, shift)
            result_var.set(f"Decrypted: {decrypted}")
        except:
            messagebox.showerror("Invalid", "Shift must be an integer.")

    app = tk.Tk()
    app.title("Cryptography App - Caesar Cipher")
    app.geometry("400x300")

    tk.Label(app, text="Enter Message:").pack()
    message_entry = tk.Entry(app, width=40)
    message_entry.pack(pady=5)

    tk.Label(app, text="Enter Shift Key:").pack()
    key_entry = tk.Entry(app, width=10)
    key_entry.pack(pady=5)

    tk.Button(app, text="Encrypt", command=encrypt_message, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(app, text="Decrypt", command=decrypt_message, bg="#2196F3", fg="white").pack(pady=5)

    result_var = tk.StringVar()
    tk.Label(app, textvariable=result_var, font=("Arial", 12), fg="blue").pack(pady=10)

    app.mainloop()

launch_app()