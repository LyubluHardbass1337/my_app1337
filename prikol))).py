from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QPushButton, QTextEdit, QLineEdit
import json

app = QApplication([])
window = QWidget()

product_names_list = QListWidget()
product_text_edit = QTextEdit()
product_line_edit = QLineEdit()
product_line_edit.setPlaceholderText('Введите продукт...')
add_product_button = QPushButton('Добавить продукт...')
edit_product_button = QPushButton('Изменить продукт...')
del_product_button = QPushButton('Удалить продукт...')

layout_main = QHBoxLayout()

layout_v = QVBoxLayout()
layout_v.addWidget(product_text_edit)
layout_v.addWidget(product_line_edit)

layout_line_buttons = QHBoxLayout()
layout_line_buttons.addWidget(add_product_button)
layout_line_buttons.addWidget(edit_product_button)
layout_line_buttons.addWidget(del_product_button)

layout_v.addLayout(layout_line_buttons)

layout_main.addWidget(product_names_list)
layout_main.addLayout(layout_v)

with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)
    product_names_list.addItems(products.keys())

def add_product():
    product = product_line_edit.text()
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    products[product] = ''
    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(products, file)
    product_names_list.clear()
    product_names_list.addItems(products.keys())

def show_product_info():
    product = product_names_list.selectedItems()[0].text()
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    product_text_edit.setText(products[product])

def edit_product():
    if product_names_list.selectedItems():
        text_product = product_text_edit.toPlainText()
        product = product_names_list.selectedItems()[0].text()
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        products[product] = text_product
        with open('products.json', 'w', encoding='utf-8') as file:
            json.dump(products, file)
        product_names_list.clear()
        product_text_edit.clear()
        product_names_list.addItems(products.keys())

def delete_product():
    if product_names_list.selectedItems():
        product = product_names_list.selectedItems()[0].text()
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        del products[product]
        with open('products.json', 'w', encoding='utf-8') as file:
            json.dump(products, file)
        product_names_list.clear()
        product_text_edit.clear()
        product_names_list.addItems(products.keys())

add_product_button.clicked.connect(add_product)
product_names_list.itemClicked.connect(show_product_info)
edit_product_button.clicked.connect(edit_product)
del_product_button.clicked.connect(delete_product)

window.setLayout(layout_main)
window.show()
app.exec()
