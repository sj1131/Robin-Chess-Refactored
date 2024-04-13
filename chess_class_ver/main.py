import pygame
import socket
import threading
from cccc import *
from utils import *
from piece import *

##############################################################################
"""
cccc.py 파일에서 [기물이름]을 검색하시면 기물별 이동위치 검사 및 이동 코드를 확인하실수 있습니다.
Ctrl + f를 누르시면 키워드 검색을 하실수 있습니다.
기물 이름 : [knight, rook, bishop, queen, king, pawn]

기물 이미지를 변경하고싶을 경우, images 파일 안에 있는 기존 기물 이미지를 삭제한 후 같은 이름으로 사진을 추가하시면 됩니다.
이미지 파일이 깨지지 않기 위해서는 가로 세로 비율을 1:1로 만들어 주세요.

소스코드를 여러번 재사용 하는것은 가능하지만, 판매하거나 불특정 다수에게 공유하는것은 불가합니다.

오류 제보 또는 문의사항은 인스타그램 dev._.robin / 개발자 로빈 으로 연락주세요.

"""
##############################################################################
pygame.init()

size = (900, 780) # 화면 비율을 수정하시면 오류가 생길수 있습니다.
display = pygame.display.set_mode(size)
Clock = pygame.time.Clock()
fps = 60
mclick = False
Turn = 111 # 111은 white Turn 입니다.
pygame.display.set_caption("Robin Chess Game Project")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
who_won = None

home = pygame.image.load("images/home.png")
home = pygame.transform.scale(home, (100, 100))

pygame.font.init()
Font = pygame.font.SysFont(None, 50)
start_font = pygame.font.Font("Merida Regular.ttf", 36)
start_font_small = pygame.font.Font("Merida Regular.ttf", 20)
main_font = pygame.font.Font("Merida Regular.ttf", 36)
main_font_ssssmaller = pygame.font.Font("Merida Regular.ttf", 15)
gameover_font = pygame.font.Font("Merida Regular.ttf", 70)
OpenSans_font_bold = pygame.font.Font("OpenSans-Bold.ttf", 55)
OpenSans_font_bold_biggger = pygame.font.Font("OpenSans-Bold.ttf", 80)

offline_start_button = xx("GAME START", 450, 650, gray, black, OpenSans_font_bold)
start_notion = start_notion_button("Robin Chess Game", 450, 150, gray, black, OpenSans_font_bold_biggger)
WHITE_turn = turn_button("Turn : WHITE", 150, 675, black, white, start_font_small)
BLACK_turn = turn_button("Turn : BLACK", 150, 675, white, black, start_font_small)
restart = button("restart", 430, 500, gray, red, start_font)
captured_up = Cap_button("Captured Pieces", 770, 20, white, black, main_font_ssssmaller)
captured_down = Cap_button("Captured Pieces", 770, 400, black, white, main_font_ssssmaller)

home_button = imagebutton(home, 5, 700)

chessboard = [[-1, -1, -1, -1, -1, -1, -1 ,-1],
             [-1, -1, -1, -1, -1, -1, -1 ,-1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]]

#-1 = black, 1 = white, 0 = nothing
#############################################
white_timer = timer(start_font_small, white, 590, 660, 20 * 60+1)
black_timer = timer(start_font_small, white, 590, 690, 20 * 60+1)
############################################
w_p = [W_knight1, W_knight2, W_rook1, W_rook2, W_bishop1, W_bishop2, W_queen,
       W_king, W_pawn1, W_pawn2, W_pawn3, W_pawn4, W_pawn5, W_pawn6, W_pawn7, W_pawn8]
b_p = [B_knight1, B_knight2, B_rook1, B_rook2, B_bishop1, B_bishop2, B_queen, B_king,
       B_pawn1, B_pawn2, B_pawn3, B_pawn4, B_pawn5, B_pawn6, B_pawn7, B_pawn8]
w_died = []
b_died = []

Ready = True
Gaming = False
online_gaming = False
while True:
    Clock.tick(fps)
    mclick = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mclick = True
            xx, yy = pygame.mouse.get_pos()
##############################################################################################
    if Ready:
        display.fill(gray)
        # display.blit(background, (0,0))
        offline_start_button.draw(display)
        # text_print(display, "Robin Chess Game", OpenSans_font_bold_biggger, white, 450, 190)
        start_notion.draw(display)
        if mclick:
            if offline_start_button.click(xx, yy):
                Ready = False
                Gaming = True
                mclick = False
