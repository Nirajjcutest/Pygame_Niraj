#print board
import os
import random
import time
def drawBoard(board):
    print ("            |   |    ")
    print ("         "+board[6]+"  | "+board[7]+" | "+board[8]+"   ")
    print ("            |   |    ")
    print ("       --------------")
    print ("            |   |    ")
    print ("         "+board[3]+"  | "+board[4]+" | "+board[5]+"   ")
    print ("            |   |    ")
    print ("       --------------")
    print ("            |   |    ")
    print ("         "+board[0]+"  | "+board[1]+" | "+board[2]+"   ")
    print ("            |   |    ")

def choose():
    y = ''
    while not ( y == 'X' or y == 'O'):
        y = input("Do you want X or O: ").upper()
    return y

def CompPlay():
    CP = random.choice(k)
    k.remove(CP)
    return CP

def CompTurn():
    print("Now Computer's Turn")
    time.sleep(1)
    AIC = CompPlay()
    Fillings[AIC - 1] = AI
    drawBoard(Fillings)

PLAY = 'y'
while PLAY == 'y':
    os.system('cls')
    g = choose()
    if g == 'X':
        AI = 'O'
    else:
        AI = 'X'
    print ("you have choose %s" %g)
    Fillings = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    n = ''
    k = [1,2,3,4,5,6,7,8,9]
    for i in range(4):
        while not (n in k):
            n = (int(input("Enter Your position(1-9): ")))
        k.remove(n)
        Fillings[n-1] = g
        drawBoard(Fillings)
        CompTurn()
    CompTurn()
    PLAY = input("Do you want to play again(y) or (n)").lower()






