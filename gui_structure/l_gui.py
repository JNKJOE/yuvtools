import sys
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.input_1 = QtWidgets.QLineEdit('1.0')
        self.input_2 = QtWidgets.QTextEdit()
        self.output = QtWidgets.QTextEdit()
        self.submit = QtWidgets.QPushButton('Submit')

        self.input_2.setPlaceholderText('Input')
        self.output.setPlaceholderText('Output')
        self.submit.clicked.connect(self.process)
        QtGui.QShortcut(QtGui.QKeySequence('Ctrl+W'), self, self.key1)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.input_1)
        self.layout.addWidget(self.input_2)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.submit)

        self.setWindowTitle('MyWidget')
        self.setGeometry(400, 300, 800, 600)
        self.show()

    @QtCore.Slot()
    def process(self):
        print('process')

    @QtCore.Slot()
    def key1(self):
        print('key1')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()

    sys.exit(app.exec())
