from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QBoxLayout, QListWidget, QPushButton, QLineEdit
import json

app = QApplication([])
window = QWidget()










products_names = QListWidget()
products_text = QTextEdit()
product_line = QLineEdit()
product_line.setPlaceholderText('Введите продукт...')
add_product_button = QPushButton('Добавить продукт...')
edit_product_button = QPushButton('Изменить продукт...')
del_product_button = QPushButton('Удалить продукт...')

layout_main = QHBoxLayout()

layout_v = QVBoxLayout()
layout_v.addWidget(products_text)
layout_v.addWidget(product_line)

layout_line_buttons = QHBoxLayout()
layout_line_buttons.addWidget(add_product_button)
layout_line_buttons.addWidget(edit_product_button)
layout_line_buttons.addWidget(del_product_button)

layout_v.addLayout(layout_line_buttons)

layout_main.addWidget(products_names)
layout_main.addLayout(layout_v)

with open('products.json', 'r', encoding='utf-8') as file:
    products = json.load(file)
    products_names.addItems(products)



def add_product():
    product = product_line.text()
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    products[product] = ''
    with open('products.json', 'r', encoding='utf-8') as file:
       json.dump(products, file)
    products_names.clear()
    products_names.addItems(product)

def info_product():
    product = products_names.selectedItems()[0].text()
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    products_text.setText(products[product])

def edit_product():
    if products_names.selectedItems():
        text_product = products_text.toPlainText()
        product = products_names.selectedItems()[0].text()
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        products[product] = text_product
          with open('products.json', 'w', encoding='utf-8') as file:
            products = json.load(file)
        products_names.clear()
        products_text.clear()
        products_names.addItems(products)

def del_product():
    if products_names.selectedItems():
        product = products_names.selectedItems()[0].text()
        with open('products.json', 'r', encoding='utf-8') as file:
            products = json.load(file)
        del products[product]
        with open('products.json', 'w', encoding='utf-8') as file:
            json.dump(products, file)
        products_names.clear()
        products_text.clear()
        products_names.addItems(products)



add_product_button.clicked.connect(add_product)
products_names.itemClicked.connect(info_product)
edit_product_button.clicked.connect(edit_product)
del_product_button.clicked.connect(del_product)

window.setLayout(layout_main)
window.show()
app.exec()