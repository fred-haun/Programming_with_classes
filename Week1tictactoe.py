#Freddy Haun
#CSE 210
#Week 1 Ponder and Prove: Tic-Tac-Toe
def getDisplay():
    # creating varaible for all selectable areas in the tic-tac-toe game
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"
    #Create variable for game winner
    Winner = 0
    # While loop that does not end until game over conditions are met.
    while (Winner == 0):
        i = 2
        # While loop that gets an input from the X player and pushes it to the display
        while i % 2 == 0:
            choice = input("x's turn to choose a square (1-9): ")
            if choice == "1":
                one = "X"
                i += 1 
            elif choice == "2":
                two = "X"
                i += 1 
            elif choice == "3":
                three = "X"
                i += 1 
            elif choice == "4":
                four = "X"
                i += 1 
            elif choice == "5":
                five = "X"
                i += 1 
            elif choice == "6":
                six = "X"
                i += 1 
            elif choice == "7":
                seven = "X"
                i += 1 
            elif choice == "8":
                eight = "X"
                i += 1 
            elif choice == "9":
                nine = "X"
                i += 1
            #if input it not valid it repeates player input 
            else:
                print("Invalid input")
            # checking conditions if X won
            print(f"\n{one}|{two}|{three}\n-+-+-\n{four}|{five}|{six}\n-+-+-\n{seven}|{eight}|{nine}\n")
            if ((one == "X" and two == "X" and three == "X")
            or (four == "X" and five == "X" and six == "X")
            or (seven == "X" and eight == "X" and nine == "X")
            or (one == "X" and four == "X" and seven == "X")
            or (two == "X" and five == "X" and eight == "X")
            or (three == "X" and six == "X" and nine == "X")
            or (one == "X" and five == "X" and nine == "X")
            or (seven == "X" and five == "X" and three == "X")):
                Winner +=1 
                print ("Congrats X!")
                raise SystemExit
            #checking conditions if their is no winner
            if (one != "1" and two != "2" and three != "3" and
                four != "4" and five != "5" and six != "6" and
                seven != "7" and eight != "8" and nine != "9"):
                print ("Nobody wins, Game over.")
                raise SystemExit
        # While loop that gets an input from the O player and pushes it to the display
        while i % 2 == 1:
            choice = input("o's turn to choose a square (1-9): ")
            if choice == "1":
                one = "O"
                i += 1 
            elif choice == "2":
                two = "O"
                i += 1 
            elif choice == "3":
                three = "O"
                i += 1 
            elif choice == "4":
                four = "O"
                i += 1 
            elif choice == "5":
                five = "O"
                i += 1 
            elif choice == "6":
                six = "O"
                i += 1 
            elif choice == "7":
                seven = "O"
                i += 1 
            elif choice == "8":
                eight = "O"
                i += 1 
            elif choice == "9":
                nine = "O"
                i += 1 
            else:
                print("Invalid input")
            # checking conditions if X won
            print(f"{one}|{two}|{three}\n-+-+-\n{four}|{five}|{six}\n-+-+-\n{seven}|{eight}|{nine}\n")
            if ((one == "O" and two == "O" and three == "O")
            or (four == "O" and five == "O" and six == "O")
            or (seven == "O" and eight == "O" and nine == "O")
            or (one == "O" and four == "O" and seven == "O")
            or (two == "O" and five == "O" and eight == "O")
            or (three == "O" and six == "O" and nine == "O")
            or (one == "O" and five == "O" and nine == "O")
            or (seven == "O" and five == "O" and three == "O")):
                Winner += 1
                print ("Congrats O!")
            if (one != "1" and two != "2" and three != "3" and
                four != "4" and five != "5" and six != "6" and
                seven != "7" and eight != "8" and nine != "9"):
                print ("Nobody wins, Game over.")
                raise SystemExit

def main():
    print(f"\n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
    #retrieves function to update display
    getDisplay()

main()