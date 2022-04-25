from knightsTour import Tour

## Driver code to run a knights tour
## Just provide:
## - The size of the board (Note: must be N x N);
## - A starting position for the knight (Note: rows and columns begin with 0
##   so there are only N - 1 valid spaces; where N = NUMROWS OR NUMCOLS);
## - Instantiate a Tour object by passing the size and starting position 
##   of the knight into the constructor
## - Call the solve() function
def main():
    NUMROWS = 8
    NUMCOLS = 8
    STARTX = 0
    STARTY = 0

    knight = Tour(NUMROWS, NUMCOLS, STARTX, STARTY)
    knight.solve()

    return 0

if __name__ == "__main__":
    main()