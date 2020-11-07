from pathlib import Path

import pandas as pd
from PyQt5 import QtGui
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import Qt
from numpy import bool_

COLORS = ['#101010', '#a1d76a', '#e9a3c9', '#a1a3c9']
DATE_COLORS = {'header': '#d0d7d0', 'values': 'afd7af'}
TOTAL_COLUMN = 'Total valid responses'
DATE_NAME = '-Sorting Date'


class PandasModel(QAbstractTableModel):

    def __init__(self, file_path=None, dataframe=None):
        QAbstractTableModel.__init__(self)
        self.path = None if file_path is None else Path(file_path).absolute()
        self.headers = None
        self._data = None
        self.date_set = False
        if dataframe is not None:
            self._data = dataframe
            self.head = True
        else:
            self._data = self.load_file()
            self.head = PandasModel(dataframe=self._data.loc[:5, :].copy())

    def load_file(self):
        if self.path.is_file():
            return pd.read_csv(self.path, header=None)
        return None

    def save_file(self, path):
        self._data.to_csv(path)

    def reset_data(self):
        self.beginResetModel()
        self.headers = None
        self.date_set = False
        self._data = self.load_file()
        self.endResetModel()

    def get_column_header_value(self, column_index):
        return str(self._data.columns[column_index])

    def get_data(self):
        return self._data

    def select_columns(self, columns):
        remove_columns = [column
                          for column_index, column in enumerate(self.get_headers())  # self._data.columns)
                          if column not in columns]
        self.removeColumn(remove_columns, )

    def set_index(self, index=None, index_value=None):
        if index is not None:
            index_value = self.get_column_header_value(column_index=index)
        if index_value:
            self.beginResetModel()
            self._data = self._data.reset_index().set_index(index_value)
            self.endResetModel()
            return self._data.index.to_list()
            # self.setHeaderData(section=orientation=Qt.Vertical)

    def set_dates(self, index):
        self.beginResetModel()
        dates_header = self.reset_header_index(header_index=index, rename=DATE_NAME)
        self._data.iloc[:, 0] = pd.to_datetime(self._data.iloc[:, 0])
        self.date_set = True
        self.endResetModel()
        return dates_header

    def get_headers(self):
        headers = self._data.columns.to_list()
        if self.date_set:
            headers.pop(0)
        return headers

    def set_headers(self, header_index):
        self.beginResetModel()
        self._data.columns = self._data.iloc[header_index, :]
        self.removeRow(header_index)
        self.endResetModel()
        return self.get_headers()

    def reset_header_index(self, header_index, new_header_index=0, rename=''):
        column_header = self.get_column_header_value(column_index=header_index)
        column = self._data.pop(column_header)
        self._data.insert(new_header_index, column.name + rename, column)
        return column_header

    @staticmethod
    def validate_column(column, correct_response):
        return pd.Series(column == correct_response, index=column.index, name=f'{column.name}-validity')

    def validate_columns(self, questions_responses):
        raw_columns = []
        validation_columns = []
        for column, response in questions_responses.items():
            raw_columns.append(self._data[column])
            validation_columns.append(self.validate_column(self._data[column], response))
        validation_df = pd.concat(validation_columns, axis=1)
        validation_total = validation_df.sum(axis=1)
        validation_total.name = TOTAL_COLUMN
        leading_columns = [validation_total]
        if self.date_set:
            date_column = self._data.iloc[:, 0]
            leading_columns.insert(0, date_column)
        final_data = leading_columns + validation_columns + raw_columns
        self._data = pd.concat(final_data, axis=1)

    def removeColumn(self, columns, **kwargs):
        if not isinstance(columns, list):
            columns = [columns]
        self._drop_data(columns=columns)

    def removeRow(self, rows, **kwargs):
        if not isinstance(rows, list):
            rows = [rows]
        # rows = [self._data.index[row] for row in rows]
        self._drop_data(rows=rows)

    def _drop_data(self, columns=None, rows=None):
        self._data = self._data.drop(index=rows, columns=columns)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        if role == Qt.BackgroundRole:
            value = self._data.iloc[index.row(), index.column()]
            column = self.get_column_header_value(column_index=index.column())
            column_type = self._data.iloc[:, index.column()].dtype
            if column == TOTAL_COLUMN:
                if value == self._data[TOTAL_COLUMN].max():
                    return QtGui.QColor(COLORS[1])
                elif value > 0:
                    return QtGui.QColor(COLORS[3])
                else:
                    return QtGui.QColor(COLORS[2])
            elif DATE_NAME in column and self.date_set:
                return QtGui.QColor(COLORS[3])
            elif column_type == bool:
                if value:
                    return QtGui.QColor(COLORS[1])
                else:
                    return QtGui.QColor(COLORS[2])
        if role == Qt.TextColorRole:
            column = self.get_column_header_value(column_index=index.column())
            column_type = self._data.iloc[:, index.column()].dtype
            if column in TOTAL_COLUMN or column_type == bool or (DATE_NAME in column and self.date_set):
                return QtGui.QColor(COLORS[0])

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                try:
                    return self.get_column_header_value(column_index=section)
                except IndexError:
                    pass

            if orientation == Qt.Vertical:
                try:
                    return str(self._data.index[section])
                except IndexError:
                    pass

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        try:
            self.layoutAboutToBeChanged.emit()
            na_position = ['first', 'last'][order]
            self._data = self._data.sort_values(self._data.columns[Ncol], ascending=not order, na_position=na_position)
            self.layoutChanged.emit()
        except Exception as e:
            print(e)
