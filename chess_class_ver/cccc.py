import pygame
from utils import *
pygame.init()
class Gameobject:

    def __init__(self, team, lx, ly, img, clicked):
        self.team = team
        self.lx = lx
        self.ly = ly
        self.img = img
        self.clicked = False

    
    def click(self, mx, my):
        if mx > self.lx*80 and mx < self.lx*80 + 80 and my > self.ly*80 and my < self.ly*80 + 80:
            self.clicked = True
        else:
            self.clicked = False
            
        
class WTknight1(Gameobject):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 1, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0

#####################################################################################

class BKknight1(Gameobject):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 1, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
######################################################################

class WTknight2(Gameobject):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 6, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
        

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
###########################################################################
class BKknight2(Gameobject):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 6, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
###################################################################

class WTrook1(Gameobject):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 0, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            
            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
###################################################################
class WTrook2(Gameobject):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 7, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
###########################################################################
class BKrook1(Gameobject):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 0, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#################################################################################
class BKrook2(Gameobject):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 7, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
##################################################################
class WTbishop1(Gameobject):
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 2, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
################################################################
class WTbishop2(Gameobject):
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 5, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8 ):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
#################################################################
class BKbishop1(Gameobject):
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 2, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#############################################################
class BKbishop2(Gameobject):
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 5, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))    

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#####################################################################
class WTqueen(Gameobject):
    dx = [1, -1, -1, 1, 1, -1, 0, 0]
    dy = [1, 1, -1, -1, 0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 3, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
            i=1
            px = self.lx + self.dx[4] * i
            py = self.ly + self.dy[4] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[4])
                    self.move_candidate_y.append(i * self.dy[4])
                    break
                self.move_candidate_x.append(i * self.dx[4])
                self.move_candidate_y.append(i * self.dy[4])
                px += self.dx[4]
                py += self.dy[4]
                i += 1
            i=1
            px = self.lx + self.dx[5] * i
            py = self.ly + self.dy[5] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[5])
                    self.move_candidate_y.append(i * self.dy[5])
                    break
                self.move_candidate_x.append(i * self.dx[5])
                self.move_candidate_y.append(i * self.dy[5])
                px += self.dx[5]
                py += self.dy[5]
                i += 1
            i=1
            px = self.lx + self.dx[6] * i
            py = self.ly + self.dy[6] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[6])
                    self.move_candidate_y.append(i * self.dy[6])
                    break
                self.move_candidate_x.append(i * self.dx[6])
                self.move_candidate_y.append(i * self.dy[6])
                px += self.dx[6]
                py += self.dy[6]
                i += 1
            i=1
            px = self.lx + self.dx[7] * i
            py = self.ly + self.dy[7] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == 1:
                    break
                if chessboard[py][px] == -1:
                    self.move_candidate_x.append(i * self.dx[7])
                    self.move_candidate_y.append(i * self.dy[7])
                    break
                self.move_candidate_x.append(i * self.dx[7])
                self.move_candidate_y.append(i * self.dy[7])
                px += self.dx[7]
                py += self.dy[7]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
