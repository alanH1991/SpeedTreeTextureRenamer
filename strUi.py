# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Speedtree_textureRenamer_v001.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 833)
        MainWindow.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 120, 120);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit{\n"
"\n"
"color: rgb(255, 255,255);\n"
"background-color: rgb(142, 142, 142);\n"
"font-size:14px;\n"
"padding:2px;\n"
"/*font-weight:bold;*/\n"
"}\n"
"\n"
"QFrame{\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:1px solid  rgb(195, 195, 195);\n"
"padding: 3px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(195,195,195);\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed{\n"
"color: rgb(0,200,0);\n"
"border-style: 3px inset  rgb(195, 195, 195);\n"
"}\n"
"\n"
"QPushButton#clearLog_pushButton::pressed{\n"
"color: rgb(200,0,0);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox::title{\n"
"subcontrol-position: bottom right;\n"
"padding: 0 10px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"border: 2px solid rgb(179, 255, 131);\n"
"border-radius: 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.groupBox.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.groupBox.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_frame = QFrame(self.groupBox)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_14)

        self.toolNameHeader_label = QLabel(self.header_frame)
        self.toolNameHeader_label.setObjectName(u"toolNameHeader_label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.toolNameHeader_label.setFont(font)
        self.toolNameHeader_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.toolNameHeader_label)

        self.toolLogo_label = QLabel(self.header_frame)
        self.toolLogo_label.setObjectName(u"toolLogo_label")
        self.toolLogo_label.setPixmap(QPixmap(u"generator_treeC.png"))
        self.toolLogo_label.setScaledContents(False)

        self.horizontalLayout_16.addWidget(self.toolLogo_label)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addWidget(self.header_frame)

        self.spreedTreeRenamer_tabWidget = QTabWidget(self.groupBox)
        self.spreedTreeRenamer_tabWidget.setObjectName(u"spreedTreeRenamer_tabWidget")
        self.spreedTreeRenamer_tabWidget.setStyleSheet(u"\n"
"QTabBar:tab:selected{\n"
"background-color: rgb(172, 172, 172);\n"
"}\n"
"\n"
"QTabBar:tab:!selected{\n"
";\n"
"	\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"\n"
"")
        self.spreedTreeRenamer_tabWidget.setDocumentMode(True)
        self.spreedTreeRenamer_tabWidget.setTabBarAutoHide(False)
        self.renaming_tab = QWidget()
        self.renaming_tab.setObjectName(u"renaming_tab")
        self.verticalLayout_2 = QVBoxLayout(self.renaming_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainUpper_02_frame = QFrame(self.renaming_tab)
        self.mainUpper_02_frame.setObjectName(u"mainUpper_02_frame")
        self.mainUpper_02_frame.setFrameShape(QFrame.StyledPanel)
        self.mainUpper_02_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainUpper_02_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pathToFiles_01_frame = QFrame(self.mainUpper_02_frame)
        self.pathToFiles_01_frame.setObjectName(u"pathToFiles_01_frame")
        self.pathToFiles_01_frame.setFrameShape(QFrame.StyledPanel)
        self.pathToFiles_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.pathToFiles_01_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pathToFiles_label = QLabel(self.pathToFiles_01_frame)
        self.pathToFiles_label.setObjectName(u"pathToFiles_label")

        self.horizontalLayout_2.addWidget(self.pathToFiles_label)

        self.pathToFiles_lineEdit = QLineEdit(self.pathToFiles_01_frame)
        self.pathToFiles_lineEdit.setObjectName(u"pathToFiles_lineEdit")

        self.horizontalLayout_2.addWidget(self.pathToFiles_lineEdit)


        self.verticalLayout.addWidget(self.pathToFiles_01_frame)

        self.assetName_01_frame = QFrame(self.mainUpper_02_frame)
        self.assetName_01_frame.setObjectName(u"assetName_01_frame")
        self.assetName_01_frame.setFrameShape(QFrame.StyledPanel)
        self.assetName_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.assetName_01_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.assetName_label = QLabel(self.assetName_01_frame)
        self.assetName_label.setObjectName(u"assetName_label")

        self.horizontalLayout.addWidget(self.assetName_label)

        self.assetName_lineEdit = QLineEdit(self.assetName_01_frame)
        self.assetName_lineEdit.setObjectName(u"assetName_lineEdit")

        self.horizontalLayout.addWidget(self.assetName_lineEdit)


        self.verticalLayout.addWidget(self.assetName_01_frame)

        self.run_01_frame = QFrame(self.mainUpper_02_frame)
        self.run_01_frame.setObjectName(u"run_01_frame")
        self.run_01_frame.setFrameShape(QFrame.StyledPanel)
        self.run_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.run_01_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(280, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.run_pushButton = QPushButton(self.run_01_frame)
        self.run_pushButton.setObjectName(u"run_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_pushButton.sizePolicy().hasHeightForWidth())
        self.run_pushButton.setSizePolicy(sizePolicy)
        self.run_pushButton.setMinimumSize(QSize(100, 21))
        self.run_pushButton.setSizeIncrement(QSize(0, 0))
        self.run_pushButton.setBaseSize(QSize(30, 0))
        self.run_pushButton.setIconSize(QSize(30, 16))
        self.run_pushButton.setAutoDefault(False)
        self.run_pushButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.run_pushButton)


        self.verticalLayout.addWidget(self.run_01_frame)


        self.verticalLayout_2.addWidget(self.mainUpper_02_frame)

        self.log_textBrowser = QTextBrowser(self.renaming_tab)
        self.log_textBrowser.setObjectName(u"log_textBrowser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.log_textBrowser.sizePolicy().hasHeightForWidth())
        self.log_textBrowser.setSizePolicy(sizePolicy1)
        self.log_textBrowser.setAcceptDrops(False)
        self.log_textBrowser.setStyleSheet(u"border: 2px solid rgb(179, 255, 131);\n"
"background-color: rgb(172, 172, 172);")
        self.log_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.log_textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.log_textBrowser.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_2.addWidget(self.log_textBrowser)

        self.clearLog_01_frame = QFrame(self.renaming_tab)
        self.clearLog_01_frame.setObjectName(u"clearLog_01_frame")
        self.clearLog_01_frame.setFrameShape(QFrame.StyledPanel)
        self.clearLog_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.clearLog_01_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.clearLog_pushButton = QPushButton(self.clearLog_01_frame)
        self.clearLog_pushButton.setObjectName(u"clearLog_pushButton")
        self.clearLog_pushButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.clearLog_pushButton)


        self.verticalLayout_2.addWidget(self.clearLog_01_frame)

        self.spreedTreeRenamer_tabWidget.addTab(self.renaming_tab, "")
        self.namingConvention_tab = QWidget()
        self.namingConvention_tab.setObjectName(u"namingConvention_tab")
        self.verticalLayout_4 = QVBoxLayout(self.namingConvention_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.components_frame = QFrame(self.namingConvention_tab)
        self.components_frame.setObjectName(u"components_frame")
        self.components_frame.setFrameShape(QFrame.StyledPanel)
        self.components_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.components_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.materialTag_01_frame = QFrame(self.components_frame)
        self.materialTag_01_frame.setObjectName(u"materialTag_01_frame")
        self.materialTag_01_frame.setFrameShape(QFrame.StyledPanel)
        self.materialTag_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.materialTag_01_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.materialTag_label = QLabel(self.materialTag_01_frame)
        self.materialTag_label.setObjectName(u"materialTag_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.materialTag_label.sizePolicy().hasHeightForWidth())
        self.materialTag_label.setSizePolicy(sizePolicy2)
        self.materialTag_label.setScaledContents(False)
        self.materialTag_label.setAlignment(Qt.AlignCenter)
        self.materialTag_label.setWordWrap(False)

        self.horizontalLayout_15.addWidget(self.materialTag_label)

        self.horizontalSpacer_4 = QSpacerItem(110, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.materialTag_lineEdit = QLineEdit(self.materialTag_01_frame)
        self.materialTag_lineEdit.setObjectName(u"materialTag_lineEdit")
        self.materialTag_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.materialTag_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.materialTag_lineEdit)


        self.verticalLayout_3.addWidget(self.materialTag_01_frame)

        self.verticalSpacer_18 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_18)

        self.useVariantNumbering_01_frame = QFrame(self.components_frame)
        self.useVariantNumbering_01_frame.setObjectName(u"useVariantNumbering_01_frame")
        self.useVariantNumbering_01_frame.setFrameShape(QFrame.StyledPanel)
        self.useVariantNumbering_01_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.useVariantNumbering_01_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.useVariantNum_checkBox = QCheckBox(self.useVariantNumbering_01_frame)
        self.useVariantNum_checkBox.setObjectName(u"useVariantNum_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.useVariantNum_checkBox.sizePolicy().hasHeightForWidth())
        self.useVariantNum_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_14.addWidget(self.useVariantNum_checkBox)

        self.horizontalSpacer_5 = QSpacerItem(35, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.variantNum_lineEdit = QLineEdit(self.useVariantNumbering_01_frame)
        self.variantNum_lineEdit.setObjectName(u"variantNum_lineEdit")
        self.variantNum_lineEdit.setEnabled(True)
        self.variantNum_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.variantNum_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.variantNum_lineEdit)


        self.verticalLayout_3.addWidget(self.useVariantNumbering_01_frame)

        self.verticalSpacer_17 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_17)

        self.diffuseMap_frame = QFrame(self.components_frame)
        self.diffuseMap_frame.setObjectName(u"diffuseMap_frame")
        self.diffuseMap_frame.setFrameShape(QFrame.StyledPanel)
        self.diffuseMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.diffuseMap_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.diffuseMap_label = QLabel(self.diffuseMap_frame)
        self.diffuseMap_label.setObjectName(u"diffuseMap_label")
        sizePolicy2.setHeightForWidth(self.diffuseMap_label.sizePolicy().hasHeightForWidth())
        self.diffuseMap_label.setSizePolicy(sizePolicy2)
        self.diffuseMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.diffuseMap_label)

        self.horizontalSpacer_6 = QSpacerItem(110, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.diffuseMap_lineEdit = QLineEdit(self.diffuseMap_frame)
        self.diffuseMap_lineEdit.setObjectName(u"diffuseMap_lineEdit")
        self.diffuseMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.diffuseMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.diffuseMap_lineEdit)


        self.verticalLayout_3.addWidget(self.diffuseMap_frame)

        self.verticalSpacer_16 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_16)

        self.glossMap_frame = QFrame(self.components_frame)
        self.glossMap_frame.setObjectName(u"glossMap_frame")
        self.glossMap_frame.setFrameShape(QFrame.StyledPanel)
        self.glossMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.glossMap_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.glossMap_label = QLabel(self.glossMap_frame)
        self.glossMap_label.setObjectName(u"glossMap_label")
        sizePolicy2.setHeightForWidth(self.glossMap_label.sizePolicy().hasHeightForWidth())
        self.glossMap_label.setSizePolicy(sizePolicy2)
        self.glossMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.glossMap_label)

        self.horizontalSpacer_7 = QSpacerItem(119, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.glossMap_lineEdit = QLineEdit(self.glossMap_frame)
        self.glossMap_lineEdit.setObjectName(u"glossMap_lineEdit")
        self.glossMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.glossMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.glossMap_lineEdit)


        self.verticalLayout_3.addWidget(self.glossMap_frame)

        self.verticalSpacer_15 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_15)

        self.normalMap_frame = QFrame(self.components_frame)
        self.normalMap_frame.setObjectName(u"normalMap_frame")
        self.normalMap_frame.setFrameShape(QFrame.StyledPanel)
        self.normalMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.normalMap_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.normalMap_label = QLabel(self.normalMap_frame)
        self.normalMap_label.setObjectName(u"normalMap_label")
        sizePolicy2.setHeightForWidth(self.normalMap_label.sizePolicy().hasHeightForWidth())
        self.normalMap_label.setSizePolicy(sizePolicy2)
        self.normalMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.normalMap_label)

        self.horizontalSpacer_8 = QSpacerItem(109, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.normalMap_lineEdit = QLineEdit(self.normalMap_frame)
        self.normalMap_lineEdit.setObjectName(u"normalMap_lineEdit")
        self.normalMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.normalMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.normalMap_lineEdit)


        self.verticalLayout_3.addWidget(self.normalMap_frame)

        self.verticalSpacer_14 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.heightMap_frame = QFrame(self.components_frame)
        self.heightMap_frame.setObjectName(u"heightMap_frame")
        self.heightMap_frame.setFrameShape(QFrame.StyledPanel)
        self.heightMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.heightMap_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.heightMap_label = QLabel(self.heightMap_frame)
        self.heightMap_label.setObjectName(u"heightMap_label")
        sizePolicy2.setHeightForWidth(self.heightMap_label.sizePolicy().hasHeightForWidth())
        self.heightMap_label.setSizePolicy(sizePolicy2)
        self.heightMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.heightMap_label)

        self.horizontalSpacer_9 = QSpacerItem(110, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.heightMap_lineEdit = QLineEdit(self.heightMap_frame)
        self.heightMap_lineEdit.setObjectName(u"heightMap_lineEdit")
        self.heightMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.heightMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.heightMap_lineEdit)


        self.verticalLayout_3.addWidget(self.heightMap_frame)

        self.verticalSpacer_13 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.opacityMap_frame = QFrame(self.components_frame)
        self.opacityMap_frame.setObjectName(u"opacityMap_frame")
        self.opacityMap_frame.setFrameShape(QFrame.StyledPanel)
        self.opacityMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.opacityMap_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.opacityMap_label = QLabel(self.opacityMap_frame)
        self.opacityMap_label.setObjectName(u"opacityMap_label")
        sizePolicy2.setHeightForWidth(self.opacityMap_label.sizePolicy().hasHeightForWidth())
        self.opacityMap_label.setSizePolicy(sizePolicy2)
        self.opacityMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.opacityMap_label)

        self.horizontalSpacer_10 = QSpacerItem(100, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.opacityMap_lineEdit = QLineEdit(self.opacityMap_frame)
        self.opacityMap_lineEdit.setObjectName(u"opacityMap_lineEdit")
        self.opacityMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.opacityMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.opacityMap_lineEdit)


        self.verticalLayout_3.addWidget(self.opacityMap_frame)

        self.verticalSpacer_12 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.sscMap_frame = QFrame(self.components_frame)
        self.sscMap_frame.setObjectName(u"sscMap_frame")
        self.sscMap_frame.setFrameShape(QFrame.StyledPanel)
        self.sscMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.sscMap_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sscMap_label = QLabel(self.sscMap_frame)
        self.sscMap_label.setObjectName(u"sscMap_label")
        sizePolicy2.setHeightForWidth(self.sscMap_label.sizePolicy().hasHeightForWidth())
        self.sscMap_label.setSizePolicy(sizePolicy2)
        self.sscMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.sscMap_label)

        self.horizontalSpacer_11 = QSpacerItem(48, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.sscMap_lineEdit = QLineEdit(self.sscMap_frame)
        self.sscMap_lineEdit.setObjectName(u"sscMap_lineEdit")
        self.sscMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.sscMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.sscMap_lineEdit)


        self.verticalLayout_3.addWidget(self.sscMap_frame)

        self.verticalSpacer_11 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.ssaMap_frame = QFrame(self.components_frame)
        self.ssaMap_frame.setObjectName(u"ssaMap_frame")
        self.ssaMap_frame.setFrameShape(QFrame.StyledPanel)
        self.ssaMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ssaMap_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ssaMap_label = QLabel(self.ssaMap_frame)
        self.ssaMap_label.setObjectName(u"ssaMap_label")
        sizePolicy2.setHeightForWidth(self.ssaMap_label.sizePolicy().hasHeightForWidth())
        self.ssaMap_label.setSizePolicy(sizePolicy2)
        self.ssaMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ssaMap_label)

        self.horizontalSpacer_12 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.ssaMap_lineEdit = QLineEdit(self.ssaMap_frame)
        self.ssaMap_lineEdit.setObjectName(u"ssaMap_lineEdit")
        self.ssaMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.ssaMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ssaMap_lineEdit)


        self.verticalLayout_3.addWidget(self.ssaMap_frame)

        self.verticalSpacer_10 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.aoMap_frame = QFrame(self.components_frame)
        self.aoMap_frame.setObjectName(u"aoMap_frame")
        self.aoMap_frame.setFrameShape(QFrame.StyledPanel)
        self.aoMap_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.aoMap_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.aoMap_label = QLabel(self.aoMap_frame)
        self.aoMap_label.setObjectName(u"aoMap_label")
        sizePolicy2.setHeightForWidth(self.aoMap_label.sizePolicy().hasHeightForWidth())
        self.aoMap_label.setSizePolicy(sizePolicy2)
        self.aoMap_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.aoMap_label)

        self.horizontalSpacer_3 = QSpacerItem(117, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.aoMap_lineEdit = QLineEdit(self.aoMap_frame)
        self.aoMap_lineEdit.setObjectName(u"aoMap_lineEdit")
        self.aoMap_lineEdit.setMaximumSize(QSize(504, 16777215))
        self.aoMap_lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.aoMap_lineEdit)


        self.verticalLayout_3.addWidget(self.aoMap_frame)


        self.verticalLayout_4.addWidget(self.components_frame)

        self.spreedTreeRenamer_tabWidget.addTab(self.namingConvention_tab, "")

        self.verticalLayout_5.addWidget(self.spreedTreeRenamer_tabWidget)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.spreedTreeRenamer_tabWidget.setCurrentIndex(0)
        self.run_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Alan Herbert 2024", None))
        self.toolNameHeader_label.setText(QCoreApplication.translate("MainWindow", u"Speed Tree Export Renamer", None))
        self.toolLogo_label.setText("")
        self.pathToFiles_label.setText(QCoreApplication.translate("MainWindow", u"Path To Files", None))
        self.assetName_label.setText(QCoreApplication.translate("MainWindow", u"Asset Name", None))
        self.assetName_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"oakEnglish01A", None))
        self.run_pushButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.clearLog_pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.spreedTreeRenamer_tabWidget.setTabText(self.spreedTreeRenamer_tabWidget.indexOf(self.renaming_tab), QCoreApplication.translate("MainWindow", u"Renaming", None))
        self.materialTag_label.setText(QCoreApplication.translate("MainWindow", u"Material Tag", None))
        self.materialTag_lineEdit.setPlaceholderText("")
        self.useVariantNum_checkBox.setText(QCoreApplication.translate("MainWindow", u"Use Variant Numbering", None))
        self.variantNum_lineEdit.setPlaceholderText("")
        self.diffuseMap_label.setText(QCoreApplication.translate("MainWindow", u"Diffuse Map", None))
        self.diffuseMap_lineEdit.setPlaceholderText("")
        self.glossMap_label.setText(QCoreApplication.translate("MainWindow", u"Gloss Map", None))
        self.glossMap_lineEdit.setPlaceholderText("")
        self.normalMap_label.setText(QCoreApplication.translate("MainWindow", u"Normal map", None))
        self.normalMap_lineEdit.setPlaceholderText("")
        self.heightMap_label.setText(QCoreApplication.translate("MainWindow", u"Height Map", None))
        self.heightMap_lineEdit.setPlaceholderText("")
        self.opacityMap_label.setText(QCoreApplication.translate("MainWindow", u"Opacity Map", None))
        self.opacityMap_lineEdit.setPlaceholderText("")
        self.sscMap_label.setText(QCoreApplication.translate("MainWindow", u"Subsurface Colour Map", None))
        self.sscMap_lineEdit.setPlaceholderText("")
        self.ssaMap_label.setText(QCoreApplication.translate("MainWindow", u"Subsurface Amount Map", None))
        self.ssaMap_lineEdit.setPlaceholderText("")
        self.aoMap_label.setText(QCoreApplication.translate("MainWindow", u"AO Map", None))
        self.aoMap_lineEdit.setPlaceholderText("")
        self.spreedTreeRenamer_tabWidget.setTabText(self.spreedTreeRenamer_tabWidget.indexOf(self.namingConvention_tab), QCoreApplication.translate("MainWindow", u"Naming Convention", None))
    # retranslateUi

