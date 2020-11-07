from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from UI.selector_row import Ui_row_selector as UI


class RowSelectorDialog(QDialog):
    """Header selector dialog."""
    def __init__(self, parent=None, model=None, purpose="drop"):
        super().__init__(parent)
        self.selected_rows = None
        # Create an instance of the GUI
        self.purpose = purpose
        if purpose == "drop":
            title_text = "Select row to delete..."
            instruction_text = "Select the row you would like to delete:"
            selection_mode = QtWidgets.QAbstractItemView.MultiSelection
        elif purpose == "header":
            title_text = "Select header row..."
            instruction_text = "Select the row containing your header labels:"
            selection_mode = QtWidgets.QAbstractItemView.SingleSelection
        else:
            return
        self.ui = UI()
        self.ui.setupUi(self)
        self.setWindowTitle(title_text)
        self.ui.label.setText(instruction_text)
        self.ui.tableView.setModel(model)
        self.ui.tableView.setSelectionMode(selection_mode)
        self.ui.buttonBox.accepted.connect(self.on_click_ok)

    def on_click_ok(self):
        self.selected_rows = [row.row() for row in self.ui.tableView.selectionModel().selectedRows()]
        if self.purpose == 'header':
            self.selected_rows = self.selected_rows[0]
        return self.selected_rows
