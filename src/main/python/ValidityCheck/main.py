# PyInstaller command line:
# python -m PyInstaller --clean --win-private-assemblies --noconsole -F main.py
import json
import sys
from datetime import datetime
from pathlib import Path

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from Column_Select import ColumnSelectorDialog
from PandasModel import PandasModel
from Question_Select import QuestionSelectorDialog
from Response_Select import ResponseSelectorDialog
from Row_Select import RowSelectorDialog
from UI.main_window import Ui_MainWindow
from UI.about import Ui_About

ORGANIZATION_NAME = 'imnotamember'
ORGANIZATION_DOMAIN = 'imnotamember.github.io'
APPLICATION_NAME = 'Validity Check'
RECENT_FILE_PATH = 'recentFiles/path'
RECENT_DATA_FILES = 'recentFiles/data'
RECENT_VALIDITY_SETTINGS_FILES = 'recentFiles/validitySettings'
RECENT_FILES_TYPES = {'data': RECENT_DATA_FILES, 'validity_settings': RECENT_VALIDITY_SETTINGS_FILES}
FILE_TYPES = {
        'data'             : {
                'title'    : 'Data',
                'extension': 'Data Files (*.csv)'},
        'validity_settings': {
                'title'    : 'Validity Settings',
                'extension': 'Validity Settings Files (*.json)'}}
DEFAULT_PATH = str(Path().home())


class ValidityCheckWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set default values
        self.model = None

        # Set default values for validity settings.
        self.validity_settings_date = datetime.now().isoformat()
        self.drop_rows = []
        self.headers = None
        self.headers_index = None
        self.subjects = None
        self.subjects_index = None
        self.dates = None
        self.dates_index = None
        self.validity_questions = None
        self.validity_questions_responses = None

        # Set list of widgets to reset to disabled whenever opening a new data file or clearing all options.
        self._widgets_disable = {
                'group_boxes'     : [self.ui.settingsGroupBox],
                'sections'        : [self.ui.validitySaveExport],
                'labels'          : [],
                'buttons'         : [],
                'recent_files'    : [self.ui.openSettingsFileFrame],
                # 'recent_files'    : [self.ui.openRecentDataFileButton, self.ui.openRecentValiditySettingsFileButton],
                'settings_buttons': [
                        self.ui.open_remove_rows,
                        self.ui.skipRemoveRows,
                        self.ui.open_header_select,
                        self.ui.open_subject_select,
                        self.ui.open_date_select,
                        self.ui.skipDateSelect,
                        self.ui.open_question_select,
                        self.ui.open_response_select]}
        self._widgets_reset = {
                'labels'             : [],
                'fields'             : [],
                'recent_files'       : [
                        self.ui.selectRecentDataFileComboBox,
                        self.ui.selectRecentValiditySettingsFileComboBox],
                'settings_checkboxes': [
                        self.ui.removeRowsCheckBox,
                        self.ui.headersCheckBox,
                        self.ui.subjectCheckBox,
                        self.ui.dateCheckBox,
                        self.ui.questionsCheckBox,
                        self.ui.responsesCheckBox]}
        # Get settings
        self.settings = QSettings()
        try:
            self.recent_file_path = self.settings.value(RECENT_FILE_PATH, DEFAULT_PATH, 'QString')
            self.recent_data_files = self.settings.value(RECENT_DATA_FILES, [], 'QStringList')
            self.recent_validity_settings_files = self.settings.value(RECENT_VALIDITY_SETTINGS_FILES, [], 'QStringList')
        except TypeError as e:
            print(e)
            self.recent_file_path = str(self.settings.value(RECENT_FILE_PATH, DEFAULT_PATH))
            self.recent_data_files = list(self.settings.value(RECENT_DATA_FILES, []))
            self.recent_validity_settings_files = list(self.settings.value(RECENT_VALIDITY_SETTINGS_FILES, []))
        self.recent_data_files = self.update_recent_files(
                combobox=self.ui.selectRecentDataFileComboBox,
                recent_files=self.recent_data_files)
        self.recent_validity_settings_files = self.update_recent_files(
                combobox=self.ui.selectRecentValiditySettingsFileComboBox,
                recent_files=self.recent_validity_settings_files)

        self.ui.actionClearSettingsData.triggered.connect(self.clear_all)
        self.ui.actionClearRecentFiles.triggered.connect(self.clear_recent_files)
        self.ui.actionAbout.triggered.connect(self.about_dialog)
        self.ui.openDataFileButton.clicked.connect(self.open_data_file)
        self.ui.openValiditySettingsFileButton.clicked.connect(self.open_validity_settings_file)
        self.ui.selectRecentDataFileComboBox \
            .currentIndexChanged \
            .connect(self.check_recent_data_selection)
        self.ui.selectRecentValiditySettingsFileComboBox \
            .currentIndexChanged \
            .connect(self.check_recent_validity_settings_selection)
        self.ui.openRecentDataFileButton \
            .clicked \
            .connect(self.open_recent_data_file)
        self.ui.openRecentValiditySettingsFileButton \
            .clicked \
            .connect(self.open_recent_validity_settings_file)

        self.ui.open_remove_rows.clicked.connect(self.drop_row_dialog)
        self.ui.skipRemoveRows.clicked.connect(self.show_header_select)
        self.ui.open_header_select.clicked.connect(self.header_dialog)
        self.ui.open_subject_select.clicked.connect(self.subject_dialog)
        self.ui.open_date_select.clicked.connect(self.date_dialog)
        self.ui.skipDateSelect.clicked.connect(self.show_questions_select)
        self.ui.open_question_select.clicked.connect(self.question_dialog)
        self.ui.open_response_select.clicked.connect(self.response_dialog)
        self.ui.clearSettings.clicked.connect(self.reset_settings)
        self.ui.saveSettingsButton.clicked.connect(self.save_validity_settings_file)
        self.ui.exportValidityReportButton.clicked.connect(self.save_validity_report)

    # define protected methods which abstract away from data/settings files
    def _add_recent_file(self, combobox, file_path, recent_files, recent_files_type):
        """
        Generic method to add a new file to the list of recent files for *data* files or *validity settings* files.
         New file is inserted at the start of the `recent_files` list, then calling `self.update_recent_files` with the
         combobox, file path, and recent files' list to perform the updates. Finally, a call to `self._update_settings`
         will update the recent files list in the apps system-wide settings (pyqt5.QtCore.QSettings).
        :param combobox:  pyqt5.Qt.Combobox, the combobox being updated with the new file.
        :param file_path: str, absolute path to the file being added to the recent files list.
        :param recent_files: list, recently used files' absolute paths where the new file path is added.
        :param recent_files_type: str, ('data' or 'validity_settings')
        """
        recent_files.insert(0, file_path)
        recent_files = list(set(recent_files))
        self.update_recent_files(combobox, file_path, recent_files)
        self._update_settings(file_path, recent_files_type, recent_files)

    @staticmethod
    def _check_iter(_item):
        """
        Check if `_item` is iterable. If not, convert to a single-item tuple.
        :param _item:
        :return: iterable variable (list, tuple, set) or single-item tuple.
        """
        if type(_item) not in (list, tuple, set):
            return (_item,)
        return _item

    @staticmethod
    def _check_recent(file_path=None, file_list=None):
        """
        Check if file path(s) (either individually as `file_path` or as a list in `file_list`) are linked to an actual
         file or if orphaned.
        :param file_path:
        :param file_list:
        :return:
        """
        if file_path is not None and not Path(file_path).is_file():
            file_path = None
        if file_list is not None:
            file_list = [_file_path for _file_path in file_list if Path(_file_path).is_file()]
            file_list = list(set(file_list))
        return file_path, file_list

    @staticmethod
    def _check_selection_and_button(combobox, button):
        button_is_disabled = combobox.currentIndex() < 0
        button.setDisabled(button_is_disabled)

    @staticmethod
    def _reset_combobox(combobox):
        combobox.setCurrentIndex(-1)

    def _toggle_settings(self, disable=None, check_box=None, enable=None, uncheck_box=None):
        for group, _disable in ((disable, True), (enable, False)):
            if group is not None:
                group = self._check_iter(group)
                [button.setDisabled(_disable) for button in group]
        for boxes, state in ((check_box, Qt.Checked), (uncheck_box, Qt.Unchecked)):
            if boxes is not None:
                boxes = self._check_iter(boxes)
                [box.setCheckState(state) for box in boxes]

    def _update_settings(self, file_path=None, recent_files_type=None, recent_files=None):
        if file_path is not None:
            self.settings.setValue(RECENT_FILE_PATH, file_path)
        if None not in (recent_files_type, recent_files):
            self.settings.setValue(RECENT_FILES_TYPES[recent_files_type], recent_files)
        self.settings.sync()

    def update_recent_files(self, combobox, file_path=None, recent_files=None):
        file_path, recent_files = self._check_recent(file_path=file_path, file_list=recent_files)
        if file_path is None:
            if recent_files:
                combobox.addItems(recent_files)
            else:
                combobox.clear()
            self._reset_combobox(combobox=combobox)
        else:
            combobox.setCurrentText(file_path)
        return recent_files

    def add_recent_data_file(self, file_path):
        self._add_recent_file(combobox=self.ui.selectRecentDataFileComboBox,
                              file_path=file_path,
                              recent_files=self.recent_data_files,
                              recent_files_type='data')
        self.ui.selectRecentDataFileComboBox.update()

    def add_recent_validity_settings_file(self, file_path):
        self._add_recent_file(combobox=self.ui.selectRecentValiditySettingsFileComboBox,
                              file_path=file_path,
                              recent_files=self.recent_validity_settings_files,
                              recent_files_type='validity_settings')
        self.ui.selectRecentValiditySettingsFileComboBox.update()

    def check_recent_selections(self):
        self.check_recent_data_selection()
        self.check_recent_validity_settings_selection()

    def check_recent_data_selection(self):
        self._check_selection_and_button(combobox=self.ui.selectRecentDataFileComboBox,
                                         button=self.ui.openRecentDataFileButton)

    def check_recent_validity_settings_selection(self):
        self._check_selection_and_button(combobox=self.ui.selectRecentValiditySettingsFileComboBox,
                                         button=self.ui.openRecentValiditySettingsFileButton)

    def open_file_dialog(self, file_type):
        return \
            QFileDialog.getOpenFileName(self, f'Open {FILE_TYPES[file_type]["title"]} file',
                                        self.recent_file_path, FILE_TYPES[file_type]["extension"])[0]

    def save_file_dialog(self, file_type):
        return \
            QFileDialog.getSaveFileName(self, f'Save {FILE_TYPES[file_type]["title"]} file',
                                        self.recent_file_path, FILE_TYPES[file_type]["extension"])[0]

    def open_data_file(self, _checked=None, path=None):
        path = self.try_path(path=path, file_type='data')
        if path is None:
            return
        self.clear_all()
        self.set_tables(path)
        self.add_recent_data_file(path)
        self.ui.data_file_location_label.setText(path)
        self.ui.openSettingsFileFrame.setDisabled(False)
        self.show_remove_rows_select()

    def open_validity_settings_file(self, _checked=None, path=None):
        path = self.try_path(path=path, file_type='validity_settings')
        if path is None:
            return
        with open(path, 'r') as f:
            validity_settings = json.load(f)
        self.reset_settings()
        self.validity_settings_date = validity_settings['date_created']
        self.drop_rows = validity_settings['drop_rows']
        self.subjects = validity_settings['subjects']
        self.subjects_index = validity_settings['subjects_index']
        self.headers = validity_settings['headers']
        self.headers_index = validity_settings['headers_index']
        self.dates = validity_settings['dates']
        self.dates_index = validity_settings['dates_index']
        self.validity_questions = validity_settings['validity_questions']
        self.validity_questions_responses = validity_settings['validity_questions_responses']
        if self.drop_rows:
            self.model.removeRow(self.drop_rows)
        if self.headers_index is not None:
            self.set_data_headers(headers_index=self.headers_index)
        if self.subjects_index is not None:
            self.set_data_subjects(subjects_index=self.subjects_index)
        if self.dates_index is not None:
            self.set_data_dates(dates_index=self.dates_index)
        if self.validity_questions is not None:
            self.model.select_columns(columns=self.validity_questions)
        if self.validity_questions_responses is not None:
            self.model.validate_columns(self.validity_questions_responses)
        self.ui.validity_settings_file_location_label.setText(path)
        self.add_recent_validity_settings_file(path)
        self.show_export()
        self.ui.centralWidget.update()
        # for checkbox in self._widgets_reset['settings_checkboxes']:
        #     checkbox.setChecked(True)
        self.hide_all_select()

    def open_recent_data_file(self):
        path = self.ui.selectRecentDataFileComboBox.currentText()
        if path is None:
            return
        self.open_data_file(path=path)

    def open_recent_validity_settings_file(self):
        path = self.ui.selectRecentValiditySettingsFileComboBox.currentText()
        if path is None:
            return
        self.open_validity_settings_file(path=path)

    def save_validity_report(self):
        path = self.try_path(file_type='data', file_dialog='save')
        if path is None:
            return
        self.model.save_file(path)
        self._update_settings(file_path=path)

    def save_validity_settings_file(self, _checked=None):
        path = self.try_path(file_type='validity_settings', file_dialog='save')
        if path is None:
            return
        validity_settings = {
                'date_created'                : datetime.now().isoformat(),
                'drop_rows'                   : self.drop_rows,
                'subjects'                    : self.subjects,
                'subjects_index'              : self.subjects_index,
                'headers'                     : self.headers,
                'headers_index'               : self.headers_index,
                'dates'                       : self.dates,
                'dates_index'                 : self.dates_index,
                'validity_questions'          : self.validity_questions,
                'validity_questions_responses': self.validity_questions_responses}
        self.save_validity_settings(path=path, validity_settings=validity_settings)
        self.add_recent_validity_settings_file(file_path=path)

    @staticmethod
    def save_validity_settings(path, validity_settings):
        with open(path, 'w') as f:
            json.dump(validity_settings, f)

    def set_data_headers(self, headers_index=None):
        self.headers_index = headers_index
        if headers_index is not None:
            self.headers = self.model.set_headers(header_index=headers_index)
        if self.headers is None:
            self.headers = self.model.headerData(orientation=Qt.Horizontal)

    def set_data_subjects(self, subjects_index=None):
        self.subjects_index = subjects_index
        if subjects_index is not None:
            self.subjects = self.model.set_index(index=subjects_index)
        if self.subjects is None:
            self.subjects = self.model.headerData(orientation=Qt.Vertical)

    def set_data_dates(self, dates_index=None):
        self.dates_index = dates_index
        if dates_index is not None:
            self.dates = self.model.set_dates(index=dates_index)

    def set_tables(self, path):
        self.model = PandasModel(file_path=path)
        self.ui.rawTableView.setModel(self.model.head)
        self.ui.validityReportTableView.setModel(self.model)

    def try_path(self, file_type, path=None, file_dialog='open'):
        if path is not None:
            return path
        if file_dialog == 'open':
            path = self.open_file_dialog(file_type=file_type)
        elif file_dialog == 'save':
            path = self.save_file_dialog(file_type=file_type)
        if path == '':
            return None
        else:
            return path

    def clear_all(self):
        # Set default values
        self.model = None
        self.ui.rawTableView.setModel(None)
        self.ui.validityReportTableView.setModel(None)
        self.reset_settings()
        self.reset_file_widgets()

    def clear_recent_files(self):
        for file_type, combobox in (('data', self.ui.selectRecentDataFileComboBox),
                                    ('validity_settings', self.ui.selectRecentValiditySettingsFileComboBox)):
            self.update_recent_files(combobox=combobox, recent_files=[])
            self._update_settings(recent_files_type=file_type, recent_files=[])

    def reset_settings(self, _checked=None):
        self.drop_rows = []
        self.subjects = None
        self.subjects_index = None
        self.dates = None
        self.dates_index = None
        self.headers = None
        self.headers_index = None
        self.validity_questions = None
        self.validity_questions_responses = None
        self.validity_settings_date = datetime.now().isoformat()
        self.reset_settings_widgets()
        if self.model is not None:
            self.model.reset_data()
            self.show_remove_rows_select()

    @staticmethod
    def _disable(ui_group):
        for disabled_widget in ui_group:
            disabled_widget.setDisabled(True)

    @staticmethod
    def _reset(ui_group):
        for reset_widget in ui_group:
            reset_widget.setChecked(False)

    def reset_file_widgets(self):
        for group in ('group_boxes', 'recent_files'):
            self._disable(ui_group=self._widgets_disable[group])
        for combobox in self._widgets_reset['recent_files']:
            self._reset_combobox(combobox=combobox)
        self.check_recent_selections()
        self.ui.rawTableView.reset()
        self.ui.validityReportTableView.reset()
        self.ui.centralWidget.update()
        self.ui.centralWidget.show()

    def reset_settings_widgets(self):
        self._reset(ui_group=self._widgets_reset['settings_checkboxes'])
        self._disable(ui_group=self._widgets_disable['settings_buttons'])

    def show_data_setup(self):
        self.ui.settingsGroupBox.setDisabled(False)
        self.show_clear_settings()
        self.show_export()

    def show_remove_rows_select(self):
        self.show_data_setup()
        self._toggle_settings(enable=(self.ui.open_remove_rows, self.ui.skipRemoveRows),
                              uncheck_box=self.ui.removeRowsCheckBox)

    def show_header_select(self):
        self._toggle_settings(disable=(self.ui.open_remove_rows, self.ui.skipRemoveRows),
                              check_box=self.ui.removeRowsCheckBox,
                              enable=self.ui.open_header_select,
                              uncheck_box=self.ui.headersCheckBox)
        self.show_clear_settings()

    def show_subject_select(self):
        self._toggle_settings(disable=self.ui.open_header_select,
                              check_box=self.ui.headersCheckBox,
                              enable=self.ui.open_subject_select,
                              uncheck_box=self.ui.subjectCheckBox)

    def show_date_select(self):
        self._toggle_settings(disable=self.ui.open_subject_select,
                              check_box=self.ui.subjectCheckBox,
                              enable=(self.ui.open_date_select, self.ui.skipDateSelect),
                              uncheck_box=self.ui.dateCheckBox)

    def show_questions_select(self):
        self._toggle_settings(disable=(self.ui.open_date_select, self.ui.skipDateSelect),
                              check_box=self.ui.dateCheckBox,
                              enable=self.ui.open_question_select,
                              uncheck_box=self.ui.questionsCheckBox)

    def show_responses_select(self):
        self._toggle_settings(disable=self.ui.open_question_select,
                              check_box=self.ui.questionsCheckBox,
                              enable=self.ui.open_response_select,
                              uncheck_box=self.ui.responsesCheckBox)

    def hide_all_select(self):
        self._toggle_settings(disable=self._widgets_disable['settings_buttons'],
                              check_box=self._widgets_reset['settings_checkboxes'])

    def show_clear_settings(self):
        self._toggle_settings(enable=self.ui.clearSettings)

    def show_export(self):
        self._toggle_settings(enable=self.ui.validitySaveExport)

    def drop_row_dialog(self):
        """Launch the question selector dialog."""
        dlg = RowSelectorDialog(self, model=self.model, purpose="drop")
        dlg.exec_()
        if dlg.selected_rows is not None:
            self.model.removeRow(dlg.selected_rows)
            self.drop_rows.extend(dlg.selected_rows)
            self.show_header_select()

    def header_dialog(self):
        """Launch the question selector dialog."""
        dlg = RowSelectorDialog(self, model=self.model, purpose="header")
        dlg.exec_()
        if dlg.selected_rows is not None:
            self.set_data_headers(headers_index=dlg.selected_rows)
            self.headers_index = dlg.selected_rows
            self.show_subject_select()

    def subject_dialog(self):
        """Launch the question selector dialog."""
        dlg = ColumnSelectorDialog(self, model=self.model, purpose="subject")
        dlg.exec_()
        if dlg.selected_column is not None:
            self.set_data_subjects(subjects_index=dlg.selected_column)
            self.subjects_index = dlg.selected_column
            self.show_date_select()

    def date_dialog(self):
        """Launch the question selector dialog."""
        dlg = ColumnSelectorDialog(self, model=self.model, purpose="date")
        dlg.exec_()
        if dlg.selected_column is not None:
            self.set_data_dates(dates_index=dlg.selected_column)
            self.dates_index = dlg.selected_column
            self.show_questions_select()

    def question_dialog(self):
        """Launch the question selector dialog."""
        dlg = QuestionSelectorDialog(self, questions=self.model.get_headers())
        dlg.exec_()
        if dlg.selected_questions is not None:
            self.validity_questions = dlg.selected_questions
            self.model.select_columns(columns=self.validity_questions)
            self.show_responses_select()

    def response_dialog(self):
        """Launch the question selector dialog."""
        dlg = ResponseSelectorDialog(self, data=self.model.get_data(), questions=self.model.get_headers(),
                                     selected_responses=self.validity_questions_responses)
        dlg.exec_()
        if dlg.selected_responses is not None:
            self.validity_questions_responses = dlg.selected_responses
            self.model.validate_columns(self.validity_questions_responses)
            self.hide_all_select()

    @staticmethod
    def about_dialog():
        about_window = AboutWindow()
        about_window.exec_()


class AboutWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    qtmodern.styles.dark(appctxt.app)

    window = ValidityCheckWindow()
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()

    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
