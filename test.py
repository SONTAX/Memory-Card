from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout

app = QApplication([])
window = QWidget()
editor = QTextEdit()
vert = QVBoxLayout()
vert.addWidget(editor)
window.setLayout(vert)
window.show()
app.exec_()