#############################################################
class BKqueen(Gameobject):
    dx = [1, -1, -1, 1, 1, -1, 0, 0]
    dy = [1, 1, -1, -1, 0, 0, 1, -1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 3, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            i = 1
            px = self.lx + self.dx[0] * i
            py = self.ly + self.dy[0] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[0])
                    self.move_candidate_y.append(i * self.dy[0])
                    break
                self.move_candidate_x.append(i * self.dx[0])
                self.move_candidate_y.append(i * self.dy[0])
                px += self.dx[0]
                py += self.dy[0]
                i += 1
            i=1
            px = self.lx + self.dx[1] * i
            py = self.ly + self.dy[1] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[1])
                    self.move_candidate_y.append(i * self.dy[1])
                    break
                self.move_candidate_x.append(i * self.dx[1])
                self.move_candidate_y.append(i * self.dy[1])
                px += self.dx[1]
                py += self.dy[1]
                i += 1
            i=1
            px = self.lx + self.dx[2] * i
            py = self.ly + self.dy[2] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[2])
                    self.move_candidate_y.append(i * self.dy[2])
                    break
                self.move_candidate_x.append(i * self.dx[2])
                self.move_candidate_y.append(i * self.dy[2])
                px += self.dx[2]
                py += self.dy[2]
                i += 1
            i=1
            px = self.lx + self.dx[3] * i
            py = self.ly + self.dy[3] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[3])
                    self.move_candidate_y.append(i * self.dy[3])
                    break
                self.move_candidate_x.append(i * self.dx[3])
                self.move_candidate_y.append(i * self.dy[3])
                px += self.dx[3]
                py += self.dy[3]
                i += 1
            i=1
            px = self.lx + self.dx[4] * i
            py = self.ly + self.dy[4] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[4])
                    self.move_candidate_y.append(i * self.dy[4])
                    break
                self.move_candidate_x.append(i * self.dx[4])
                self.move_candidate_y.append(i * self.dy[4])
                px += self.dx[4]
                py += self.dy[4]
                i += 1
            i=1
            px = self.lx + self.dx[5] * i
            py = self.ly + self.dy[5] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[5])
                    self.move_candidate_y.append(i * self.dy[5])
                    break
                self.move_candidate_x.append(i * self.dx[5])
                self.move_candidate_y.append(i * self.dy[5])
                px += self.dx[5]
                py += self.dy[5]
                i += 1
            i=1
            px = self.lx + self.dx[6] * i
            py = self.ly + self.dy[6] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[6])
                    self.move_candidate_y.append(i * self.dy[6])
                    break
                self.move_candidate_x.append(i * self.dx[6])
                self.move_candidate_y.append(i * self.dy[6])
                px += self.dx[6]
                py += self.dy[6]
                i += 1
            i=1
            px = self.lx + self.dx[7] * i
            py = self.ly + self.dy[7] * i
            while(px >= 0 and px < 8 and py >= 0 and py < 8):
                if chessboard[py][px] == -1:
                    break
                if chessboard[py][px] == 1:
                    self.move_candidate_x.append(i * self.dx[7])
                    self.move_candidate_y.append(i * self.dy[7])
                    break
                self.move_candidate_x.append(i * self.dx[7])
                self.move_candidate_y.append(i * self.dy[7])
                px += self.dx[7]
                py += self.dy[7]
                i += 1
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#########################################################
class WTking(Gameobject):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(1, 4, 7, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
#######################################################
class BKking(Gameobject):
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    move_candidate_x = []
    move_candidate_y = []
    def __init__(self, img):
        super().__init__(-1, 4, 0, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드

            for i in range(len(self.dx)):
                if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                        self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                    continue
                elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] == self.team:
                    continue
                else:
                    self.move_candidate_x.append(self.dx[i])
                    self.move_candidate_y.append(self.dy[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0

        
#####################################################################################






class WTpawn1(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 0, 6, img, False)
    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                        # if chessboard[int(self.ly-1)][int(self.lx+1)] == -1:
                        #     self.move_candidate_x.append(self.lx+1)
                        #     self.move_candidate_y.append(self.ly-1)
                            
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                        # if chessboard[int(self.ly-1)][int(self.lx+1)] == -1:
                        #     self.move_candidate_x.append(self.lx+1)
                        #     self.move_candidate_y.append(self.ly-1)
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0

        
#################################################################################
class WTpawn2(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 1, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
##################################################################################
class WTpawn3(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 2, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
########################################################################################
class WTpawn4(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 3, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
##########################################################################
class WTpawn5(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 4, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []#후보지 초기화
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0

##################################################################
class WTpawn6(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 5, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
                
################################################################
class WTpawn7(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 6, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0

##############################################################
class WTpawn8(Gameobject):
    dx = [0]
    dy = [-1]
    ax = [1,-1]
    ay = [-1,-1]
    F_dx = [0, 0]
    F_dy = [-1, -2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(1, 7, 6, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != -1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

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
                    chessboard[self.ly][self.lx] = 1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "W", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "W", 0, 0, 0, 0
#######################################################################
#######################################################################
#############################################################################
######################################################################3
class BKpawn1(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    
    def __init__(self, img):
        super().__init__(-1, 0, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn2(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 1, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn3(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 2, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn4(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 3, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            
            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn5(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 4, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn6(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 5, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn7(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1,-1]
    ay = [1,1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True
    def __init__(self, img):
        super().__init__(-1, 6, 1, img, False)

    def drawX(self, display, Font, color,chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:
            
            #만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])
                
            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            #만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40, (self.ly + self.move_candidate_y[i]) * 80 + 40)
                
                
    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x,y, chessboard, w_p, w_died):
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
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag=False
                    self.First_move = False
                    return "B", px, py, cx, cy
            

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################
class BKpawn8(Gameobject):
    dx = [0]
    dy = [1]
    ax = [1, -1]
    ay = [1, 1]
    F_dx = [0, 0]
    F_dy = [1, 2]
    move_candidate_x = []
    move_candidate_y = []
    First_move = True

    def __init__(self, img):
        super().__init__(-1, 7, 1, img, False)

    def drawX(self, display, Font, color, chessboard):
        if self.clicked and len(self.move_candidate_x) == 0 and len(self.move_candidate_y) == 0:

            # 만약 move candidate x가 비어있다면 채워주는 코드
            # firstmove가  true면 1or 2칸 선택(앞에 다른놈 있으면 불가능)
            # 아니면 한칸앞 or 대각선(공격전용(1이 있을때만))
            if self.First_move:
                for i in range(len(self.F_dx)):
                    if self.lx + self.F_dx[i] < 0 or self.lx + self.F_dx[i] > 7 or \
                            self.ly + self.F_dy[i] < 0 or self.ly + self.F_dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.F_dy[i])][int(self.lx + self.F_dx[i])] != 0:
                        break
                    else:
                        self.move_candidate_x.append(self.F_dx[i])
                        self.move_candidate_y.append(self.F_dy[i])

            else:
                for i in range(len(self.dx)):
                    if self.lx + self.dx[i] < 0 or self.lx + self.dx[i] > 7 or \
                            self.ly + self.dy[i] < 0 or self.ly + self.dy[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.dy[i])][int(self.lx + self.dx[i])] != 0:
                        continue
                    else:
                        self.move_candidate_x.append(self.dx[i])
                        self.move_candidate_y.append(self.dy[i])
                for i in range(len(self.ax)):
                    if self.lx + self.ax[i] < 0 or self.lx + self.ax[i] > 7 or \
                            self.ly + self.ay[i] < 0 or self.ly + self.ay[i] > 7:
                        continue
                    elif chessboard[int(self.ly + self.ay[i])][int(self.lx + self.ax[i])] != 1:
                        continue
                    else:
                        self.move_candidate_x.append(self.ax[i])
                        self.move_candidate_y.append(self.ay[i])
        elif self.clicked:
            # 만약 차있다면 move candidate x, y에 있는 값들을 토대로 x를 그려준다.
            for i in range(len(self.move_candidate_x)):
                text_print(display, "X", Font, color, (self.lx + self.move_candidate_x[i]) * 80 + 40,
                           (self.ly + self.move_candidate_y[i]) * 80 + 40)

    def draw(self, display):
        display.blit(self.img, (8 + self.lx * 80, 8 + self.ly * 80))

    def moveclick(self, x, y, chessboard, w_p, w_died):
        xx = x // 80
        yy = y // 80
        xx -= self.lx
        yy -= self.ly
        ##if xx랑 YY가 후보지에 존재하고 INDEX도 같으면 TRUE 아님 fALSE

        if self.clicked:
            flag = True
            for i in range(len(self.move_candidate_x)):
                if (self.move_candidate_x[i] == xx and self.move_candidate_y[i] == yy):
                    chessboard[self.ly][self.lx] = 0
                    px = self.lx
                    py = self.ly
                    self.lx += xx
                    self.ly += yy
                    cx = self.lx
                    cy = self.ly
                    for i in w_p:
                        if self.lx == i.lx and self.ly == i.ly:
                            w_p.remove(i)
                            w_died.append(i)
                    chessboard[self.ly][self.lx] = -1
                    self.clicked = False
                    self.move_candidate_x = []
                    self.move_candidate_y = []
                    flag = False
                    self.First_move = False
                    return "B", px, py, cx, cy

            if flag:
                self.clicked = False
                self.move_candidate_x = []
                self.move_candidate_y = []
        return "B", 0, 0, 0, 0
#######################################################################