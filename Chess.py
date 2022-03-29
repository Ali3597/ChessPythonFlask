from Board import Board
import Piece

class Chess():

    def __init__(self):
        self._board = Board()
        self._turn = 1
        
    def get_board(self):
        return self._board

    def get_turn(self):
        return self._turn

    
    def changeTurn(self):
        if self._turn==1:
            self._turn=2
        else:
            self._turn=1



    def move(self,start,destination):
        if  self._board.get_board()[start[0]][start[1]].get_player() == None :
           raise ValueError("Vous essayez de jouer une case sans piece")
        if self._turn != self._board.get_board()[start[0]][start[1]].get_player()  :
           raise ValueError("Vous ne pas jouez les pieces de l'adevrsaire")
        if self._turn == self._board.get_board()[destination[0]][destination[1]].get_player()  :
            raise ValueError("Il ya une de vos piece ou vous voulez aller") 
        if self._board.get_board()[start[0]][start[1]].is_valid_move(self._board,start,destination):
            self._board.get_board()[destination[0]][destination[1]] = self._board.get_board()[start[0]][start[1]]
            self._board.get_board()[start[0]][start[1]]= Piece.Empty(0)

    def canYouEatTheKing(self,playerWhoMayWin):
        for x in range(len(self._board.get_board())):
            for i in range(len(self._board.get_board()[x])):
                if self._board.get_board()[x][i].get_player() == playerWhoMayWin:
                    try:
                        if(self._board.get_board()[x][i].is_valid_move(self._board,(x,i),self._board.get_kingPositions()[1 if playerWhoMayWin == 1 else 0])):
                            return True
                    except: 
                        pass

        return False

    def getBox(self,x, y):
        return  self._board.get_board()[x][y];

    def promotePawn(self,player,promote,position):
        if promote == "Q":
            self._board.get_board()[position[0]][position[1]] = Piece.Queen(player)
        if promote == "R":
            self._board.get_board()[position[0]][position[1]] = Piece.Rook(player)
        if promote == "N":
            self._board.get_board()[position[0]][position[1]] = Piece.Knight(player)
        if promote == "B":
            self._board.get_board()[position[0]][position[1]] = Piece.Bishop(player)

        
            

        
        


