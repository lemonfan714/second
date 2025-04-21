from PyQt5.QtWidgets import *
import json
from datetime import datetime
from Window_apps.config import DARK_STYLE, LIGHT_STYLE, COLORFULL_THEME

print(datetime.now())
notes = {
    'Добро пожаловать':{'текст':'инструкция для заметок',
                        'теги':['приложение', 'инструкция']}
}
def save_to_json():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file)

app = QApplication([])
wind = QWidget()
wind.resize(800, 600)
wind.setWindowTitle('Smart notes')
wind.setStyleSheet(COLORFULL_THEME)

#LAyouts
main_hlayout = QHBoxLayout()
ver_layout1 = QVBoxLayout()
ver_layout2 = QVBoxLayout()
ver_layout3 = QVBoxLayout()
hor_layout1 = QHBoxLayout()
hor_layout2 = QHBoxLayout()

#Widjets
text_box = QTextEdit()
spisok_label = QLabel('Список заметок')
notes_list = QListWidget()
creator_btn = QPushButton('Создать заметку')
deleter_btn = QPushButton('Удалить заметку')
saver_btn = QPushButton('Сохранить заметку')
str_tags = QLabel('Список тегов')
tags_list = QListWidget()
str_searcher = QLineEdit()
str_searcher.setPlaceholderText('Введите тэг:')
btn_adder = QPushButton('Добавить тег к заметке')
btn_unplugger = QPushButton('Открепить от заметки')
btn_notes_searcher = QPushButton('Искать заметки по тегу')
btn_theme_switcher = QPushButton('темная тема')
btn_theme_switcher.setObjectName('btn')


with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
notes_list.addItems(notes)

def change_theme():
    if btn_theme_switcher.text() == 'темная тема':
        wind.setStyleSheet(DARK_STYLE)
        btn_theme_switcher.setText('Светлая тема')
    else:
        wind.setStyleSheet(LIGHT_STYLE)
        btn_theme_switcher.setText('темная тема')


def show_note():
    note_name = notes_list.selectedItems()[0].text()
    need_dict = notes[note_name]
    text_box.setText(need_dict['текст'])
    tags_list.clear()
    tags_list.addItems(need_dict['теги'])

def create_note():
    name, ok = QInputDialog().getText(wind, 'добавление заметки', 'Введите название заметки:')
    if ok:
        if name == '':
            data = str(datetime.now())

            name = f'заметка от{data[:data.rfind(":")]}'
        notes[name] = {'текст':'','теги': []}
        notes_list.addItem(name)


def delete_note():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0]
        name = name.text()
        del notes[name]
        notes_list.clear()
        notes_list.addItems(notes)
        text_box.clear()
        tags_list.clear()
        save_to_json()

def save_note():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0]
        name = name.text()
        notes[name]['текст'] = text_box.toPlainText()
        save_to_json()

def add_tag():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0]
        name = name.text()
        tag_name = str_searcher.text()
        if tag_name not in notes[name]['теги'] and tag_name != '':
            notes[name]['теги'].append(tag_name)
            save_to_json()
            tags_list.clear()
            tags_list.addItems(notes[name]['теги'])
            str_searcher.clear()

def remove_tag():
    if notes_list.selectedItems():
        name = notes_list.selectedItems()[0]
        name = name.text()
        if tags_list.selectedItems():
            tag_name = tags_list.selectedItems()[0].text()
            notes[name]['теги'].remove(tag_name)
            tags_list.clear()
            tags_list.addItems(notes[name]['теги'])
            save_to_json()
def search_with_tag():
    search_text = str_searcher.text()
    if search_text != '':
        if btn_notes_searcher.text() == 'Искать заметки по тегу':
            filtered_list = []
            for note in notes:
                if search_text in notes[note]['теги']:
                    filtered_list.append(note)
                    notes_list.clear()
                    notes_list.addItems(filtered_list)
                    btn_notes_searcher.setText('сбросить фильтр')
        else:
            notes_list.clear()
            tags_list.clear()
            notes_list.addItems(notes)
            btn_notes_searcher.setText('Искать заметки по тегу')


btn_notes_searcher.clicked.connect(search_with_tag)
btn_unplugger.clicked.connect(remove_tag)
btn_adder.clicked.connect(add_tag)
saver_btn.clicked.connect(save_note)
creator_btn.clicked.connect(create_note)
notes_list.itemClicked.connect(show_note)
deleter_btn.clicked.connect(delete_note)
btn_theme_switcher.clicked.connect(change_theme)

#Цепляние
ver_layout1.addWidget(text_box)
ver_layout2.addWidget(spisok_label)
ver_layout2.addWidget(notes_list)
ver_layout2.addLayout(hor_layout1)
hor_layout1.addWidget(creator_btn)
hor_layout1.addWidget(deleter_btn)
ver_layout2.addWidget(saver_btn)
ver_layout2.addWidget(str_tags)
ver_layout2.addWidget(tags_list)
ver_layout2.addWidget(str_searcher)
ver_layout2.addLayout(hor_layout2)
hor_layout2.addWidget(btn_adder)
hor_layout2.addWidget(btn_unplugger)
ver_layout2.addWidget(btn_notes_searcher)
ver_layout3.addWidget(btn_theme_switcher)
main_hlayout.addLayout(ver_layout1, 60)
main_hlayout.addLayout(ver_layout2, 35)
main_hlayout.addLayout(ver_layout3, 5)

wind.setLayout(main_hlayout)

wind.show()
app.exec_()