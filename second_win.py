# напиши здесь код для второго экрана приложения
from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from final_win import *
from PyQt5.QtGui import QFont
class Experiment():
    def __init__(self, age, p1, p2, p3):
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.name_label = QLabel(txt_name)
        self.name_input = QLineEdit(txt_hintname)
        self.age_label = QLabel(txt_age)
        self.age_input = QLineEdit(txt_hintage)
        
        self.test_text1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.starttest1.clicked.connect(self.timer_test)
        self.result1 = QLineEdit(txt_hinttest1)

        self.test_text2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)

        self.test_text3 = QLabel(txt_test3)
        self.starttest3 = QPushButton(txt_starttest3)
        self.result2 = QLineEdit(txt_hinttest2)
        self.result3 = QLineEdit(txt_hinttest3)

        self.send_result = QPushButton(txt_sendresults)
        self.timer = QLabel('00:00:00')

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.name_label, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.name_input, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.age_label, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.age_input, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.test_text1, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.starttest1, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.result1, alignment=Qt.AlignLeft)

        self.hline1 = QHBoxLayout()
        self.hline1.addWidget(self.test_text2, alignment=Qt.AlignLeft)
        self.hline1.addWidget(self.timer, alignment=Qt.AlignRight)

        self.vline.addLayout(self.hline1)
        self.vline.addWidget(self.starttest2, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.test_text3, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.starttest3, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.result2, alignment=Qt.AlignLeft)
        self.vline.addWidget(self.result3, alignment=Qt.AlignLeft)

        self.hline2 = QHBoxLayout()
        self.hline2.addWidget(self.send_result, alignment=Qt.AlignCenter)
        self.vline.addLayout(self.hline2)
        self.setLayout(self.vline)
    def connects(self):
        self.send_result.clicked.connect(self.next)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_test2)
        self.starttest3.clicked.connect(self.timer_test3)
    def next(self):
        self.hide()
        self.exp = Experiment(self.age_input.text(), self.result1.text(), self.result2.text(), self.result3.text())
        self.fw = FinalWin(self.exp)
    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer1Event)
        self.timer1.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer.setText(time.toString('hh:mm:ss'))
        self.timer.setFont(QFont('Times', 36, QFont.Bold))
        self.timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer1.stop()
    def timer_test2(self):
        global time
        time = QTime(0, 0, 30)
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer2Event)
        self.timer1.start(1500)
    def timer2Event(self):
        self.timer.setText(time.toString('hh:mm:ss')[6:8])
    def timer_test3(self):
        global time
        time = QTime(0, 1, 0)
        
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer3Event)
        self.timer1.start(1000)
    def timer3Event(self):
        global time
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.timer.setStyleSheet('color: rgb(0, 0, 0)')
