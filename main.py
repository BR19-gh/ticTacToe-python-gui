import random
from os import system, name
from time import sleep
from tkinter import *

menu=0
chooseCharacterWindow=0
multiPlayerWindow=0
singlePlayerWindow=0
finishWindow=0
firstPlayer=0
secondPlayer=0
player=0
gameMode=0
playerWon=False
computerTurn=False
singlePlayerVal=False
ps1=0
ps2=0
ps3=0
ps4=0
ps5=0
ps6=0
ps7=0
ps8=0
ps9=0


board={
    "0":"-","1":"-","2":"-",
    "3":"-","4":"-","5":"-",
    "6":"-","7":"-","8":"-"
    }

def choosingCharchter(playerChar):
    global firstPlayer,secondPlayer,chooseCharacterWindow, singlePlayerVal
    if(playerChar=='X'):
        firstPlayer='X'
        secondPlayer='O'
    elif(playerChar=='O'):
        firstPlayer='O'
        secondPlayer='X'
    
    if(gameMode==1):
        singlePlayerVal=True
        chooseCharacterWindow.destroy()
        willComputerPlayFirst=random.randint(0,1)
        singlePlayer(willComputerPlayFirst)
    elif(gameMode==2):
        singlePlayerVal=False
        chooseCharacterWindow.destroy()
        multiPlayers()

def chooseCharacter(gameModeChoosed):
    global gameMode, chooseCharacterWindow, menu
    menu.destroy()
    if gameModeChoosed==1:
        gameMode=1
    elif gameModeChoosed==2:
        gameMode=2

    chooseCharacterWindow = Tk()
    chooseCharacterWindow.title('Choose Character')
    chooseCharacterWindow.geometry('450x100')

        #choosing palyers
    player=random.randint(1,2)

    l1 = Label(chooseCharacterWindow, text=f"Player-{str(player)}, choose your character, either X or O: ", font="Default")
    l1.place(x=5,y=5)
    
    xBtn = Button(chooseCharacterWindow, text='X', font="Default", width=5)
    xBtn.place(x=155,y=50)
    oBtn = Button(chooseCharacterWindow, text='O', font="Default", width=5)
    oBtn.place(x=255,y=50)

    xBtn.bind('<Button-1>',lambda e: choosingCharchter('X'))
    oBtn.bind('<Button-1>',lambda e: choosingCharchter('O'))
    
    xBtn.bind('<Enter>',lambda e: hover(xBtn))
    oBtn.bind('<Enter>',lambda e: hover(oBtn))
    xBtn.bind('<Leave>',lambda e: notHover(xBtn))
    oBtn.bind('<Leave>',lambda e: notHover(oBtn))


    chooseCharacterWindow.mainloop()


def replay():
    global board,playerWon,firstPlayer,secondPlayer,player,singlePlayerVal
    board={
    "0":"-","1":"-","2":"-",
    "3":"-","4":"-","5":"-",
    "6":"-","7":"-","8":"-"
    }
    playerWon=False
    firstPlayer=0
    secondPlayer=0
    player=0
    finishWindow.destroy()
    if singlePlayerVal==True:
        singlePlayerWindow.destroy()

    elif singlePlayerVal==False:
        multiPlayerWindow.destroy()
    
    main()
    return


def winningWindow(winner):
    global playerWon,finishWindow
    finishWindow = Tk()
    finishWindow.title(f'Player-{board["0"]} won!!')
    finishWindow.geometry('270x100')

    
    l1 = Label(finishWindow, text=f'Player-{winner} won, congrats.', font="Default")
    l1.place(x=5,y=5)

    exitBtn = Button(finishWindow, text='Exit', font="Default", width=5)
    exitBtn.place(x=5,y=50)

    replayBtn = Button(finishWindow, text='Replay', font="Default", width=5)
    replayBtn.place(x=195,y=50)

    exitBtn.bind('<Button-1>',lambda e: exit())
    exitBtn.bind('<Enter>',lambda e: hover(exitBtn))
    exitBtn.bind('<Leave>',lambda e: notHover(exitBtn))

    replayBtn.bind('<Button-1>',lambda e: replay())
    replayBtn.bind('<Enter>',lambda e: hover(replayBtn))
    replayBtn.bind('<Leave>',lambda e: notHover(replayBtn))
    playerWon=True
    finishWindow.mainloop()
    return

    
