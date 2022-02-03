import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Squares(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.run()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def run(self):
        side = int(self.sideEdit.text())
        coef = float(self.coefEdit.text())
        number = int(self.numberEdit.text())
        startx = int((500 - side) / 2)
        starty = int((500 - side) / 2) + 100


        self.qp.setPen(QColor(255, 0, 0))
        for i in range(number):
            self.qp.drawRect(startx, starty, side, side)
            new_side = int(side * coef)
            shift = (side - new_side) // 2
            startx += shift
            starty += shift
            side = new_side


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Squares()
    ex.show()
    sys.exit(app.exec_())