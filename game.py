tokens = 21
validAnswers = ["first", "f", "last", "l"]

def first_or_second():
    turn = None
    while turn not in validAnswers:
        turn = input("Please choose whether you would like to go (F)IRST or (L)AST. ").lower()
    return turn

if __name__ == "__main__":
    print(first_or_second())
