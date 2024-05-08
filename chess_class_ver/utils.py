import pygame
import time

from pygame.font import Font
from os import listdir, getcwd

base_dir = "./" if "images" in listdir(getcwd()) else "./chess_class_ver"
img_base = f"{base_dir}/images"

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)
check_bright = (238,238,210)#(234, 198, 150)
check_dark = (118,150,86)#(86,52,42)
gray = (158, 158, 158)
back_color = (39, 37, 34)
skyblue = (135, 206, 235)
start_back = (234, 198, 150)

def text_print(display, message,font_style, color, x, y):
    text = font_style.render(message, True, color)
    text_rect = text.get_rect(center=(x,y))
    display.blit(text, text_rect)

def draw_board(bri, dar, display):
    for row in range(8):
        for col in range(8):
            color = bri if (row + col) % 2 == 0 else dar
            pygame.draw.rect(display, color, (col * 80, row * 80, 80, 80))

def team2str(team:int):
    return "white" if team== 1 else "black"

class TextWidget:
    def __init__(self, msg:str, wh:tuple, center:tuple, bg:tuple, fg:tuple, font:pygame.font.Font):
        cx, cy = center
        self.text = font.render(msg, True, fg)
        self.text_rect = self.text.get_rect(center=(cx, cy))
        self.bg_color = bg
        self.w, self.h = wh
        self.x = cx - self.w / 2
        self.y = cy - self.h / 2

    def draw(self,display):
        pygame.draw.rect(display, self.bg_color, (self.x, self.y, self.w, self.h))
        display.blit(self.text, self.text_rect)


class Button(TextWidget):
    def click(self, mx, my):
        return True if (mx > self.x and mx < self.x + self.w and my > self.y and my < self.y + self.h) else False

class ImageButton(Button):
    def __init__(self, img:pygame.Surface, wh:tuple, center:tuple):
        self.img = img
        self.x, self.y = center
        self.w, self.h = wh

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

class Timer:
    def __init__(self, Font, color, x, y, total_seconds):
        self.Font = Font
        self.color = color
        self.x = x
        self.y = y
        self.total_seconds = total_seconds
        self.current_seconds = self.total_seconds
        self.paused = False
        self.timeover = False

    def countdown(self, display):
        minutes = int(self.current_seconds) // 60
        seconds = int(self.current_seconds) % 60
        timer_text = f"{minutes:02d}:{seconds:02d}"
        
        text_print(display, timer_text, self.Font, self.color, self.x, self.y)
        
        if not self.paused:
            self.current_seconds -= 1 / 60
            if self.current_seconds < 0:
                self.current_seconds = 0
        if timer_text == "00:00":
            self.timeover = True

    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False

    def reset(self):
        self.current_seconds = self.total_seconds
        self.paused = False
        self.timeover = False
