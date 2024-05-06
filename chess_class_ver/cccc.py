import pygame
from utils import *
pygame.init()

class Gameobject:
    dx = []
    dy = []
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, team:int, lx:int, ly:int, img:pygame.Surface, *args):
        self.team = team
        self.team_str = "W" if self.team == 1 else "B"
        self.lx = lx
        self.ly = ly
        self._lx = lx
        self._ly = ly
        self.img = img
        self.clicked = False
    
    def click(self, mx, my):
        if mx > self.lx*80 and mx < self.lx*80 + 80 and my > self.ly*80 and my < self.ly*80 + 80:
            self.clicked = True
            self.dx = []
            self.dy = []
            self.move_candidate_x = []
            self.move_candidate_y = []
        else:
            self.clicked = False
    
    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            #만약 move candidate x가 비어있다면 채워주는 코드
            for i, x in enumerate(self.dx):
                if self.lx + x not in list(range(0, 8)) or self.ly + self.dy[i] not in list(range(0, 8)):
                    continue
                elif chessboard[self.ly + self.dy[i]][self.lx + x] == self.team:
                    continue
                self.move_candidate_x.append(x)
                self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
    
    def moveclick(self, x,y, chessboard, b_p, b_died):
        xx = x//80
        yy = y//80
        xx -= self.lx
        yy -= self.ly
        ##if xx랑 YY가 후보지에 존재하고 INDEX도 같으면 TRUE 아님 fALSE

        if self.clicked:
            flag = True
            for i in range(len(self.move_candidate_x)):
                if(self.move_candidate_x[i] == xx and self.move_candidate_y[i] == yy):
                    chessboard[self.ly][self.lx] = 0
                    px = self.lx
                    py = self.ly
                    self.lx += xx
                    self.ly += yy
                    cx = self.lx
                    cy = self.ly
                    for i in b_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            b_p.remove(i)
                            b_died.append(i)
                    chessboard[self.ly][self.lx] = self.team
                    self.clicked = False
                    flag=False
                    return self.team_str, px, py, cx, cy
            
            if flag:
                self.clicked = False
        return self.team_str, 0, 0, 0, 0
    
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))
    
    def reset(self):
        self.lx = self._lx
        self.ly = self._ly
        self.clicked = False

#####################################################################################

class Knight(Gameobject):
    def drawX(self, display, Font, color, chessboard):
        self.dx = [ 2,  1, -1, -2, -2, -1, 1, 2]
        self.dy = [-1, -2, -2, -1,  1,  2, 2, 1]
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Rook(Gameobject):
    def drawX(self, display, Font, color, chessboard):
        for i in range(-1, -self.lx-1, -1):
            self.dy.append(0)
            self.dx.append(i)
            if chessboard[self.ly][self.lx + i]: break

        for i in range(1, 8-self.lx, 1):
            self.dy.append(0)
            self.dx.append(i)
            if chessboard[self.ly][self.lx + i]: break

        for i in range(-1, -self.ly-1, -1):
            self.dx.append(0)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx]: break

        for i in range(1, 8-self.ly, 1):
            self.dx.append(0)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx]: break

        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Bishop(Gameobject):
    def drawX(self, display, Font, color, chessboard):
        self.dx = []
        self.dy = []
        # Right Up
        for i in range(1, 8-max(self.lx, 7-self.ly), 1):
            self.dx.append(i)
            self.dy.append(-i)
            if chessboard[self.ly - i][self.lx + i]: break
        # Right Down
        for i in range(1, 8-max(self.lx, self.ly), 1):
            self.dx.append(i)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx + i]: break
        # Left Up
        for i in range(1, max(self.lx, self.ly), 1):
            self.dx.append(-i)
            self.dy.append(-i)
            if chessboard[self.ly - i][self.lx - i]: break
        # Left Down
        for i in range(1, 8-max(self.lx, self.ly), 1):
            self.dx.append(-i)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx - i]: break
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Queen(Gameobject):
    def drawX(self, display, Font, color, chessboard):
        self.dx = []
        self.dy = []
        # VERTICAL MOVE
        for i in range(-1, -self.lx-1, -1):
            self.dy.append(0)
            self.dx.append(i)
            if chessboard[self.ly][self.lx + i]: break

        for i in range(1, 8-self.lx, 1):
            self.dy.append(0)
            self.dx.append(i)
            if chessboard[self.ly][self.lx + i]: break

        for i in range(-1, -self.ly-1, -1):
            self.dx.append(0)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx]: break

        for i in range(1, 8-self.ly, 1):
            self.dx.append(0)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx]: break

        # DIAGONAL MOVE
        for i in range(1, 8-max(self.lx, 7-self.ly), 1):
            self.dx.append(i)
            self.dy.append(-i)
            if chessboard[self.ly - i][self.lx + i]: break

        for i in range(1, 8-max(self.lx, self.ly), 1):
            self.dx.append(i)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx + i]: break

        for i in range(1, max(self.lx, self.ly), 1):
            self.dx.append(-i)
            self.dy.append(-i)
            if chessboard[self.ly - i][self.lx - i]: break

        for i in range(1, 8-max(self.lx, self.ly), 1):
            self.dx.append(-i)
            self.dy.append(i)
            if chessboard[self.ly + i][self.lx - i]: break
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class King(Gameobject):
    def drawX(self, display, Font, color, chessboard):
        self.dx = [1,  1,  0, -1, -1, -1, 0, 1]
        self.dy = [0, -1, -1, -1,  0,  1, 1, 1]
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Pawn(Gameobject):
    def __init__(self, team: int, lx: int, ly: int, img: pygame.Surface, *args):
        super().__init__(team, lx, ly, img, *args)
        self.First_move = True
        self.front = self.team * -1

    def drawX(self, display, Font, color, chessboard):
        if self.First_move:
            self.dx += [0, 0]
            self.dy += [-1, -2] if self.team == 1 else [1, 2]
        else:
            self.dx.append(0)
            self.dy.append(self.front)
        for i in [1, -1]:
            try:
                if chessboard[self.ly + self.front][self.lx + i] == self.team * -1:
                    self.dx.append(i)
                    self.dy.append(self.front)
            except:
                pass
        return super().drawX(display, Font, color, chessboard)
    
    def moveclick(self, x, y, chessboard, b_p, b_died):
        res = super().moveclick(x, y, chessboard, b_p, b_died)
        if self.First_move and res[1] + res[2] + res[3] + res[4]:
            self.First_move = False
        return res
    
    def reset(self):
        self.First_move = True
        return super().reset()
