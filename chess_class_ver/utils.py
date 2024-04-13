import pygame
import time

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

class button:
    def __init__(self, message, cx, cy, bg_color, tx_color, font_style):
        self.text = font_style.render(message, True, tx_color)
        self.text_rect = self.text.get_rect(center=(cx, cy))
        self.bg_color = bg_color
        self.w = 250
        self.h = 60
        self.x = cx - self.w/2
        self.y = cy - self.h/2

        
    def draw(self,display):
        pygame.draw.rect(display, self.bg_color, (self.x, self.y, self.w, self.h))
        display.blit(self.text, self.text_rect)

    def click(self, mx, my):
        if mx > self.x and mx < self.x + self.w and my > self.y and my < self.y + self.h:
            return True
        else:
            return False
         
class xx(button):
    def __init__(self, message, cx, cy, bg_color, tx_color, font_style):
        super().__init__(message,cx,cy,bg_color,tx_color,font_style)
        self.w=350
        self.h=80
        self.x = cx - self.w/2
        self.y = cy - self.h/2


class start_notion_button:
    def __init__(self, message, cx, cy, bg_color, tx_color, font_style):
        self.text = font_style.render(message, True, tx_color)
        self.text_rect = self.text.get_rect(center=(cx, cy))
        self.bg_color = bg_color

        self.w = 780
        self.h = 100
        self.x = cx - self.w/2
        self.y = cy - self.h/2
    def draw(self,display):
        pygame.draw.rect(display, self.bg_color, (self.x, self.y, self.w, self.h))
        display.blit(self.text, self.text_rect)

class turn_button:
    def __init__(self, message, cx, cy, bg_color, tx_color, font_style):
        self.text = font_style.render(message, True, tx_color)
        self.text_rect = self.text.get_rect(center=(cx, cy))
        self.bg_color = bg_color

        self.w = 250
        self.h = 50
        self.x = cx - self.w/2
        self.y = cy - self.h/2
    def draw(self,display):
        pygame.draw.rect(display, self.bg_color, (self.x, self.y, self.w, self.h))
        display.blit(self.text, self.text_rect)

class Cap_button:
    def __init__(self, message, cx, cy, bg_color, tx_color, font_style):
        self.text = font_style.render(message, True, tx_color)
        self.text_rect = self.text.get_rect(center=(cx, cy))
        self.bg_color = bg_color

        self.w = 200
        self.h = 33
        self.x = cx - self.w/2
        self.y = cy - self.h/2
    def draw(self,display):
        pygame.draw.rect(display, self.bg_color, (self.x, self.y, self.w, self.h))
        display.blit(self.text, self.text_rect)


class timer:
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
            
####################################################################
class imagebutton:
    def __init__(self, img, cx, cy):
        self.img = img
        self.x = cx
        self.y = cy
    def draw(self,display):
        display.blit(self.img, (self.x, self.y))

    def click(self, mx, my):
        if mx > self.x and mx < self.x + 100 and my > self.y and my < self.y + 100:
            return True
        else:
            return False

####################################################################