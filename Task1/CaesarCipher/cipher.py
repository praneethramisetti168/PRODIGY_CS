from tkinter import *
from tkinter import messagebox
import base64

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        try:
            shift = int(shift_entry.get())
            encrypted_message = caesar_cipher(message, shift)
            text_result_encrypt.delete(1.0, END)
            text_result_encrypt.insert(END, encrypted_message)
        except ValueError:
            messagebox.showerror("Encryption Error", "Invalid shift value. Please enter an integer.")
    elif password == "":
        messagebox.showerror("Encryption Error", "Please enter the password")
    else:
        messagebox.showerror("Encryption Error", "Invalid password")

def decrypt():
    password = code.get()
    if password == "1234":
        message = text1.get(1.0, END).strip()
        try:
            shift = int(shift_entry.get())
            decrypted_message = caesar_cipher(message, -shift)
            text_result_decrypt.delete(1.0, END)
            text_result_decrypt.insert(END, decrypted_message)
        except ValueError:
            messagebox.showerror("Decryption Error", "Invalid shift value. Please enter an integer.")
    elif password == "":
        messagebox.showerror("Decryption Error", "Please enter the password")
    else:
        messagebox.showerror("Decryption Error", "Invalid password")

def reset():
    code.set("")
    text1.delete(1.0, END)
    text_result_encrypt.delete(1.0, END)
    text_result_decrypt.delete(1.0, END)
    shift_entry.delete(0, END)

def encryption_screen():
    global screen_encrypt
    global code
    global text1
    global text_result_encrypt
    global shift_entry

    screen_encrypt = Toplevel()
    screen_encrypt.geometry("400x400")
    screen_encrypt.title("Encryption")

    label1 = Label(screen_encrypt, text="Enter Text:", font=("calibri", 13))
    label1.pack(pady=10)

    text1 = Text(screen_encrypt, font=("Roboto", 12), wrap=WORD, height=5)
    text1.pack(padx=10, pady=5, fill=BOTH, expand=True)

    label2 = Label(screen_encrypt, text="Enter Shift Value:", font=("calibri", 13))
    label2.pack(pady=10)

    shift_entry = Entry(screen_encrypt, width=10, font=("Arial", 12))
    shift_entry.pack()

    label3 = Label(screen_encrypt, text="Enter Secret Key:", font=("calibri", 13))
    label3.pack(pady=10)

    code = StringVar()
    entry_key = Entry(screen_encrypt, textvariable=code, width=30, font=("Arial", 12), show="*")
    entry_key.pack()

    btn_encrypt = Button(screen_encrypt, text="ENCRYPT", bg="#ed3833", fg="white", font=("Arial", 12), command=encrypt)
    btn_encrypt.pack(pady=10, fill=X)

    btn_reset = Button(screen_encrypt, text="RESET", bg="#1089ff", fg="white", font=("Arial", 12), command=reset)
    btn_reset.pack(pady=10, fill=X)

    text_result_encrypt = Text(screen_encrypt, font=("Roboto", 12), wrap=WORD, height=5)
    text_result_encrypt.pack(padx=10, pady=5, fill=BOTH, expand=True)

def decryption_screen():
    global screen_decrypt
    global code
    global text1
    global text_result_decrypt
    global shift_entry

    screen_decrypt = Toplevel()
    screen_decrypt.geometry("400x400")
    screen_decrypt.title("Decryption")

    label1 = Label(screen_decrypt, text="Enter Text:", font=("calibri", 13))
    label1.pack(pady=10)

    text1 = Text(screen_decrypt, font=("Roboto", 12), wrap=WORD, height=5)
    text1.pack(padx=10, pady=5, fill=BOTH, expand=True)

    label2 = Label(screen_decrypt, text="Enter Shift Value:", font=("calibri", 13))
    label2.pack(pady=10)

    shift_entry = Entry(screen_decrypt, width=10, font=("Arial", 12))
    shift_entry.pack()

    label3 = Label(screen_decrypt, text="Enter Secret Key:", font=("calbri", 13))
    label3.pack(pady=10)

    code = StringVar()
    entry_key = Entry(screen_decrypt, textvariable=code, width=30, font=("Arial", 12), show="*")
    entry_key.pack()

    btn_decrypt = Button(screen_decrypt, text="DECRYPT", bg="#00bd56", fg="white", font=("Arial", 12), command=decrypt)
    btn_decrypt.pack(pady=10, fill=X)

    btn_reset = Button(screen_decrypt, text="RESET", bg="#1089ff", fg="white", font=("Arial", 12), command=reset)
    btn_reset.pack(pady=10, fill=X)

    text_result_decrypt = Text(screen_decrypt, font=("Roboto", 12), wrap=WORD, height=5)
    text_result_decrypt.pack(padx=10, pady=5, fill=BOTH, expand=True)

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x150")
    screen.title("Caesar Cipher Encryption & Decryption")

    btn_encrypt = Button(screen, text="Encryption", bg="#ed3833", fg="white", font=("Arial", 12), command=encryption_screen)
    btn_encrypt.pack(pady=10, fill=X)

    btn_decrypt = Button(screen, text="Decryption", bg="#00bd56", fg="white", font=("Arial", 12), command=decryption_screen)
    btn_decrypt.pack(pady=10, fill=X)

    screen.mainloop()

main_screen()
