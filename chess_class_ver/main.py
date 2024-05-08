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

# Refactored by SJ(Instagram @sjlee1131)
##############################################################################

import pygame
from pygame.font import Font
import copy
import socket
import threading
from cccc import *
from utils import *
from piece import *


pygame.init()

size = (900, 780) # 화면 비율을 수정하시면 오류가 생길수 있습니다.
display = pygame.display.set_mode(size)
Clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Robin Chess Game Project")
icon = pygame.image.load(f"{img_base}/icon.png")
pygame.display.set_icon(icon)
who_won = None

home = pygame.image.load(f"{img_base}/home.png")
home = pygame.transform.scale(home, (100, 100))

default_font         = pygame.font.SysFont(None, 50)
start_font           = Font(f"{base_dir}/Merida Regular.ttf", 36)
start_font_s         = Font(f"{base_dir}/Merida Regular.ttf", 20)
main_font            = Font(f"{base_dir}/Merida Regular.ttf", 36)
main_font_s          = Font(f"{base_dir}/Merida Regular.ttf", 15)
gameover_font        = Font(f"{base_dir}/Merida Regular.ttf", 70)
OpenSans_bold        = Font(f"{base_dir}/OpenSans-Bold.ttf", 55)
OpenSans_bold_s      = Font(f"{base_dir}/OpenSans-Bold.ttf", 30)
OpenSans_bold_l      = Font(f"{base_dir}/OpenSans-Bold.ttf", 80)

offline_start_button = Button("GAME START", (350, 60), (450, 650), gray, black, OpenSans_bold)
start_notion         = TextWidget("Robin Chess Game", (780, 100), (450, 150), gray, black, OpenSans_bold_l)
subtitle             = TextWidget("Refactored by @sjlee1131", (780, 100), (450, 250), gray, black, OpenSans_bold_s)
WHITE_turn           = TextWidget("Turn : WHITE", (250, 50), (150, 675), black, white, start_font_s)
BLACK_turn           = TextWidget("Turn : BLACK", (250, 50), (150, 675), white, black, start_font_s)
restart              = Button("restart", (250, 60), (430, 500), gray, red, start_font)
captured_up          = TextWidget("Captured Pieces", (200, 33), (770, 20), white, black, main_font_s)
captured_down        = TextWidget("Captured Pieces", (250, 33), (770, 400), black, white, main_font_s)
home_button          = ImageButton(home, (5, 700))

__cb = [[-1, -1, -1, -1, -1, -1, -1 ,-1],
        [-1, -1, -1, -1, -1, -1, -1 ,-1],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  1,  1,  1,  1],
        [ 1,  1,  1,  1,  1,  1,  1,  1]]

#-1 = black, 1 = white, 0 = nothing

def mainloop():
    white_timer = Timer(start_font_s, white, 590, 660, 20 * 60+1)
    black_timer = Timer(start_font_s, white, 590, 690, 20 * 60+1)

    w_team = Team(team=1)
    b_team = Team(team=-1)

    Ready = True
    Gaming = False
    online_gaming = False
    Turn = 1

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
            # RESET
            chessboard = copy.deepcopy(__cb)
            Turn = 1
            w_team.reset()
            b_team.reset()

            white_timer.reset()
            black_timer.reset()

            display.fill(gray)
            for widget in [offline_start_button, start_notion, subtitle]:
                widget.draw(display)
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
            text_print(display, "WHITE : ", start_font_s, white, 470, 660)
            text_print(display, "BLACK : ", start_font_s, white, 470, 690)
            white_timer.countdown(display)
            black_timer.countdown(display)
            if mclick:
                if home_button.click(xx, yy):
                    Ready = True
                    mclick = False
                    Gaming = False
            if Turn == 1:
                white_timer.resume()
                black_timer.pause()
                WHITE_turn.draw(display)
            else:
                white_timer.pause()
                black_timer.resume()
                BLACK_turn.draw(display)
                
            #################################################################################
            for p in w_team.get_alive() + b_team.get_alive():
                p:Gameobject
                p.draw(display)

                other_team = w_team if p in b_team.alive else b_team
                if Turn == p.team:
                    if mclick:
                        if not p.clicked:
                            p.click(xx,yy)
                        else:
                            socket_list = p.moveclick(xx, yy, chessboard, other_team)
                            if socket_list[1] != socket_list[3] or socket_list[2] != socket_list[4]:
                                print(socket_list)
                                Turn *= -1

                    if p.clicked:
                        p.drawX(display, default_font, black, chessboard)

            mclick=False
            
            w_team.render_dead(display=display)
            b_team.render_dead(display=display)
                    
            if w_team.king_died or white_timer.timeover:
                who_won = "BLACK"
                Gaming = False
            elif b_team.king_died or black_timer.timeover:
                who_won = "WHITE"
                Gaming = False

        else:
            display.fill(black)
            text_print(display, "Game Over", gameover_font, red, 440, 300)
            text_print(display, str(who_won) + " WON !!", main_font, white, 445, 400)
            restart.draw(display)
            if mclick and restart.click(xx, yy):
                Ready = True
                Gaming = False
                who_won = ""
                ##################################################################################
                print("XXXX")
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    mainloop()