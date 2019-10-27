import sys
from PyQt5 import QtWidgets
import crisscross
#import random

class CrissCrossApp(QtWidgets.QMainWindow, crisscross.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newGameButton.clicked.connect(self.newGame)
        
        self.gameButton_0.clicked.connect(self.button_0)
        self.gameButton_1.clicked.connect(self.button_1)
        self.gameButton_2.clicked.connect(self.button_2)
        
        self.gameButton_3.clicked.connect(self.button_3)
        self.gameButton_4.clicked.connect(self.button_4)
        self.gameButton_5.clicked.connect(self.button_5)
        
        self.gameButton_6.clicked.connect(self.button_6)
        self.gameButton_7.clicked.connect(self.button_7)
        self.gameButton_8.clicked.connect(self.button_8)
        
        self.M = 3
        self.N = 3
        self.turn = True
        self.win = False
        self.matr = [['-' for y in range(self.M)] for x in range(self.N)]
    def newGame(self):
        self.matr = [['-' for y in range(self.M)] for x in range(self.N)]
        self.turn = True
        self.win = False
        
        self.gameButton_0.setText(' ')
        self.gameButton_1.setText(' ')
        self.gameButton_2.setText(' ')
        
        self.gameButton_3.setText(' ')
        self.gameButton_4.setText(' ')
        self.gameButton_5.setText(' ')
        
        self.gameButton_6.setText(' ')
        self.gameButton_7.setText(' ')
        self.gameButton_8.setText(' ')
        
        self.newGameButton.setText('New Game')
        
    def checkForWin(self):
        if self.matr[0][0] == self.matr[0][1] == self.matr[0][2] != '-' or self.matr[1][0] == self.matr[1][1] == self.matr[1][2] != '-' or self.matr[2][0] == self.matr[2][1] == self.matr[2][2] != '-' or self.matr[0][0] == self.matr[1][0] == self.matr[2][0] != '-' or self.matr[0][1] == self.matr[1][1] == self.matr[2][1] != '-' or self.matr[0][2] == self.matr[1][2] == self.matr[2][2] != '-' or self.matr[0][0] == self.matr[1][1] == self.matr[2][2] != '-' or self.matr[2][0] == self.matr[1][1] == self.matr[0][2] != '-':
            return True
        else:
            return False
    def button_0(self):
        if not self.win:
            if self.turn:
                self.matr[0][0] = 'X'
                self.gameButton_0.setText('X')
                self.turn = not self.turn
            else:
                self.matr[0][0] = 'O'
                self.gameButton_0.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_1(self):
        if not self.win:
            if self.turn:
                self.matr[0][1] = 'X'
                self.gameButton_1.setText('X')
                self.turn = not self.turn
            else:
                self.matr[0][1] = 'O'
                self.gameButton_1.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_2(self):
        if not self.win:
            if self.turn:
                self.matr[0][2] = 'X'
                self.gameButton_2.setText('X')
                self.turn = not self.turn
            else:
                self.matr[0][2] = 'O'
                self.gameButton_2.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')   
    def button_3(self):
        if not self.win:
            if self.turn:
                self.matr[1][0] = 'X'
                self.gameButton_3.setText('X')
                self.turn = not self.turn
            else:
                self.matr[1][0] = 'O'
                self.gameButton_3.setText('O')
                self.turn = not self.turn
        
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_4(self):
        if not self.win:
            if self.turn:
                self.matr[1][1] = 'X'
                self.gameButton_4.setText('X')
                self.turn = not self.turn
            else:
                self.matr[1][1] = 'O'
                self.gameButton_4.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_5(self):
        if not self.win:
            if self.turn:
                self.matr[1][2] = 'X'
                self.gameButton_5.setText('X')
                self.turn = not self.turn
            else:
                self.matr[1][2] = 'O'
                self.gameButton_5.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_6(self):
        if not self.win:
            if self.turn:
                self.matr[2][0] = 'X'
                self.gameButton_6.setText('X')
                self.turn = not self.turn
            else:
                self.matr[2][0] = 'O'
                self.gameButton_6.setText('O')
                self.turn = not self.turn
        
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_7(self):
        if not self.win:
            if self.turn:
                self.matr[2][1] = 'X'
                self.gameButton_7.setText('X')
                self.turn = not self.turn
            else:
                self.matr[2][1] = 'O'
                self.gameButton_7.setText('O')
                self.turn = not self.turn
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
    def button_8(self):
        if not self.win:
            if self.turn:
                self.matr[2][2] = 'X'
                self.gameButton_8.setText('X')
                self.turn = not self.turn
            else:
                self.matr[2][2] = 'O'
                self.gameButton_8.setText('O')
                self.turn = not self.turn
        
            if self.checkForWin():
                self.win = True
                self.newGameButton.setText('Game over, try again?')
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CrissCrossApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()