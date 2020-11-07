from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLabel
from UI.selector_response import Ui_response_selector


class ResponseSelectorDialog(QDialog):
    """Response selector dialog."""
    def __init__(self, parent=None, data=None, questions=None, selected_responses=None):
        super().__init__(parent)
        self.selected_responses = selected_responses
        self.data = data
        if questions is None:
            questions = self.data.columns.to_list()
        self.questions = questions
        self.data_dict = self.data_to_dict()
        self.form_rows = {}
        # Create an instance of the GUI
        self.ui = Ui_response_selector()
        self.ui.setupUi(self)
        self.populate_form_layout()
        self.ui.buttonBox.accepted.connect(self.on_click_ok)

    def data_to_dict(self):
        return {key: list(self.data.loc[:, key].astype(str).unique()) for key in self.questions}

    def populate_form_layout(self):
        for row, items in enumerate(self.data_dict.items()):
            question, responses = items
            question_label = QLabel(question)
            question_label.setObjectName(question)
            question_label.setWordWrap(True)
            response_box = QComboBox()
            response_box.setObjectName(question)
            response_box.setEditable(True)
            response_box.addItems(responses)
            response_box.setCurrentText("Select/enter valid response...")
            response_box.setInsertPolicy(QComboBox.InsertAtTop)
            response_box.setCurrentIndex(-1)
            self.ui.formLayout.addRow(QLabel(question), response_box)
            self.form_rows[row] = {"QuestionLabel": question_label, "ResponseBox": response_box}

    def on_click_ok(self):
        responses_dict = {}
        for row, items in self.form_rows.items():
            question_label = items['QuestionLabel']
            response_box = items['ResponseBox']
            responses_dict[question_label.text()] = response_box.currentText()
        self.selected_responses = responses_dict

