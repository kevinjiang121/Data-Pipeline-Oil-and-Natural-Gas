import sys
from UIWindow import UIWindow
from PyQt6 import QtWidgets, uic
app = QtWidgets.QApplication(sys.argv)

def main():
    window = UIWindow()
    app.exec()

if __name__ == "__main__":
    main()
