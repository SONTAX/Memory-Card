from PyQt5.QtWidgets import QLineEdit, QFormLayout

from memo_app import app

wer1 = QLineEdit('')
wer2 = QLineEdit('')
wer3 = QLineEdit('')
wer4 = QLineEdit('')
wer5 = QLineEdit('')
wer6 = QFormLayout()
wer6.addRow('питання:', wer1)
wer6.addRow('правильна відповідь:', wer2)
wer6.addRow('неправильна відповідь:', wer3)
wer6.addRow('неправильна відповідь:', wer4)
wer6.addRow('неправильна відповідь:', wer5)
