#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unreal Script Sanitizer

Main Python 
"""

__author__ = "Hamed Nemati"
__copyright__ = "Copyright 2012, Hamed Nemati"
__credits__ = [""]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "hitech.innovative@gmail.com"
__status__ = "Prototype"


class UCLint():
    """
    Class implementing a sanitizer for unreal script.
    """
    def __init__(self):
        import  sys
        
        self._level = 0
        pass
        
    
    def stip_comments(self, line):
        """
        """
        pass
        
    def fixWhiteSpaces(self, contents):
        """
        """
        pass
    
    def fixIndents(self, line):
        """
        """
        pass
                        
if __name__ == '__main__':
    main = UCLint()
    
