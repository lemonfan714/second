from fileinput import filename

from PIL.ImageOps import scale
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageOps, ImageFilter

workdir = ''

app = QApplication([])
wind = QWidget()
wind.resize(600, 600)

#Лейауты
main_l = QHBoxLayout()
ver_1_l = QVBoxLayout()
ver_2_l = QVBoxLayout()
hor_l = QHBoxLayout()

#Кнопки
folder_btn = QPushButton('Папка')
files_list_widget = QListWidget()
img_label = QLabel('Картинка')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркально')
sharpness_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч/Б')
save_btn = QPushButton('Сохранить')
ultrabutton = QPushButton('Сбросить фильтры')
joke_btn = QPushButton('рулетка')

#Привязка
wind.setLayout(main_l)
main_l.addLayout(ver_1_l)
main_l.addLayout((ver_2_l))

ver_1_l.addWidget(folder_btn)
ver_1_l.addWidget(files_list_widget)

ver_2_l.addWidget(img_label)
ver_2_l.addLayout(hor_l)

hor_l.addWidget(left_btn)
hor_l.addWidget(right_btn)
hor_l.addWidget(mirror_btn)
hor_l.addWidget(sharpness_btn)
hor_l.addWidget(bw_btn)
hor_l.addWidget(save_btn)
hor_l.addWidget(ultrabutton)
hor_l.addWidget(joke_btn)

#Доля марштрутки
def joke():
    image = Image.open('../Garbage/Снимок экрана 2024-11-05 130807.png')
    image.show()

class ImageProcessor:
    def __init__(self):
        self.filename = None
        self.img = None
        self.dir = 'Modified/'

    def load_img(self, dir, filename):
        self.workdir = dir
        self.filename = filename
        path = os.path.join(self.workdir, self.filename)
        self.original = Image.open(path)
        self.img = self.original

    def show_img(self, path):
        pixmap = QPixmap(path)
        high, width = img_label.height(), img_label.width()
        scaled = pixmap.scaled(high, width, Qt.KeepAspectRatio)
        img_label.setPixmap(scaled)
        img_label.setVisible(True)

    def save_img(self):
        path = os.path.join(self.workdir, self.dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        img_path = os.path.join(path, self.filename)
        self.img.save(img_path)

    def do_bw(self):
        self.img = self.img.convert('L')
        self.save_img()
        path= os.path.join(self.workdir, self.dir, self.filename)
        self.show_img(path)

    def do_mirror(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_img()
        path= os.path.join(self.workdir, self.dir, self.filename)
        self.show_img(path)

    def do_reset(self):
        path = os.path.join(self.workdir, self.filename)
        self.show_img(path)


workimage = ImageProcessor()

def show_choosen():
    if files_list_widget.currentRow() >= 0:
        filename = files_list_widget.currentItem().text()
        workimage.load_img(workdir, filename)
        path = os.path.join(workimage.workdir, workimage.filename)
        workimage.show_img(path)

def filter_files(files:list, extensions:list):
    res = []
    for name in files:
        for exct in extensions:
            if name.endswith(exct):
                res.append(name)
    return res

def show_folder_files():
    global workdir
    workdir = QFileDialog().getExistingDirectory(wind, 'Выберите папку')
    if workdir != '':
        folder_files = os.listdir(workdir)
        ext_s = ['png', 'jpeg', 'gif', 'jpg']
        files = filter_files(folder_files, ext_s)
        files_list_widget.clear()
        files_list_widget.addItems(files)

folder_btn.clicked.connect(show_folder_files)
joke_btn.clicked.connect(joke)
files_list_widget.currentRowChanged.connect(show_choosen)
bw_btn.clicked.connect(workimage.do_bw)
mirror_btn.clicked.connect(workimage.do_mirror)


wind.show()
app.exec_()