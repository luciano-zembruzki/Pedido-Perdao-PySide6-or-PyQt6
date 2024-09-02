from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from gui.py.ui_widget import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current = 0

        self.questions = [
            {"question": "Você está brava?", "image": "question1.png"},  # noqa
            {"question": "Me Perdoa?", "image": "question2.png"},  # noqa
        ]

        self.label.setText(self.questions[self.current]["question"])

        self.pic.setPixmap(QPixmap(f"{self.questions[self.current]['image']}"))

        self.no.clicked.connect(self.no_op)
        self.yes.clicked.connect(self.yes_op)

        self.original_size = self.yes.size()

    def no_op(self):
        current_size_yes = self.yes.size()
        self.yes.setMinimumSize(
            current_size_yes.width() + 10, current_size_yes.height() + 10
        )

    def yes_op(self):
        if self.current == len(self.questions) - 1:
            self.label.setText("Te amo!")
            self.pic.setPixmap(QPixmap("end.png"))
            self.yes.hide()
            self.no.hide()
            return
        else:
            self.current += 1
            self.label.setText(self.questions[self.current]["question"])
            self.pic.setPixmap(QPixmap(f"{self.questions[self.current]['image']}"))
            self.yes.setMinimumSize(self.original_size)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
