import sys

import random
from PyQt6 import uic
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


class DrawEllipse(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawn = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor('yellow'))
        if self.drawn:
            for i in range(3):
                diametr = random.randint(1, 100)
                center = QPointF(float(random.randint(1, 500)), 100.0)
                painter.drawEllipse(center, diametr, diametr)
        painter.end()

    def draw(self):
        self.drawn = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawEllipse()
    ex.show()
    sys.exit(app.exec())
