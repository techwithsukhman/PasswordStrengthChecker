import customtkinter as ctk
from tkinter import messagebox
import string

def check():
    # print(entry.get())
    passwd = entry.get()
    
    if passwd == "":
        tips.pack_forget()
        messagebox.showerror("Warning","Please enter something")
        return

    has_lower = any(char in string.ascii_lowercase for char in passwd)
    has_upper = any(char in string.ascii_uppercase for char in passwd)
    has_digit = any(char in string.digits for char in passwd)
    has_symbols = any(char in string.punctuation for char in passwd)
    is_length = len(passwd) >= 8
    
    if has_lower and has_digit and has_symbols and has_upper and is_length:
        # print("Strong password")
        passwd_status_var.set("Strong password")
        passwd_status.configure(text_color="green")
        tips.pack_forget()
    else:
        # print("weak password")
        passwd_status_var.set("Weak password")
        passwd_status.configure(text_color="red",)
        tips.pack()
        
        
       
    
ctk.set_appearance_mode("system")

root = ctk.CTk()

root.geometry("500x400")
root.title("Password Strength Checker")

frame1 = ctk.CTkFrame(root,fg_color="transparent")
frame1.pack(padx=4,pady=50)

entry = ctk.CTkEntry(frame1,width=250,placeholder_text="Enter your password here")
entry.pack(padx=(0,8),pady=5,side="left")
entry.bind("<Return>", lambda event: check())
btn = ctk.CTkButton(frame1,text="Check",command=check).pack(pady=5,side="left")

passwd_status_var = ctk.StringVar()
status_font = ctk.CTkFont(family="Arial", size=18, weight="bold")
passwd_status = ctk.CTkLabel(root,textvariable=passwd_status_var,font=status_font)
passwd_status.pack(pady=4)
tips = ctk.CTkLabel(root,text="Tips: Add at least one capital letter, \n add at least one symbol,\n add numbers, \n add small letters,\n Length is more than 8.\n e.g. :- @TechWithSukhman2026")

brand = ctk.CTkLabel(
    root, 
    text="Developed by Sukhmandeep Singh (TechWithSukhman)", 
    font=ctk.CTkFont(family="Arial", size=18)
)
brand.pack(side="bottom", pady=15)

root.mainloop()