def tieWindow():
    global finishWindow,singlePlayerVal
    finishWindow = Tk()
    finishWindow.title("It's a tie..")
    finishWindow.geometry('390x150')
    textSingleMode="Wow! You tied with the Computer!\nI guess AI won't take over the planet..."
    textMultiMode="Wow! It's a tie... Good luck to you two!"
    if singlePlayerVal==True:
        textWritten=textSingleMode
    else:
        textWritten=textMultiMode
    l1 = Label(finishWindow, text=f'{textWritten}', font="Default")
    l1.place(x=5,y=5)

    exitBtn = Button(finishWindow, text='Exit', font="Default", width=5)
    exitBtn.place(x=5,y=100)

    replayBtn = Button(finishWindow, text='Replay', font="Default", width=5)
    replayBtn.place(x=315,y=100)

    exitBtn.bind('<Button-1>',lambda e: exit())
    exitBtn.bind('<Enter>',lambda e: hover(exitBtn))
    exitBtn.bind('<Leave>',lambda e: notHover(exitBtn))

    replayBtn.bind('<Button-1>',lambda e: replay())
    replayBtn.bind('<Enter>',lambda e: hover(replayBtn))
    replayBtn.bind('<Leave>',lambda e: notHover(replayBtn))
    finishWindow.mainloop()
    return

def checkWin():
    # 1 2 3
    #
    #
    if (board["0"]!='-' and board["0"]==board["1"] and board["1"]==board["2"]):
        winningWindow(board["0"])

    #
    # 4 5 6
    #
    elif (board["3"]!='-' and board["3"]==board["4"] and board["4"]==board["5"]):
        winningWindow(board["3"])

    #
    #
    # 7 8 9
    elif (board["6"]!='-' and board["6"]==board["7"] and board["7"]==board["8"]):
        winningWindow(board["6"])

    # 1 # #
    # 4 # #
    # 7 # #
    elif (board["0"]!='-' and board["0"]==board["3"] and board["3"]==board["6"]):
        winningWindow(board["0"])

    # # 2 #
    # # 5 #
    # # 8 #
    elif (board["1"]!='-' and board["1"]==board["4"] and board["4"]==board["7"]):
        winningWindow(board["1"])

    # # # 3
    # # # 6
    # # # 9
    elif (board["2"]!='-' and board["2"]==board["5"] and board["5"]==board["8"]):
        winningWindow(board["2"])

    # 1
        # 5
            # 9
    elif (board["0"]!='-' and board["0"]==board["4"] and board["4"]==board["8"]):
        winningWindow(board["0"])

            # 3
        # 5
    # 7
    elif (board["2"]!='-' and board["2"]==board["4"] and board["4"]==board["6"]):
        winningWindow(board["2"])
    
    # tie
    else:
        j=0
        while(j<9):
            if(board[f"{j}"]=='-'):
                break
            elif(j==8):
                tieWindow()
            j=j+1
    return False


def changeChosenPosition(position,computerChar):
    if position==0:
        ps1.config(text=f"{computerChar}")
    elif position==1:
        ps2.config(text=f"{computerChar}")
    elif position==2:
        ps3.config(text=f"{computerChar}")
    elif position==3:
        ps4.config(text=f"{computerChar}")
    elif position==4:
        ps5.config(text=f"{computerChar}")
    elif position==5:
        ps6.config(text=f"{computerChar}")
    elif position==6:
        ps7.config(text=f"{computerChar}")
    elif position==7:
        ps8.config(text=f"{computerChar}")
    elif position==8:
        ps9.config(text=f"{computerChar}")
    return


