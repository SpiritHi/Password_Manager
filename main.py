import random
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Password Keeper")
window.config(padx=100, pady=100)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(website, f"These are the information you provided: "
                                            f"\nemail: {email} \nPassword: {password}. Is this okay?")
    if is_ok:
        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please do not leave website and password entrys empty.")
        else:
            with open("data.txt", "a") as data_file:
                data_file.write(f"| {website} | {email} | {password} |\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="w")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w")

website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
#email_entry.insert(0, "INSERT YOUR EMAIL HERE")
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, sticky="w")

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()