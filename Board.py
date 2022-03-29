import Piece

class Board():

    def __init__(self):
        self._board= []
        self._theme= True
        for x in range(2,0,-1):
            if x==2:
                self._board.append(self.PlayerLign(x))
                self._board.append(self.PawnLign(x))
                for i in range(4):
                    self._board.append(self.ligneVide())
            else:
                self._board.append(self.PawnLign(x))
                self._board.append(self.PlayerLign(x))
        self._kingPositions= [(7,4),(0,4)]

    def get_board(self):
        return self._board

    def get_kingPositions(self):
        return self._kingPositions


    def print_boardConsole(self):
        n=len(self._board)
        toPrintBefore="    "
        if self._theme:
            print(toPrintBefore+"  ▄▄▄▄    ▄▄▄▄    ▄▄▄▄    ▄▄▄▄")
        else:
            print("  ▄▄▄▄    ▄▄▄▄    ▄▄▄▄    ▄▄▄▄")
        for x in range(n):
            if x!= 0:
                if self._theme:
                    print("  ▀▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄")
                else:
                    print("  ▄▄▄▄▀▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▀▀▄▄▄▄▀▀▀▀")
            print (n-x,end=' ')
            for i in self._board[x]:
                if i.get_name() != "":
                    if self._theme :
                        printedBeetween = " "
                    else:
                        printedBeetween = "█"
                    print (printedBeetween + i.get_symbol() + " "+printedBeetween,end="")
                else:
                    if self._theme :
                        print(i.get_symbol(),end="")
                    else:
                        print(i.get_symbol() ,end="")
                self._theme = not self._theme
            print("")
            self._theme = not self._theme
        if self._theme:
            print("  ▀▀▀▀    ▀▀▀▀    ▀▀▀▀    ▀▀▀▀")
        else:
            print( toPrintBefore+"  ▀▀▀▀    ▀▀▀▀    ▀▀▀▀    ▀▀▀▀")
        print("   A   B   C   D   E   F   G   H")

    def PawnLign(self,player):
        ligne = []
        for i in range(8):    
            ligne.append(Piece.Pawn(player))  
        return ligne

    def PlayerLign(self,player):
        return [ Piece.Rook(player),Piece.Knight(player),Piece.Bishop(player) ,Piece.Queen(player), Piece.King(player) , Piece.Bishop(player) , Piece.Knight(player), Piece.Rook(player)]
    
    def ligneVide(self):
        ligne = []
        for i in range(8):    
            ligne.append(Piece.Empty(0))  
        return ligne