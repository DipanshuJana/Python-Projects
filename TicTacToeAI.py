import random

# main game function
def game():
    boardList = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']] # represents the whole game board
    adList = [ ['00', '01', '02'], # stores winning posibilities
            ['10', '11', '12'],
            ['20', '21', '22'],
            ['00', '10', '20'], 
            ['01', '11', '21'],
            ['02', '12', '22'],
            ['00', '11', '22'],
            ['02', '11', '20'] ]
    botVal = input('Enter bot symbol: ')[0]
    while (True):
        userVal = input('Enter your symbol: ')[0]
        if (userVal == botVal):
            print('Both players cannot have same symbol!')
        else: break

    turn = userVal # change the turn 
    result = 0 # stores the result (bot win / user win / draw)

    printBoard(boardList, userVal, botVal)

    while(True):
        if (turn == userVal):
            while(True):
                print("Your turn! Enter the position in [i][j]:")
                inpVal = input()
                valI = int(inpVal[0])
                valJ = int(inpVal[1])
                try:
                    if (boardList[valI][valJ] == inpVal):
                        boardList[valI][valJ] = userVal
                        break
                    else:
                        print("Value already present!")
                except IndexError:
                    print("Invalid poistion")

            turn = botVal
        
        else:
            print("Bot's turn")
            botValIn = AI(adList, boardList, userVal, botVal)
            if (botValIn == 0):
                while(True):
                    randI = boardList.index(random.choice(boardList))
                    randJ = boardList[randI].index(random.choice(boardList[randI]))

                    if (boardList[randI][randJ] != userVal):
                        botValIn = f'{randI}{randJ}'
                        boardList[randI][randJ] = botVal
                        break

            else:
                boardList[int(botValIn[0])][int(botValIn[1])] = botVal           
            
            turn = userVal

        printBoard(boardList, userVal, botVal)
        
        r = winCheck(boardList, adList, userVal, botVal, result)
        if (r == 1):
            print ("You won!")
            break
        elif (r == 2): 
            print ("Bot won!")
            break
        elif(r == 3):
            print("Draw!")
            break


# intellegence algorithm
def AI(adList, boardList, userVal, botVal):
    for i in range(len(adList)):
        IJ1Val = boardList[int(adList[i][0][0])][int(adList[i][0][1])]
        IJ2Val = boardList[int(adList[i][1][0])][int(adList[i][1][1])]
        IJ3Val = boardList[int(adList[i][2][0])][int(adList[i][2][1])]

        winChance = False

        for j in range(len(adList)):
            loopIJ1Val = boardList[int(adList[j][0][0])][int(adList[j][0][1])]
            loopIJ2Val = boardList[int(adList[j][1][0])][int(adList[j][1][1])]
            loopIJ3Val = boardList[int(adList[j][2][0])][int(adList[j][2][1])]
            if (loopIJ1Val == loopIJ2Val and len(loopIJ3Val) > 1 and loopIJ1Val == loopIJ2Val == botVal):
                winChance = True
                return f'{adList[j][2][0]}{adList[j][2][1]}'
                break
            elif (loopIJ2Val == loopIJ3Val and len(loopIJ1Val) > 1 and loopIJ2Val == loopIJ3Val == botVal):
                winChance = True
                return f'{adList[j][0][0]}{adList[j][0][1]}'
                break
            if (loopIJ1Val == loopIJ3Val and len(loopIJ2Val) > 1 and loopIJ1Val == loopIJ3Val == botVal):
                winChance = True
                return f'{adList[j][1][0]}{adList[j][1][1]}'
                break
        
        if (IJ1Val == IJ2Val and len(IJ3Val) > 1 and IJ1Val == IJ2Val == userVal):
            return f'{int(adList[i][2][0])}{int(adList[i][2][1])}'
            break
        elif(IJ2Val == IJ3Val and len(IJ1Val) > 1 and IJ2Val == IJ3Val == userVal):
            return f'{int(adList[i][0][0])}{int(adList[i][0][1])}'
            break
        elif(IJ1Val == IJ3Val and len(IJ2Val) > 1 and IJ1Val == IJ3Val == userVal):
            return f'{int(adList[i][1][0])}{int(adList[i][1][1])}'
            break
        elif (i == len(adList) - 1): 
            return 0    
            break

# prints the updated board after each value is entered
def printBoard(boardList, userVal, botVal):
    for i in range(3):
        for j in range(3):
            if (len(boardList[i][j]) == 1):
                if (j == 1): print(f" {boardList[i][j]} ", end = "")
                else: print(f"| {boardList[i][j]} |", end = "")    
            else:
                if (j == 1): print("   ", end="")
                else: print("|   |", end="")
        print()

# checks for any possible win
def winCheck(boardList, adList, userVal, botVal, result): 
    for i in range(3):
        for j in range(3):
            if (len(boardList[i][j]) > 1):
                result = 4
                break
    if (result == 4): result = 0
    elif(result == 0): return 3
   
    for i in range(len(adList)):
        OIJ1Val = boardList[int(adList[i][0][0])][int(adList[i][0][1])]
        OIJ2Val = boardList[int(adList[i][1][0])][int(adList[i][1][1])]
        OIJ3Val = boardList[int(adList[i][2][0])][int(adList[i][2][1])]

        if (OIJ1Val == OIJ2Val == OIJ3Val == userVal):
            result = 1
            return result
            break
        elif (OIJ1Val == OIJ2Val == OIJ3Val == botVal):
            result = 2
            return result
            break

if __name__ == "__main__":
    gameCount = 0
    while (True):
        if (gameCount == 0):
            game()
            gameCount += 1
        else:
            choice = input('\nDo you want to play again? Y/N: ')[0]
            if (choice == 'Y' or choice == 'y'):
                game()
            else: break