from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QLabel, QRadioButton, QMessageBox)
from meme import data, number_data
#from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(600, 500)
window.setWindowTitle('Memory Card')
window.move(100, 100)

main_layout = QVBoxLayout()
v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

btn_menu = QPushButton('Меню') # додати нове питання

# створюємо віджети з питаннями
question = QLabel()
r_answer_1 = QRadioButton()
r_answer_2 = QRadioButton()
r_answer_3 = QRadioButton()
r_answer_4 = QRadioButton()

def show_result(answer):
    global window_result
    window_result = QWidget()
    window_result.resize(200, 200)
    window_result.move(window.x(), window.y())
    v_line = QHBoxLayout()
    l = QLabel()
    a = QLabel(answer)
    r = QLabel()
    v_line.addWidget(l)
    v_line.addWidget(a)
    v_line.addWidget(r)
    window_result.setLayout(v_line)
    window_result.show()

def check_result():
    global number_data
    try:
        if r_answer_1.isChecked(): # перевірка неправильної відповіді
            show_result('Неправильно')
        elif r_answer_2.isChecked(): # перевірка правильної відповіді
            show_result('Правильно')
            number_data += 1
            show_question(number_data)
        if r_answer_3.isChecked(): # перевірка неправильної відповіді
            show_result('Неправильно')
        if r_answer_4.isChecked(): # перевірка неправильної відповіді
            show_result('Неправильно')

    except Exception as e:
        print(e)

def show_question(number):
    question.setText(data[number]['question'])
    r_answer_1.setText(data[number]['wrong_answers'][0])
    r_answer_2.setText(data[number]['right_answer'])
    r_answer_3.setText(data[number]['wrong_answers'][1])
    r_answer_4.setText(data[number]['wrong_answers'][2])

btn_ok = QPushButton('Відповісти')
btn_ok.clicked.connect(check_result)

main_layout.addWidget(btn_menu)
main_layout.addWidget(question)#, alignment=Qt.AlignCenter

h_line1.addWidget(r_answer_1) # , alignment=Qt.AlignmentFlag.AlignCenter для pyqt6
h_line1.addWidget(r_answer_2)
h_line2.addWidget(r_answer_3)
h_line2.addWidget(r_answer_4)

main_layout.addLayout(h_line1)
main_layout.addLayout(h_line2)
main_layout.addWidget(btn_ok)

window.setLayout(main_layout)

show_question(number_data)

window.show()
app.exec_()