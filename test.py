import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Registration system")
root.resizable(False, False)
root.geometry("400x350")
## Style theme 
style = ttk.Style()
style.theme_use('alt')
style.configure("TButton", background='#660f9d', foreground='white', width = 20, focuscolor='none')
style.map('TButton', background=[('active', '#ab43ed')])
user_name = tk.StringVar()
email = tk.StringVar()
password = tk.StringVar()
male = tk.StringVar()
female = tk.StringVar()
def register():
    user_info = user_name.get()
    user_email = email.get()
    user_password = password.get()
    male_val = male.get()
    female_val = female.get()
    print(male_val)
    if user_info and user_email and user_password:
        file = open(f"{user_info}.txt", "w")
        file.write(f"user name: {user_info} \n")
        file.write(f"email: {user_email} \n")
        file.write(f"Password: {user_password} \n")
        file.write(f"Gender: {male_val or female_val}")
        file.close()

        user_name_input.delete("0", "end")
        email_input.delete("0", "end")
        password_input.delete("0", "end")

        label_output = ttk.Label(root, text="Registration Success", foreground="green", font=("Arial", 10), padding=10)
        label_output.grid(column=0, row=13,columnspan=2, sticky="EW")
        print(user_info , user_email, user_password)
    else:
        label_output = ttk.Label(root, text="Please Enter all required field", foreground="red", font=("Arial", 10), padding=10)
        label_output.grid(column=0, row=13,columnspan=2, sticky="EW")
def show_password():
    p = password.get()
    if p:
        label = ttk.Label(root, text="Your Password is: " + str(p))
        label.grid(column=0, row=11, columnspan=2)

# Widgets
logo = ImageTk.PhotoImage(Image.open("users/sign-in-logo.png"))
my_label = tk.Label(image=logo, width=50, height=50)
male_option = ttk.Radiobutton(root, text="Male", variable=male, value="male")
female_option = ttk.Radiobutton(root, text="Female", variable=female , value="female")
user_label = ttk.Label(root, text="Username", padding=10)
user_name_input = ttk.Entry(root, width=25, textvariable=user_name)

email_label = ttk.Label(root, text="Email", padding=10)
email_input = ttk.Entry(root, width=25, textvariable=email)

password_label = ttk.Label(root, text="Password", padding=10)
password_input = ttk.Entry(root, width=25,show="*", textvariable=password)
register_button = ttk.Button(root, text="Register",cursor="hand2", command=register)
show = ttk.Button(root, text="Show Password", command=show_password)
# Layout 
my_label.grid(column=0,row=0,rowspan=2, columnspan=2)
user_label.grid(column=0, row=2, sticky="E", padx=5, pady=5)
user_name_input.grid(column=1, row=2, sticky="EW", padx=5, pady=5)
user_name_input.focus()

email_label.grid(column=0, row=3, sticky="E", padx=5, pady=5)
email_input.grid(column=1, row=3, sticky="EW", padx=5, pady=5)

password_label.grid(column=0, row=4, sticky="E", padx=5, pady=5)
password_input.grid(column=1, row=4, sticky="EW", padx=5, pady=5)
show.grid(column=0, row=10,columnspan=2, padx=5, pady=5)
register_button.grid(column=0, row=12, columnspan=2, sticky="EW", padx=5, pady=5)
male_option.grid(column=0, row=8)
female_option.grid(column=1, row=8)
root.mainloop()