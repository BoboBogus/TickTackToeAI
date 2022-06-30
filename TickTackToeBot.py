from tkinter import*
from tkinter import messagebox
import random
from PIL import *
board = 0
playerTurn = True
boardPos = [['','',''],
            ['','',''],
            ['','','']]

nMove = []

wPos=[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]

boardButton = {
    (0,0):0,
    (0,1):1,
    (0,2):2,
    (1,0):3,
    (1,1):4,
    (1,2):5,
    (2,0):6,
    (2,1):7,
    (2,2):8,
    }

gameStop = False
root = Tk()
Buttons = []
Buttons.append(Button(root,width=2, command=lambda: Place(0, 0, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(0, 1, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(0, 2, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(1, 0, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(1, 1, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(1, 2, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(2, 0, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(2, 1, True)))
Buttons.append(Button(root,width=2, command=lambda: Place(2, 2, True)))

Buttons[0].grid(row=0, column=0)
Buttons[1].grid(row=0, column=1)
Buttons[2].grid(row=0, column=2)
Buttons[3].grid(row=1, column=0)
Buttons[4].grid(row=1, column=1)
Buttons[5].grid(row=1, column=2)
Buttons[6].grid(row=2, column=0)
Buttons[7].grid(row=2, column=1)
Buttons[8].grid(row=2, column=2)

def Place(x, y, isplayer):
    if gameStop == False:
        global playerTurn
        if isplayer:
            if playerTurn :
                 if boardPos[x][y] == "":
                    boardPos[x][y] = 'X'
                    playerTurn = False
                    Update()
                    enemyTurn()
            else:
                messagebox.showinfo("Error", "Wait For enemy turn")
        else:
            boardPos[x][y] = 'O'
            playerTurn = True
            Update()

def enemyTurn():
    # minmax ai
    remboard = rTiles()
    var = MiniMax(remboard)
    nx = var[0]
    ny = var[1]
    Place(x = nx, y = ny, isplayer = False)

def rTiles():
    movePos = []
    for x in range(0,3):
        for y in range(0,3):
            if boardPos[x][y] == '':
                movePos.append((x,y))
    return movePos

def MiniMax(board):
    global nMove
    for x, y in board:
        boardPos[x][y] = 'O'
        if CalculateWin(False) == True: #if the random is the winning
            boardPos[x][y] = ''
            return (x,y)
        boardPos[x][y] = ''
    return miniMaxpCheck(board)

def miniMaxpCheck(board):
    global nMove
    for x, y in board:
        boardPos[x][y] = 'X'
        if CalculateWin(True) == True: #if the random is the winning
            boardPos[x][y] = ''
            return (x,y)
        boardPos[x][y] = ''
        if CalculateWin(False) == False and CalculateWin(True) == False: #nutral
            boardPos[x][y] = ''
            nMove.append((x,y)) #future error
        boardPos[x][y] = ''

    rSpot = random.choice(nMove)
    nMove.remove(rSpot)
    return rSpot


def Update():
    board = 0 
    for x in range(0,3):
        for y in range(0,3):
            z = boardButton[(x,y)]
            Buttons[z].configure(text = boardPos[x][y])

    for x in range(0,9):
        if Buttons[x]['text'] != '':
            board +=1
    if board >= 9:
        messagebox.showinfo("GAME END", "TIE GAME")
    WinCheck(True)
    WinCheck(False)
    
def CalculateWin(isplayer):
    if isplayer == True:
        for list in wPos:
            num = 0
            for x, y in list:
                if boardPos[x][y] == "X":
                    num += 1
                    if num == 3:
                        return True
        if num != 3:
            return False
    else:
        for list in wPos:
            num = 0
            for x, y in list:
                if boardPos[x][y] == "O":
                    num += 1
                    if num == 3:
                        return True
        if num != 3:
            return False

def WinCheck(isplayer):
    if isplayer == True:
        for list in wPos:
            num = 0
            for x, y in list:
                if boardPos[x][y] == "X":
                    num += 1
                    if num == 3:
                        endgame(list, False)
    else:
        for list in wPos:
            num = 0
            for x, y in list:
                if boardPos[x][y] == "O":
                    num += 1
                    if num == 3:
                        endgame(list, False)

def endgame(list, isplayer):
    global playerTurn
    playerTurn = False
    global gameStop
    gameStop = True
    for x, y in list:
        Buttons[boardButton[(x,y)]].configure(bg = "red")
    if isplayer:
        messagebox.showinfo("GAME END", "You Won!")
    else:
        messagebox.showinfo("GAME END", "Enemy Won!")


root.mainloop()