import random

class TicTacToeGame(object):
    def __init__(self):
        self.title = "T I C - T A C - T O E"
        self.end_game = [False, None]
        self.picDict = self.build_picDict()
        self.moveSet = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]
        self.madeMoves = []
        """    col
             |     |
          X  |  X  |  X         1,2  1,8  1,14
        _ _ _|_ _ _|_ _ _
     r       |     |
     o    X  |  X  |  X         4,2  4,8  4,14
     w  _ _ _|_ _ _|_ _ _
             |     |
          X  |  X  |  X         7,2  7,8  7,14
             |     |
        """

        """
        AI brute force
        If AI goes first - only 3 distinct moves to be made
            (1,1), (2,2), (1,2) - all others are equivalent based on symmetry

        """

    def build_picDict(self):
        """
        This method creates the tic-tac-toe board base 0, with keys equating to rows and the values equating to columns
        :return: a dictionary representing the tic-tac-toe board
        """
        picDict = {}
        rowList = [[0,1,3,4,6,7,8],[2,5]]
        rowPic = [[' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                  ['_',' ','_',' ','_','|','_',' ','_',' ','_','|','_',' ','_',' ','_']]
        # build picture
        counter = 0
        for rows in rowList:
            for row in rows:
                picDict[row] = list(rowPic[counter])
            counter += 1
        return picDict

    def update_pic(self,move,symbol):
        self.picDict[move[0]][move[1]] = symbol

    def print_pic(self):
        """ Prints the hangman picture in its current state
        """
        for i in range(len(self.picDict)):
            print reduce(self.smush,self.picDict[i])

    def make_move(self, move, symbol):
        """ Used to determine whether or not a guessed letter is in the answer and
            Take appropriate action

        """
        # Validate the move
        if move not in self.moveSet:
            print '"%s" is not valid - move must be two integers (1,2,or 3) separated by a comma - move again' % str((move))
            return False
        if move in self.madeMoves:
            print 'Your move %s has already been made - move again' % str((move))
            return False

        # Transform move coordinates from player into dictionary address
        dicMove = ((move[0] - 1) * 3 + 1, (move[1] - 1) * 6 + 2)
        self.update_pic(dicMove,symbol)
        self.madeMoves.append(move)
        return True

    def player_move(self,player,symbol):
        while True:
            print 'Player %s (%s): Make a move.' % (str(player), symbol)
            move = raw_input('Move (row, col): ')
            try:
                move_tuple = (int(move.split(',')[0]),int(move.split(',')[1]))
                if self.make_move(move_tuple,symbol):
                    break
            except ValueError:
                print '"%s" is not valid - move must be two integers (1,2,or 3) separated by a comma - move again' % str((move))


    def announce_win(self,player):
        print
        print 'Player %s has won! Congrats!' % (str(player))
        self.print_pic()

    def play(self):
        print self.title
        # determine how many humans will play
        roundCounter = 0
        while True:
            roundCounter += 1
            print '----Round %s----' % (roundCounter)
            self.print_pic()
            if roundCounter >= 4:
                win = self.check_win(self.picDict,"O") # check for win with O
                if win:
                    self.announce_win(2)
                    break
            self.player_move(1,'X')
            print
            self.print_pic()
            if roundCounter >= 3:
                win = self.check_win(self.picDict,"X") # check for win with X
                if win:
                    self.announce_win(1)
                    break
            if roundCounter == 5:
                print 'Game is over - tie!'
                break
            self.player_move(2,'O')
            print


    def check_win(self,board,symbol):
        wStr = symbol * 3
        # check horizontal wins
        for i in (1,4,7):
            if board[i][2] + board[i][8] + board[i][14] == wStr:
                # update pic appropriately
                for j in (0,1,3,4,6,7,9,10,12,13,15,16):
                    self.update_pic((i,j),'-')
                return True
        # check vertical wins
        for i in (2,8,14):
            if board[1][i] + board[4][i] + board[7][i] == wStr:
                for j in (0,2,3,5,6,8):
                    self.update_pic((j,i),'|')
                return True
        # check diagonal wins
        if board[1][2] + board[4][8] + board[7][14] == wStr:
            for i in [(0,0), (2,4), (3,6), (5,10), (6,12), (8,16)]:
                self.update_pic((i[0],i[1]),'\\')
            return True
        if board[7][2] + board[4][8] + board[1][14] == wStr:
            for i in [(8,0), (6,4), (5,6), (3,10), (2,12), (0,16)]:
                self.update_pic((i[0],i[1]),'/')
            return True

    def smush(self,x,y):
        return x + y

def _main_():
    start = 'Y'
    answer = ''
    gameCounter = 0
    while answer.upper() == 'Y' or start == 'Y':
        start, answer = '', ''
        gameCounter += 1
        print
        print 'GAME NUMBER ' + str(gameCounter) + ' OF... '
        curTic = TicTacToeGame()
        result = curTic.play()
        while answer.upper() not in ('Y','N'):
            answer = raw_input('Play again (y/n): ')

_main_()
# print (1,1) in curTic.moveSet