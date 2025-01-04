import random
import time
import keyboard

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, \
    QHBoxLayout
from PyQt5.QtGui import QColor, QFont
import sys
import numpy as np
from nltk import flatten

import matplotlib.pyplot as plt

jeden=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

dwa=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

trzy=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

cztery=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

piec=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

szesc=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

sie=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

osie=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

dzie=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

zero=[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


zo=[1,0,0,0,0,0,0,0,0,0]
z=[zero, jeden, dwa, trzy, cztery, piec, szesc, sie, osie, dzie]

jo=[1,0,0,0,0,0,0,0,0,0]
j=[jeden, zero, dwa, trzy, cztery, piec, szesc, sie, osie, dzie]

do=[1,0,0,0,0,0,0,0,0,0]
d=[dwa,zero,jeden,trzy, cztery, piec,szesc,sie,osie,dzie]


to=[1,0,0,0,0,0,0,0,0,0]
t=[trzy, jeden,dwa, cztery,piec,szesc,sie,osie,dzie,zero]


co=[1,0,0,0,0,0,0,0,0,0]

c=[cztery,jeden,dwa,trzy,piec,szesc,sie,osie,dzie,zero]

po=[1,0,0,0,0,0,0,0,0,0]
p=[piec,jeden,dwa,trzy,cztery,szesc,sie,osie,dzie,zero]

szo=[1,0,0,0,0,0,0,0,0,0]
sz=[szesc,zero,jeden,dwa,trzy,cztery,piec,sie,osie,dzie]


so=[1,0,0,0,0,0,0,0,0,0]
s=[sie,zero,jeden,dwa,trzy,cztery,piec,szesc,osie,dzie]

oo=[1,0,0,0,0,0,0,0,0,0]
o=[osie,zero,jeden,dwa,trzy,cztery,piec,szesc,sie,dzie]

dzo=[1,0,0,0,0,0,0,0,0,0]
dz=[dzie,zero,jeden,dwa,trzy,cztery,piec,szesc,sie,osie]





class Adline:
    def __init__(self, no_of_inputs, iterations, learning_rate=0.2):
        #self.fft=fft
        self.no_of_inputs = no_of_inputs
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.weights = np.random.rand(self.no_of_inputs + 1)



    def predict(self, x):           #predykcja
        return self.activation_function(np.dot(self.weights[1:],x) + self.weights[0])

    def activation_function(self, x):  #f.aktywacji
        self.sigma = 1 / (1 + np.exp(-x))
        return self.sigma


    def activation_function_der(self,x):
        return self.activation_function(x) * (1 - self.activation_function(x))

    def train(self, train_x, train_y):
        self.errors = []

        train_x = np.array(train_x)
        for _ in range(self.iterations):
            e = 0
            for x, y in zip(train_x, train_y):
                out = self.predict(x)
                self.weights[1:] += self.learning_rate * (y - out) * x * self.activation_function_der(out-y)
                self.weights[0] += self.learning_rate * (y - out) * 1 * self.activation_function_der(out-y)
                e += (y - out) ** 2
            self.errors.append(e)

    def plot_errors(self):      #wykres bledow dla kazdej cyfry
        plt.plot(range(self.iterations), self.errors)
        plt.xlabel('Iterations')
        plt.ylabel('Error')
        plt.show()

    def outputwyjsciowe(self,x):
        wag=self.weights
        return np.dot(wag[1:],x) + wag[0]

    def outputwyjsciowe2(self,x):
        wag=self.weights
        return self.activation_function(np.dot(wag[1:],x) + wag[0])


class Grid(QWidget):


    def __init__(self,width,height,cell_size):
        super().__init__()
        self.lista = [z, j, d, t, c, p, sz, s, o, dz]     #lista cyfr
        self.width=width
        self.height=height
        self.cell_size= cell_size
        self.perceptrons=[]
        self.no_of_categories = len(self.lista)
        self.input=64*2
        self.iterations=100
        self.grid=[[False for _ in range(width)] for _ in range(height)]                        #ustawienia poczatkowe - false na kazdym polu
        self.buttons = [[QPushButton(self) for _ in range(width)] for _ in range(height)]
        #self.liczba=-1
        self.przew=-1
        self.lab = [zo, jo, do, to, co, po, szo, so, oo, dzo]
        self.lista2=[jeden,dwa,trzy,cztery,piec,szesc,sie,osie,dzie]



        for i in range(self.no_of_categories):
            self.perceptrons.append(Adline(self.input, self.iterations))



        for row in range(width):
            for col in range(height):
                self.buttons[row][col].setStyleSheet(f"background-color: white; border: 1px solid black")
                self.buttons[row][col].setFixedSize(cell_size,cell_size)
                self.buttons[row][col].clicked.connect(self.make_toggle(row,col))


        self.layout=QGridLayout()

        for row in range(width):
            for col in range(height):
                self.layout.addWidget(self.buttons[row][col],row,col)

        hbox = QHBoxLayout()                    #dodawanie paneli i przycisków + laczenie z funkcja
        hbox2 = QHBoxLayout()
        hbox3= QHBoxLayout()
        hbox4=QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox6 = QHBoxLayout()
        p1_button = QPushButton('wyczyść')
        p2_button = QPushButton('zaszum')

        buttons = [QPushButton(str(i)) for i in range(1, 10)]
        for i, button in enumerate(buttons, start=11):
            globals()[f"p{i}_button"] = button

        p10_button = QPushButton('0')
        p01_button = QPushButton('ucz się')
        p22_button = QPushButton('rozstrzygnij')

        p23_button = QPushButton('<')
        p24_button = QPushButton('>')
        p25_button = QPushButton('^')
        p26_button = QPushButton('v')

        p27_button = QPushButton('⭮')

         #łączenie przycisków z funkcją

        p2_button.clicked.connect(self.zaszum)
        p1_button.clicked.connect(self.wyczysc)
        p01_button.clicked.connect(self.uczsie)
        p22_button.clicked.connect(self.weryfikuj)

        buttons = [p11_button, p12_button, p13_button, p14_button, p15_button, p16_button, p17_button, p18_button,
                   p19_button]
        for i, button in enumerate(buttons, start=1):
            button.clicked.connect(lambda _, x=i: self.liczby(x))

        p10_button.clicked.connect(lambda:self.liczby(0))
        p23_button.clicked.connect(self.lewo)
        p24_button.clicked.connect(self.prawo)
        p25_button.clicked.connect(self.gora)
        p26_button.clicked.connect(self.dol)
        p27_button.clicked.connect(self.obroc)



        hbox.addWidget(p1_button)
        hbox.addWidget(p2_button)
        hbox.addWidget(p11_button)
        hbox.addWidget(p12_button)
        hbox.addWidget(p13_button)
        hbox.addWidget(p14_button)

        hbox3.addWidget(p15_button)
        hbox3.addWidget(p16_button)
        hbox3.addWidget(p17_button)
        hbox3.addWidget(p18_button)
        hbox3.addWidget(p19_button)
        hbox3.addWidget(p10_button)

        hbox5.addWidget(p23_button)
        hbox5.addWidget(p24_button)
        hbox5.addWidget(p25_button)
        hbox5.addWidget(p26_button)

        hbox6.addWidget(p27_button)

        hbox2.addWidget(p01_button)
        hbox2.addWidget(p22_button)
        hbox.setAlignment(Qt.AlignBottom)

        self.label_2 = QLabel(self)
        hbox4.addWidget(self.label_2)


        self.layout.addLayout(hbox, height, 0, 1, width)
        self.layout.addLayout(hbox3, height + 1, 0, 1, width)
        self.layout.addLayout(hbox6, height + 3, 0, 1, width)
        self.layout.addLayout(hbox2, height+4, 0, 1, width)
        self.layout.addLayout(hbox4, height +5, 0, 1, width)
        self.layout.addLayout(hbox5, height + 2, 0, 1, width)

        self.setLayout(self.layout)

        self.show()


    def fourier_transform(self,x):       #transformata fouriera
        t = np.abs(np.fft.fft(x))
        return (t - np.mean(t)) / np.std(t)

    def make_toggle(self,row,col):            #funkcja zmienijająca kolor przycisku po kliknięciu
        def toggle():
            self.grid[row][col]=not self.grid[row][col]
            color="black" if self.grid[row][col] else "white"
            self.buttons[row][col].setStyleSheet(f"background-color:{color}; border: 1px solid black")
            self.zamiana()
            print(self.grid)
        return toggle





    def output4(self,lista, x):                     #funkcja zwracająca indeks największej wartosci dzialania aktywacji.akt wśród 10 perceptronów
        print("Działanie funkcji aktywacji poszczególnych perceptronów: ", np.array([lista[i].outputwyjsciowe2(x) for i in range(self.no_of_categories)]))
        return np.array([lista[i].outputwyjsciowe2(x) for i in range(self.no_of_categories)]).argmax()


#mozna zmieniac - zaszumiac, przemieszczac narysowane/ umieszczone cyfry
    def zaszum(self):
        for row in range(self.width):
            for col in range(self.height):
                if self.grid[row][col]==True:
                    if random.random() < 0.2:
                        self.grid[row][col]=False
                    '''if random.random() < 0.3:
                        self.grid[row + random.randint(0, 1)][col+ random.randint(0, 1)] = True'''
                color = "black" if self.grid[row][col] else "white"
                self.buttons[row][col].setStyleSheet(f"background-color:{color}; border: 1px solid black")
        self.zamiana()
        print(self.grid)

    def wyczysc(self):
        for row in range(self.width):
            for col in range(self.height):
                self.grid[row][col] = False
                color = "black" if self.grid[row][col] else "white"
                self.buttons[row][col].setStyleSheet(f"background-color:{color}; border: 1px solid black")

    def zamiana(self):          #funkcja zamieniająca ,,FALSE" I "TRUE" na 0/1
        for row in range(self.width):
            for col in range(self.height):
                if self.grid[row][col] == False:
                    self.grid[row][col]=0
                else:
                    self.grid[row][col]=1
        return self.grid


    def koloruj(self):
        for row in range(self.width):
            for col in range(self.height):
                color = "black" if self.grid[row][col]==1 else "white"
                self.buttons[row][col].setStyleSheet(f"background-color:{color}; border: 1px solid black")


    def lewo(self):
        nowa_siatka = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for row in range(self.width):
            for col in range(self.height):
                nowa_siatka[row][col-1] = self.grid[row][col]

        self.grid = nowa_siatka
        self.koloruj()
        print(self.grid)



    def obroc(self):
        nowa_siatka = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                nowa_siatka[col][self.height - 1 - row] = self.grid[row][col]
        self.grid = nowa_siatka
        self.width, self.height = self.height, self.width
        self.koloruj()
        print(self.grid)



    def prawo(self):
        nowa_siatka2 = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for row in range(self.width):
            for col in range(self.height):
                nowa_siatka2[row][(col + 1) % self.height] = self.grid[row][col]

        self.grid = nowa_siatka2
        self.koloruj()
        print(self.grid)

    def gora(self):

        nowa_siatka3 = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for row in range(self.width):
            for col in range(self.height):
                    nowa_siatka3[row - 1][col] = self.grid[row][col]
        self.grid = nowa_siatka3
        self.koloruj()
        print(self.grid)

        self.grid = nowa_siatka3
        self.koloruj()
        print(self.grid)

    def dol(self):
        nowa_siatka4 = [[0 for _ in range(self.height)] for _ in range(self.width)]
        for row in range(self.width):
            for col in range(self.height):
                nowa_siatka4[(row + 1) % self.height][col] = self.grid[row][col]

        self.grid = nowa_siatka4
        self.koloruj()
        print(self.grid)




#do wybierania w przyciskach
    def liczby(self, x):         #poszczególne liczby
        if x==1:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, False, False, True, False, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, True, False, False, False], [False, False, False, False, True, False, False, False], [False, False, False, False, True, False, False, False], [False, False, False, True, True, True, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba=1
            print(self.grid)

        elif x==0:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, False, True, True, False, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 0
            print(self.grid)
        elif x==2:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, False, True, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, True, False, False, False], [False, False, False, True, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 2
            print(self.grid)
        elif x==3:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, False, True, False, False], [False, False, False, False, True, False, False, False], [False, False, False, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, False, True, True, False, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 3
            print(self.grid)
        elif x==4:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, True, False, False, False, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 4
            print(self.grid)
        elif x == 5:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, True, False, False, False, False, False], [False, False, True, True, True, False, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, False, True, False, False], [False, False, True, True, True, False, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 5
            print(self.grid)
        elif x == 6:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, True, False, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 6
            print(self.grid)
        elif x == 7:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, True, False, False, False], [False, False, False, True, False, False, False, False], [False, False, False, True, False, False, False, False], [False, False, False, True, False, False, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 7
            print(self.grid)
        elif x == 8:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, False, True, False, False], [False, False, False, True, True, False, False, False], [False, False, True, False, False, True, False, False], [False, False, True, False, False, True, False, False], [False, False, False, True, True, False, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 8
            print(self.grid)
        else:
            self.grid=[[False, False, False, False, False, False, False, False], [False, False, True, True, True, True, False, False], [False, False, True, False, False, True, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, True, False, False], [False, False, False, False, False, True, False, False], [False, False, True, True, True, True, False, False], [False, False, False, False, False, False, False, False]]
            self.zamiana()
            self.liczba = 9
            print(self.grid)

        for row in range(self.width):
            for col in range(self.height):
                color = "black" if self.grid[row][col] else "white"
                self.buttons[row][col].setStyleSheet(f"background-color:{color}; border: 1px solid black")


    def preprocessing(self, x):

        return 0.8 * x + 0.1

    def uczsie(self):        #uczenie perceptronu
        lista=self.lista      #lista to lista z przykladu 1 cyfry w dobrej wersji + inne cyfry
        for w in range(self.no_of_categories):
            xx = []
            x2=[]
            for i in range(len(lista[w])):                #każdy wariant spłaszczamy, opakowujemy transformat i dodajemy labelkę
                xx.append(self.fourier_transform(flatten(lista[w][i])).tolist())
                #print(xx)#dzięki przejściu w pętli w (0-9)
                x2.append(flatten(lista[w][i]) )
                #print(x2)
            x3=[]
            for i in range(len(lista[w])):
                x3.append(xx[i]+x2[i])
            '''print(type(xx[0]))
            print(type(x2[0]))'''

            pr=[]
            for j in range(len(lista[w])):
                print(x3[j])
                pr.append(self.preprocessing(np.array(x3[j])))


            print(x3)
            print(xx)
            print("tu")
            t=np.array(self.lab[w])
            print(t)
            self.perceptrons[w].train(pr,t)                         #uczymy perceptrony w zależności od miejsca
            self.perceptrons[w].plot_errors()
        self.label_2.setText("Uczenie zakończone sukcesem!")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("color: green;font-weight: bold")
        self.label_2.setFont(QFont('Calibri', 13))

        #print(self.perceptrons)



    def weryfikuj(self):
        self.zamiana()
        z=list(self.grid)
        dane = self.fourier_transform(flatten(z)).tolist() + flatten(z)  ####łączenie zwykłych daych (spłaszczonych) z fourierem na spłaszczeniu
        dane2 = self.preprocessing(np.array(dane))   #preprocessing na zakres 0.1 0.9

        self.przew=self.output4(self.perceptrons,dane2)             #weryfikujemy wyjścia korzystając z wczesniej zdeiniowanej funkcji
        self.info=str(self.przew)

        self.label_2.setText("Wynik: " + self.info)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet("font-weight: bold")
        self.label_2.setFont(QFont('Arial', 13))





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)    #ustawienia okna itp
        self.setWindowTitle("Pixel Grid")
        self.grid=Grid(8,8,90)
        self.setCentralWidget(self.grid)
        self.show()

   #mozna wybierac cyfry i wybierac przyciski tez na klawiaturze

    def keyPressEvent(self, event):    #polączenie z klawiturą


        key2 = event.text()
        print(key2)

        for i in range(0,11):
            if key2==str(i):
                self.grid.liczby(i)

        if key2 =="a":
            self.grid.lewo()
        if key2 =="d":
            self.grid.prawo()
        if key2 == "w":
            self.grid.gora()
        if key2 == "s":
            self.grid.dol()

        if key2 == "u":
            self.grid.uczsie()

        if key2 == "i":
            self.grid.weryfikuj()



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())


