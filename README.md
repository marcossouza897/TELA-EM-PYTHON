# TELA-EM-PYTHON
PyTela
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class janela(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "primeira janela"

        botao1 = QPushButton("Botao 1", self)
        botao1.move(150,200)
        botao1.resize(150,80)
        botao1.setStyleSheet('QPushButton {background-color:#2268ff;font:bold;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton("Botao 1", self)
        botao2.move(350,200)
        botao2.resize(150,80)
        botao2.setStyleSheet('QPushButton {background-color:#2268ff;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao1_click)

        self.CarregarJanela()

        

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('click, click e click')
    
aplicacao = QApplication(sys.argv)

j=janela()
sys.exit(aplicacao.exec_())