#######################################################################################
    elif Gaming:
        
        display.fill(back_color)
        draw_board(check_bright, check_dark, display)
        captured_down.draw(display)
        captured_up.draw(display)
        home_button.draw(display)
        text_print(display, "WHITE : ", start_font_small, white, 470, 660)
        text_print(display, "BLACK : ", start_font_small, white, 470, 690)
        white_timer.countdown(display)
        black_timer.countdown(display)
        if mclick:
            if home_button.click(xx, yy):
                Ready = True
                mclick = False
                Gaming = False
                
                chessboard =[[-1, -1, -1, -1, -1, -1, -1 ,-1],
                        [-1, -1, -1, -1, -1, -1, -1 ,-1],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]
                
                
                #-1 = black, 1 = white, 0 = nothing
                w_died = []
                b_died = []
                white_timer = timer(start_font_small, white, 590, 660, 20 * 60+1)
                black_timer = timer(start_font_small, white, 590, 690, 20 * 60+1)
                w_p = [W_knight1, W_knight2, W_rook1, W_rook2, W_bishop1, W_bishop2, W_queen, W_king,
                        W_pawn1, W_pawn2, W_pawn3, W_pawn4, W_pawn5, W_pawn6, W_pawn7, W_pawn8]
                b_p = [B_knight1, B_knight2, B_rook1, B_rook2, B_bishop1, B_bishop2, B_queen, B_king,
                        B_pawn1, B_pawn2, B_pawn3, B_pawn4, B_pawn5, B_pawn6, B_pawn7, B_pawn8]
                Turn = 111
                W_knight1.lx= 1
                W_knight1.ly = 7
                W_knight2.lx = 6
                W_knight2.ly = 7
                W_rook1.lx = 0
                W_rook1.ly = 7
                W_rook2.lx = 7
                W_rook2.ly = 7
                W_bishop1.lx = 2
                W_bishop1.ly = 7
                W_bishop2.lx = 5
                W_bishop2.ly = 7
                W_queen.lx = 3
                W_queen.ly = 7
                W_king.lx = 4
                W_king.ly = 7
                W_pawn1.lx = 0
                W_pawn1.ly = 6
                W_pawn2.lx = 1
                W_pawn2.ly = 6
                W_pawn3.lx = 2
                W_pawn3.ly = 6
                W_pawn4.lx = 3
                W_pawn4.ly = 6
                W_pawn5.lx = 4
                W_pawn5.ly = 6
                W_pawn6.lx = 5
                W_pawn6.ly = 6
                W_pawn7.lx = 6
                W_pawn7.ly = 6
                W_pawn8.lx = 7
                W_pawn8.ly = 6

                ################################################################################
                B_knight1.lx = 1
                B_knight1.ly = 0
                B_knight2.lx = 6
                B_knight2.ly = 0
                B_rook1.lx = 0
                B_rook1.ly = 0
                B_rook2.lx = 7
                B_rook2.ly = 0
                B_bishop1.lx = 2
                B_bishop1.ly = 0
                B_bishop2.lx = 5
                B_bishop2.ly = 0
                B_queen.lx = 3
                B_queen.ly = 0
                B_king.lx = 4
                B_king.ly = 0
                B_pawn1.lx = 0
                B_pawn1.ly = 1
                B_pawn2.lx = 1
                B_pawn2.ly = 1
                B_pawn3.lx = 2
                B_pawn3.ly = 1
                B_pawn4.lx = 3
                B_pawn4.ly = 1
                B_pawn5.lx = 4
                B_pawn5.ly = 1
                B_pawn6.lx = 5
                B_pawn6.ly = 1
                B_pawn7.lx = 6
                B_pawn7.ly = 1
                B_pawn8.lx = 7
                B_pawn8.ly = 1
                ##################################################################################
                W_pawn1.First_move = True
                B_pawn1.First_move = True
                W_pawn2.First_move = True
                B_pawn2.First_move = True
                W_pawn3.First_move = True
                B_pawn3.First_move = True
                W_pawn4.First_move = True
                B_pawn4.First_move = True
                W_pawn5.First_move = True
                B_pawn5.First_move = True
                W_pawn6.First_move = True
                B_pawn6.First_move = True
                W_pawn7.First_move = True
                B_pawn7.First_move = True
                W_pawn8.First_move = True
                B_pawn8.First_move = True
                
        if Turn == 111:
            white_timer.paused = False
            black_timer.paused = True
            WHITE_turn.draw(display)
        if Turn == 222:
            white_timer.paused = True
            black_timer.paused = False
            BLACK_turn.draw(display)
            
