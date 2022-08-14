import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class janela(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "primeira janela"
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
aplicacao = QApplication(sys.argv)

j=janela()
sys.exit(aplicacao.exec_())