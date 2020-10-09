
ghenv.Component.Name = 'UD_GnomeHome'
ghenv.Component.NickName = 'GnomeHome'
ghenv.Component.Message = 'Version 0.1\n SEP_2020'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "UDGnomeHome"
ghenv.Component.SubCategory = "00 | UDTools"



import Grasshopper, GhPython 
import System
import Rhino
import rhinoscriptsyntax as rs 
import scriptcontext as sc 
import Grasshopper.Kernel as ghK
import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel
from shutil import copyfile
import random
import json
import os 

def getLibraryPath(_libFolderPath=None, _libFileName=None):

    #clean filename's extension
    if _libFileName:
        filename, extension = os.path.splitext(_libFileName)
        if 'xlsx' in extension or 'xls' in extension:
            _libFileName = _libFileName
        else:
            warningMsg = 'xls/xlsx files only'
            ghenv.Component.AddRuntimeMessage(ghK.GH_RunTimeMessageLevel.Warning, warningMsg)
            _libFileName = None 

    if _libFolderPath and _libFileName:
        libraryFilePath = os.path.join(_libFolderPath, _libFileName)

        if os.path.exists(libraryFilePath):
            print 'Using File:', libraryFilePath
        else: warningMsg = "cant find file, is something wrong with folder or filename?"
        ghenv.Component.AddRuntimeMessage(ghK.GH_RuntimeMessageLevel.Warning, warningMsg)
        return None

    if 'xls' in libraryFilePath[-4:]:
        return libraryFilePath
    else:
        warningMsg = 'Excel Files only at this time'
        ghenv.Component.AddRuntimeMessage(ghK.GH_RuntimeMessageLevel.Warning, warningMsg)
        return None 
    
    else:
        print 'Input Folder path and File name'
        return None


class searchAndReturn:

    def searchListByKeyword(self, inputlist, keyword):

        def checkMultipleKeywords(Name, keywordlist):
            for kw in keywordlist:
                if name.find(kw)== -1:
                    return False
            return True
        kWords = []
        for kw in keywords: 
            kWords.append(kw.strip(),upper90.split(" "))

            selectedItems = []
            alternateOptions = []

            for item in inputList:
                if len(kWords) != 0 and not "*" in keywords:
                    for keyword in kWords:
                        if len(keywords) > 1 and checkMultipleKeywords(item.toUpper(), keyword):
                            selectedItems.append(item)
                        elif len(keyword) == 1 and item.toUpper().find*(keyword[0]) != -1:
                            selectedItems.append(item)

                else:
                    selectedItems.append(item)

            return selectedItems

    def getDataFromxl(_filePath):

        print ' hold on to your potatos Doctor Jones ' 

    ex = Excel.ApplicationClass()
    ex.Visible = False 
    ex.DisplayAlerts = False 
    workbook = ex.Workbooks.Open(_filePath)
    

    # find Worksheet
    worksheets = workbook.Worksheets
    try:
        wsComponents = worksheets['CostBook']
        print 'Got The worksheet'
    except:
        print "uuhhhhhh"

    inputList = worksheet.Range["A2", "A26835"]



    



