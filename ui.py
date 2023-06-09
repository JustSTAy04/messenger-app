from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit, QMessageBox, QListWidget, QListWidgetItem, QTextBrowser
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


# stores all colors that are used in our app for comfort
colors = {
    'white': '#FFFFFF',
    'purple': '#9375BF',
    'light_gray': '#F3F3F3',
    'dark_gray': '#303030'
}


# adds a text (qlabel) to our window with some text and styles
def add_label(text, boldness=400, size=16, align='l', tmar=0, rmar=0, bmar=0, lmar=0, tpad=0, rpad=0, bpad=0, lpad=0, background=colors['white'], color=colors["dark_gray"]):
    label = QLabel(text)
    if align == 'r':
        label.setAlignment(QtCore.Qt.AlignRight)
    elif align == 'c':
        label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(f'font-family: Roboto; font-weight: {boldness}; color: {color}; font-size: {size}px; margin: {tmar}px {rmar}px {bmar}px {lmar}px; padding: {tpad}px {rpad}px {bpad}px {lpad}px; background: {background};')
    return label


# adds a button (qpushbutton) to our window with some text and styles
def add_button(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('*{font-family: Roboto; font-weight: 500; font-size: 16px; padding: 5px 5px; margin: 0px 145px; border-radius: 4px;'
    + f'color: {colors["dark_gray"]}; border: 2px solid {colors["purple"]};' + '}' + '*:hover{' + f'background: {colors["purple"]}; color: {colors["white"]};' + '}')
    return button


# adds a text button (qpushbutton) to our window with some text and styles
def add_text_button(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFlat(True)
    button.setStyleSheet('*{font-family: Roboto; font-weight: 400; font-size: 14px; text-decoration: underline; margin: 0px 140px;'
    + f'color: {colors["purple"]};' + '}' + '*:hover{font-weight: 500;}')
    return button


# adds an input line (qlineedit) to our window with some placeholder and styles
def add_line_edit(text):
    line_edit = QLineEdit()
    line_edit.setMaxLength(12)
    line_edit.setFrame(False)
    line_edit.setPlaceholderText(text)
    line_edit.setStyleSheet(
        'font-family: Roboto; font-weight: 400; font-size: 16px; margin: 0px 10px 10px 10px; border-radius: 4px;'
        + f'color: {colors["dark_gray"]}; border: 2px solid {colors["light_gray"]};')
    return line_edit


# adds a list widget (qlistwidget) to our window
def add_list_widget(color='white'):
    list_widget = QListWidget()
    list_widget.setStyleSheet('border: none;' + f'background: {colors[color]}; font-size: 18px; color: {colors["dark_gray"]}; font-weight: 500;')
    return list_widget


# adds an input line (qlineedit) to our window with some placeholder and styles
def add_text_edit(text):
    line_edit = QLineEdit()
    line_edit.setFrame(False)
    line_edit.setPlaceholderText(text)
    line_edit.setStyleSheet(
        'font-family: Roboto; font-weight: 400; font-size: 16px; padding: 5px;'
        + f'color: {colors["dark_gray"]}; border: 2px solid {colors["light_gray"]};')
    return line_edit


# adds a list widget item with some text
def add_list_widget_item(text):
    return QListWidgetItem(text)


# adds an exit button (qpushbutton) to our main window with some text and styles
def add_exit_button(text):
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('*{font-family: Roboto; font-weight: 500; font-size: 16px; padding: 5px 0px;'
    + f'color: {colors["dark_gray"]}; border: 0px solid {colors["white"]};' + '}' + '*:hover{' + f'background: {colors["purple"]}; color: {colors["white"]};' + '}')
    return button


# adds a text browser for messages
def add_text_browser():
    text_browser = QTextBrowser()
    text_browser.setStyleSheet(f'background: {colors["light_gray"]}; font-size: 18px; font-weight: 500; font-family: Roboto; color: {colors["dark_gray"]}; border: 0px solid {colors["light_gray"]};')
    return text_browser


# creates an error message (qmessagebox) with some text
def error_message(msg):
    error = QMessageBox()
    error.setWindowTitle('Ooops!')
    error.setText(msg)
    error.setIcon(QMessageBox.Warning)
    error.setStandardButtons(QMessageBox.Ok)
    error.setStyleSheet(f'background: {colors["white"]}; color: {colors["dark_gray"]}; font-size: 14px; font-family: Roboto;')
    error.exec()
