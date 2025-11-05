import tkinter as tk
from tkinter import messagebox
import re
import random
import string
import pygame


def is_hex(hex_digit):
    return bool(re.fullmatch(r'[0-9A-Fa-f]+', hex_digit))


def hex_to_dec(hex_digit):
    dec_digits = str(int(hex_digit, 16))
    digits = string.ascii_uppercase + string.digits
    pieces = []

    for i in range(3):
        place = random.randint(0, 4)
        res = ''.join(random.choice(digits) for _ in range(place)) + dec_digits[i]
        res += ''.join(random.choice(digits) for _ in range(5 - place - 1))
        pieces.append(res)

    key = f"{'-'.join(pieces)} {dec_digits[-2:]}"
    return key


def create_key_label(parent, key):
    label_2 = tk.Label(
        parent,
        text='Ваш ключ:',
        font=('Arial Bold', 20),
        bg='white',
        fg='red',
    )
    label_key = tk.Label(
        parent,
        text=key,
        font=('Arial Bold', 20),
        bg='white',
        fg='red',
        pady=10,
        padx=20,
        highlightcolor='red',
        highlightbackground='red',
        highlightthickness=3,
    )
    label_2.pack()
    label_key.pack()


def key_root(hex_digit):
    key_window = tk.Toplevel(root)
    key_window.title('Ключ')
    key_window.geometry('400x150')
    key_window.resizable(width=False, height=False)
    key_window['bg'] = 'white'
    key_window.iconphoto(False, icon)

    key = hex_to_dec(hex_digit)

    new_frame = tk.Frame(key_window, bg='white')
    new_frame.place(relx=0.5, rely=0.5, anchor='center')

    create_key_label(new_frame, key)

    key_window.update()
    window_name = key_window.winfo_pathname(key_window.winfo_id())
    root.eval(f'tk::PlaceWindow {window_name} center')
    return key_window


def clicked():
    hex_digit = entry.get()
    if is_hex(hex_digit):
        if len(hex_digit) < 5:
            messagebox.showinfo('Ошибка', 'Число должно содержать 5 символов.')
        else:
            key_root(hex_digit)
    else:
        messagebox.showinfo('Ошибка', 'Введённое вами число не HEX.')


def limit_text(entry_value):
    return len(entry_value) <= 5


def create_main_frame(parent):
    frame = tk.Frame(
        parent,
        bg='red',
        highlightcolor='white',
        highlightbackground='white',
        highlightthickness=3,
        width=600,
    )
    frame.pack(side=tk.LEFT, padx=100)
    return frame


def create_title_label(parent):
    return tk.Label(
        parent,
        text='Введите пятизначное HEX-число:',
        font=('Arial Bold', 20),
        bg='red',
        fg='white',
    )


def create_entry(parent, root):
    vcmd = (root.register(limit_text), '%P')
    entry = tk.Entry(
        parent,
        width=15,
        fg='red',
        font=('Arial Bold', 30),
        validate='key',
        validatecommand=vcmd,
        justify='center',
    )
    entry.focus()
    return entry


def create_button(parent):
    return tk.Button(
        parent,
        text='Сгенерировать',
        font=('Arial Bold', 20),
        bg='red',
        fg='white',
        activebackground='white',
        activeforeground='red',
        command=clicked,
    )


def create_background_label(parent, image):
    tk.Label(parent, image=image, bg='red').pack(side='right')


def main():
    global root, icon, entry

    root = tk.Tk()
    root.title('Генератор ключа')
    root.geometry('1280x720')
    root.resizable(width=False, height=False)
    root['bg'] = 'red'

    icon = tk.PhotoImage(file='icon.png')
    root.iconphoto(False, icon)

    bg = tk.PhotoImage(file='spider.png')
    create_background_label(root, bg)

    main_frame = create_main_frame(root)
    label_title = create_title_label(main_frame)
    entry = create_entry(main_frame, root)
    button = create_button(main_frame)

    label_title.grid(column=0, row=0, padx=10, pady=10)
    entry.grid(column=0, row=1, padx=10, pady=10)
    button.grid(column=0, row=2, padx=10, pady=10)

    
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()


if __name__ == '__main__':
    main()
