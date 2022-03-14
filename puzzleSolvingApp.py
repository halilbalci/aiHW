from CSPPuzzle import CSPPuzzle

def main():
    x=inputInteger("Choose a puzzle 1 or 2 or 3 (0 to quit):")
    while(x==None):
        x=inputInteger("Choose a puzzle 1 or 2 or 3:")
    if(x!=0):
        try:
            puzzle=CSPPuzzle(str(x))
            puzzle.solve()
        except SystemExit:
            print("------------Puzzle is solved--------")
        except:
            print("ERROR! \n please try again.")
            main()
def inputInteger(text):
    user_input = input(text)
    print("\n")
    try:
        val = int(user_input)
        return val
    except ValueError:
        print("input is not an integer.")
        return None

if __name__ == '__main__':
    main()