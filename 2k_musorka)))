from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QPushButton, QTextEdit, QLineEdit
import json

app = QApplication([])
window = QWidget()

hero_list_widget = QListWidget()
hero_text_edit = QTextEdit()
hero_line_edit = QLineEdit()
hero_line_edit.setPlaceholderText('Введите героя...')
add_hero_button = QPushButton('Добавить героя...')
edit_hero_button = QPushButton('Изменить героя...')
del_hero_button = QPushButton('Удалить героя...')

main_layout = QHBoxLayout()

vertical_layout = QVBoxLayout()
vertical_layout.addWidget(hero_text_edit)
vertical_layout.addWidget(hero_line_edit)

line_button_layout = QHBoxLayout()
line_button_layout.addWidget(add_hero_button)
line_button_layout.addWidget(edit_hero_button)
line_button_layout.addWidget(del_hero_button)

vertical_layout.addLayout(line_button_layout)

main_layout.addWidget(hero_list_widget)
main_layout.addLayout(vertical_layout)

with open('heroes.json', 'r', encoding='utf-8') as file:
    heroes = json.load(file)
    hero_list_widget.addItems(heroes.keys())

def add_hero():
    new_hero = hero_line_edit.text()
    with open('heroes.json', 'r', encoding='utf-8') as file:
        heroes = json.load(file)
    heroes[new_hero] = ''
    with open('heroes.json', 'w', encoding='utf-8') as file:
        json.dump(heroes, file)
    hero_list_widget.clear()
    hero_list_widget.addItems(heroes.keys())

def show_hero_info():
    selected_hero = hero_list_widget.selectedItems()[0].text()
    with open('heroes.json', 'r', encoding='utf-8') as file:
        heroes = json.load(file)
    hero_text_edit.setText(heroes[selected_hero])

def edit_hero():
    if hero_list_widget.selectedItems():
        edited_hero = hero_text_edit.toPlainText()
        selected_hero = hero_list_widget.selectedItems()[0].text()
        with open('heroes.json', 'r', encoding='utf-8') as file:
            heroes = json.load(file)
        heroes[selected_hero] = edited_hero
        with open('heroes.json', 'w', encoding='utf-8') as file:
            json.dump(heroes, file)
        hero_list_widget.clear()
        hero_text_edit.clear()
        hero_list_widget.addItems(heroes.keys())

def delete_hero():
    if hero_list_widget.selectedItems():
        selected_hero = hero_list_widget.selectedItems()[0].text()
        with open('heroes.json', 'r', encoding='utf-8') as file:
            heroes = json.load(file)
        del heroes[selected_hero]
        with open('heroes.json', 'w', encoding='utf-8') as file:
            json.dump(heroes, file)
        hero_list_widget.clear()
        hero_text_edit.clear()
        hero_list_widget.addItems(heroes.keys())

add_hero_button.clicked.connect(add_hero)
hero_list_widget.itemClicked.connect(show_hero_info)
edit_hero_button.clicked.connect(edit_hero)
del_hero_button.clicked.connect(delete_hero)

window.setLayout(main_layout)
window.show()
app.exec()
