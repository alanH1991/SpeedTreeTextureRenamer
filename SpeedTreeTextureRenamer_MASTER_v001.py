import sys
import os
import glob
import re
import shutil
import xml.etree.ElementTree as ET

from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

#don't have underscorces in the naming of your python file that you want to referance
from strUi import Ui_MainWindow
'''
Things to do:
-remove glob
-only single instance of tool exist

'''
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Turn on checkbox by default
        self.ui.useVariantNum_checkBox.setChecked(1)
        #Button Click Actions
        self.ui.run_pushButton.clicked.connect(self.onRunAction)
        self.ui.clearLog_pushButton.clicked.connect(self.clearLog)
        self.ui.useVariantNum_checkBox.clicked.connect(self.toggleCheckBox)
        

        self.ui.materialTag_lineEdit.setText("SHR")
        #if useVariantNum_checkBox = True the enable variantNum_lineEdit
        self.ui.variantNum_lineEdit.setText("00")
        self.ui.diffuseMap_lineEdit.setText("COL")
        self.ui.glossMap_lineEdit.setText("GLS")
        self.ui.normalMap_lineEdit.setText("NRM")
        self.ui.heightMap_lineEdit.setText("DSP")
        self.ui.opacityMap_lineEdit.setText("OPC")
        self.ui.sscMap_lineEdit.setText("SSC")
        self.ui.ssaMap_lineEdit.setText("SSA")
        self.ui.aoMap_lineEdit.setText("AO")


    def onRunAction(self):
        returnedIssue = self.CollectPathToFiles()
        if returnedIssue == 0:
            returnedIssue = self.CollectAssetName()
            if returnedIssue == 0:
                returnedIssue , errorDetails = self.checkNamingConvention()
                if returnedIssue == 0:
                    self.printToLogFunct("-"*100 +"\nPROCESS START\n"+"-"*100+"\n\n")
                    self.printToLogFunct(f"Valid Source Directory: {self.ui.pathToFiles_lineEdit.text()} \n")
                    newPath = self.makeNewDirCopy()
                    self.printToLogFunct(f"Output Directory: {newPath}\n")
                    self.printToLogFunct(f"Asset Name: {self.ui.assetName_lineEdit.text()} \n \n")                    
                    self.coreRenaming(newPath)
                    self.printToLogFunct("-"*100 +"\nPROCESS COMPLETE\n"+"-"*100+"\n\n")

                else:
                    self.errorFunction(errorDetails)

            else:
                self.errorFunction(returnedIssue)                
        else:
            self.errorFunction(returnedIssue)


    def printToLogFunct(self,printToLog):
            logContents = self.ui.log_textBrowser.toPlainText()
            #to maintain the current text in the textBroweser we need to get that already exists and add the new line to it and then reprint it.
            printToLog = logContents + printToLog        
            self.ui.log_textBrowser.setText(printToLog)
            #setScrollBar to bottom of log printOut
            self.ui.log_textBrowser.verticalScrollBar().setValue(self.ui.log_textBrowser.verticalScrollBar().maximum())     

    def CollectPathToFiles(self):
        pathToFiles = self.ui.pathToFiles_lineEdit.text()
        if os.path.exists(pathToFiles):
            stmatFile = glob.glob(pathToFiles+"/*.stmat")
            if len(stmatFile)==1:
                self.ui.log_textBrowser.setStyleSheet("QTextBrowser#log_textBrowser{border: 2px solid rgb(179, 255, 131); background-color: rgb(172, 172, 172);}")  
                inputIssue = 0
                return inputIssue
            
            elif len(stmatFile)>1:
                return "ERROR: More than one .stmat file detected in directory \n"
            else:
                return "ERROR: No .stmat File detected in directory \n"          
        else:
            return "ERROR: Path to files is invalid \n"
        
    def CollectAssetName(self):
        assetNameUserInput = self.ui.assetName_lineEdit.text()
        if len(assetNameUserInput) > 0: 
            inputIssue = 0
            return inputIssue
        else:
            return "ERROR: Asset Name is blank \n"
        
    def checkNamingConvention(self):
        for child in self.ui.components_frame.findChildren(QLineEdit):
            #print(f"{child.text()} -- {len(child.text())}")           
            if len(child.text())>0:
                continue
            
            elif self.ui.useVariantNum_checkBox.isChecked() == 0 :
                continue
            
            else:
                emptyTagField = child.objectName()
                emptyTagField = emptyTagField.replace("_lineEdit","")
                emptyTagField = emptyTagField.replace("Map","")
                emptyTagField = emptyTagField.replace("Tag","")
                errorDetails =  f"ERROR: {emptyTagField} tag in the naming convention settings is blank \n"
                inputIssue = 1
                
                return inputIssue , errorDetails
        inputIssue = 0
        errorDetails = "null"
        return inputIssue , errorDetails


    def toggleCheckBox(self):
        if self.ui.useVariantNum_checkBox.isChecked()==1:
            self.ui.variantNum_lineEdit.setEnabled(1)
            self.ui.variantNum_lineEdit.setStyleSheet("QLineEdit#variantNum_lineEdit {color:rgb(255,255,255)};")
        else:
            self.ui.variantNum_lineEdit.setEnabled(0)
            self.ui.variantNum_lineEdit.setStyleSheet("QLineEdit#variantNum_lineEdit {color:rgb(170,170,170)};")


    def clearLog(self):
        self.ui.log_textBrowser.setText("")
        self.ui.log_textBrowser.setStyleSheet("QTextBrowser#log_textBrowser{border: 2px solid rgb(179, 255, 131); background-color: rgb(172, 172, 172);}")

    def errorFunction(self,returnedError):
        logContents = self.ui.log_textBrowser.toPlainText()
        printToLog = logContents + "#"*100+"\n"+ returnedError + "#"*100+"\n"
        self.ui.log_textBrowser.setText(printToLog)
        #setScrollBar to bottom of log printOut
        self.ui.log_textBrowser.verticalScrollBar().setValue(self.ui.log_textBrowser.verticalScrollBar().maximum())        
        self.ui.log_textBrowser.setStyleSheet("QTextBrowser#log_textBrowser{border: 2px solid rgb(255, 0, 0); background-color: rgb(172, 172, 172);}")

    def makeNewDirCopy(self):

        assetName = self.ui.assetName_lineEdit.text()
        pathToFiles = self.ui.pathToFiles_lineEdit.text()

        os.chdir(pathToFiles)
        #make directory
        os.chdir("../")
        try:
            os.mkdir("{0}_speedTreeExport".format(assetName))
            os.chdir("./{0}_speedTreeExport".format(assetName))
            newPath = os.getcwd()

            #copy files
            os.chdir(pathToFiles)
            for file in os.listdir(pathToFiles):
                file = os.path.abspath(file)        
                shutil.copy2(os.path.abspath(file),newPath)

                        
        except FileExistsError:
            self.errorFunction("Directory already exists under that asset name\n")

        #set current working directory to the new duplicate   
        os.chdir(newPath)
        return newPath    


    def coreRenaming(self,newPath):

        #naming Convention Dicitonary
        #Colour / _DIF_00 assigned out of dicitionary arry as some maps don't have anything to match agains even though they are mapType Color

        if self.ui.useVariantNum_checkBox.isChecked()==1:
            variantNum = "_"+self.ui.variantNum_lineEdit.text()
        else:
            variantNum = ""       

        ahMapType = {"Color":"",
                    "BaseColor":"",
                    "Opacity":"_" + self.ui.opacityMap_lineEdit.text() + variantNum,
                    "Normal":"_" + self.ui.normalMap_lineEdit.text() + variantNum,
                    "Gloss":"_" + self.ui.glossMap_lineEdit.text() + variantNum,
                    "Height":"_" + self.ui.heightMap_lineEdit.text() + variantNum,
                    "SubsurfaceColor": "_" + self.ui.sscMap_lineEdit.text() + variantNum,
                    "SubsurfaceAmount": "_" + self.ui.ssaMap_lineEdit.text() + variantNum,
                    "AO":"_" + self.ui.aoMap_lineEdit.text() + variantNum}
        ahMapTypeDIF="_" +  self.ui.diffuseMap_lineEdit.text() + variantNum

        assetName = self.ui.assetName_lineEdit.text()
        materialTag = self.ui.materialTag_lineEdit.text()   

        #break the asset name into components
        numPattern = r'[0-9]'
        nameCheck = re.sub(numPattern,'',assetName)
        nameCheck = re.findall("[a-zA-Z][^A-Z]*",nameCheck)

        #get .stmat file
        for file in os.listdir(newPath):
            if file.endswith(".stmat"):
                stmatFile = file
                

        #filter out single letter character from list.
        #result from removeing the numbers as part of the variant ID but not a letter component 
        for word in nameCheck:
            if len(word)<=1:
                nameCheck.remove(word)

        #bad practice to append to a list you are looping through, hence toAppendNameCheck created and reassinged to nameCheck after
        toAppendNameCheck = []
        for word in nameCheck:
            #make everything word start with a capital and lower the other letters     
            toAppendNameCheck.append(word.capitalize())
            #lower all letters
            toAppendNameCheck.append(word.lower())
        #merging two lists
        nameCheck = toAppendNameCheck
        #Add in the defult naming speedtree gives to materials tags
        nameCheck.append("Mat")

        ''' Open up XML doc'''
        tree = ET.parse(r"{0}/{1}".format(newPath,stmatFile))
        root = tree.getroot()

        ''' Create new material name following convention '''
        materials = root
        #For every material in the XML doc loop through
        indexVarMaterial = 0        
        for material in materials:

            material = root[indexVarMaterial]
            oldMatName = material.attrib.get("Name")
            
            for word in nameCheck:
                if word in oldMatName:
                    oldMatName = oldMatName.replace(word,'')
                newMatName = oldMatName.replace('_','') + '_' + materialTag     
                    

            ''' edit XML doc to new naming for material '''
            material.attrib.update({"Name":newMatName})
            tree.write(r"{0}/{1}".format(newPath,stmatFile),encoding="UTF-8",xml_declaration=True)
            

            #print_material_to_log
            logContents = self.ui.log_textBrowser.toPlainText()
            printToLog = logContents + "\n""Material: " + newMatName + "\n"            
            self.ui.log_textBrowser.setText(printToLog)

            #For Each material loop and list each texture map
            indexVarMap = 0
            for Map in material:
                #find the relevent info for each texture map    
                MapType = root[indexVarMaterial][indexVarMap].attrib.get("Name")
                originalFileName = root[indexVarMaterial][indexVarMap].attrib.get("File")
                FileName = originalFileName

                ''' Renaming the texture map files to naming convention'''
                #isolate only texture maps, remove 'None' types
                if 'None' not in str(FileName):         
                    for word in nameCheck:
                        if word in FileName:
                            FileName = FileName.replace(word,'')
                        FileName = FileName.replace('_','')
                        
                    #change the naming of the orginal files to match the convention in the dicitionary 
                    try:
                        FileName=FileName.replace(MapType,ahMapType.get(MapType))
                        #colour has some variations on the naming for the orginal file
                        if MapType == "Color":
                            basename,ext=FileName.split(".")
                            FileName = basename+ahMapTypeDIF+"."+ext
                            
                    except TypeError:
                        continue
                    
                    #prefrix asset name and lower the first letter of the file name
                    FileName = f"{assetName}_"+FileName[0].lower() + FileName[1:]
                    root[indexVarMaterial][indexVarMap].attrib.update({"File":FileName})

                    ''' Renaming texture files in directory '''
                    os.rename(originalFileName,FileName)
                    
                    printToLog = f"ORGINAL: {originalFileName:-<70}{MapType:-<30}{FileName}\n"
                    self.printToLogFunct(printToLog)
                    indexVarMap+=1
                    
                else:
                    indexVarMap+=1
                    pass
            indexVarMaterial+=1


if __name__ == '__main__':
    app=QApplication(sys.argv)

    window=MainWindow()
    window.setWindowTitle("SpeedTree Export Renamer")
    window.show()

    sys.exit(app.exec())