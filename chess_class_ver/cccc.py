from pygame.image import load
from pygame.transform import scale
from utils import *

class Gameobject:
    dx = []
    dy = []
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, team:int, lx:int, ly:int, type:str):
        self.team = team
        self.team_str = team2str(team)[0].upper()
        self.lx = lx
        self.ly = ly
        self._lx = lx
        self._ly = ly
        self.img = scale(load(f"{img_base}/{team2str(team)} {type}.png"), (55, 55))
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
    
    def drawX(self, display, Font, color,chessboard, draw=True):
        if None in [display, Font, color]:
            return
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            #만약 move candidate x가 비어있다면 채워주는 코드
            for i, x in enumerate(self.dx):
                if self.lx + x not in range(0, 8) or self.ly + self.dy[i] not in range(0, 8):
                    continue
                elif chessboard[self.ly + self.dy[i]][self.lx + x] == self.team:
                    continue
                self.move_candidate_x.append(x)
                self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
    
    def moveclick(self, x, y, chessboard, other_team):
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
                    for p in other_team.get_alive():
                        p:Gameobject
                        if (self.lx, self.ly) == p.get_pos():
                            other_team.kill(p)
                    chessboard[self.ly][self.lx] = self.team
                    self.clicked = False
                    flag=False
                    return [self.team_str, px, py, self.lx, self.ly]

            if flag:
                self.clicked = False
        return [self.team_str, 0, 0, 0, 0]
    
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))
    
    def get_pos(self):
        return (self.lx, self.ly)
    
    def getDxDy(self, chessboard):
        self.drawX(None, None, None, chessboard=chessboard)
        if not self.dx or not self.dy: return None
        res = []
        for i in range(len(self.dx)):
            tx = self.lx + self.dx[i]
            ty = self.ly + self.dy[i]
            if tx not in range(0, 8) or ty not in range(0, 8):
                continue
            if chessboard[ty][tx]:
                if chessboard[ty][tx] == self.team:
                    continue
                if self.lx == tx and self.ly == ty:
                    continue
            res.append((tx, ty))
        return res

    def reset(self):
        self.lx = self._lx
        self.ly = self._ly
        self.clicked = False

#####################################################################################

class Knight(Gameobject):
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "knight")
    def drawX(self, display, Font, color, chessboard):
        self.dx = [ 2,  1, -1, -2, -2, -1, 1, 2]
        self.dy = [-1, -2, -2, -1,  1,  2, 2, 1]
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Rook(Gameobject):
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "rook")
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
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "bishop")
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
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "queen")
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
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "king")
    def drawX(self, display, Font, color, chessboard):
        self.dx = [1,  1,  0, -1, -1, -1, 0, 1]
        self.dy = [0, -1, -1, -1,  0,  1, 1, 1]
        return super().drawX(display, Font, color, chessboard)

#####################################################################################

class Pawn(Gameobject):
    def __init__(self, team: int, lx: int, ly: int):
        super().__init__(team, lx, ly, "pawn")
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
    
    def moveclick(self, x, y, chessboard, other_team):
        res = super().moveclick(x, y, chessboard, other_team)
        if self.First_move and res[1] + res[2] + res[3] + res[4]:
            self.First_move = False
        return res
    
    def reset(self):
        self.First_move = True
        return super().reset()
