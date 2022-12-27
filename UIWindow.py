from PyQt6 import QtWidgets, uic
from WebScrape import WebScrape as Ws
from LoadDatabase import LoadDatabase as ld
import os
import sys


class UIWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UIWindow, self).__init__()
        uic.loadUi('UIWindow.ui', self)
        self.show()
        self.extract_Btn = self.layout().itemAt(0).widget().findChild(QtWidgets.QPushButton, 'Extract')
        self.transform_Btn = self.layout().itemAt(0).widget().findChild(QtWidgets.QPushButton, 'Transform')
        self.load_Btn = self.layout().itemAt(0).widget().findChild(QtWidgets.QPushButton, 'Load')
        self.extract_Btn.clicked.connect(lambda: self.extract())
        self.transform_Btn.clicked.connect(lambda: self.transform())
        self.load_Btn.clicked.connect(lambda: self.load())

    def extract(self):
        self.path = ''
        self.path = input("Enter CSV path location: ")
        self.path = r'' + self.path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        dates = Ws.date_list(12, 2016, 1, 2019)

        # puts all data into a dataframe then converts it to a CSV
        df_all_data = Ws.scrape_site(dates, self.path)
        df_all_data.to_csv(self.path + '\\df_all_data.csv')
    def transform(self):
        print("transform")
    def load(self):
        uic.loadUi('LoadDatabaseWindow.ui', self)