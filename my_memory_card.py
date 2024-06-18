#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, 
 QRadioButton, QLabel, QMessageBox, QGroupBox, QButtonGroup)
from random import*
class Question():
    def __init__(self, question, r_answer, w1, w2, w3):
        self.question = question
        self.r_answer = r_answer
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

questions_list = []
questions_list.append(Question('Государственый язык бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Иглу', 'Хата', 'Юрта'))

app = QApplication([])

main = QWidget()
btnOk = QPushButton("ответить")
main.setWindowTitle('Memory Card')
quathion = QLabel("Какой национальности не существует?")
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')
RadioGroup = QButtonGroup()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layot_main = QVBoxLayout()
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('Правильно/неправильно')
lb_Correct = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(quathion, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btnOk, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main.setLayout(layout_card)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btnOk.setText('Следующий вопроc')
def show_questhion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btnOk.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == btnOk.text():
        show_result()
    else:
        show_questhion()
answers = [rbtn1, rbtn2, rbtn3, rbtn4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.r_answer)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    quathion.setText(q.question)
    lb_Correct.setText(q.r_answer)
    show_questhion()

def show_correct(res):
    lb_result.setText(res)
    show_result()
def next_question():
    if len(questions_list) > 0:
        app.total += 1
        print(f'Статистика:\n-Всего вопросов: {app.total}\n-Правильных ответов: {app.score}')
        cur_question = randint(0, len(questions_list) - 1)
        q = questions_list[cur_question]
        questions_list.remove(q)
        ask(q)
    else:
        show_statistics()
    

def show_statistics():
    msg = QMessageBox()
    msg.setWindowTitle('Статстика и рейтинг')
    msg.setText(f"Cтатистика:\n-Всего вопросов:{app.total}\n-Правильных ответов: {app.score}\n"
                f"Рейтинг: {round(app.score / app.total * 100, 2)}%")
    msg.exec()

def chek_ansewer():
    if answers[0].isChecked():
        show_correct('Правильно')
        app.score += 1
        print(f'Статистика:\n-Всего вопросов: {app.total}\n-Правильных ответов: {app.score}')
        print(f"Рейтинг: {round(app.score / app.total * 100, 2)}%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print(f'Рейтинг: {round(app.score / app.total * 100,2)}%')
def click_OK():

    if 'Ответить' == btnOk.text():
        chek_ansewer()
    else:
        next_question()
btnOk.clicked.connect(click_OK)
app.score = 0
app.total = 0
next_question()
main.show()
app.exec()
