# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:24:38 2022

@author: Mitchell.Canty
"""

import pandas as pd


class Piece:
    def __init__(self, XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol):
        self.XPosition = int(XPosition)
        self.YPosition = int(YPosition)
        self.Player = str(Player)
        self.MaxMoveY = int(MaxMoveY)
        self.MaxMoveX = int(MaxMoveX)
        self.Symbol = str(Symbol)
        
        
class Pawn(Piece):  
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 2, MaxMoveX = 1, Symbol = "PW"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)

    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)  
        
        if x > 1 or y > 2:
            raise ValueError
        elif (self.Player == "White" and self.YPosition == 2) or (self.Player == "Black" and self.YPosition == 7):
            if x == 1 and y == 2:
                raise ValueError
            elif type(z) == str:
                if x == 0:
                    pass
                else:
                    raise ValueError
            else:
                if x == 1:
                    pass
                else:
                    raise ValueError
        else:
            if y > 1:
                raise ValueError
            else:
                pass
        

class Rook(Piece):
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 8, MaxMoveX = 8, Symbol = "RK"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)
    
    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)  
        
        if x > 8 or y > 8:
            raise ValueError
        if x > 0 and y > 0:
            raise ValueError
                


class Knight(Piece):
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 2, MaxMoveX = 2, Symbol = "KN"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)
    
    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)  
        
        if x > 2 or y > 2:
            raise ValueError
        if x > 1 and y > 1:
            raise ValueError      
            


class Bishop(Piece):
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 8, MaxMoveX = 8,Symbol = "BS"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)
    
    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)        
        
        if x > 8 or y > 8:
            raise ValueError
        if x == y:
            pass
        else:
            raise ValueError

    
class King(Piece):
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 1, MaxMoveX = 1, Symbol = "KG"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)
    
    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)        
        
        if x > 1 or y > 1:
            raise ValueError
    
    
class Queen(Piece):
    def __init__(self, XPosition, YPosition, Player, MaxMoveY = 8, MaxMoveX = 8, Symbol = "QN"):
        super().__init__(XPosition, YPosition, Player, MaxMoveY, MaxMoveX, Symbol)
        
    def Move(self, x, y, z):
        x = abs(x)
        y = abs(y)        
        
        if x > 0 and y > 0:
            if x == y:
                pass
            else:
                raise ValueError
                
        if x > 8 or y > 8:
            raise ValueError

Pieces = []       
 

BPawn1 = Pawn(1,7,"Black")
Pieces.append(BPawn1)
BPawn2 = Pawn(2,7,"Black")
Pieces.append(BPawn2)
BPawn3 = Pawn(3,7,"Black")
Pieces.append(BPawn3)
BPawn4 = Pawn(4,7,"Black")
Pieces.append(BPawn4)
BPawn5 = Pawn(5,7,"Black")
Pieces.append(BPawn5)
BPawn6 = Pawn(6,7,"Black")
Pieces.append(BPawn6)
BPawn7 = Pawn(7,7,"Black")
Pieces.append(BPawn7)
BPawn8 = Pawn(8,7,"Black")
Pieces.append(BPawn8)

WPawn1 = Pawn(1,2,"White")
Pieces.append(WPawn1)
WPawn2 = Pawn(2,2,"White")
Pieces.append(WPawn2)
WPawn3 = Pawn(3,2,"White")
Pieces.append(WPawn3)
WPawn4 = Pawn(4,2,"White")
Pieces.append(WPawn4)
WPawn5 = Pawn(5,2,"White")
Pieces.append(WPawn5)
WPawn6 = Pawn(6,2,"White")
Pieces.append(WPawn6)
WPawn7 = Pawn(7,2,"White")
Pieces.append(WPawn7)
WPawn8 = Pawn(8,2,"White")
Pieces.append(WPawn8)
    
WRook1 = Rook(1,1,"White")
Pieces.append(WRook1)
WRook2 = Rook(8,1,"White")
Pieces.append(WRook2)

BRook1 = Rook(1,8,"Black")
Pieces.append(BRook1)
BRook2 = Rook(8,8,"Black")
Pieces.append(BRook2)

WKnight1 = Knight(2,1,"White")
Pieces.append(WKnight1)
WKnight2 = Knight(7,1,"White")
Pieces.append(WKnight2)

BKnight1 = Knight(2,8,"Black")
Pieces.append(BKnight1)
BKnight2 = Knight(7,8,"Black")
Pieces.append(BKnight2)

WBishop1 = Bishop(3,1,"White")
Pieces.append(WBishop1)
WBishop2 = Bishop(6,1,"Black")
Pieces.append(WBishop2)

BBishop1 = Bishop(3,8,"Black")
Pieces.append(BBishop1)
BBishop2 = Bishop(6,8,"Black")
Pieces.append(BBishop2)

WKing = King(5,1,"White")
Pieces.append(WKing)

BKing = King(4,8,"Black")
Pieces.append(BKing)

WQueen = Queen(4,1,"White")
Pieces.append(WQueen)

BQueen = Queen(5,8,"Black")
Pieces.append(BQueen)


LetterToCoordDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8}
CoordToLetterDict = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}

def BoardUpdate():
    global BoardDict
    global VisualBoardDict
    global VisualBoard
    global Board
    
    
    BoardDict = {}
    
    for i in range(1,9):
        BoardDict[i] = list(range(1,9))
    
    for i in Pieces:
        index = BoardDict[i.XPosition].index(i.YPosition)
        BoardDict[i.XPosition][index] = i
        
    for i in BoardDict:
        for j in BoardDict[i]:
            if type(j) == int:
                index = BoardDict[i].index(j)
                BoardDict[i][index] = ' '
            else:
                pass        
                
    VisualBoardDict = {}
            
    for i in range(1,9):
        VisualBoardDict[CoordToLetterDict[i]] = list(range(1,9))
        
            
    for i in Pieces:
        index = VisualBoardDict[CoordToLetterDict[i.XPosition]].index(i.YPosition)
        VisualBoardDict[CoordToLetterDict[i.XPosition]][index] = i.Symbol
    
    for i in VisualBoardDict:
        for j in VisualBoardDict[i]:
            if type(j) == int:
                index = VisualBoardDict[i].index(j)
                VisualBoardDict[i][index] = ' '
            else:
                pass
    
    VisualBoard = pd.DataFrame.from_dict(VisualBoardDict,orient = 'index', columns = range(1,9,1)).transpose()

    Board = pd.DataFrame.from_dict(BoardDict,orient = 'index', columns = range(1,9,1)).transpose()
    print('__________________________________\n')
    print(VisualBoard)
    print('\n__________________________________\n')

BoardUpdate()
      

def Turn(User):
    
    #User = "White"
    
    global SelectedPiece
    global TargetUnit
    
    SelectedPiece = None
    UserPiece = None
    TargetEndPoint = None
    TargetUnit = None
    
    while SelectedPiece == None:

        while UserPiece == None:
            UserPiece = input("Choose a coordinate of the piece you'd like to move.") 
            try:
                SelectX, SelectY = list(UserPiece)
                
                SelectY = int(SelectY)
                SelectX = LetterToCoordDict[SelectX]
        
                SelectedPiece = Board[SelectX][SelectY]
                
            except:
                print("Invalid input.")
                UserPiece = None
    
        
        if SelectedPiece.Player == User:
            pass
        else:
            print("That's not your piece.")
            SelectedPiece = None
            UserPiece = None
        

    while TargetUnit == None:
        while TargetEndPoint == None: 
            try:
                TargetEndPoint = input("Choose the coordinate where you'd like to move the piece.")  
                TargetX, TargetY = list(TargetEndPoint)
                
                TargetY = int(TargetY)
                TargetX = LetterToCoordDict[TargetX]
                
                TargetUnit = Board[TargetX][TargetY]
                
                
                SelectedPiece.Move(SelectX-TargetX, SelectY-TargetY, TargetUnit)
                print("".join([type(SelectedPiece).__name__, " from ", UserPiece, " to ", TargetEndPoint, "."]))
                if TargetUnit == ' ':
                    SelectedPiece.XPosition = TargetX
                    SelectedPiece.YPosition = TargetY
                else:
                    Pieces.remove(TargetUnit)
                    SelectedPiece.XPosition = TargetX
                    SelectedPiece.YPosition = TargetY
            except ValueError:
                print("That unit can't move like that.")    
                TargetEndPoint = None
                TargetUnit = None




TurnCounter = 1

while BQueen in Pieces and WQueen in Pieces:
    if TurnCounter % 2 == 1:
        print("White's Turn.")
        Turn("White")
        BoardUpdate()
        TurnCounter += 1
    elif TurnCounter % 2 == 0:
        print("Black's Turn")
        Turn("Black")
        BoardUpdate()
        TurnCounter += 1
        
if BQueen in Pieces:
    print("Black wins!")
else:
    print("White wins!")

