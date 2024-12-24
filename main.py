import sys
from src.views.book_view import BookView
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = BookView()
    view.show()

    sys.exit(app.exec_()) 