#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unreal Script Sanitizer

Main Python 
"""

import re
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, SIGNAL, QUrl
from PyQt4.QtGui import QApplication,  QFileDialog,  QPlainTextEdit, QStatusBar, QFileSystemModel,  QMessageBox
from UI.Ui_MainWindow import Ui_MainWindow

__author__ = "Hamed Nemati"
__copyright__ = "Copyright 2012, Hamed Nemati Ziabari"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "hitech.innovative@gmail.com"
__status__ = "Development"

class UCLint():
    """
    Class implementing a sanitizer for unreal script.
    """
    def __init__(self):
        import  sys
        self.lastWasIf = False
        self._level = 0
        self._outText = ''
        self.dir = ''
        self.isInComment = False
        self.file_names = []
        self.files = []
        self.file_index = -1
        
        app = QtGui.QApplication(sys.argv)
        self.window = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.sourceTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        
        QObject.connect(self.ui.ucLintButton, SIGNAL('clicked()'), self.on_lint_clicked)
        QObject.connect(self.ui.dirSelectButton, SIGNAL('clicked()'), self.on_dir_select_clicked)
        QObject.connect(self.ui.nextButton, SIGNAL('clicked()'), self.on_next_clicked)
        QObject.connect(self.ui.previousButton, SIGNAL('clicked()'), self.on_previous_clicked)
        self.ui.actAbout.triggered.connect(self.about)
                
        self.window.show()
        sys.exit(app.exec_())
    
    def stip_comments(self, line):
        """
        """
        rs = re.search('^(//).*', line)
        if (rs):
            grouped = rs.group()
            if (grouped):                
                line = line.replace(grouped, '')
                return line
        else:
            return line
        #   return None
        
    def fixWhiteSpaces(self, contents):
        """
        """
        out = ''
        matchs = re.search('(}{1})(\s*?)(\n+)(\s*?)else(\s*)({{1})', contents, re.DOTALL|re.I|re.MULTILINE)
        if not matchs:
            self._outText = contents
            return
        part1 = contents[0:matchs.start()]
        part2 = contents[matchs.end():]
        out += (part1 + '} else {' + part2)
        self.fixWhiteSpaces(out)
    
    def fixIndents(self, line):
        """
        """
        line = line.strip()
        tabs = ''
        tabs += '\t' * self._level
        line = tabs + line
        return line
        
    def lint(self, fileName):        
        try:
            f = open(fileName,  'r')
            contents =''            
            for line in f:            
                contents += line
            self.fixWhiteSpaces(contents)
            f.close()

            contents = ''
            lines = self._outText.split('\n')
            for line in lines:
                line = line.strip()
                if (self.ui.commentscheckBox.isChecked()):
                    if (line != ''):
                        striped_comment = self.stip_comments(line)
                        line = striped_comment
                        if (line == ''):
                            continue
                                        
                matchs = re.search('^(/\*)(.*)', line, re.DOTALL)
                if matchs:
                    self.isInComment = True
                    
                matchs = re.search('(.*)(\*/)$', line, re.DOTALL)
                if matchs:
                    self.isInComment = False
                    
                if (self.isInComment):
                    indent = self._level * '\t'
                    line = indent + line + '\n'
                    contents += line
                    continue
                
                matchs = re.search('^(//)', line, re.DOTALL)
                if matchs:
                    indent = self._level * '\t'
                    line = indent + line + '\n'
                    contents += line
                    continue                
                
                if (('{' in line) and (not '}' in line)):                
                    if (line == '{'):
                        if (self.lastWasIf):
                            self.lastWasIf = False                            
                            self._level -= 1
                        indent = self._level * '\t'
                        line = indent + line + '\n'
                        contents += line
                        self._level += 1
                        continue
                    indent = self._level * '\t'
                    line = indent + line + '\n'
                    contents += line
                    self._level += 1
                    continue
                if ('}' in line):
                    self._level -= 1
                    if (not 'else' in line):                    
                        indent = self._level * '\t'
                        line = indent + line + '\n'
                        contents += line
                        if ('{' in line):
                            self._level += 1
                    else:                    
                        indent = self._level * '\t'
                        line = indent + line + '\n'
                        contents += line                    
                        self._level += 1
                    continue
                if ('if (' in line or 'if(' in line):                
                    self.lastWasIf = True
                    indent = self._level * '\t'
                    line = indent + line + '\n'
                    contents += line
                    self._level += 1
                    continue
                if (self.lastWasIf):
                    self.lastWasIf = False
                    indent = self._level * '\t'
                    line = indent + line + '\n'
                    contents += line
                    self._level -= 1
                    continue
                indent = self._level * '\t'
                line = indent + line + '\n'
                contents += line
            self.ui.sourceTextEdit.setTabStopWidth(12)
            self.files.append(contents)
            f.close()
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            self.ui.statusBar.showMessage("I/O error({0}): {1}".format(errno, strerror))
            raise
        except ValueError:
            print "Could not convert data to an integer."
            self.ui.statusBar.showMessage("Could not convert data to an integer.")
        except:
            import sys
            print "Unexpected error:", sys.exc_info()[0]
            self.ui.statusBar.showMessage("Unexpected error:" + str(sys.exc_info()[0]),  3000)
            raise
        else:
            f.close()
        
    def on_dir_select_clicked(self):
        """
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly);
        filename = ''
        if(dialog.exec_()) :
            filename = dialog.selectedFiles()
        if (filename):
            text = ''
            self.dir = filename[0]
            if (filename[0].length() > 40):
                text = filename[0]
                text = text[0:39] + '...'                
            self.ui.dirLabel.setText(text)
            
    def on_lint_clicked(self):
        """
        """
        import glob
        import os
        self.ui.ucLintButton.setEnabled(False)
        self.ui.dirSelectButton.setEnabled(False)
        self.ui.commentscheckBox.setEnabled(False)
        self.ui.previousButton.setEnabled(False)
        self.ui.nextButton.setEnabled(False)
        os.chdir(str(self.dir))    
        for files in glob.glob("*.uc"):
            self.file_names.append(os.path.basename(files))
            self.lastWasIf = False
            self._level = 0
            self._outText = ''
            self.isInComment = False
            self.ui.fileNamelabel.setText('Sanitizing ' + files)
            self.lint(files)
            QApplication.processEvents()
            
        if (self.files):
            if (len(self.files) > 1):
                self.ui.nextButton.setEnabled(True)
            self.ui.sourceTextEdit.setPlainText(self.files[0])
            self.file_index = 0
            self.ui.fileNamelabel.setText(self.file_names[0])
            self.ui.saveButton.setEnabled(True)
        else:
            self.ui.fileNamelabel.setText('Directory is empty!')
            self.ui.saveButton.setEnabled(False)
            
        self.ui.ucLintButton.setEnabled(True)
        self.ui.dirSelectButton.setEnabled(True)
        self.ui.commentscheckBox.setEnabled(True)
        self.ui.previousButton.setEnabled(True)
        self.ui.nextButton.setEnabled(True)
            
            
    def on_next_clicked(self):
        """
        """
        self.file_index += 1
        if (self.file_index == (len(self.files) - 1)):
            self.ui.nextButton.setEnabled(False)
        self.ui.previousButton.setEnabled(True)
        self.ui.sourceTextEdit.setPlainText(self.files[self.file_index])
        self.ui.fileNamelabel.setText(self.file_names[self.file_index])
        
    def on_previous_clicked(self):
        """
        """
        self.file_index -= 1
        if (self.file_index == 0):
            self.ui.previousButton.setEnabled(False)
        self.ui.nextButton.setEnabled(True)
        self.ui.sourceTextEdit.setPlainText(self.files[self.file_index])
        self.ui.fileNamelabel.setText(self.file_names[self.file_index])
        
    def about(self):
        	QMessageBox.about(self.window, "About",
                """<p>The <b>UCLint</b> is a <a href="http://udk.com/">UDK/UE3</a>
                script (UnrealScript) Sanitizer.</p>
                <p>It is an open source project; you can always find the latest
                version of code at <a href="https://github.com/thesoulless/UCLint">github</a>
                page.</p>
                <p>Current version: 0.0.1</p>
                """)
                        
if __name__ == '__main__':
    lint = UCLint()
