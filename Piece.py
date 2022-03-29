
class Piece():
    def __init__(self,player):
        self._name = ""
        self._symbol= ""
        self._player = player
        
    def get_name(self):
        return self._name
    
    def get_symbol(self):
        return self._symbol

    def get_player(self):
        return self._player


    def is_valid_move(self):
        return False
    
    def check_diag(self,board, start, destination):
        if (destination[0] - start[0] > 0):
            xMouvement=1
        else:
            xMouvement=-1
        if (destination[1] - start[1] > 0):
            yMouvement=1
        else:
            yMouvement=-1
        
        i = start[0] + xMouvement
        j = start[1] + yMouvement
        while (i < destination[0] if xMouvement==1 else i > destination[0]):
            if board[i][j].get_name() != "":
                raise ValueError("Il ya une piece sur le passage")
            i += xMouvement
            j += yMouvement
        return True
    
    def check_CrossDirection(self,board, start, destination):
        if start[0] == destination[0]:
            if (start[1] < destination[1]):
                smaller = start[1] 
                bigger = destination[1]
            else:
                smaller= destination[1]
                bigger= start[1]

            for i in range(smaller + 1, bigger):
                if board[start[0]][i].get_name() != "":
                    raise ValueError("Il ya une piece sur le passage")
            return True
        else:
            if (start[0] < destination[0]):
                smaller = start[0] 
                bigger = destination[0]
            else:
                smaller= destination[0]
                bigger= start[0]
            for i in range(smaller + 1, bigger):
                if board[i][start[1]].get_name() != "":
                    raise ValueError("Il ya une piece sur le passage")
            return True


class Rook(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "R"
        if player==2:
            self._symbol = "♜"
        else:
            self._symbol = "♖"
        

    def is_valid_move(self, board, start, destination):
        if start[0] == destination[0] or start[1] == destination[1]:
            return self.check_CrossDirection(board.get_board(), start, destination)
        raise ValueError("Ce n'est pas un valide mouvement ")

class Knight(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "N"
        if player==2:
            self._symbol = "♞"
        else:
            self._symbol = "♘"
        

    def is_valid_move(self ,board, start, destination):
        if abs(start[0] - destination[0]) == 2 and abs(start[1] - destination[1]) == 1:
            return True
        if abs(start[0] - destination[0]) == 1 and abs(start[1] - destination[1]) == 2:
            return True
        raise ValueError("Ce n'est pas un valide mouvement ")

class Bishop(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "B"
        if player==2:
            self._symbol = "♝"
        else:
            self._symbol = "♗"


    def is_valid_move(self, board, start, destination):
        if abs(start[0] - destination[0]) != abs(start[1] - destination[1]):
            raise ValueError("Ce n'est pas un valide mouvement ")
        return self.check_diag(board.get_board(), start, destination)

class Queen(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Q"
        if player==2:
            self._symbol = "♛"
        else:
            self._symbol = "♕"
        

    def is_valid_move(self, board, start, destination):
        if abs(start[0] - destination[0]) == abs(start[1] - destination[1]):
            return self.check_diag(board.get_board(), start, destination)
        elif start[0] == destination[0] or start[1] == destination[1]:
            return self.check_CrossDirection(board.get_board(), start, destination)
        raise ValueError("Ce n'est pas un valide mouvement ")

class King(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "K"
        if player==2:
            self._symbol = "♚"
        else:
            self._symbol = "♔"
        

    def is_valid_move(self, board, start, destination):
        if  board.get_board()[destination[0]][destination[1]].get_name() == "K":
            raise ValueError("Un roi ne peut pas manger un autre roi")
        if abs(start[0] - destination[0]) == 1 or start[0] - destination[0] == 0:
            if start[1] - destination[1] == 0 or abs(start[1] - destination[1]) == 1:
                board.get_kingPositions()[self._player-1] = (destination[0],destination[1])
                return True
        raise ValueError("Ce n'est pas un valide mouvement ")
    


class Pawn(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._name = "P"
        if player==2:
            self._symbol = "♟︎"
        else:
            self._symbol = "♙"
        self._first_move = True

    def is_valid_move(self, board, start, destination):
        if self._player==1:
            # diagonal move
            if start[0] == destination[0] + 1 and (start[1] == destination[1] + 1 or start[1] == destination[1] - 1):
                if board.get_board()[destination[0]][destination[1]].get_name() != "":
                    self._first_move = False
                    return True
                raise ValueError("Un pion ne peut pas se deplacer en diagonal seulment s'il mange une piece advrsaire")

            # vertical move
            if start[1] == destination[1]:
                if (start[0] - destination[0] == 2 and self._first_move) or (start[0] - destination[0] == 1):
                    for i in range(start[0] - 1, destination[0] - 1, -1):
                        if board.get_board()[i][start[1]].get_name() != "":
                            raise ValueError("Il ya une piece sur le passage")
                    self._first_move = False
                    return True
                raise ValueError("Ce n'est pas un valide mouvement ")
            raise ValueError("Ce n'est pas un valide mouvement ")
        else:
            if start[0] == destination[0] - 1 and (start[1] == destination[1] + 1 or start[1] == destination[1] - 1):
                if board.get_board()[destination[0]][destination[1]].get_name() != "":
                    self._first_move = False
                    return True
                raise ValueError("Il ya une piece sur le passage")
            if start[1] == destination[1]:
                if (destination[0] - start[0] == 2 and self._first_move) or (destination[0] - start[0] == 1):
                    for i in range(start[0] + 1, destination[0] + 1):
                        if board.get_board()[i][start[1]].get_name() != "":
                            raise ValueError("Il ya une piece sur le passage")
                    self._first_move = False
                    return True
                raise ValueError("Le pion peut avancer de deux cases qu'a son prmier mouvement")
            raise ValueError("Ce n'est pas un valide mouvement ")

class Empty(Piece):
    def __init__(self, player):
        super().__init__(player)
        self._symbol= ""
    def is_valid_move(self, board, start, destination):
        raise ValueError("Cette emplcement ne contient pas de piece  ")
