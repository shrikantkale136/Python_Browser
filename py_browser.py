import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('E:/PythonProjects/Python_Browser/assets/chrome.png')) 
        self.setWindowTitle("My Chrome") # set the title
        self.setIconSize(QSize(23,23)) 
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        navbar.setIconSize(QSize(26,26))
        navbar.setMovable(False)
        self.addToolBar(navbar) 

        back_btn = QAction(QIcon('E:/PythonProjects/Python_Browser/assets/previous.png'),'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        navbar.addSeparator()
        
        forward_btn = QAction(QIcon('E:/PythonProjects/Python_Browser/assets/next.png'),'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        navbar.addSeparator()
        
        reload_btn = QAction(QIcon('E:/PythonProjects/Python_Browser/assets/reload.png'),'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        navbar.addSeparator()
        
        home_btn = QAction(QIcon('E:/PythonProjects/Python_Browser/assets/home.png'),'Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        navbar.addSeparator()
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()