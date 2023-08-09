# from tkinter import *
# FONT_NAME="Courier"
from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json

#search password
def search_password():
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
            password=data[website_entry.get().title()]["password"]
        messagebox.showinfo(title=f"{website_entry.get().title()}", message=f"email: piyush9211vaibhav@gmail.com \npassword: {password}")
        pyperclip.copy(password)
    except:
        messagebox.showinfo(title=f"{website_entry.get().title()}", message="This is invalid input")

# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 =[random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list2 = [random.choice(symbols) for char1 in range(nr_symbols)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list3 = [random.choice(numbers) for char2 in range(nr_numbers)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list=password_list1+password_list2+password_list3
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:
                  {"email":email,
                   "password":password
                }
    }
# using \n now each password detail will be entered in new line
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:

                #reading old data
                data=json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file,indent=4 )
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# # ---------------------------- UI SETUP ------------------------------- #
# window=Tk()
# window.config(padx=20, pady=20)
# window.title("Password Manager")
#
# canvas=Canvas(width=200, height=200)
# canvas_img=PhotoImage(file="logo.png")
# canvas.create_image(100,100,image=canvas_img)
# canvas.grid(row=0, column=1)
#
# website_label=Label(text="Website:")
# website_label.grid(row=1, column=0)
#
# username_label=Label(text="Email/Username:")
# username_label.grid(row=2, column=0)
#
# password_label=Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# website_entry=Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
#
# username_entry=Entry(width=35)
# username_entry.grid(row=2, column=1, columnspan=2)
#
# password_entry=Entry(width=21)
# password_entry.grid(row=3, column=1)
#
#
# generate_password_button=Button(text="Generate Password")
# generate_password_button.grid(row=3, column=2)
# #
# add_button=Button(text="Add", width=35)
# add_button.grid(row=4, column=1, columnspan=2)
# #
#
# #
# #
# #
# #
#
#
#
#
#
#
#
# window.mainloop()
window=Tk()
window.title("My password manager")
window.config(padx=50, pady=50)

canvas=Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry=Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "piyush9211vaibhav@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_password_button=Button(text="Generate Password", command=create_password)
generate_password_button.grid(row=3, column=2)

add_button= Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button= Button(text="search", width=15, command=search_password)
search_button.grid(row=1, column=2)






window.mainloop()

