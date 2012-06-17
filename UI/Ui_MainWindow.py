# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Documents and Settings\Null\My Documents\GitHub\UCLint\UI\MainWindow.ui'
#
# Created: Sun Jun 17 23:09:55 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(538, 527)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sourceTextEdit = QtGui.QPlainTextEdit(self.centralWidget)
        self.sourceTextEdit.setObjectName(_fromUtf8("sourceTextEdit"))
        self.gridLayout.addWidget(self.sourceTextEdit, 2, 0, 1, 4)
        self.dirSelectButton = QtGui.QPushButton(self.centralWidget)
        self.dirSelectButton.setObjectName(_fromUtf8("dirSelectButton"))
        self.gridLayout.addWidget(self.dirSelectButton, 0, 0, 1, 1)
        self.dirLabel = QtGui.QLabel(self.centralWidget)
        self.dirLabel.setMargin(2)
        self.dirLabel.setIndent(5)
        self.dirLabel.setObjectName(_fromUtf8("dirLabel"))
        self.gridLayout.addWidget(self.dirLabel, 1, 0, 1, 2)
        self.ucLintButton = QtGui.QPushButton(self.centralWidget)
        self.ucLintButton.setObjectName(_fromUtf8("ucLintButton"))
        self.gridLayout.addWidget(self.ucLintButton, 3, 0, 1, 1)
        self.saveButton = QtGui.QPushButton(self.centralWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 3, 3, 1, 1)
        self.commentscheckBox = QtGui.QCheckBox(self.centralWidget)
        self.commentscheckBox.setObjectName(_fromUtf8("commentscheckBox"))
        self.gridLayout.addWidget(self.commentscheckBox, 0, 2, 1, 1)
        self.previousButton = QtGui.QPushButton(self.centralWidget)
        self.previousButton.setEnabled(False)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.gridLayout.addWidget(self.previousButton, 1, 2, 1, 1)
        self.nextButton = QtGui.QPushButton(self.centralWidget)
        self.nextButton.setEnabled(False)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.gridLayout.addWidget(self.nextButton, 1, 3, 1, 1)
        self.fileNamelabel = QtGui.QLabel(self.centralWidget)
        self.fileNamelabel.setText(_fromUtf8(""))
        self.fileNamelabel.setObjectName(_fromUtf8("fileNamelabel"))
        self.gridLayout.addWidget(self.fileNamelabel, 3, 1, 1, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menu_File.addAction(self.action_Quit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "UCLint", None, QtGui.QApplication.UnicodeUTF8))
        self.dirSelectButton.setText(QtGui.QApplication.translate("MainWindow", "Choose Project Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.dirLabel.setText(QtGui.QApplication.translate("MainWindow", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.ucLintButton.setText(QtGui.QApplication.translate("MainWindow", "UCLint", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.commentscheckBox.setText(QtGui.QApplication.translate("MainWindow", "Delete Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Previuos File", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("MainWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Next File", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

