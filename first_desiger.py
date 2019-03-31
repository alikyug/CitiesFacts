from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random
import os
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MyFirstGame.ui', self)

        self.radioButton.toggled.connect(lambda: self.inserter_paris())

        self.radioButton_2.toggled.connect(lambda: self.inserter_rome())

        self.radioButton_3.toggled.connect(lambda: self.inserter_madrid())

        self.radioButton_4.toggled.connect(lambda: self.inserter_tokyo())

        self.pushButton.clicked.connect(self.update_fact)

        #self.plainTextEdit.setEnabled(False)

        im = QPixmap('Madrid/madrid1.jpg')
        self.image_label.setPixmap(im)
        self.image_label.setScaledContents(True)

    def fact_picker(self, city):
        facts_city = str(city).capitalize()
        with open(facts_city + '.txt', 'r', encoding='utf8') as f:
            fact_list = f.readlines()
        current_fact = self.plainTextEdit.toPlainText()
        fact = random.choice(fact_list)
        while current_fact == fact:
            fact = random.choice(fact_list)
        self.plainTextEdit.clear()
        self.plainTextEdit.insertPlainText(fact)

    def image_picker(self, city):  #use WHILE to get distinct image:
        # current_image = self.image_label.
        images = os.listdir(city)
        rand_image = random.choice(images)
        im = QPixmap(city + '/' + rand_image)
        self.image_label.setPixmap(im)

    def update_fact(self):
        if self.radioButton.isChecked():
            city = 'Paris'
            self.fact_picker(city)
            self.image_picker(city)

            #change Paris picture
            #images_paris = os.listdir('Paris')

            #rand_image = random.choice(images_paris)
            #im = QPixmap('Paris/' + rand_image)
            #self.image_label.setPixmap(im)

        elif self.radioButton_2.isChecked():
            city = 'Rome'
            self.fact_picker(city)
            self.image_picker(city)

        elif self.radioButton_3.isChecked():
            city = 'Madrid'
            self.fact_picker(city)
            self.image_picker(city)

        elif self.radioButton_4.isChecked():
            city = 'Tokyo'
            self.fact_picker(city)
            self.image_picker(city)

    def inserter_paris(self):
        city = 'Paris'
        self.fact_picker(city)

    def inserter_rome(self):
        city = 'Rome'
        self.fact_picker(city)

    def inserter_madrid(self):
        city = 'Madrid'
        self.fact_picker(city)

    def inserter_tokyo(self):
        city = 'Tokyo'
        self.fact_picker(city)


app = QApplication([])
w = Window()
w.show()
# to handle exit
sys.exit(app.exec())



