import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
# TODO: Figure out maya < 2025 and >= 2025 support
#from shiboken2 import wrapInstance
#from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from shiboken6 import wrapInstance
from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial  # optional, for passing args during signal function calls
import sys
import pathlib

class SpaceSwitcherMainToolWindow(QtWidgets.QWidget):
    """
    The main entrypoint into the tool
    """
    @staticmethod
    def openMainToolWindowInstance():
        # QtWidgets.QApplication(sys.argv)
        mayaMainWindowPtr = omui.MQtUtil.mainWindow()
        mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
        window = SpaceSwitcherMainToolWindow(parent=mayaMainWindow)
        window.setWindowTitle('Space Switcher')
        window.show()

    def __init__(self, parent=None):
        """
        Initialize class.
        """
        super(SpaceSwitcherMainToolWindow, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widgetPath = str(pathlib.Path(__file__).parent.resolve())
        print(self.widgetPath + '\\MainToolWindow.ui')  # TODO Remove
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath + '\\SpaceSwitcherMainToolWindow.ui')
        self.widget.setParent(self)
        # set initial window sizes
        self.resize(640, 480)
        # locate UI widgets
        self.btn_create = self.widget.findChild(QtWidgets.QPushButton, 'btn_create')
        self.btn_create.clicked.connect(self.create)
        self.btn_wipe = self.widget.findChild(QtWidgets.QPushButton, 'btn_wipe')
        # self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')
        # # assign functionality to buttons
        # self.btn_close.clicked.connect(self.close)

    """
    Your code goes here
    """

    def create(selfself):
        pass

    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())

    def closeWindow(self):
        """
        Close window.
        """
        print('closing window')
        self.destroy()
