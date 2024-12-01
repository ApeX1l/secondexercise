import sys

import random
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget


class DrawEllipse(QWidget):
    def __init__(self):
        super().__init__()
        self.interface = Interface()
        self.interface.setParent(self)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if self.interface.drawn:
            for i in range(3):
                r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                diametr = random.randint(1, 100)
                painter.setBrush(QColor(r, g, b))
                center = QPointF(float(random.randint(1, 500)), 100.0)
                painter.drawEllipse(center, diametr, diametr)
        painter.end()


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.drawn = False
        self.setFixedSize(500, 500)
        self.pushButton = QPushButton(self)
        self.pushButton.move(200, 260)
        self.pushButton.resize(93, 28)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.drawn = True
        self.parent().repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawEllipse()
    ex.show()
    sys.exit(app.exec())
