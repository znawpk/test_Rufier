from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.connects()

        self.set_appear()

        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.self.move(win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_testl = QLabel (txt_test1)
        self.text_test2 = QLabel (txt_test2)
        self.text_test3 = QLabel (txt_test3)
        self.text_timer = QLabel(txt_timer)
        # NEW
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QuBoxLayout()
        self.r_line = QuBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addwidget(self.text_timer, alignment = QtAlignCenter)
        self.l_line.addwidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addwidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    # NEW (метод изменен)
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.line_age.text()), self.line_test1.text(), self.line_test2.text(), self.line_test2.text())
        self.fw = Finalwin(self.exp)

    def timer_test (self):
        global time
        time = ОТ1те(0, 0, 15)
        self.timer = QTimer()
        self.timer. timeout. connect (self. timer1Event)
        self.timer.start(1000)


    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer. timeout. connect (self. timer2Event)
        #00Ho приседание 6 1.5 секунды
        self.timer.start(1500)

    # NEW
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3event)
        self.timer.start(1000)

    # NEW
    def timer1Event (self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStylesheet("color: rgb(0,6,0)")
        if time.tostring("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    # NEW   
    def timer2Event (self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.tostring("hh:mm:ss")[6:8])
        self.text_timer.setStylesheet("color: rgb(0,6,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.tostring("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    # NEW
    def timer3Event (self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.tostring(" :55"))
        if int(time.tostring("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgh(0,255,0)")
        elif int(time.tostring("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setstylesheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setstylesheet("color: rgh(e,0,0)")
            self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.tostring("hh:mm:ss") == "00:00:00":
            self.timer.stop()

     # NEW (метод изменен)
    def connects (self):
        self.btn_next. clicked. connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3. clicked. connect (self. timer_final)