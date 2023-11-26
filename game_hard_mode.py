from slow_print import slow_print
from time import sleep as slp

tokens = 24
gameRun = True

def player_choose(tokenCount):
    if tokens != 0:
        playerNumber = int(input(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3) "))
        while playerNumber < 1 or playerNumber > 3:
            playerNumber = int(input(f"Tokens left: {tokenCount} | Please choose a number between 1 and 3. "))
        return int(tokenCount - playerNumber), playerNumber

def cpu_choose(tokenCount, playerChoice):
    if gameRun == True:
        if tokenCount > 3 and tokens != None:
            print(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3)")
            cpuNumber = 4 - playerChoice
            slp(1.5)
            slow_print(f"Computer chooses {cpuNumber} tokens.")
            return tokenCount - cpuNumber
        elif tokenCount <= 3 and tokenCount > 0 and tokens != None:
            print(f"Tokens left: {tokenCount} | How many tokens do you want to take? (1-3)")
            cpuNumber = tokenCount
            slp(0.5)
            slow_print("Hm...")
            slp(1.0)
            slow_print("Ah ha!")
            slp(0.5)
            slow_print(f"Computer chooses {cpuNumber} tokens.")
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
    print("Player goes first.")
    while gameRun == True:
        tokens, playerTokenChoice = player_choose(tokens)
        gameRun = check_if_win(tokens)
        tokens = cpu_choose(tokens, playerTokenChoice)
        if tokens != None:
            gameRun = check_if_win(tokens)
