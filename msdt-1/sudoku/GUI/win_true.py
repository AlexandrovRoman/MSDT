from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QDialog,
    QPushButton,
    QLabel,
    QLineEdit,
)
from PyQt5 import QtCore


class UiDialog(object):
    def setup_ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(201, 152)
        verticalLayoutWidget = QWidget(Form)
        verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 151))
        verticalLayout = QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        Form.setWindowTitle("Form", "Победа!")
        congratulation_to_win = QLabel(verticalLayoutWidget)
        congratulation_to_win.setMaximumSize(QtCore.QSize(250, 50))
        congratulation_to_win.setAlignment(QtCore.Qt.AlignCenter)
        congratulation_to_win.setText("Поздравляем с победой.\n Ваше время:")
        verticalLayout.addWidget(congratulation_to_win)
        input_your_name = QLabel(verticalLayoutWidget)
        input_your_name.setMaximumSize(QtCore.QSize(200, 30))
        input_your_name.setAlignment(QtCore.Qt.AlignCenter)
        input_your_name.setText("Введите ваше имя:")
        verticalLayout.addWidget(input_your_name)
        self.name = QLineEdit(verticalLayoutWidget)
        self.name.setMaximumSize(QtCore.QSize(200, 16777215))
        verticalLayout.addWidget(self.name)
        self.ok = QPushButton(verticalLayoutWidget)
        self.ok.setMaximumSize(QtCore.QSize(200, 80))
        self.ok.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ok.setText("Ok")
        verticalLayout.addWidget(self.ok)

        QtCore.QMetaObject.connectSlotsByName(Form)


class WinDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.nick = None
        self.ui = UiDialog()
        self.ui.setup_ui(self)
        self.ui.ok.clicked.connect(self.on_click)

    def on_click(self):
        """В случае если пользователь ввел ник - закрываем окно"""
        self.nick = self.ui.name.text()
        if self.nick:
            self.accept()
