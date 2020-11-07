from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QListWidgetItem
from UI.selector_question import Ui_question_selector


class QuestionSelectorDialog(QDialog):
    """Question selector dialog."""
    def __init__(self, parent=None, questions=None):
        super().__init__(parent)
        self.selected_questions = None
        self.questions = [QListWidgetItem(question) for question in questions]
        # Create an instance of the GUI
        self.ui = Ui_question_selector()
        self.ui.setupUi(self)
        self.load_questions()
        self.ui.buttonBox.accepted.connect(self.on_click_ok)

    def load_questions(self):
        for question in self.questions:
            self.ui.listWidget.addItem(question)

    def on_click_ok(self):
        self.selected_questions = [item.text() for item in self.ui.listWidget.selectedItems()]
