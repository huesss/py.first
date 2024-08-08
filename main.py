import json
from tkinter import *

def open_register_window():
    def register_user():
        login = register_loginInput.get()
        password = register_passField.get()
        confirm_password = register_confirmPasswordField.get()

        if not login or not password or not confirm_password:
            register_errorMsg.config(text='Вы не ввели все данные!', fg='red')
            register_info_label.config(text='')
        elif password != confirm_password:
            register_errorMsg.config(text='Пароли не совпадают!', fg='red')
            register_info_label.config(text='')
        else:
            try:
                with open('users.json', 'r') as file:
                    users = json.load(file)
            except FileNotFoundError:
                users = {}

            if login in users:
                register_errorMsg.config(text='Пользователь с таким логином уже существует!', fg='red')
                register_info_label.config(text='')
            else:
                users[login] = password
                with open('users.json', 'w') as file:
                    json.dump(users, file)
                register_errorMsg.config(text='')
                register_info_label.config(text='Регистрация выполнена успешно!', fg='green')
                register_window.destroy()
                root.deiconify()

    root.withdraw()
    register_window = Toplevel(root)
    register_window.title('Регистрация')
    register_window.geometry('1024x800')
    register_window.resizable(False, False)
    register_window.configure(bg='#333333')

    register_errorMsg = Label(register_window, text='', bg='#333333', fg='red', font=('Gilroy', 12))
    register_errorMsg.pack(pady=10)

    register_info_label = Label(register_window, text='', bg='#333333', font=('Gilroy', 12))
    register_info_label.pack()

    register_title = Label(register_window, text='Регистрация', bg='#333333', fg='#FFFFFF', font=('Gilroy', 18))
    register_title.pack(pady=10)

    register_loginInput = Entry(register_window, bg='#F0F0F0', font=('Gilroy', 12))
    register_loginInput.pack(pady=5)

    register_passField = Entry(register_window, bg='#F0F0F0', show='*', font=('Gilroy', 12))
    register_passField.pack(pady=5)

    register_confirmPasswordField = Entry(register_window, bg='#F0F0F0', show='*', font=('Gilroy', 12))
    register_confirmPasswordField.pack(pady=5)

    register_button = Button(register_window, text='Зарегистрироваться', bg='#333333', fg='#FFFFFF',
                             font=('Gilroy', 14),
                             command=register_user)
    register_button.pack(pady=10)

def login():
    login = loginInput.get()
    password = passField.get()

    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    if login in users and users[login] == password:
        errorMsg.config(text='')
        info_label.config(text='Вход выполнен успешно!', fg='green')
        user_label.config(text=f'Привет, {login}!', fg='white')
        print('Вход выполнен успешно')
        root.withdraw()
        open_control_panel()
    else:
        print('Неправильный логин или пароль')
        errorMsg.config(text='Неправильный логин или пароль', fg='red')
        info_label.config(text='')

def open_control_panel():
    def toggle_server():
        if server_status_var.get() == "Включен":
            server_status_var.set("Выключен")
            server_status_label.config(text="Центральный сервер: Выключен", fg="red")
        else:
            server_status_var.set("Включен")
            server_status_label.config(text="Центральный сервер: Включен", fg="green")

    def update_online_label(val):
        online_label.config(text=f"Онлайн: {int(float(val))}/1000")

    control_panel = Toplevel(root)
    control_panel.title("Панель управления")
    control_panel.geometry("1024x800")
    control_panel.resizable(False, False)
    control_panel.configure(bg="#333333")

    server_status_var = StringVar(value="Выключен")
    server_status_label = Label(control_panel, text="Центральный сервер: Выключен", bg="#333333", fg="red",
                                 font=("Gilroy", 14))
    server_status_label.pack(pady=20)

    toggle_button = Button(control_panel, text="Включить/Выключить сервер", bg="#333333", fg="#FFFFFF",
                            font=("Gilroy", 12), command=toggle_server)
    toggle_button.pack()

    online_label = Label(control_panel, text="Онлайн: 0/1000", bg="#333333", fg="#FFFFFF", font=("Gilroy", 18))
    online_label.pack(pady=12)

    online_slider = Scale(control_panel, from_=0, to=1000, orient=HORIZONTAL, command=update_online_label,
                          bg="#333333", fg="#FFFFFF", troughcolor="#F0F0F0", highlightthickness=0)
    online_slider.pack()

root = Tk()
root.title('Центральное управление SCPLF')
root.geometry('1024x800')
root.resizable(False, False)
root.configure(bg='#333333')

errorMsg = Label(root, text='', bg='#333333', fg='red', font=('Gilroy', 12))
errorMsg.pack(pady=10)

info_label = Label(root, text='', bg='#333333', font=('Gilroy', 12))
info_label.pack()

title = Label(root, text='Вход', bg='#333333', fg='#FFFFFF', font=('Gilroy', 18))
title.pack(pady=30)

loginInput = Entry(root, bg='#F0F0F0', font=('Gilroy', 12))
loginInput.pack(pady=10)

passField = Entry(root, bg='#F0F0F0', show='*', font=('Gilroy', 12))
passField.pack(pady=10)

login_btn = Button(root, text='Войти', bg='#333333', fg='#FFFFFF', font=('Gilroy', 14), command=login)
login_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

register_btn = Button(root, text='Регистрация', bg='#333333', fg='#FFFFFF', font=('Gilroy', 14),
                        command=open_register_window)
register_btn.place(relx=0.1, rely=0.1, anchor=NW)

user_label = Label(root, text='', bg='#333333', font=('Gilroy', 12))
user_label.place(relx=0.9, rely=0.9, anchor=SE)

root.mainloop()