def computerPlay(computerChar,labelWhichTurn):
    global computerTurn
    computerPlayed=0
    while(computerPlayed==0):
        position=random.randint(0,8)
        if (board[f"{position}"]=='-'):
            board[f"{position}"]=computerChar
            if computerChar=='X':
                player="O"
            elif computerChar=='O':
                player="X"
            
            computerPlayed=1
    changeChosenPosition(position,computerChar)
    labelWhichTurn.config(text=f"Computer as {computerChar} played in position #{position+1}.\nNow is Player-{str(player)} turn, \nclick on the position you want to play in:")
    checkWin()
    computerTurn=False
    return


def insertIntoBoard(playerArg,chosenPositionNum,chosenPositionBtn,labelWhichTurn):
        global player, playerWon, secondPlayer, computerTurn, singlePlayerVal
        if playerWon==True:
            pass
        else:
            #check if the chosen position is occupied
            if(board[f"{chosenPositionNum}"]!='-'):
                pass

            else:#if not occupied continue
                if singlePlayerVal==False:
                    if (playerArg == firstPlayer):
                        player = secondPlayer
                    elif (playerArg == secondPlayer):
                        player = firstPlayer
                board[f"{chosenPositionNum}"]=playerArg
                chosenPositionBtn.config(text=f"{playerArg}")
                labelWhichTurn.config(text=f"Player-{str(player)} click on the position you want to play in:")
                computerTurn=True

                checkWin()
                if singlePlayerVal==True:
                    if computerTurn==True:
                        if firstPlayer=='X':
                            secondPlayer='O'
                        elif firstPlayer=='O': 
                            secondPlayer='X'
                        if playerWon==False:
                            computerPlay(secondPlayer,labelWhichTurn)
                    computerTurn==True


