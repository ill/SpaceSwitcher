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
        window = SpaceSwitcherMainToolWindow(parent = mayaMainWindow)
        window.setWindowTitle('Space Switcher')
        window.show()

    def __init__(self, parent=None):
        """
        Initialize class.
        """
        super(SpaceSwitcherMainToolWindow, self).__init__(parent = parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widgetPath = str(pathlib.Path(__file__).parent.resolve())
        print(self.widgetPath + '\\MainToolWindow.ui')  # TODO Remove
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath + '\\SpaceSwitcherMainToolWindow.ui')
        self.widget.setParent(self)
        # set initial window sizes
        self.resize(640, 480)
        # locate UI widgets
        self.btn_refreshSelection = self.widget.findChild(QtWidgets.QPushButton, 'btn_refreshSelection')
        self.btn_refreshSelection.clicked.connect(self.onRefreshSelectionPressed)
        self.btn_create = self.widget.findChild(QtWidgets.QPushButton, 'btn_create')
        self.btn_create.clicked.connect(self.createPressed)
        self.btn_wipe = self.widget.findChild(QtWidgets.QPushButton, 'btn_wipe')
        # self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')
        # # assign functionality to buttons
        # self.btn_close.clicked.connect(self.close)

    """
    Your code goes here
    """

    def onRefreshSelectionPressed(self):
        print("REFRESH")
        # Find the last selected transform object
        selectedTransform = cmds.ls(selection=True, transforms=True, tail = 1)
        self.onRefreshFocusedTransform(selectedTransform[0]
                                       if len(selectedTransform) > 0
                                       else None)

    def onRefreshFocusedTransform(self, focusedTransform):
        self.focusedTransform = focusedTransform

        print(self.focusedTransform)

        # Check if the selected object has a SpaceSwitcher node already connected to the Offset Parent Matrix

        if self.focusedTransform is not None:
            pass
        else:
            pass

    def createPressed(self):

        print("CREATE")

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
