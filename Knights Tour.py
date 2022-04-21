class Tour():
    def __init__(self, numRows: int, numCols: int, startX: int, startY: int) -> None:
        self.numRows = numRows
        self.numCols = numCols
        self.size = numRows * numCols
        self.spaceNum = 0

        try:
            self.board = [[-1 for row in range(self.numRows)]for col in range(self.numCols)]
            self.board[startX][startY] = 0
        except:
            print("STARTING POSITION [" + str(startX) + ", " + str(startY) + "] IS OUT OF RANGE!")
            print("CHOOSE A DIFFERENT STARTING POSITION!")
            raise SystemExit

        self.moveXY = [
        [2, 1], [1, 2],
        [-1, 2], [-2, 1],
        [-2, -1], [-1, -2],
        [1, -2], [2, -1]]
        return
    
    def printBoard(self) ->  None:
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.board[row][col], end = ' \t')
            print()
        return

    def validMove(self, moveToX: int, moveToY: int) -> bool:
        if((moveToX > -1) and (moveToX < self.numCols)):
            if((moveToY > -1) and (moveToY < self.numRows)):
                if(self.board[moveToX][moveToY] == -1):
                    return True
        return False

    def moveToNextSpace(self, moveToX: int, moveToY: int) -> None:
        self.spaceNum += 1
        self.board[moveToX][moveToY] = self.spaceNum
        return

    def backtrack(self, moveToX: int, moveToY: int) -> None:
        self.spaceNum -= 1
        self.board[moveToX][moveToY] = -1
        return

    def generateTour(self, nextX: int, nextY: int) -> bool:
        if(self.spaceNum == self.size - 1):
            return True

        for i in range(len(self.moveXY)):
            newX = nextX + self.moveXY[i][0]
            newY = nextY + self.moveXY[i][1]

            if(self.validMove(newX, newY) == True):
                self.moveToNextSpace(newX, newY)

                if(self.generateTour(newX, newY) == True):
                    return True
                    
                self.backtrack(newX, newY)
        return False

    def solve(self, startX: int, startY: int) -> None:
        if(self.generateTour(startX, startY) == False):
            print("NO SOLUTION!")
        else:
            self.printBoard()
        return

def main():
    NUMROWS = 8
    NUMCOLS = 8
    STARTX = 8
    STARTY = 8

    knight = Tour(NUMROWS, NUMCOLS, STARTX, STARTY)
    knight.solve(STARTX, STARTY)

    return 0

if __name__ == "__main__":
    main()