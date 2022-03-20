from pytube import YouTube  # Retirar musics do Youtube
from PyQt5 import uic, QtWidgets  # Interface
from PyQt5.QtGui import QPixmap  # Interface
from PyQt5.QtWidgets import QFileDialog  # Interface
import os  # comandos cmd
import requests  # requests para trocar a imagem


def check():  # checar local do download
    global local
    local = QFileDialog.getExistingDirectory()


def mp4():  # download para video
    try:
        link = login.lineEdit.text()  # Infos do video
        video = YouTube(link)  # Infos do video
        try:
            stream = video.streams.get_highest_resolution()  # Qualidade no Full
            stream.download(local)  # Download na pasta selecionada
            login.label.setText(video.title)  # Informaçoes do video/musica
            login.label_4.setText(video.author)  # Informaçoes do video/musica
            label = login.label_img  # imagem thumb
            url = video.thumbnail_url  # imagem thumb
            pega_url = requests.get(url)  # imagem thumb
            img = QPixmap()  # imagem thumb
            img.loadFromData(pega_url.content)  # imagem thumb
            label.setPixmap(img)  # imagem thumb
            label.setScaledContents(True)  # imagem thumb

        except:
            login.label.setText("Selecione o caminho da pasta!")
    except:
        login.label.setText('Link Incorreto!')


def music():
    try:
        link = login.lineEdit.text()  # Infos do video
        ys = YouTube(link)  # Infos do video
        v = ys.streams.get_audio_only()  # Selecionado download em modo audio
        try:
            out_file = v.download(local)  # Download na pasta selecionada
            login.label.setText(ys.title)  # Informaçoes do video/musica
            login.label_4.setText(ys.author)  # Informaçoes do video/musica
            label = login.label_img  # imagem thumb
            url = ys.thumbnail_url  # imagem thumb
            pega_url = requests.get(url)  # imagem thumb
            img = QPixmap()  # imagem thumb
            img.loadFromData(pega_url.content)  # imagem thumb
            label.setPixmap(img)  # imagem thumb
            label.setScaledContents(True)  # imagem thumb
            base, ext = os.path.splitext(out_file)  # transformando em mp3
            new_file = base + '.mp3'  # transformando em mp3
            os.rename(out_file, new_file)  # transformando em mp3
        except:
            login.label.setText("Selecione o caminho da pasta!")
    except:
        login.label.setText('Link Incorreto')


app = QtWidgets.QApplication([])  # base
login = uic.loadUi("main.ui")  # base
login.pushButton.clicked.connect(music)  # base
login.pushButton_2.clicked.connect(mp4)  # base
login.pushButton_3.clicked.connect(check)  # base
label = login.label_img  # base

login.show()  # iniciador
app.exec()  # iniciador
