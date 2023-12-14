from PyQt5.QtWidgets import QWidget, QListView, QHBoxLayout, QVBoxLayout, QPushButton

from memo_edit_layout import wer6
from memo_app import app

qwe1 = QListView()
qwe2 = QWidget()
qwe2.setLayout(wer6)
qwe3 = QPushButton('нове питання')
qwe4 = QPushButton('видалити')
qwe5 = QPushButton('тестування')
qwe6 = QVBoxLayout()
qwe6.addWidget(qwe1)
qwe6.addWidget(qwe3)
qwe7 = QVBoxLayout()
qwe7.addWidget(qwe2)
qwe7.addWidget(qwe4)
qwe8 = QHBoxLayout()
qwe8.addLayout(qwe6)
qwe8.addLayout(qwe7)
qwe9 = QHBoxLayout()
qwe9.addStretch(1)
qwe9.addWidget(qwe5, stretch=2)
qwe9.addStretch(1)
qwe10 = QVBoxLayout()
qwe10.addLayout(qwe8)
qwe10.addLayout(qwe9)