###########################
        for wp in w_p:
            wp.draw(display)
            if Turn == 111:
                if mclick:
                    if not wp.clicked:
                        wp.click(xx,yy)
                    else:
                        a, b, c, d, e = wp.moveclick(xx, yy, chessboard, b_p, b_died)
                        socket_list = []
                        socket_list.append(a)
                        socket_list.append(b)
                        socket_list.append(c)
                        socket_list.append(d)
                        socket_list.append(e)
                        if socket_list[1] != socket_list[3] or socket_list[2] != socket_list[4]:
                            print(socket_list[0:5])
                            Turn = 222
                        
                            
                if wp.clicked:
                    wp.drawX(display, Font, black, chessboard)
        
                
        for bp in b_p:
            bp.draw(display)
            if Turn == 222:
                if mclick:
                    if not bp.clicked:
                        bp.click(xx,yy)
                    else:
                        a, b, c, d, e = bp.moveclick(xx, yy, chessboard, w_p, w_died)
                        socket_list = []
                        socket_list.append(a)
                        socket_list.append(b)
                        socket_list.append(c)
                        socket_list.append(d)
                        socket_list.append(e)
                        if socket_list[1] != socket_list[3] or socket_list[2] != socket_list[4]:
                            print(socket_list[0:5])
                            Turn = 111
                if bp.clicked:
                    bp.drawX(display, Font, black, chessboard)
                    
        mclick=False
        xi = 670
        yi = 45
        for wDD in w_died:
            display.blit(wDD.img, (xi, yi))
            xi += 70
            if xi >= 850:
                xi = 670
                yi += 70
        xxi = 670
        yyi = 420
        for bDD in b_died:
            display.blit(bDD.img, (xxi, yyi))
            xxi += 70
            if xxi >= 850:
                xxi = 670
                yyi += 70
                
        if not W_king in w_p:
            who_won = "BLACK"
            Gaming = False
        if not B_king in b_p:
            who_won = "WHITE"
            Gaming = False
            
        if white_timer.timeover:
            who_won = "BLACK"
            Gaming = False
        if black_timer.timeover:
            who_won = "WHITE"
            Gaming = False
    else:
        display.fill(black)
        text_print(display, "Game Over", gameover_font, red, 440, 300)
        text_print(display, str(who_won) + " WON !!", main_font, white, 445, 400)
        restart.draw(display)
        if mclick and restart.click(xx, yy):
            Ready = True
            chessboard =[[-1, -1, -1, -1, -1, -1, -1 ,-1],
                    [-1, -1, -1, -1, -1, -1, -1 ,-1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1]]#-1 = black, 1 = white, 0 = nothing
            w_died = []
            b_died = []
            white_timer = timer(start_font_small, white, 590, 660, 20 * 60+1)
            black_timer = timer(start_font_small, white, 590, 690, 20 * 60+1)
            w_p = [W_knight1, W_knight2, W_rook1, W_rook2, W_bishop1, W_bishop2, W_queen, W_king,
                    W_pawn1, W_pawn2, W_pawn3, W_pawn4, W_pawn5, W_pawn6, W_pawn7, W_pawn8]
            b_p = [B_knight1, B_knight2, B_rook1, B_rook2, B_bishop1, B_bishop2, B_queen, B_king,
                    B_pawn1, B_pawn2, B_pawn3, B_pawn4, B_pawn5, B_pawn6, B_pawn7, B_pawn8]
            Turn = 111
            W_knight1.lx= 1
            W_knight1.ly = 7
            W_knight2.lx = 6
            W_knight2.ly = 7
            W_rook1.lx = 0
            W_rook1.ly = 7
            W_rook2.lx = 7
            W_rook2.ly = 7
            W_bishop1.lx = 2
            W_bishop1.ly = 7
            W_bishop2.lx = 5
            W_bishop2.ly = 7
            W_queen.lx = 3
            W_queen.ly = 7
            W_king.lx = 4
            W_king.ly = 7
            W_pawn1.lx = 0
            W_pawn1.ly = 6
            W_pawn2.lx = 1
            W_pawn2.ly = 6
            W_pawn3.lx = 2
            W_pawn3.ly = 6
            W_pawn4.lx = 3
            W_pawn4.ly = 6
            W_pawn5.lx = 4
            W_pawn5.ly = 6
            W_pawn6.lx = 5
            W_pawn6.ly = 6
            W_pawn7.lx = 6
            W_pawn7.ly = 6
            W_pawn8.lx = 7
            W_pawn8.ly = 6

            ################################################################################
            B_knight1.lx = 1
            B_knight1.ly = 0
            B_knight2.lx = 6
            B_knight2.ly = 0
            B_rook1.lx = 0
            B_rook1.ly = 0
            B_rook2.lx = 7
            B_rook2.ly = 0
            B_bishop1.lx = 2
            B_bishop1.ly = 0
            B_bishop2.lx = 5
            B_bishop2.ly = 0
            B_queen.lx = 3
            B_queen.ly = 0
            B_king.lx = 4
            B_king.ly = 0
            B_pawn1.lx = 0
            B_pawn1.ly = 1
            B_pawn2.lx = 1
            B_pawn2.ly = 1
            B_pawn3.lx = 2
            B_pawn3.ly = 1
            B_pawn4.lx = 3
            B_pawn4.ly = 1
            B_pawn5.lx = 4
            B_pawn5.ly = 1
            B_pawn6.lx = 5
            B_pawn6.ly = 1
            B_pawn7.lx = 6
            B_pawn7.ly = 1
            B_pawn8.lx = 7
            B_pawn8.ly = 1
            ##################################################################################
            W_pawn1.First_move = True
            B_pawn1.First_move = True
            W_pawn2.First_move = True
            B_pawn2.First_move = True
            W_pawn3.First_move = True
            B_pawn3.First_move = True
            W_pawn4.First_move = True
            B_pawn4.First_move = True
            W_pawn5.First_move = True
            B_pawn5.First_move = True
            W_pawn6.First_move = True
            B_pawn6.First_move = True
            W_pawn7.First_move = True
            B_pawn7.First_move = True
            W_pawn8.First_move = True
            B_pawn8.First_move = True
            print("XXXX")
    pygame.display.flip()
pygame.quit()