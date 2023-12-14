from random import randint, shuffle

from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex

from memo_edit_layout import wer1, wer2, wer3, wer4, wer5

wrong = "не правильно"
correct = "правильно"


class Question():
    def __init__(self, question='', crt='',
                 wrn1='', wrn2='', wrn3=''):
        self.question = question
        self.crt = crt
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3


class QuestionView():
    def __init__(self, form, question, crt, wrn1, wrn2, wrn3):
        # конструктор получает и запоминает объект с данными и виджеты, соответствующие полям анкеты
        self.form = form  # может получить и None - ничего страшного не случится,
        # но для метода show нужно будет предварительно обновить данные методом change
        self.question = question
        self.crt = crt
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3

    def wer(self):
        self.question.setText(self.form.question)
        self.crt.setText(self.form.crt)
        self.wrn1.setText(self.form.wrn1)
        self.wrn2.setText(self.form.wrn2)
        self.wrn3.setText(self.form.wrn3)


class AnswerCheck(QuestionView):
    def __init__(self, form, question, crt, wrn1, wrn2, wrn3, answer, resultat):
        super().__init__(form, question, crt, wrn1, wrn2, wrn3)
        self.answer = answer
        self.resultat = resultat

    def tr(self):
        if self.crt.isChecked():
            self.resultat.setText(correct)
        else:
            self.resultat.setText(wrong)
        self.answer.setText(self.form.crt)


class QuestionListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []

    def rowCount(self, index):
        return len(self.form_list)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question

    def insertRows(self, parent=QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position)
        self.form_list.append(Question())
        self.endInsertRows()
        QModelIndex()
        return True

    def removeRows(self, position, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]


def random_question(questions, question, qd, answer, resultat):
    form = questions.random_question()
    shuffle(qd)
    form_card = AnswerCheck(form, question, qd[0], qd[1], qd[2], qd[3], answer, resultat)
    return form_card


def update(form):
    wer1.setText(form.question)
    wer2.setText(form.crt)
    wer3.setText(form.wrn1)
    wer4.setText(form.wrn2)
    wer5.setText(form.wrn3)
