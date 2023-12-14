from PyQt5.QtWidgets import QWidget

from memo_app import app
from memo_card_layout import rew, wer21, rew3, wer11, wer12, wer6, wer7, wer8, wer9, rew4, resultat, question
from memo_data import *
from memo_main_layout import qwe1, qwe3, qwe4, qwe5, qwe10

qd = [wer6, wer7, wer8, wer9]

questions = QuestionListModel()
form = Question('Чи подобається вам PUBG: Mobile?', 'норм гра', 'ні, погана гра', 'норм, але івенти зіпсували',
                'в неї хтось грає???????? роблокс краще')
questions.form_list.append(form)
form = Question('Що робити коли заблукав?', 'йти додому', 'не йти додому і сидіти в кущах', "ваз з'їли кліщі",
                'ви не заблукали')
questions.form_list.append(form)
form = Question('Коли у тебе день народження?', '23 серпня', '20 квітня', '29 вересня', '1 вересня')
questions.form_list.append(form)
form = Question('сяомі?', '.', "мінус пам'ять", 'топ за свої грощі', 'в мене айфон ((')
questions.form_list.append(form)

form_card = None


def nq():
    if rew4.text() != ("наступне питання"):
        form_card.tr()
        resultat()
    else:
        show_random()


def start():
    show_random()
    card.show()
    menu.hide()


def tre():
    card.hide()
    menu.show()


def show_random():
    global form_card
    form_card = random_question(questions, rew3, qd, wer12, wer11)
    form_card.wer()
    question()


def edit(i):
    if i.isValid():
        i = i.row()
        form = questions.form_list[i]
        update(form)


def add():
    questions.insertRows()
    last = questions.rowCount(0) - 1
    i = questions.index(last)
    qwe1.setCurrentIndex(i)
    edit(i)


def delete():
    questions.removeRows(qwe1.currentIndex().row())
    edit(qwe1.currentIndex())


def save():
    i = qwe1.currentIndex().row()
    questions.form_list[i].question = wer1.text()
    questions.form_list[i].crt = wer2.text()
    questions.form_list[i].wrn1 = wer3.text()
    questions.form_list[i].wrn2 = wer4.text()
    questions.form_list[i].wrn3 = wer5.text()


card = QWidget()
menu = QWidget()
card.resize(600, 500)
menu.resize(1000, 450)
card.setLayout(wer21)
menu.setLayout(qwe10)
qwe1.setModel(questions)
qwe1.clicked.connect(edit)
rew4.clicked.connect(nq)
qwe5.clicked.connect(start)
qwe3.clicked.connect(add)
qwe4.clicked.connect(delete)
rew.clicked.connect(tre)
wer1.textEdited.connect(save)
wer2.textEdited.connect(save)
wer3.textEdited.connect(save)
wer4.textEdited.connect(save)
wer5.textEdited.connect(save)
menu.show()
app.exec_()
