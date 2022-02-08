from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ext_ico_path = {
                "TXT":"images/extensions/txt.png",
                "EXE":"images/extensions/exe.png",
                "MP4":"images/extensions/mp4.png",
                "MP3":"images/extensions/mp3.png",
                "ISO":"images/extensions/iso.png",
                "ZIP":"images/extensions/zip.png",
                "RAR":"images/extensions/zip.png",
                "CSV":"images/extensions/csv.png",
                "PPT":"images/extensions/ppt.png",
                "XLS":"images/extensions/xls.png",
                "DOC":"images/extensions/doc.png",
                "AVI":"images/extensions/avi.png",
                "PDF":"images/extensions/pdf.png",
                "JPEG":"images/extensions/image.png",
                "PNG":"images/extensions/image.png",
                "MKV":"images/extensions/mkv.png",
                "file":"images/extensions/file.png"
        }

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 846)
        MainWindow.setWindowIcon(QtGui.QIcon('images/logo.svg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_10 = QtWidgets.QHBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setStyleSheet("text-align: left;\n"
        "padding-left: 10;\n"
        "padding-right: 10px;\n"
        "border: 2px solid black;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);\n"
        "font: 75 14pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.verticalLayout_10)

        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("text-align: left;\n"
        "padding: 3;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "color: rgb(85, 0, 127);\n"
        "font: 75 11pt \"MS Sans Serif\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_14.addWidget(self.lineEdit)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setStyleSheet("padding: 4;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);\n"
        "text-align: left;\n"
        "border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "font: 75 11pt \"MS Sans Serif\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_14.addWidget(self.pushButton_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        #############################################################################################################
        self.userScroll = QtWidgets.QScrollArea()
        self.userWidget = QtWidgets.QWidget()

        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        usrData = [{"name": "Ashes"}, {"name": "Utkarsh"}, {"name": "Mondal"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}, {"name": "Utkarsh"}]
        for i in range(0, len(usrData)):
                self.usrHbox = QtWidgets.QHBoxLayout()
                self.usrHbox.setObjectName("hbox_" + str(i))
                _translate = QtCore.QCoreApplication.translate

                self.usrlabel = QtWidgets.QLabel(self.userWidget)
                self.usrlabel.setStyleSheet("text-align: left;\n"
                "padding-left: 10;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.usrlabel.setObjectName("usrlabel_" + str(i))
                self.usrlabel.setText(_translate("MainWindow", usrData[i]["name"].upper() + "_" + str(i) ))
                self.usrHbox.addWidget(self.usrlabel)

                self.msgPushButton = QtWidgets.QPushButton(self.userWidget)
                self.msgPushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.msgPushButton.setStyleSheet("font-size: 15px;\n"
                "margin: 5px 10px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(255, 255, 127);"
                # "background-color:rgb(198, 226, 247);"
                "background-color: rgb(237, 237, 237);"
                
                )
                self.msgPushButton.setObjectName("msgPushButton_" + str(i))
                
                # self.msgPushButton.setText(_translate("MainWindow", "M"))
                ##msgPushButton icon
                self.msgPushButton.setIcon(QtGui.QIcon('images/chat.png'))
                self.msgPushButton.setIconSize(QtCore.QSize(32,32))
                
                self.usrHbox.addWidget(self.msgPushButton)

                self.filePushButton = QtWidgets.QPushButton(self.userWidget)
                self.filePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.filePushButton.setStyleSheet("font-size: 15px;\n"
                # "border: 2px solid black;\n"
                "margin: 5px 10px;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                # "background-color: rgb(250, 240, 200);"
                "background-color: rgb(237, 237, 237);"
                
                )
                self.filePushButton.setObjectName("filePushButton_" + str(i))
                
                # self.filePushButton.setText(_translate("MainWindow", "F"))
                #filePushButton icon
                self.filePushButton.setIcon(QtGui.QIcon('images/shared-folder.png'))
                self.filePushButton.setIconSize(QtCore.QSize(32,32))
                
                self.usrHbox.addWidget(self.filePushButton)

                self.usrHbox.setStretch(0, 5)
                self.usrHbox.setStretch(1, 1)
                self.usrHbox.setStretch(2, 1)
                self.verticalLayout_9.addLayout(self.usrHbox)

                self.usrline = QtWidgets.QFrame(self.centralwidget)
                self.usrline.setFrameShape(QtWidgets.QFrame.HLine)
                self.usrline.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.usrline.setObjectName("usrline_" + str(i))
                self.verticalLayout_9.addWidget(self.usrline)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)

        self.userWidget.setLayout(self.verticalLayout_9)
        #Scroll Area Properties
        self.userScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.userScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userScroll.setWidgetResizable(True)
        self.userScroll.setWidget(self.userWidget)
        self.verticalLayout_5.addWidget(self.userScroll)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setStyleSheet("text-align: left;\n"
        "padding-left: 10;\n"
        "padding-right: 10px;\n"
        "border: 2px solid black;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);\n"
        "font: 75 14pt \"MS Sans Serif\";")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.userSrchScroll = QtWidgets.QScrollArea()
        self.userSearchWidget = QtWidgets.QWidget()

        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")

        userFilesData = [
                {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
                {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
                {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
                {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
                {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
                {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
                {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
                {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
                {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
                {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
        ]

        for i in range(0, len(userFilesData)):
                self.usrSrchHbox = QtWidgets.QHBoxLayout()
                self.usrSrchHbox.setObjectName("srchHbox_" + str(i))
                _translate = QtCore.QCoreApplication.translate

                self.fileTypeBtn = QtWidgets.QPushButton(self.userSearchWidget)
                self.fileTypeBtn.setStyleSheet("margin: 5px 10px;\n"
                "font-size: 15px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                "background-color: rgb(237, 237, 237);"
                )
                self.fileTypeBtn.setObjectName("fileTypeBtn" + str(i))

                path = ext_ico_path[userFilesData[i]["type"]] if userFilesData[i]["type"] in ext_ico_path.keys() else ext_ico_path["file"]
                self.fileTypeBtn.setIcon(QtGui.QIcon(path))
                self.fileTypeBtn.setIconSize(QtCore.QSize(35,35))
                self.usrSrchHbox.addWidget(self.fileTypeBtn)

                self.fileName = QtWidgets.QLabel(self.userSearchWidget)
                self.fileName.setStyleSheet("text-align: left;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.fileName.setObjectName("fileName" + str(i))
                self.fileName.setText(_translate("MainWindow", userFilesData[i]["fileName"]))
                self.fileName.setToolTip(userFilesData[i]["fileName"])
                self.usrSrchHbox.addWidget(self.fileName)

                self.fileSize = QtWidgets.QLabel(self.userSearchWidget)
                self.fileSize.setStyleSheet("text-align: left;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.fileSize.setObjectName("fileSize" + str(i))
                self.fileSize.setText(_translate("MainWindow", userFilesData[i]["fileSize"]))
                self.usrSrchHbox.addWidget(self.fileSize)

                self.deleteBtn = QtWidgets.QPushButton(self.userSearchWidget)
                self.deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.deleteBtn.setStyleSheet("QPushButton {\n"
                "margin: 5px 10px;\n"
                "font-size: 15px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                # "background-color: rgb(147, 207, 250);"
                "background-color: rgb(237, 237, 237);"
                "}\n"
                "QPushButton::hover {\n"
                "    border: 2px solid red;\n"
                "    background-color: red;\n"
                "}\n"
                )
                self.deleteBtn.setObjectName("deleteBtn" + str(i))
                self.deleteBtn.setIcon(QtGui.QIcon('images/delete.png'))
                self.deleteBtn.setIconSize(QtCore.QSize(32,32))
                self.usrSrchHbox.addWidget(self.deleteBtn)

                self.usrSrchHbox.setStretch(0, 1)
                self.usrSrchHbox.setStretch(1, 4)
                self.usrSrchHbox.setStretch(2, 2)
                self.usrSrchHbox.setStretch(3, 1)
                self.verticalLayout_18.addLayout(self.usrSrchHbox)

                self.usrline = QtWidgets.QFrame(self.userSearchWidget)
                self.usrline.setFrameShape(QtWidgets.QFrame.HLine)
                self.usrline.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.usrline.setObjectName("usrline_" + str(i))
                self.verticalLayout_18.addWidget(self.usrline)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem1)

        self.userSearchWidget.setLayout(self.verticalLayout_18)
        #Scroll Area Properties
        self.userSrchScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.userSrchScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userSrchScroll.setWidgetResizable(True)
        self.userSrchScroll.setWidget(self.userSearchWidget)
        self.verticalLayout_6.addWidget(self.userSrchScroll)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uploadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uploadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uploadBtn.setStyleSheet("QPushButton {\n"
        "    font: 75 18pt \"Georgia\";\n"
        "    padding: 5px;\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "    color:rgba(255, 255, 255, 210);\n"
        "    border: 2px solid black;\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
        "}\n"
        "\n"
        "QPushButton::pressed {\n"
        "    padding-left:5px;\n"
        "    padding-top:5px;\n"
        "    background-color:rgba(105, 118, 132, 200);\n"
        "}")
        self.uploadBtn.setObjectName("uploadBtn")
        self.horizontalLayout_8.addWidget(self.uploadBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 10)

        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setStyleSheet("text-align: left;\n"
        "padding: 7;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "color: rgb(85, 0, 127);\n"
        "font: 75 11pt \"MS Sans Serif\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_11.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("padding: 8;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);\n"
        "text-align: left;\n"
        "border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "font: 75 11pt \"MS Sans Serif\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        # self.line_8 = QtWidgets.QFrame(self.centralwidget)
        # self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_8.setObjectName("line_8")
        # self.verticalLayout_7.addWidget(self.line_8)

        ###########################################################################################################
        self.fileSrchScroll = QtWidgets.QScrollArea()
        self.fileSearchWidget = QtWidgets.QWidget()

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        # Sample Data
        fileSrchData = [
                {"type": "TXT", "fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
                {"type": "EXE", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "MP4", "fileName": "Hotel.Transylvania.4.Transformania.2022.1080p.WEBRip.x264-RARBG/Hotel.Transylvania.4.Transformania.2022.1080p.WEBRip.x264-RARBG.mp4", "owner": "Utkarsh", "size": "40MB"},
                {"type": "MP3", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "AVI", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "ISO", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "ZIP", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "RAR", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "CSV", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "PPT", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "XLS", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "DOC", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "PDF", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "JPEG", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "BIN", "fileName": "Road-Rash", "owner": "Utkarsh", "size": "40MB"},
                {"type": "MKV", "fileName": "Eternals.2021.2160p.WEB-DL.x265.10bit.SDR.DDP5.1.Atmos-NOGRP.mkv", "owner": "Utkarsh", "size": "40MB"}
                
        ]

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.fileSearchWidget)
        self.label_18.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.label_18)
        self.label_17 = QtWidgets.QLabel(self.fileSearchWidget)
        self.label_17.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.label_16 = QtWidgets.QLabel(self.fileSearchWidget)
        self.label_16.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.label_15 = QtWidgets.QLabel(self.fileSearchWidget)
        self.label_15.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.label_14 = QtWidgets.QLabel(self.fileSearchWidget)
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 7)
        self.horizontalLayout_5.setStretch(3, 2)
        self.horizontalLayout_5.setStretch(4, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.line_9 = QtWidgets.QFrame(self.fileSearchWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_13.addWidget(self.line_9)

        for i in range(0, len(fileSrchData)):
                self.fileSrchHbox = QtWidgets.QHBoxLayout()
                self.fileSrchHbox.setObjectName("fileSrchHbox_" + str(i))
                _translate = QtCore.QCoreApplication.translate

                self.fileType = QtWidgets.QPushButton(self.fileSearchWidget)
                self.fileType.setStyleSheet("margin: 5px 7px;\n"
                "font-size: 15px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                "background-color: rgb(237, 237, 237);"
                )
                self.fileType.setObjectName("fileType_" + str(i))
                
                # self.fileType.setText(_translate("MainWindow", fileSrchData[i]["type"]))
                
                # self.fileType.setText(_translate("MainWindow", "D"))
                path = ext_ico_path[fileSrchData[i]["type"]] if fileSrchData[i]["type"] in ext_ico_path.keys() else ext_ico_path["file"]
                self.fileType.setIcon(QtGui.QIcon(path))
                self.fileType.setIconSize(QtCore.QSize(35,35))
                
                self.fileSrchHbox.addWidget(self.fileType)

                self.fileName = QtWidgets.QLabel(self.fileSearchWidget)
                self.fileName.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.fileName.setStyleSheet("text-align: center;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.fileName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.fileName.setObjectName("fileName" + str(i))
                self.fileName.setText(_translate("MainWindow", fileSrchData[i]["fileName"][:20]))
                self.fileName.setToolTip(fileSrchData[i]["fileName"])
                self.fileSrchHbox.addWidget(self.fileName)

                self.ownerName = QtWidgets.QLabel(self.fileSearchWidget)
                self.ownerName.setStyleSheet("text-align: center;\n"
                "padding-left: 10;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.ownerName.setAlignment(QtCore.Qt.AlignCenter)
                self.ownerName.setObjectName("ownerName" + str(i))
                self.ownerName.setText(_translate("MainWindow", fileSrchData[i]["owner"].upper() + "_" + str(i) ))
                self.fileSrchHbox.addWidget(self.ownerName)

                self.fileSize = QtWidgets.QLabel(self.fileSearchWidget)
                self.fileSize.setStyleSheet("text-align: center;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
                self.fileSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.fileSize.setObjectName("fileSize" + str(i))
                self.fileSize.setText(_translate("MainWindow", fileSrchData[i]["size"]))
                self.fileSrchHbox.addWidget(self.fileSize)

                self.dwnloadBtn = QtWidgets.QPushButton(self.fileSearchWidget)
                self.dwnloadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.dwnloadBtn.setStyleSheet("QPushButton {\n"
                "margin: 5px 10px;\n"
                "font-size: 15px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                # "background-color: rgb(147, 207, 250);"
                "background-color: rgb(237, 237, 237);"
                "}\n"
                "QPushButton::hover {\n"
                "    border: 2px solid #ffffff;\n"
                "    background-color: #ffffff;\n"
                "}\n"
                )
                self.dwnloadBtn.setObjectName("dwnloadBtn_" + str(i))
                
                # self.dwnloadBtn.setText(_translate("MainWindow", "D"))
                self.dwnloadBtn.setIcon(QtGui.QIcon('images/download.png'))
                self.dwnloadBtn.setIconSize(QtCore.QSize(32,32))
                
                self.fileSrchHbox.addWidget(self.dwnloadBtn)

                self.fileSrchHbox.setStretch(0, 1)
                self.fileSrchHbox.setStretch(1, 4)
                self.fileSrchHbox.setStretch(2, 4)
                self.fileSrchHbox.setStretch(3, 4)
                self.fileSrchHbox.setStretch(4, 1)
                self.verticalLayout_13.addLayout(self.fileSrchHbox)

                self.line_7 = QtWidgets.QFrame(self.fileSearchWidget)
                self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_7.setObjectName("line_7")
                self.verticalLayout_13.addWidget(self.line_7)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)

        self.fileSearchWidget.setLayout(self.verticalLayout_13)
        #Scroll Area Properties
        self.fileSrchScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.fileSrchScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fileSrchScroll.setWidgetResizable(True)
        self.fileSrchScroll.setWidget(self.fileSearchWidget)
        self.verticalLayout_7.addWidget(self.fileSrchScroll)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 10)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("text-align: left;\n"
        "padding-left: 10;\n"
        "padding-right: 10px;\n"
        "border: 2px solid black;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);\n"
        "font: 75 14pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_16.addWidget(self.label_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_16)

        self.dlFileSrchScroll = QtWidgets.QScrollArea()
        self.dlFileSearchWidget = QtWidgets.QWidget()

        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")

        downloadsList = [
                {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
                {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
                {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
                {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
                {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
                {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
                {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
                {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"}
        ]

        for i in range(0, len(downloadsList)):
                self.dlFileVbox = QtWidgets.QVBoxLayout()
                self.dlFileVbox.setObjectName("dlFileHbox_" + str(i))
                _translate = QtCore.QCoreApplication.translate

                self.dlFileInfoHbox = QtWidgets.QHBoxLayout()
                self.dlFileInfoHbox.setContentsMargins(-1, -1, 0, -1)
                self.dlFileInfoHbox.setObjectName("dlFileInfoHbox" + str(i))

                self.dlFileInfo = QtWidgets.QLabel(self.dlFileSearchWidget)
                self.dlFileInfo.setStyleSheet("text-align: left;\n"
                "margin-top: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 10pt \"Verdana\";")
                self.dlFileInfo.setObjectName("dlFileInfo" + str(i))
                info = downloadsList[i]["fileName"] + " | " + downloadsList[i]["owner"] + " | " + downloadsList[i]["size"]
                self.dlFileInfo.setText(_translate("MainWindow", info))
                self.dlFileInfoHbox.addWidget(self.dlFileInfo)
                self.dlFileVbox.addLayout(self.dlFileInfoHbox)

                self.dlFileProgressHbox = QtWidgets.QHBoxLayout()
                self.dlFileProgressHbox.setObjectName("dlFileProgressHbox")

                self.dlProgressBar = QtWidgets.QProgressBar(self.dlFileSearchWidget)
                self.dlProgressBar.setProperty("value", 24)
                self.dlProgressBar.setObjectName("dlProgressBar")
                self.dlFileProgressHbox.addWidget(self.dlProgressBar)

                self.pOr = QtWidgets.QPushButton(self.dlFileSearchWidget)
                self.pOr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pOr.setStyleSheet("QPushButton {\n"
                # "margin: 5px 10px;\n"
                "font-size: 25px;\n"
                # "border: 2px solid black;\n"
                "border-radius: 10px;\n"
                "padding: 4;\n"
                # "color: rgb(85, 0, 127);\n"
                # "background-color: rgb(85, 255, 255);"
                # "background-color: rgb(147, 207, 250);"
                "background-color: rgb(85, 255, 255);\n"
                "}\n"
                "QPushButton::hover {\n"
                "    border: 2px solid #ffffff;\n"
                "    background-color: #ffffff;\n"
                "}\n"
                )
                self.pOr.setIcon(QtGui.QIcon('images/pause.png'))
                self.dlFileProgressHbox.addWidget(self.pOr)

                self.dlFileProgressHbox.setStretch(0, 25)
                self.dlFileProgressHbox.setStretch(1, 1)
                self.dlFileVbox.addLayout(self.dlFileProgressHbox)
                self.verticalLayout_15.addLayout(self.dlFileVbox)

                self.line_10 = QtWidgets.QFrame(self.dlFileSearchWidget)
                self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_10.setObjectName("line_10")
                self.verticalLayout_15.addWidget(self.line_10)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem3)

        self.dlFileSearchWidget.setLayout(self.verticalLayout_15)
        #Scroll Area Properties
        self.dlFileSrchScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dlFileSrchScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dlFileSrchScroll.setWidgetResizable(True)
        self.dlFileSrchScroll.setWidget(self.dlFileSearchWidget)
        self.verticalLayout_8.addWidget(self.dlFileSrchScroll)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 7)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOCAL-DC++"))
        self.label.setText(_translate("MainWindow", "CURRENT ONLINE USERS"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search a User"))
        self.pushButton_11.setText(_translate("MainWindow", "Search"))
        self.label_19.setText(_translate("MainWindow", "YOUR FILES"))
        self.uploadBtn.setText(_translate("MainWindow", "INSERT A FILE"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Search Files"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "DOWNLOADS"))
        self.label_18.setText(_translate("MainWindow", "Type"))
        self.label_17.setText(_translate("MainWindow", "File-Name"))
        self.label_16.setText(_translate("MainWindow", "Owner"))
        self.label_15.setText(_translate("MainWindow", "Size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
