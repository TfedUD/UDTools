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

# Forward unto aforementioned shenanigans

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


PI = math.pi

rc.Runtime.HostUtils.DisplayOleAlerts(False)
tolerance = sc.doc.ModelAbsoluteTolerance

class CheckIn():

    def __init__(self, defaultFolder, folderIsSetByUser=False):

        self.folderIsSetByUser = folderIsSetByUser
        self.gnomesGnoming = True
        
        if defaultFolder:
            # user set folder 
            defaultFolder = os.path.normpath(defaultFolder) = os.sep

            if (" " in defaultFolder):
                msg = "default folder cant have whitespaces, little legs, gnomes need _bridges" + \
                      "\nGnomes cant Gnome" 


                print msg
                ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
                sc.sticky["GnomeLibDefaultFolder"] = ""
                self.gnomesGnoming = False
                return 
            else:
                # create if not created the folder 
                if not os.path.isdir(defaultFolder):
                    try: os.mkdir(defaultFolder)
                    except:
                        msg = "Cannot create default folder, Try a different filepath" + \
                              "\nGnomes cant Gnome"
                        print msg
                        ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
                        sc.sticky["GnomeLibDefaultFolder"] = ""
                        self.gnomesGnoming = False 
                        return 
            
            #Looks good lets do
            sc.sticky["GnomeLibDefaultFolder"] = defaultFolder
            self.folderIsSetByUser = True

        #setup default pass
        if not self.folderIsSetByUser:
            if os.path.exists("c:\udToolsD\\") and os.access(os.path.dirname("c:\\udToolsD\\"), os.F_OK):
                # already exists: all is well 
                sc.sticky["GnomeLibDefaultFolder"] = "c:\\udToolsD\\"
            elif os.access(os.path.dirname("c:\\"), os.F_OK):
                # does not exist lets change that 
                sc.sticky["GnomeLibDefaultFolder"] = "c:\\udToolsD\\"
            else:
                # lets use user folder
                appdata = os.getenv("APPDATA")
                # make sure username doesnt have space 
                if(" " in appdata):
                    msg = "User name on this system: " + appdata + " has white space, gnomes have little legs and at least need _bridges" + \
                        "\nGnomes cant Gnome"
                    print msg 
                    ghenv.Component.AddRuntimeMessage(gh.GH_RuntimeMessageLevel.Warning, msg)
                    sc.sticky["GnomeLibDefaultFolder"] = ""
                    self.gnomesGnoming = False
                    return 
                
                sc.sticky["GnomeLibDefaultFolder"] = os.path.join(appdata, "udToolsD\\")

##### Hopefully sets up objs 
class PrepareGnomeLibFiles(object):

    def __init__(self, workingDir = None, findLibFiles = False, ):

        if not workingDir: workingDir = sc.sticky["GnomeLibDefaultFolder"]
        if not sc.sticky.has_key("nceCostEstLib"): sc.sticky["nceCostEstLib"] = {}

        self.workingDir = workingDir
        