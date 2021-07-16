# Main Cool Source Code!
# Licensed under MIT.

# - Modules - #
import sys
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

# - Main Code - #
arguments = sys.argv # Get arguments

if arguments[1] == "https":
  print('Https enabled.')
  print('Connecting to site: ' + arguments[2])
  # Create a main window class
  # Create a main window class
  class MainWindow(QMainWindow):
    # Constructor of this class
    def __init__(self):
        super(MainWindow, self).__init__()
        # To provide a widget for viewing and editing web documents:
        self.browser = QWebEngineView()
        # To set default browser homepage as google homepage:
        self.browser.setUrl(QUrl(arguments[2]))
        # To set browser as central widget of main window:
        self.setCentralWidget(self.browser)
        # To open browser in a maximized window:
        self.showMaximized()
print('Cool v1')