def singlePlayer(willComputerPlayFirst):
    global player,computerTurn,ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8,ps9,secondPlayer,singlePlayerWindow
    
    if (player==0):
        player=firstPlayer
  

    singlePlayerWindow = Tk()
    singlePlayerWindow.title('Single Player Window')
    singlePlayerWindow.geometry('460x290')
    
    labelWhichTurn = Label(singlePlayerWindow, text=f"Player-{str(player)} click on the position you want to play in:", font="Default")
    labelWhichTurn.place(x=5,y=5)


    ps1 = Button(singlePlayerWindow, text=board["0"],font="Default",width=3)
    ps1.place(x=130,y=110)
    ps2 = Button(singlePlayerWindow, text=board["1"],font="Default",width=3)
    ps2.place(x=180,y=110)
    ps3 = Button(singlePlayerWindow, text=board["2"],font="Default",width=3)
    ps3.place(x=230,y=110)
    ps4 = Button(singlePlayerWindow, text=board["3"],font="Default",width=3)
    ps4.place(x=130,y=160)
    ps5 = Button(singlePlayerWindow, text=board["4"],font="Default",width=3)
    ps5.place(x=180,y=160)
    ps6 = Button(singlePlayerWindow, text=board["5"],font="Default",width=3)
    ps6.place(x=230,y=160)
    ps7 = Button(singlePlayerWindow, text=board["6"],font="Default",width=3)
    ps7.place(x=130,y=210)
    ps8 = Button(singlePlayerWindow, text=board["7"],font="Default",width=3)
    ps8.place(x=180,y=210)
    ps9 = Button(singlePlayerWindow, text=board["8"],font="Default",width=3)
    ps9.place(x=230,y=210)

    computerTurn=True
    if (willComputerPlayFirst==0):
        pass
    elif (willComputerPlayFirst==1):
        if firstPlayer=='O':
            secondPlayer='X'
        else: 
            secondPlayer='O'
        computerPlay(secondPlayer,labelWhichTurn)

    ps1.bind('<Button-1>',lambda e: insertIntoBoard(player,0,ps1,labelWhichTurn))
    ps2.bind('<Button-1>',lambda e: insertIntoBoard(player,1,ps2,labelWhichTurn))
    ps3.bind('<Button-1>',lambda e: insertIntoBoard(player,2,ps3,labelWhichTurn))
    ps4.bind('<Button-1>',lambda e: insertIntoBoard(player,3,ps4,labelWhichTurn))
    ps5.bind('<Button-1>',lambda e: insertIntoBoard(player,4,ps5,labelWhichTurn))
    ps6.bind('<Button-1>',lambda e: insertIntoBoard(player,5,ps6,labelWhichTurn))
    ps7.bind('<Button-1>',lambda e: insertIntoBoard(player,6,ps7,labelWhichTurn))
    ps8.bind('<Button-1>',lambda e: insertIntoBoard(player,7,ps8,labelWhichTurn))
    ps9.bind('<Button-1>',lambda e: insertIntoBoard(player,8,ps9,labelWhichTurn))

    ps1.bind('<Enter>',lambda e: hover(ps1))
    ps2.bind('<Enter>',lambda e: hover(ps2))
    ps3.bind('<Enter>',lambda e: hover(ps3))
    ps4.bind('<Enter>',lambda e: hover(ps4))
    ps5.bind('<Enter>',lambda e: hover(ps5))
    ps6.bind('<Enter>',lambda e: hover(ps6))
    ps7.bind('<Enter>',lambda e: hover(ps7))
    ps8.bind('<Enter>',lambda e: hover(ps8))
    ps9.bind('<Enter>',lambda e: hover(ps9))

    ps1.bind('<Leave>',lambda e: notHover(ps1))
    ps2.bind('<Leave>',lambda e: notHover(ps2))
    ps3.bind('<Leave>',lambda e: notHover(ps3))
    ps4.bind('<Leave>',lambda e: notHover(ps4))
    ps5.bind('<Leave>',lambda e: notHover(ps5))
    ps6.bind('<Leave>',lambda e: notHover(ps6))
    ps7.bind('<Leave>',lambda e: notHover(ps7))
    ps8.bind('<Leave>',lambda e: notHover(ps8))
    ps9.bind('<Leave>',lambda e: notHover(ps9))

    
    singlePlayerWindow.mainloop()

