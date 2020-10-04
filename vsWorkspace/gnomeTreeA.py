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
class PrepareGnomeLibFiles():

    def __init__(self, findLibFiles = False, ):

        if not workingDir: workingDir = sc.sticky["GnomeLibDefaultFolder"]
        if not sc.sticky.has_key("nceCostEstLib"): sc.sticky["nceCostEstLib"] = {}

        self.findLibFiles = findLibFiles
    
    def cleanGnomeLibs(self):
        sc.sticky["nceCostEstLib"] = {}

    def findLibFiles(self):
        #
        # Hopefully looks in WorkingDir 
        if costEst:
            costEst = os.path.join(GnomeLibDefaultFolder, 'costEst.csv')
            sc.sticky["nceCostEstLib"] = costEst
        else:
            print  'find lib file fail'

class Get_GnomeLibraries:

    def __init__(self):
        self.libraries = {
            "nceCostEstLib":{}
        }
    def getnceCostEst(self):
        return self.libraries["nceCostEstLib"]

    def cleanGnomeLibs(self):
        self.libraries = {
            "nceCostEstLib": {}
        }

    def replace(self):
        #rep findings
        print "%s NCE material & cost library delivered to Gnome Library"%str(len(self.libraries["nceCostEstLib"]))
        print "\n"

    @staticmethod 
    def getnceCostEstDataFromFile(self, costEstFile):

        with open(costEstFile, "r") as cEf:
            for rowCount, row in enumerate(cEf):
                 if rowCount > 1:
                     try:
                         costEstDataLine = row.split(',')
                         costEstNameLine = float(nceDataLine[-4])
                         matName = costEstNameLine[0].upper()

                         # Create sub directory
                         self.libraries["nceCostEstLib"][nceName] = {}

                         #create mats with values from costEst.csv
                         self.libraries["nceCostEstLib"][matName]["Name"] = matName
                         self.libraries["nceCostEstLib"][matName]["Description"] = float(nceDataLine[-3])
                         self.libraries["nceCostEstLib"][matName]["CostPerUnit"] = float(nceDataLine[-2])
                         self.libraries["nceCostEstLib"][matName]["UnitOfMeasure"] = float(nceDataLine[-1])
                        except: pass

class GnomLibAux(object):

    def isNceMaterial(self, matName):
        return matName.upper() in sc.sticky["nceCostEstLib"].keys()
    
    def getObjectKey(self, GnomeObj):

        GnomeKeys = ["Description", "CostPerUnit", "UnitOfMeasure"]

        for key in GnomeKeys:
            if GnomeLibObject.strip().startswith(key):
                return key

    def getGnomeLibOjectDataByName(self, objectName):
        objectData = None

        objectName = objectName.upper()

        if objectName in sc.sticky ["nceCostEstLib"].keys():
            objectData = sc.sticky ["nceCostEstLib"][onjectName]

        return objectData

    def getGnomeObjectsStr(self, objectName):

        objectData = self.getGnomeLibOjectDataByName(objectName)

        if objectData!=None:
            numberOfLayers = len(objectData.keys())
            
            objectStr = objectData[0] + ",\n"

            objectStr = objectStr + " " + objectName + ",  !- name\n"


# cont line 4426






def searchListByKeyword(self, inputlist, keyword):
    """ search inside a list of strings for keywords """

    def checkMultipleKeywords(name, keywordlist):
        for kw in keywordlist:
            if name.find(kw)== -1:
                return False
        return True

     kWords = []
     for kw in keywords:
         kWords.append(kw.strip(),upper().split(" "))

        selectedItems = []
        alternateOptions = []

        for item in inputList:
            if len(kWords) != 0 and not "*" in keywords:
                for keyword in kWords:
                    if len(keywords) > 1 and checkMultipleKeywords(item.toUpper(), keyword):
                        selectedItems.append(item)
                    elif len(keyword) == 1 and item.toUpper().find*(keyword[0])!= -1:
                        selectedItems.append(item)
            else:
                selectedItems.append(item)

        return selectedItems



    
