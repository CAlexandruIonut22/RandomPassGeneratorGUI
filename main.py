import tkinter as tk
from cryptography.fernet import Fernet
import pass_functions as psfct
import random


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


def create_random_pass(length):
    password = []
    for i in range(length):
        type_of_char = random.randint(1, 3)
        if type_of_char == 1:
            generated_char = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
            password.append(generated_char)
        elif type_of_char == 2:
            generated_char = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
            password.append(generated_char)
        elif type_of_char == 3:
            generated_char = chr(random.randint(33, 38))  # Generate a random symbol (based on ASCII code)
            password.append(generated_char)
    password = ''.join(password)
    password = shuffle(password)
    # l2.config(text=password)
    return password


def change_text():
    l2_2.config(text=create_random_pass(int(E1.get())))
    l3_2.config(text=psfct.encrypt_pass(key, l2_2['text']))
    l4_2.config(text=psfct.decrypt_pass(key, l3_2['text']))
    l5_2.config(text=psfct.hash_pass(l2_2['text']))


key = Fernet.generate_key()

window = tk.Tk()
window.geometry("800x640")
window.resizable(width=True, height=False)
window.title('Random Password Generator')

# length = tk.IntVar()
E1 = tk.Entry(window)

l1 = tk.Label(text="Random Password Generator", font=("Arial", 20), fg="Black")

b1 = tk.Button(text="Click on me to generate a random password", font=("Arial", 15), bg="#A3E4D7",
               command=change_text)
l1_1 = tk.Label(font=("Arial", 16), text='Enter size of password:')

l2_1 = tk.Label(font=("Arial", 16), text='Generated password is:')
l2_2 = tk.Label(font=("Arial", 12))

l3_1 = tk.Label(font=("Arial", 16), text='Encrypted password is:')
l3_2 = tk.Label(font=("Arial", 12))

l4_1 = tk.Label(font=("Arial", 16), text='Decrypted password is:')
l4_2 = tk.Label(font=("Arial", 12))

l5_1 = tk.Label(font=("Arial", 16), text='Hashed password is:')
l5_2 = tk.Label(font=("Arial", 12))

l1.place(x=165, y=20)
b1.place(x=200, y=530)

l1_1.place(x=65, y=60)
E1.place(x=300, y=65)

l2_1.place(x=65, y=130)
l2_2.place(x=300, y=130)

l3_1.place(x=65, y=230)
l3_2.place(x=300, y=230)

l4_1.place(x=65, y=330)
l4_2.place(x=300, y=330)

l5_1.place(x=65, y=430)
l5_2.place(x=300, y=430)
window.mainloop()
