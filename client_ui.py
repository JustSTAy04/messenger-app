import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit, QMessageBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from client import check_user, check_username, add_user


widgets = {
    'label': [],
    'button': [],
    'input': []
}

colors = {
    'white': '#FFFFFF',
    'purple': '#9375BF',
    'light_gray': '#F3F3F3',
    'dark_gray': '#303030'
}


def clear_widgets():
    for widget in widgets:
        if widgets[widget]:
            widgets[widget][-1].hide()
        for i in range(len(widgets[widget])):
            widgets[widget].pop()


def add_label(text, boldness=400, size=16, align='l', tmar=0, rmar=0, bmar=0, lmar=0, tpad=0, rpad=0, bpad=0, lpad=0):
    label = QLabel(text)
    if align == 'r':
        label.setAlignment(QtCore.Qt.AlignRight)
    elif align == 'c':
        label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(f'font-family: Roboto; font-weight: {boldness}; color: {colors["dark_gray"]}; font-size: {size}px; margin: {tmar}px {rmar}px {bmar}px {lmar}px; padding: {tpad}px {rpad}px {bpad}px {lpad}px')
    return label


def add_button(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('*{font-family: Roboto; font-weight: 500; font-size: 16px; padding: 5px 5px; margin: 0px 145px; border-radius: 4px;'
    + f'color: {colors["dark_gray"]}; border: 2px solid {colors["purple"]};' + '}' + '*:hover{' + f'background: {colors["purple"]}; color: {colors["white"]};' + '}')
    return button


def add_text_button(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFlat(True)
    button.setStyleSheet('*{font-family: Roboto; font-weight: 400; font-size: 14px; text-decoration: underline; margin: 0px 140px;'
    + f'color: {colors["purple"]};' + '}' + '*:hover{font-weight: 500;}')
    return button


def add_line_edit(text):
    line_edit = QLineEdit()
    line_edit.setMaxLength(12)
    line_edit.setFrame(False)
    line_edit.setPlaceholderText(text)
    line_edit.setStyleSheet(
        'font-family: Roboto; font-weight: 400; font-size: 16px; margin: 0px 10px 10px 10px; border-radius: 4px;'
        + f'color: {colors["dark_gray"]}; box-shadow: 0px 0px 4px {colors["light_gray"]}; border: 2px solid {colors["light_gray"]};')
    return line_edit


def login_frame():
    clear_widgets()

    widgets['label'].append(add_label('Hello there!', boldness=500, size=18, align='c', tmar=17))
    grid.addWidget(widgets['label'][-1], 0, 1)

    widgets['label'].append(add_label('Username:', lmar=10, rmar=10))
    grid.addWidget(widgets['label'][-1], 1, 1)

    widgets['input'].append(add_line_edit('Enter your username'))
    grid.addWidget(widgets['input'][-1], 2, 1)

    widgets['label'].append(add_label('Password:', lmar=10, rmar=10))
    grid.addWidget(widgets['label'][-1], 3, 1)

    widgets['input'].append(add_line_edit('Enter your password'))
    grid.addWidget(widgets['input'][-1], 4, 1)

    widgets['button'].append(add_button('Login'))
    widgets['button'][-1].clicked.connect(login)
    grid.addWidget(widgets['button'][-1], 5, 1)

    widgets['label'].append(add_label('Need an account?', size=14, align='c', tmar=10, bmar=0))
    grid.addWidget(widgets['label'][-1], 6, 1)

    widgets['button'].append(add_text_button('Sign up'))
    widgets['button'][-1].clicked.connect(sign_up_frame)
    grid.addWidget(widgets['button'][-1], 7, 1)


def sign_up_frame():
    clear_widgets()

    widgets['label'].append(add_label('Welcome!', boldness=500, size=18, align='c', tmar=17))
    grid.addWidget(widgets['label'][-1], 0, 1)

    widgets['label'].append(add_label('Username:', lmar=10, rmar=10))
    grid.addWidget(widgets['label'][-1], 1, 1)

    widgets['input'].append(add_line_edit('Enter your username'))
    grid.addWidget(widgets['input'][-1], 2, 1)

    widgets['label'].append(add_label('Password:', lmar=10, rmar=10))
    grid.addWidget(widgets['label'][-1], 3, 1)

    widgets['input'].append(add_line_edit('Enter your password'))
    grid.addWidget(widgets['input'][-1], 4, 1)

    widgets['button'].append(add_button('Sign Up'))
    grid.addWidget(widgets['button'][-1], 5, 1)
    widgets['button'][-1].clicked.connect(sign_up)

    widgets['label'].append(add_label('Already a user?', size=14, align='c', tmar=10, bmar=0))
    grid.addWidget(widgets['label'][-1], 6, 1)

    widgets['button'].append(add_text_button('Login'))
    widgets['button'][-1].clicked.connect(login_frame)
    grid.addWidget(widgets['button'][-1], 7, 1)


def error_message(msg):
    error = QMessageBox()
    error.setWindowTitle('Ooops!')
    error.setText(msg)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    error.setStyleSheet(f'background: {colors["white"]}; color: {colors["dark_gray"]}; font-size: 14px; font-family: Roboto;')
    error.exec()


def return_user_data():
    return widgets['input'][0].text().strip(), widgets['input'][1].text()


def sign_up():
    username, password = return_user_data()
    name_msg = username_is_valid(username)
    pass_msg = password_is_valid(password)
    if name_msg != 'ok':
        error_message('Username ' + name_msg)
    elif pass_msg != 'ok':
        error_message('Password ' + pass_msg)
    else:
        if check_username(username):
            add_user(username, password)
        else:
            error_message('This username is already taken.')


def login():
    username, password = return_user_data()
    print(username, password)
    if check_user(username, password):
        error_message('Incorrect username or password!')
    else:
        print('Logged in!')


def username_is_valid(username):
    if len(username) < 4:
        return 'is too short (minimum 4 symbols).'
    elif username[0].isnumeric():
        return 'can`t start with a number.'
    else:
        return 'ok'


def password_is_valid(password):
    if len(password) < 4:
        return 'is too short (minimum 4 symbols).'
    elif len([i for i in password if i == ' ']) > 0:
        return 'can`t contain spaces.'
    elif not(password.isalpha() or password.isalnum()):
        return 'must contain letters.'
    else:
        return 'ok'


def main_frame():
    clear_widgets()
    window.setFixedWidth(800)
    window.setFixedHeight(600)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowIcon(QtGui.QIcon('chat.png'))

window.setWindowTitle('Chatium')
window.setFixedWidth(400)
window.setFixedHeight(300)
window.setStyleSheet(f'background: {colors["white"]}; ')

grid = QGridLayout()