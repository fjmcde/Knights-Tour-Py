## -Tour class which encapsulates all relevant data:
##      - Number of rows (numRows), number of columns (numCols), the size of the board (size; # of spaces),
##        the knights starting position (startX, startY), the number of spaces that have been visited while
##        the knight traverses the board (spaceNum)
## - Has bounds checking for the starting position of the knight; to ensure the user has entered a valid
##   starting location. If invalid, will inform the user.
## - Ensures that the size of the board is (N x N) and not (N x M). Notifies the user when N x M is given
## - A list of legal moves that the knight can make. These moves are grouped as lists of two elements which
##   represent an [x, y] pair
class Tour():
    def __init__(self, numRows: int, numCols: int, startX: int, startY: int) -> None:
        if(numRows != numCols):
            print("INVALID BOARD SIZE: GIVEN N X M!")
            print("NUMBER OF ROWS MUST EQUAL THE NUMBER OF COLUMNS (N X N)")
            raise SystemExit

        self.numRows = numRows
        self.numCols = numCols
        self.size = numRows * numCols
        self.spaceNum = 0

        if((startX > -1 and startX < numRows) and (startY > -1 and startY < numRows)):
                self.board = [[-1 for row in range(self.numRows)]for col in range(self.numCols)]
                self.board[startY][startX] = 0
        else:
            print("STARTING POSITION [" + str(startX) + ", " + str(startY) + "] IS OUT OF RANGE!")
            print("CHOOSE A DIFFERENT STARTING POSITION!")
            raise SystemExit

        self.startX = startX
        self.startY = startY

        self.moveXY = [
        [2, 1], [1, 2],     ## right-down
        [-1, 2], [-2, 1],   ## left-down
        [-2, -1], [-1, -2], ## left-up
        [1, -2], [2, -1]]   ## right-up
        return
    
    ## prints the values of the board in row-major order
    def printBoard(self) -> None:
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.board[row][col], end = ' \t')
            print()
        return

    ## checks whether a move is valid.
    ## A move is valid when:
    ## - Both the x and y cooordinates are within the bounds
    ##   of the board
    ## - And the space has not been visited yet
    def validMove(self, moveToX: int, moveToY: int) -> bool:
        if((moveToX > -1) and (moveToX < self.numCols)):
            if((moveToY > -1) and (moveToY < self.numRows)):
                if(self.board[moveToY][moveToX] == -1):
                    return True
        return False

    ## Warnsdorff's heuristics:
    ## Warnsdorff's rule states that the knight is to be moved
    ## so that it always proceeds to a space  from which the knight will
    ## have the fewest possible moves. That is, we find the move which
    ## has the lowest degree of moves to proceed
    def findLowestDegree(self, nextX: int, nextY: int) -> list:
        degrees = []

        ## for each valid move from the current space...
        for i in range(len(self.moveXY)):
            newX = nextX + self.moveXY[i][0]
            newY = nextY + self.moveXY[i][1]
            count = 0
            
            if(self.validMove(newX, newY) == True):

                ## ... count the number of moves that can be made from
                ## the resultant space
                for j in range(len(self.moveXY)):
                    checkX = newX + self.moveXY[j][0]
                    checkY = newY + self.moveXY[j][1]

                    if(self.validMove(checkX, checkY) == True):
                        count += 1

                ## a pair of integers: the index from the self.moveXY list
                ## and the number of degrees counted is appended to a list...
                pair = [i, count]
                degrees.append(pair)
                count = 0
        
        ## ... which is then sorted, in descending order by degree
        degrees.sort(key = lambda x: x[1])

        return degrees

    ## uses the resultant list form findLowestDegree to
    ## build a new list of optimal moves.
    ## The first element in the degrees list corresponds to the
    ## index of the move (from Tour's moveXY list) which has the
    ## lowest degree of possible moves. A list of optimal moves is
    #  created by reordering valid moves from the moveXY list
    def getOptimalMoves(self, degrees):
        optimalMoveList = []

        for i in range(len(degrees)):
            index = degrees[i][0]
            optimalMoveList.append(self.moveXY[index])

        return optimalMoveList
    
    ## moves knight to a new space
    ## the new space gets updated with a new space number
    def moveToNextSpace(self, moveToX: int, moveToY: int) -> None:
        self.spaceNum += 1
        self.board[moveToY][moveToX] = self.spaceNum
        return

    ## backtracks the knight to the previous space
    ## decrements the spaceNumber
    def backtrack(self, moveToX: int, moveToY: int) -> None:
        self.spaceNum -= 1
        self.board[moveToY][moveToX] = -1
        return

    ## generates a tour by:
    ##  - calculating which move has the lowest number of possible moves
    ##    thereof (degrees).
    ##  - moving the knight to that space
    ##  - recursively generate a new tour using the new space: 
    ##      - returning False when no valid moves exist from that space
    ##          - when false recursively backtracking
    ##  - when the all spaces have been visited returns true to break recursion
    def generateTour(self, nextX: int, nextY: int) -> bool:
        if(self.spaceNum == self.size - 1):
            return True
    
        degrees = self.findLowestDegree(nextX, nextY)
        
        if len(degrees) == 0:
            return False

        optimalMoves = self.getOptimalMoves(degrees)

        for i in range(len(optimalMoves)):
            newX = nextX + optimalMoves[i][0]
            newY = nextY + optimalMoves[i][1]

            self.moveToNextSpace(newX, newY)

            if(self.generateTour(newX, newY) == True):
                return True
                
            self.backtrack(newX, newY)
        return False

    ## solver function which initally calls generateTour
    ## - when generateTour returns False, displays a message that
    ##   there is no valid solution.
    ## - when generateTour returns True, prints the contents of the
    ##   board.
    def solve(self) -> None:
        if(self.generateTour(self.startX, self.startY) == False):
            print("NO SOLUTION!")
        else:
            self.printBoard()
        return