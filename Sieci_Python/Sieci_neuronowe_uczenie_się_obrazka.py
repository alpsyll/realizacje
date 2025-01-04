import time
import numpy as np
import matplotlib.pyplot as plt
from IPython.external.qt_for_kernel import QtGui, QtCore
from skimage import data, io
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, \
    QHBoxLayout, QMessageBox
from PyQt5.QtGui import QColor, QFont, QPixmap
import sys
from nltk import flatten
from skimage.io import imread
from skimage import io
from skimage import data, io
from skimage.io import imread

def norm( x):
    return x/63

class NeuralNetwork3():   #tworzenie sieci
    def __init__(self, structure, eta=0.1):    #struktura
        assert len(structure) == 5
        self.structure = structure
        self.input_dim = structure[0]
        self.hidden_dim1 = structure[1]
        self.hidden_dim2 = structure[2]
        self.hidden_dim3 = structure[3]
        self.output_dim = structure[4]
        self.eta = eta

        self.w1 = 2 * np.random.randn(self.input_dim, self.hidden_dim1) - 1
        self.w2 = 2 * np.random.randn(self.hidden_dim1, self.hidden_dim2) - 1
        self.w3 = 2 * np.random.randn(self.hidden_dim2, self.hidden_dim3) - 1
        self.w4 = 2 * np.random.randn(self.hidden_dim3, self.output_dim) - 1
        self.errors = []

    def sigmoid(self, x):   #funkcja sigmoidalna
        return 1 / (1 + np.exp(-x))

    def forward(self, x):        #propagacja forward
        self.y0 = x.copy()
        self.a1 = np.dot(self.y0, self.w1)
        self.y1 = self.sigmoid(self.a1)

        self.a2 = np.dot(self.y1, self.w2)
        self.y2 = self.sigmoid(self.a2)

        self.a3 = np.dot(self.y2, self.w3)
        self.y3 = self.sigmoid(self.a3)

        self.a4 = np.dot(self.y3, self.w4)
        self.y4 = self.sigmoid(self.a4)

        return self.y4

    def backward(self, y):  #propagacja wstecz
        self.epsilon4 = y - self.y4
        self.delta4 = self.epsilon4 * self.y4 * (1 - self.y4)

        self.epsilon3 = self.delta4.dot(self.w4.T)
        self.delta3 = self.epsilon3 * self.y3 * (1 - self.y3)

        self.epsilon2 = self.delta3.dot(self.w3.T)
        self.delta2 = self.epsilon2 * self.y2 * (1 - self.y2)

        self.epsilon1 = self.delta2.dot(self.w2.T)
        self.delta1 = self.epsilon1 * self.y1 * (1 - self.y1)

        self.w4 += self.eta * np.dot(self.y3.T, self.delta4)
        self.w3 += self.eta * np.dot(self.y2.T, self.delta3)
        self.w2 += self.eta * np.dot(self.y1.T, self.delta2)
        self.w1 += self.eta * np.dot(self.y0.T, self.delta1)

    def train(self, x, y, epochs):   #uczenie
        for epoch in range(epochs):
            self.forward(x)
            self.backward(y)
            self.errors.append(self.loss(y, self.y4))

    def loss(self, ty, y):
        return np.mean(np.square(ty - y))

