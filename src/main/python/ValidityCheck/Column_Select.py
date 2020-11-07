from PyQt5.QtWidgets import QDialog
from UI.selector_column import Ui_column_selector as UI


class ColumnSelectorDialog(QDialog):
    """Header selector dialog."""
    def __init__(self, parent=None, model=None, purpose="date"):
        super().__init__(parent)
        self.selected_column = None
        # Create an instance of the GUI
        if purpose == "date":
            title_text = "Select date column..."
            instruction_text = "Select the column with date or time (for sorting):"
        elif purpose == "subject":
            title_text = "Select subject ID column..."
            instruction_text = "Select the column containing your subject ID's:"
        else:
            return
        self.ui = UI()
        self.ui.setupUi(self)
        self.setWindowTitle(title_text)
        self.ui.label.setText(instruction_text)
        self.ui.tableView.setModel(model)
        self.ui.buttonBox.accepted.connect(self.on_click_ok)

    def on_click_ok(self):
        self.selected_column = self.ui.tableView.selectionModel().selectedColumns()[0].column()
