from pytube import YouTube
from PyQt5 import uic, QtWidgets  # Interface
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import os
import requests


def check():
    global local
    local = QFileDialog.getExistingDirectory()


def mp4():
    try:
        link = login.lineEdit.text()
        video = YouTube(link)
        try:
            stream = video.streams.get_highest_resolution()
            stream.download(local)
            login.label.setText(video.title)
            label = login.label_img
            url = video.thumbnail_url
            pega_url = requests.get(url)
            img = QPixmap()
            img.loadFromData(pega_url.content)
            label.setPixmap(img)
            label.setScaledContents(True)
            login.label_4.setText(video.author)
        except:
            login.label.setText("Selecione o caminho da pasta!")
    except:
        login.label.setText('Link Incorreto!')


def music():
    try:
        link = login.lineEdit.text()
        ys = YouTube(link)
        v = ys.streams.get_audio_only()
        try:
            out_file = v.download(local)
            login.label.setText(ys.title)
            login.label_4.setText(ys.author)
            label = login.label_img
            url = ys.thumbnail_url
            pega_url = requests.get(url)
            img = QPixmap()
            img.loadFromData(pega_url.content)
            label.setPixmap(img)
            label.setScaledContents(True)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except:
            login.label.setText("Selecione o caminho da pasta!")
    except:
        login.label.setText('Link Incorreto')


app = QtWidgets.QApplication([])
login = uic.loadUi("main.ui")
login.pushButton.clicked.connect(music)
login.pushButton_2.clicked.connect(mp4)
login.pushButton_3.clicked.connect(check)
label = login.label_img

login.show()
app.exec()
