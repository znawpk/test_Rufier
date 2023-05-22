from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQts.Qteui import QDoublevalidator, QIntvalidator, QFont # npoBepka типов бводилых значений
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QBoxLayout, \
QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

from instr import *

class Finalwin(Quidget):
    def init (self, exp):
        super().__init__()

self.exp = exp

self.initUI()

self.set_appear()

self .show()

def results(self):
    if self.exp.age < 7:
        self.index = ©
        return
    self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
    if self.exp.age == 7 ог self.exp.age == 8:
        if self.index >= 21:
            return txt_res1
        elif self.index < 21 and self.index >= 17:
            return txt_res2
        elif self.index < 17 and self.index >= 12:
            return txt_res3
        elif self.index < 12 and self.index >= 6.5:
            return txt_res4
        else:
            return txt_res5
    if self.exp.age == 9 or self.exp.age — 10:
        if self.index >= 19.5:
            return txt_resl
        elif self.index < 19.5 and self.index >= 15.5:
            return txt_res2
        elif self.index < 15.5 and self.index >= 10.5:
            return txt_res3
        elif self.index < 10.5 and self.index >= 5:
            return txt_res4
        else:
            return txt_res5
    if self.exp.age == 11 or self.exp.age —= 12:
        if self.index >= 18:
            return txt_res1
        elif self.index < 18 and self.index >= 14:
            return txt_res2
        elif self.index < 14 and self.index >= 9:
            return txt_res3
        elif self.index < 9 and self.index >= 3.5:
            return txt_res4
        else:
            return txt_res5
    if self.exp.age —- 13 or self.exp.age —= 14:
        if self.index >= 16.5:
            return txt_res1
        elif self.index < 16.5 and self.index >= 12.5:
            return txt_res2
        elif self.index < 12.5 and self.index >= 7.5:
            return txt_res3
        elif self.index < 7.5 and self.index >= 2:
            return txt_res4
        else:
            return txt_res5
    if self.exp.age >= 15:
        if self.index >= 15:
            return txt_res1
        elif self.index < 15 and self.index >= 11:
            return txt_res2
        elif self.index < 11 and self.index >= 6:
            return txt_res3
        elif self.index < 6 and self.index >= 0.5:
            return txt_res4
        else:
            return txt_res5

    # NEW (метод изменен)
    def initUI(self):
        self.work text = QLabel(txt workheart + self.results()) 
        self.index text = QLabel(txt index + str(self.index))


        self.layout line = QuBoxLayout()
        self.layout_line.addwidget(self.index text, alignment - Qt.AlignCenter)
        self.layout_line.addwidget(self.work text, alignment - Qt.AlignCenter)
        self.setLayout(self.layout line)

    def set арреаг (self):
        self.setwindowTitle(txt_finalwin)
        self.resize(win width, win height)
        self.move(win_x, win y)