def multiPlayers():
    global player,multiPlayerWindow,singlePlayerVal
    if (player==0):
        player=firstPlayer

    multiPlayerWindow = Tk()
    multiPlayerWindow.title('Multi Player Window')
    multiPlayerWindow.geometry('460x290')

    labelWhichTurn = Label(multiPlayerWindow, text=f"Player-{str(player)} click on the position you want to play in:", font="Default")
    labelWhichTurn.place(x=5,y=5)

    p1 = Button(multiPlayerWindow, text=board["0"],font="Default",width=3)
    p1.place(x=130,y=110)
    p2 = Button(multiPlayerWindow, text=board["1"],font="Default",width=3)
    p2.place(x=180,y=110)
    p3 = Button(multiPlayerWindow, text=board["2"],font="Default",width=3)
    p3.place(x=230,y=110)
    p4 = Button(multiPlayerWindow, text=board["3"],font="Default",width=3)
    p4.place(x=130,y=160)
    p5 = Button(multiPlayerWindow, text=board["4"],font="Default",width=3)
    p5.place(x=180,y=160)
    p6 = Button(multiPlayerWindow, text=board["5"],font="Default",width=3)
    p6.place(x=230,y=160)
    p7 = Button(multiPlayerWindow, text=board["6"],font="Default",width=3)
    p7.place(x=130,y=210)
    p8 = Button(multiPlayerWindow, text=board["7"],font="Default",width=3)
    p8.place(x=180,y=210)
    p9 = Button(multiPlayerWindow, text=board["8"],font="Default",width=3)
    p9.place(x=230,y=210)

    p1.bind('<Button-1>',lambda e: insertIntoBoard(player,0,p1,labelWhichTurn))
    p2.bind('<Button-1>',lambda e: insertIntoBoard(player,1,p2,labelWhichTurn))
    p3.bind('<Button-1>',lambda e: insertIntoBoard(player,2,p3,labelWhichTurn))
    p4.bind('<Button-1>',lambda e: insertIntoBoard(player,3,p4,labelWhichTurn))
    p5.bind('<Button-1>',lambda e: insertIntoBoard(player,4,p5,labelWhichTurn))
    p6.bind('<Button-1>',lambda e: insertIntoBoard(player,5,p6,labelWhichTurn))
    p7.bind('<Button-1>',lambda e: insertIntoBoard(player,6,p7,labelWhichTurn))
    p8.bind('<Button-1>',lambda e: insertIntoBoard(player,7,p8,labelWhichTurn))
    p9.bind('<Button-1>',lambda e: insertIntoBoard(player,8,p9,labelWhichTurn))

    p1.bind('<Enter>',lambda e: hover(p1))
    p2.bind('<Enter>',lambda e: hover(p2))
    p3.bind('<Enter>',lambda e: hover(p3))
    p4.bind('<Enter>',lambda e: hover(p4))
    p5.bind('<Enter>',lambda e: hover(p5))
    p6.bind('<Enter>',lambda e: hover(p6))
    p7.bind('<Enter>',lambda e: hover(p7))
    p8.bind('<Enter>',lambda e: hover(p8))
    p9.bind('<Enter>',lambda e: hover(p9))

    p1.bind('<Leave>',lambda e: notHover(p1))
    p2.bind('<Leave>',lambda e: notHover(p2))
    p3.bind('<Leave>',lambda e: notHover(p3))
    p4.bind('<Leave>',lambda e: notHover(p4))
    p5.bind('<Leave>',lambda e: notHover(p5))
    p6.bind('<Leave>',lambda e: notHover(p6))
    p7.bind('<Leave>',lambda e: notHover(p7))
    p8.bind('<Leave>',lambda e: notHover(p8))
    p9.bind('<Leave>',lambda e: notHover(p9))

    multiPlayerWindow.mainloop()


def exitWindow(window):
    window.destroy()
    return
    

def exitProgram(e):
    exit()

# Hover Event
def hover(widget):
    widget.config(cursor="tcross",bg="#aaaaaa")

def notHover(widget):
    widget.config(cursor="arrow",bg="#f0f0f0")


def main():
    global menu
    menu = Tk()
    menu.title('Menu')
    menu.geometry('230x180')

    l1 = Label(menu, text='Welcome to <X && O>.',font="Default")
    l1.grid(column=0, row=0)
    
    l2 = Label(menu, text='Choose form the menu:',font="Default")
    l2.grid(column=0, row=1)

    l3 = Label(menu, text=' 1- Single Player',font="Default")
    l3.grid(column=0, row=2)
    l4 = Label(menu, text=' 2- Multi Players',font="Default")
    l4.grid(column=0, row=3)
    l6 = Label(menu, text=' 3- Exit             ',font="Default")
    l6.grid(column=0, row=5)

    # Click Event
    l3.bind('<Button-1>',lambda e: chooseCharacter(1))
    l4.bind('<Button-1>',lambda e: chooseCharacter(2))
    l6.bind('<Button-1>',exitProgram)
    
    # Hover Event
    l3.bind('<Enter>',lambda e: hover(l3))
    l4.bind('<Enter>',lambda e: hover(l4))
    l6.bind('<Enter>',lambda e: hover(l6))
    l3.bind('<Leave>',lambda e: notHover(l3))
    l4.bind('<Leave>',lambda e: notHover(l4))
    l6.bind('<Leave>',lambda e: notHover(l6))

    menu.mainloop()


main()
