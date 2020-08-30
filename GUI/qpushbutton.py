from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬GUI")

        button = QtWidgets.QPushButton(self)
        button.setText("일반버튼")

        disableButton = QtWidgets.QPushButton(self)
        disableButton.setText("비활성화")
        disableButton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText("체크버튼")
        checkButton.setCheckable(True)
        checkButton.toggle()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(disableButton)
        layout.addWidget(checkButton)

        self.setLayout(layout)
        self.show()


app = QtWidgets.QApplication([])
win = MyWindows()

app.exec_()
