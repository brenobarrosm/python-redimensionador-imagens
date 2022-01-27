import sys, os
from turtle import width
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resize_image)
        self.btnSave.clicked.connect(self.save_image)

    def open_image(self):
        defaultPath = r'/home/' + os.getlogin() + r'/Imagens'
        img, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            defaultPath,
        )
        self.inputPath.setText(img)
        self.original_img = QPixmap(img)
        self.labelImg.setPixmap(self.original_img)

        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resize_image(self):
        width = int(self.inputWidth.text())
        self.new_img = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_img)
        self.inputWidth.setText(str(self.new_img.width()))
        self.inputHeight.setText(str(self.new_img.height()))

    def save_image(self):
        defaultPath = r'/home/' + os.getlogin() + r'/Imagens'
        img, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            defaultPath
        )
        self.new_img.save(img, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    ri = ResizeImage()
    ri.show()
    qt.exec_()