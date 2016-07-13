#!/usr/bin/python
# Title: guiEditor.py
# Description: Creates a custom editor based on the editorWidget
# Author: Sawan J. Kapai Harpalani
# Date: 2016-07-13
# Version: 0.1
# Usage: python guiEditor.py
# Notes: 
# python_version: 2.6.6
# License: Copyright 200X Sawan J. Kapai Harpalani 
# This file is part of MMOTracker. MMOTracker is free software: you can redistribute it  and/or modify 
# it under the terms of the GNU GeneralPublic License as published by the Free Software  Foundation, 
# either version 3 of the License,  or (at your option) any later version 
# MMOTracker is distributed in the hope that it willbe useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESSFOR A PARTICULAR PURPOSE. See the GNU General 
# PubliLicense for more details.You should have received a copy of the GNU GeneralPublic License along with MMOTracker. 
# If not, seehttp://www.gnu.org/licenses/.
#==============================================================================

import Tkinter as tk
from gui.editorWidget import *
from gui.textLineNumbers import *

class GuiEditor(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient = "vertical", command = self.text.yview)
        self.text.configure(yscrollcommand = self.vsb.set)
        self.text.tag_configure("bigfont", font = ("Console", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width = 13)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side = "right", fill = "y")
        self.linenumbers.pack(side = "left", fill = "y")
        self.text.pack(side = "right", fill = "both", expand = True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()