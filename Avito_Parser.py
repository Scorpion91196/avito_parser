import avito_parser_ui
import sys
from PyQt5 import QtCore, QtWidgets
from video_cards import start_video_cards_parser
from computers import start_computers_parser
from motherboards import start_motherboards_parser
from processors import start_processors_parser


class AvitoDesign(QtWidgets.QMainWindow, avito_parser_ui.Ui_Form):
    display_report_signal = QtCore.pyqtSignal(str, name='display_report_signal')
    edit_progress_bar_signal = QtCore.pyqtSignal(int, name='edit_progress_bar_signal')

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_parsing)

        self.display_report_signal.connect(self.display_report, QtCore.Qt.QueuedConnection)
        self.edit_progress_bar_signal.connect(self.edit_progress_bar, QtCore.Qt.QueuedConnection)

    def start_parsing(self):
        if self.radioButton.isChecked():
            start_video_cards_parser(self.display_report_signal,
                                     self.edit_progress_bar_signal,
                                     self.searchInput.toPlainText()
                                     )
        if self.radioButton_2.isChecked():
            start_motherboards_parser(self.display_report_signal,
                                      self.edit_progress_bar_signal,
                                      self.searchInput.toPlainText()
                                      )
        if self.radioButton_3.isChecked():
            start_processors_parser(self.display_report_signal,
                                    self.edit_progress_bar_signal,
                                    self.searchInput.toPlainText()
                                    )
        if self.radioButton_4.isChecked():
            start_computers_parser(self.display_report_signal,
                                   self.edit_progress_bar_signal,
                                   self.searchInput.toPlainText()
                                   )

    def edit_progress_bar(self, data):
        self.progressBar.setValue(data)

    def display_report(self, data):  # Вызывается для обработки сигнала
        self.Programm_notification.appendPlainText(data)


def main():

    # Объявляем количество потоков

    app = QtWidgets.QApplication(sys.argv)
    window = AvitoDesign()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
