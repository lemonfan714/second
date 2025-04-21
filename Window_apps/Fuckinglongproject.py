#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint
app = QApplication([])
wind = QWidget()
wind.right_answers = 0
wind.total_answers = 0
wind.resize(400, 400)
wind.setWindowTitle('Memo card')
verl_1 = QVBoxLayout()
verl_2 = QVBoxLayout()
verl_3 = QVBoxLayout()
questions = QLabel('Вопрос')
answers = QGroupBox('Варианты ответов')
horl_1 = QHBoxLayout()
horl_2 = QHBoxLayout()
quest_1 = QRadioButton('Энцы')
quest_2 = QRadioButton('Чулымцы')
quest_3 = QRadioButton('Смурфы')
quest_4 = QRadioButton('Алеуты')
horl_1.addWidget(quest_1, alignment=Qt.AlignHCenter)
horl_1.addWidget(quest_2, alignment=Qt.AlignHCenter)
horl_2.addWidget(quest_3, alignment=Qt.AlignHCenter)
horl_2.addWidget(quest_4, alignment=Qt.AlignHCenter)
verl_1.addLayout(horl_1)
verl_1.addLayout(horl_2)
answers.setLayout(verl_1)
ranswers = QGroupBox('Правильный ответ')
statistics = QLabel('')
nadpis = QLabel('правильно/неправильно')
right = QLabel('Правильный ответ')
verl_3.addWidget(nadpis)
verl_3.addWidget(right, alignment=Qt.AlignCenter)
verl_3.addWidget(statistics)
ranswers.setLayout(verl_3)
knopka = QPushButton('Ответить')
verl_2.addWidget(questions, alignment=Qt.AlignCenter)
verl_2.addWidget(answers)
verl_2.addWidget(ranswers)
verl_2.addWidget(knopka, alignment=Qt.AlignCenter)
wind.setLayout(verl_2)
ranswers.hide()

def stats():
    if wind.right_answers == 0:
        statistics.setText(f'''Правильных ответов:{wind.right_answers} из {wind.total_answers}
статистика - 0%''')
    else:
        statistics.setText(f'''Правильных ответов:{wind.right_answers} из {wind.total_answers}
статистика - {round(wind.right_answers/wind.total_answers*100, 2)}%''')

class Question():
    def __init__(self, text_quest, rights, wrong_1, wrong_2, wrong_3):
      self.question = text_quest
      self.right = rights
      self.wrong_1 = wrong_1
      self.wrong_2 = wrong_2
      self.wrong_3 = wrong_3

list_questions = []
list_questions.append(Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Бразильский', 'Испанский'))
list_questions.append(Question('Какая рыба водится в море', 'Зеленуха', 'Голавль', 'Жерех', 'Судак'))
list_questions.append(Question('Как называли строителя в старину', 'Бондарь', 'Бортник', 'Зодчий', 'Кормчий'))
list_questions.append(Question('Какая студия создала RDR2', 'Rockstar', 'NorthWood', 'Bethesda', 'Naughty Dog'))
list_questions.append(Question('Какого дерева не существует', 'Забор', 'Береза', 'Дуб', 'Сосна'))
list_questions.append(Question('Как звали главного героя игры Watch Dogs 2', 'Маркус', 'Ренч', 'Ситара', 'Джош'))

def switcher():
    answers.hide()
    ranswers.show()
    knopka.setText('Следующий вопрос')
    stats()

radiobuttons = QButtonGroup()
radiobuttons.addButton(quest_1)
radiobuttons.addButton(quest_2)
radiobuttons.addButton(quest_3)
radiobuttons.addButton(quest_4)

def unswitcher():
    ranswers.hide()
    answers.show()
    knopka.setText('Ответить')
    radiobuttons.setExclusive(False)
    quest_1.setChecked(False)
    quest_2.setChecked(False)
    quest_3.setChecked(False)
    quest_4.setChecked(False)
    radiobuttons.setExclusive(True)
def definer():
    if knopka.text() == 'Ответить':
        check_ans()
    else:
        next_quest()

lister = [quest_1, quest_2, quest_3, quest_4]

def ask(q:Question):
    shuffle(lister)
    questions.setText(q.question)
    lister[0].setText(q.wrong_1)
    lister[1].setText(q.wrong_2)
    lister[2].setText(q.wrong_3)
    lister[3].setText(q.right)
    right.setText(q.right)
    unswitcher()

def next_quest():
    q = list_questions[randint(0, len(list_questions) - 1)]
    ask(q)

def check_ans():
    if lister[3].isChecked():
        wind.right_answers += 1
        nadpis.setText('Правильно!')
    else:
        nadpis.setText('Не правильно!')
    wind.total_answers += 1
    switcher()

knopka.clicked.connect(definer)
next_quest()
wind.show()
app.exec_()