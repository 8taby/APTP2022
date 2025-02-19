# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sdcn.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('src/icons/songdoIcon.PNG'))
        Dialog.resize(400, 600)
        Dialog.setMinimumSize(QtCore.QSize(400, 600))
        Dialog.setMaximumSize(QtCore.QSize(400, 600))
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnWidth(0, int(self.tableWidget.width()*1/5))
        self.tableWidget.setColumnWidth(1, int(self.tableWidget.width()*4/5))
        self.tableWidget.setHorizontalHeaderLabels(['Node', '건물 이름'])
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('gatea'))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem('연돌(임시정문)'))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('gateb'))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem('서문(트스 방향)'))
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem('UML'))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem('언더우드기념도서관(1층 출입구)'))    
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem('Yplaza'))
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem('언더우드기념도서관(지하1층), Y-plaza'))
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem('YICfield'))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem('운동장'))
        self.tableWidget.setItem(5, 0, QtWidgets.QTableWidgetItem('LiberA'))
        self.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem('자유관A'))
        self.tableWidget.setItem(6, 0, QtWidgets.QTableWidgetItem('LiberB'))
        self.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem('자유관B'))
        self.tableWidget.setItem(7, 0, QtWidgets.QTableWidgetItem('Futsal'))
        self.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem('풋살장'))
        self.tableWidget.setItem(8, 0, QtWidgets.QTableWidgetItem('WisA'))
        self.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem('지혜관A'))
        self.tableWidget.setItem(9, 0, QtWidgets.QTableWidgetItem('WisB'))
        self.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem('지혜관B'))
        self.tableWidget.setItem(10, 0, QtWidgets.QTableWidgetItem('WisC'))
        self.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem('지혜관C'))
        self.tableWidget.setItem(11, 0, QtWidgets.QTableWidgetItem('Woori'))
        self.tableWidget.setItem(11, 1, QtWidgets.QTableWidgetItem('우리은행'))
        self.tableWidget.setItem(12, 0, QtWidgets.QTableWidgetItem('DormA'))
        self.tableWidget.setItem(12, 1, QtWidgets.QTableWidgetItem('송도학사A'))
        self.tableWidget.setItem(13, 0, QtWidgets.QTableWidgetItem('DormB'))
        self.tableWidget.setItem(13, 1, QtWidgets.QTableWidgetItem('송도학사B'))
        self.tableWidget.setItem(14, 0, QtWidgets.QTableWidgetItem('DormC'))
        self.tableWidget.setItem(14, 1, QtWidgets.QTableWidgetItem('송도학사C'))
        self.tableWidget.setItem(15, 0, QtWidgets.QTableWidgetItem('DormD'))
        self.tableWidget.setItem(15, 1, QtWidgets.QTableWidgetItem('송도학사D'))
        self.tableWidget.setItem(16, 0, QtWidgets.QTableWidgetItem('DormE'))
        self.tableWidget.setItem(16, 1, QtWidgets.QTableWidgetItem('송도학사E'))
        self.tableWidget.setItem(17, 0, QtWidgets.QTableWidgetItem('DormF'))
        self.tableWidget.setItem(17, 1, QtWidgets.QTableWidgetItem('송도학사F'))
        self.tableWidget.setItem(18, 0, QtWidgets.QTableWidgetItem('DormG'))
        self.tableWidget.setItem(18, 1, QtWidgets.QTableWidgetItem('송도학사G'))
        self.tableWidget.setItem(19, 0, QtWidgets.QTableWidgetItem('VeriA'))
        self.tableWidget.setItem(19, 1, QtWidgets.QTableWidgetItem('진리관A'))
        self.tableWidget.setItem(20, 0, QtWidgets.QTableWidgetItem('VeriB'))
        self.tableWidget.setItem(20, 1, QtWidgets.QTableWidgetItem('진리관B'))
        self.tableWidget.setItem(21, 0, QtWidgets.QTableWidgetItem('VeriC'))
        self.tableWidget.setItem(21, 1, QtWidgets.QTableWidgetItem('진리관C'))
        self.tableWidget.setItem(22, 0, QtWidgets.QTableWidgetItem('VeriD'))
        self.tableWidget.setItem(22, 1, QtWidgets.QTableWidgetItem('진리관D'))
        self.tableWidget.setItem(23, 0, QtWidgets.QTableWidgetItem('SLBigen'))
        self.tableWidget.setItem(23, 1, QtWidgets.QTableWidgetItem('에스엘바이젠의학연구소'))
        self.tableWidget.setItem(24, 0, QtWidgets.QTableWidgetItem('Vision'))
        self.tableWidget.setItem(24, 1, QtWidgets.QTableWidgetItem('종합관'))
        self.tableWidget.setItem(25, 0, QtWidgets.QTableWidgetItem('Chapl'))
        self.tableWidget.setItem(25, 1, QtWidgets.QTableWidgetItem('크리스틴채플'))
        self.tableWidget.setItem(26, 0, QtWidgets.QTableWidgetItem('IMCH'))
        self.tableWidget.setItem(26, 1, QtWidgets.QTableWidgetItem('국제캠퍼스기념관'))
        self.tableWidget.setItem(27, 0, QtWidgets.QTableWidgetItem('Mntnc'))
        self.tableWidget.setItem(27, 1, QtWidgets.QTableWidgetItem('파워플랜트'))
        self.tableWidget.setItem(28, 0, QtWidgets.QTableWidgetItem('Ghome'))
        self.tableWidget.setItem(28, 1, QtWidgets.QTableWidgetItem('저에너지친환경실험주택'))
        self.tableWidget.setItem(29, 0, QtWidgets.QTableWidgetItem('posco'))
        self.tableWidget.setItem(29, 1, QtWidgets.QTableWidgetItem('포스코그린빌딩'))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
