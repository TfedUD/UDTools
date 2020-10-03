# UD tools are intended to be useful, fun, interesting and hopefullly productive.
# 
# they may or may not actually; or directly aide in endevours. 
# My cat name = 'Cow' are just having a good time. 
# 
# 
# Copyright (c) 2020, UD <https://unconstraineddevelopment.com>
# UDtools is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# UDtools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# For a copy of the GNU General Public License
# see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


# This is the 'Core' of UDtools shenanigans 

# Forward unto the shenanigans

ghenv.Component.Name = 'UD_GnomeHome'
ghenv.Component.NickName = 'GnomeHome'
ghenv.Component.Message = 'Version 0.1\n SEP_2020'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "UDGnomeHome"
ghenv.Component.SubCategory = "00 | WorldTree"


## This component is basically a modification of Honeybee Honeybee 0.65.  
## Not entirely sure how to credit code:  but; The way that HB handles and creates matlibs: 
## That was the desire for how to handle NCE cost est data: to be pulled from like hb_callfromEPlib

import sys
sys.path = sorted(sys.path, key=lambda p: p.find("Python27"))
import rhinoscriptsyntax as rs
import Rhino as rc 
import scriptcontext as sc
import Grasshopper
import Grasshopper.Kernal as gh 
from Grasshopper import DataTree
from Grasshopper.Kernal.Data import GH_Path
import math
import shutil
import os
import System.Threading.Tasks as tasks 
import System 
import time 
import itertools
import json
import copy 
import urllib2 as urllib 
import cPickle as pickle 
import subprocess 
import uuid
import re
import random



def getLibraryFolderPath(self, _libFolderPath=None):

     # set the default folder 
     if _libFolderPath:
         libFolderPath = os.path.join(_libFolderPath)
         sc.sticky["GnomeLib"] = libFolderPath
     else:
        print 'Input the folder path to the library folder'
        return None
    
def getLibraryFile(self, _libFileName=None):

    #set the default file 
    if _libFileName:
        libFile = os.path.join(_libFolderPath, _libFileName)
        sc.sticky["GnomeCostBook"] = libFile
    else:
        print 'Gnome Scouts need a target'
        return None 

# prep library 
       