class Grid(QWidget):
    def __init__(self):
        super().__init__()

        self.NN = NeuralNetwork3(structure=[30, 60, 150, 80, 3], eta=0.002)
        self.layout=QGridLayout()
        self.obrazek = None

        self.status = QLabel("Wybierz obrazek naucz i odwzoruj (klawiatura: 1/2/u/r)")
        self.status.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.status, 1, 0, 1, 3)

    #panele i przyciski

        przyciski = [
            ('obrazek1', self.obrazek1),
            ('obrazek2', self.obrazek2),
            ('ucz się', self.ucz_sie),
            ('rysuj', self.rysuj)
        ]

        hbox2 = QHBoxLayout()

        for label, x in przyciski:
            przycisk = QPushButton(label)
            przycisk.clicked.connect(x)
            hbox2.addWidget(przycisk)


        self.label_3 = QLabel(self)
        hbox2.addWidget(self.label_3)

        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label3)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.label4)

        self.layout.addLayout(hbox, 0, 0)
        self.layout.addLayout(hbox2, 0, 1)
        self.layout.addLayout(hbox3, 0, 2)

        self.layout.setColumnMinimumWidth(0, 300)  # Ustawia minimalną szerokość pierwszej kolumny
        self.layout.setRowMinimumHeight(0, 300)
        self.layout.setAlignment(hbox2, Qt.AlignCenter)
        self.setLayout(self.layout)
        self.show()

    def laduj(self, image_path):
        self.pixmap = QPixmap(image_path)
        self.pixmap4 = self.pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.label3.setPixmap(self.pixmap4)
        self.obrazek = io.imread(image_path)


    def obrazek1(self):
        self.laduj('tt.jpg')

    def obrazek2(self):
        self.laduj('tt2.jpg')

    def status_zmiana(self, tekst, kolor):

        self.status.setText(tekst)
        self.status.setStyleSheet(f"""
                        QLabel {{ font-size: 14px; color: {kolor}; }} """)
        QApplication.processEvents()

    def ucz_sie(self): #uczenie+wykres bledow
        if self.obrazek is None:
            QMessageBox.warning(self, "Błąd", "Najpierw wybierz obrazek!")
            return


        self.status_zmiana("Uczenie w toku, czekaj...", "red")

        QApplication.processEvents()
        self.x11 = np.mgrid[0:64, 0:64].reshape(2, -1).T
        self.x = norm(self.x11)
        self.y1 = self.obrazek.reshape(-1, 3)
        self.y = self.y1 / 255

        self.combined = np.concatenate((self.x, np.sin(self.x), np.cos(self.x), np.sin(2 * self.x), np.cos(3 * self.x), np.sin(4 * self.x), np.cos(4 * self.x),
                                   np.sin(5 * self.x), np.cos(5 * self.x), np.sin(6 * self.x), np.cos(6 * self.x), np.sin(7 * self.x),
                                   np.cos(7 * self.x), np.sin(8 * self.x), np.cos(8 * self.x)), axis=1)


        self.NN.train(np.array(self.combined), np.array(self.y),500)

        plt.figure()
        plt.plot(range(len(self.NN.errors)), self.NN.errors)
        plt.xlabel('Iteracja')
        plt.ylabel('Błąd')
        plt.title('Wykres błędów')
        plt.show()

        self.trained = True

        self.status_zmiana("Zakończono", "green")


    def rysuj(self):  #przewidywanie obrazka

        if not hasattr(self, 'obrazek') or self.obrazek is None:

            QtGui.QMessageBox.warning(self, "Brak obrazka", "Nie wybrano obrazka do przetwarzania!")
            return

        if not hasattr(self, 'trained') or not self.trained:

            QtGui.QMessageBox.warning(self, "Model nienauczony",
                                      "Najpierw naciśnij przycisk 'ucz się', aby nauczyć model!")
            return

        predicted_image = np.zeros((64, 64, 3))
        w = self.NN.forward(np.array(self.combined))

        for i in range(len(self.x)):
            x2, y2 = self.x11[i]
            predicted_image[x2, y2] = w[i]


        predicted_image = np.multiply(predicted_image, 255).astype(np.uint8)
        height, width, channel = predicted_image.shape
        bytes_per_line = 3 * width
        qimage = QtGui.QImage(predicted_image.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)

        self.pixmap2 = QtGui.QPixmap.fromImage(qimage)
        self.pixmap5 = self.pixmap2.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.label4.setPixmap(self.pixmap5)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 960, 400)

        #styl przyciskow i wyskakujacych okienek
        self.setWindowTitle("Sieci neuronowe - uczenie się obrazka")
        self.setStyleSheet("""
            QPushButton {
                border: 1px solid #cccccc; 
                border-radius: 12px; 
                padding: 15px 12px; 
                color: black; 
                font-size: 15px; 
                
            }
            QPushButton:hover {
                background-color: #00ccbe; 
                border-color: green; 
            }
            QPushButton:pressed {
                background-color: #d4edda; 
                border-color: #28a745; 
            }
            QLabel {
                font-size: 13px; 
                color: #4a4a4a; 
            }
            QWidget {
                background-color: white; 
            }
            QMessageBox {
                background-color: white; 
                border-radius: 8px; 
            }
            QMessageBox QLabel {
                font-size: 14px; 
                color: black; 
            }
            QMessageBox QPushButton {
                border: 1px solid #cccccc; 
                border-radius: 6px; 
                padding: 6px 10px; 
                background-color: white;
            }
            QMessageBox QPushButton:hover {
                background-color: #00ccbe; 
                border-color: green; 
            }
        """)

        self.grid=Grid()
        self.setCentralWidget(self.grid)
        self.show()

    def keyPressEvent(self, event):   #polączenie z klawiturą
        key2 = event.text()
        print(key2)
        if key2 =="1":
            self.grid.obrazek1()
        if key2 =="2":
            self.grid.obrazek2()

        if key2 == "u":
            self.grid.ucz_sie()
        if key2 == "r":
            self.grid.rysuj()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())
