from pygame.image import load
from pygame.transform import scale
from cccc import *

BLACK_pawn    =  load("images/black pawn.png")
WHITE_pawn    =  load("images/white pawn.png")
BLACK_rook    =  load("images/black rook.png")
WHITE_rook    =  load("images/white rook.png")
BLACK_knight  =  load("images/black knight.png")
WHITE_knight  =  load("images/white knight.png")
BLACK_bishop  =  load("images/black bishop.png")
WHITE_bishop  =  load("images/white bishop.png")
BLACK_queen   =  load("images/black queen.png")
WHITE_queen   =  load("images/white queen.png")
BLACK_king    =  load("images/black king.png")
WHITE_king    =  load("images/white king.png")


sc = (55, 55)
BLACK_pawn    = scale(BLACK_pawn,   sc)
WHITE_pawn    = scale(WHITE_pawn,   sc)
BLACK_rook    = scale(BLACK_rook,   sc)
WHITE_rook    = scale(WHITE_rook,   sc)
BLACK_knight  = scale(BLACK_knight, sc)
WHITE_knight  = scale(WHITE_knight, sc)
BLACK_bishop  = scale(BLACK_bishop, sc)
WHITE_bishop  = scale(WHITE_bishop, sc)
BLACK_queen   = scale(BLACK_queen,  sc)
WHITE_queen   = scale(WHITE_queen,  sc)
BLACK_king    = scale(BLACK_king,   sc)
WHITE_king    = scale(WHITE_king,   sc)


W_knight1 = Knight(team=1, lx=1, ly=7, img=WHITE_knight)
W_knight2 = Knight(team=1, lx=6, ly=7, img=WHITE_knight)
W_rook1   = Rook(  team=1, lx=0, ly=7, img=WHITE_rook)
W_rook2   = Rook(  team=1, lx=7, ly=7, img=WHITE_rook)
W_bishop1 = Bishop(team=1, lx=2, ly=7, img=WHITE_bishop)
W_bishop2 = Bishop(team=1, lx=5, ly=7, img=WHITE_bishop)
W_queen   = Queen( team=1, lx=3, ly=7, img=WHITE_queen)
W_king    = King(  team=1, lx=4, ly=7, img=WHITE_king)

B_knight1 = Knight(team=-1, lx=1, ly=0, img=BLACK_knight)
B_knight2 = Knight(team=-1, lx=6, ly=0, img=BLACK_knight)
B_rook1   = Rook(  team=-1, lx=0, ly=0, img=BLACK_rook)
B_rook2   = Rook(  team=-1, lx=7, ly=0, img=BLACK_rook)
B_bishop1 = Bishop(team=-1, lx=2, ly=0, img=BLACK_bishop)
B_bishop2 = Bishop(team=-1, lx=5, ly=0, img=BLACK_bishop)
B_queen   = Queen( team=-1, lx=3, ly=0, img=BLACK_queen)
B_king    = King(  team=-1, lx=4, ly=0, img=BLACK_king)

W_pawns = []
B_pawns = []
for i in range(8):
    W_pawns.append(Pawn(team=1, lx=i, ly=6, img=WHITE_pawn))
    B_pawns.append(Pawn(team=-1, lx=i, ly=1, img=BLACK_pawn))
