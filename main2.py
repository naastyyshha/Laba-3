import string
from tkinter import messagebox, Tk, PhotoImage, Label, Entry, Button
import random



def generate_key():
    input_number = entry.get()
    if not input_number.isdigit() or len(input_number) != 6:
        messagebox.showerror("Error", "Введите шестизначное число.")
        return

    block1_digits = input_number[3:6]
    block2_digits = input_number[0:3]

    letters1 = ''.join(random.choices(string.ascii_uppercase, k=2))
    letters2 = ''.join(random.choices(string.ascii_uppercase, k=2))

    sum_block = int(block1_digits) + int(block2_digits)

    generated_key = f"{block1_digits}{letters1}-{block2_digits}{letters2}-{sum_block:04d}"

    result_label.config(text=f"Сгенерированный ключ: {generated_key}")


wind = Tk()
wind.title("Keygen")
wind.geometry("800x500")
background_image = PhotoImage(file='the_sims4.png')
background_label = Label(wind, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

instruction_label = Label(wind, text="Введите шестизначное число:", bg="white", font=("Arial", 12))
instruction_label.place(x=310, y=130)

entry = Entry(wind, font=("Arial", 12), width=10)
entry.place(x=370, y=170)

generate_button = Button(wind, text="Генерировать ключ", command=generate_key, font=("Arial", 12), bg="pink",
                            fg="white")
generate_button.place(x=340, y=230)

result_label = Label(wind, text="", bg="white", font=("Arial", 12))
result_label.place(x=250, y=280)


wind.mainloop()