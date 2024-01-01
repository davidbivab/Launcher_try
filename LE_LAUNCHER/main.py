from test_window import Ui_MainWindow
import sys
from PySide6.QtWidgets import QMainWindow,QApplication
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec())