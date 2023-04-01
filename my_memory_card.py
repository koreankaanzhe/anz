#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLaoyut, QLabel, QVBoxLayout, QMessageBox, QRadioButton)


app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Memory Card')
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question =question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()




question = QLabel('Какой национальности не существует')
bth_answer1 = QRadioButton('Энцы')
bth_answer2 = QRadioButton('Чулымцы')
bth_answer3 = QRadioButton('Смурфы')
bth_answer4 = QRadioButton('Алеуты')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
layuot_ans1 = QHBoxLayout()
layuot_ans2 = QHBoxLayout()
layuot_ans3 = QHBoxLayout()

layuot_ans2.addWiget(rbtn1)
layuot_ans2.addWiget(rbtn2)
layuot_ans3.addWiget(rbtn3)
layuot_ans3.addWiget(rbtn4)
layuot_ans1.addWiget(layuot_ans2)
layuot_ans1.addWiget(layuot_ans3)

RadioGroupBox.setLayout(layuot_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут')
layuot_res = QVBoxLayout()
layuot_res.addWidget(lb_Result, alignment = (Qt.AlignLeft |  Qt.AlignTop))
layuot_res.addWidget(lb_Correct, alignment = (Qt.AlignHCenter | stretch == 2))
AnsGroupBox.setlayout(layuot_res)

layuot_line1 =QHBoxLayout()
layuot_line2 =QHBoxLayout()
layuot_line3 =QHBoxLayout()
layuot_line1.addWidget(lb_Question,alignment=(Qt.AlignHCenter |  Qt.AligVCenter))
  

layuot_line2.addWidget(RadioGroupBox)
layuot_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()
layuot_line3.addStretch(1)
layuot_line3.addWidget(btn_Ok, stretch=2)
layuot_line3.addStretch(1)

layuot_card = QVBoxLayout()
layuot_card.addLayout(layout_line1 ,stretch = 2)
layuot_card.addLayout(layout_line1 ,stretch =8)
layuot_card.addStretch(1)
layuot_card.addLayout(layout_line3 ,stretch = 1)
layuot_card.addStretch(1)
layuot_card.addStretch(5)

def show_corect(res):
    lb_Resuit.setText(res)
    show_result()

def check_answeer():
    if answer[0].isChecked():
        show_corect('Правильно!')
    else:




def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()




def next_question():
    cur_question = randint
    q = Question_list[cur_question]
    window_total +=1

def check_answer():
    if answers[0].isChecked:


questions_list = []
ql = Question('Государственный язык Португалии', "Португальский ", "Английский " ,"Испанский",  " Французский")


q = Question('Выбери перевод слова "переменная"',' varible', 'variation', 'variant', 'changig')
ask(q)

window = QWidget()
window.setlayout(layuot_card)
window.setWindowTitle('Memory card')

window.show()

app.exec_()

