import random as rnd
from time import sleep as slp

tokens = 21
gameRun = True

def first_or_second(turn = None):
    validAnswers = ["first", "f", "last", "l"]
    while turn not in validAnswers:
        turn = input("Please choose whether you would like to go (F)IRST or (L)AST. ").lower()
    return turn

def player_choose(tokenCount):
    if tokens != 0:
        playerNumber = int(input(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3) "))
        while playerNumber < 1 or playerNumber > 3:
            playerNumber = int(input(f"Tokens left: {tokenCount} | Please choose a number between 1 and 3. "))
        return int(tokenCount - playerNumber)

def cpu_choose(tokenCount):
    if gameRun == True:
        if tokenCount > 3 and tokens != None:
            print(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3)")
            cpuNumber = rnd.randint(1, 3)
            slp(1.5)
            print(f"Computer chooses {cpuNumber} tokens.")
            return tokenCount - cpuNumber
        elif tokenCount <= 3 and tokenCount > 0 and tokens != None:
            print(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3)")
            cpuNumber = tokenCount
            slp(1.5)
            print(f"Computer chooses {cpuNumber} tokens.")
            return int(tokenCount - cpuNumber)
        elif tokenCount == None:
            pass

def check_if_win(totalTokens):
    if totalTokens == 0:
        print("Big winner over here!")
        return False
    else:
        print("Next turn comin' up!")
        return True

if __name__ == "__main__":
    turnOrder = first_or_second()
    if turnOrder == "first" or turnOrder == "f":
        print("Player goes first.")
        while gameRun == True:
            tokens = player_choose(tokens)
            gameRun = check_if_win(tokens)
            tokens = cpu_choose(tokens)
            if tokens != None:
                gameRun = check_if_win(tokens)
    else:
        print("CPU goes first.")
        while gameRun == True:
            tokens = cpu_choose(tokens)
            gameRun = check_if_win(tokens)
            tokens = player_choose(tokens)
            if tokens != None:
                gameRun = check_if_win(tokens)
