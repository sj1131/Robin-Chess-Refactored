from cccc import *

p_list = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook] + [Pawn] * 8

class Team:
    def __init__(self, team) -> None:
        self.alive = []
        self.dead  = []
        self.team = team
        self.king_died = False
        ly = 7 if team == 1 else 0
        i  = 0
        for p in p_list:
            if p == Pawn and ly in [0, 7]:
                ly -= team
            self.alive.append(p(team=team, lx=i, ly=ly))
            i = (i + 1) % 8
    
    def render_dead(self, display:pygame.Surface):
        xi = 670
        yi = 45 if self.team == 1 else 420
        for dead in self.dead:
            dead:Gameobject
            display.blit(dead.img, (xi, yi))
            xi += 70
            if xi >= 850:
                xi = 670
                yi += 70

    def kill(self, target:Gameobject):
        if target not in self.alive:
            return
        idx = self.alive.index(target)
        self.dead.append(self.alive[idx])
        self.alive.remove(target)
        if type(target) == King:
            self.king_died = True

    def reset(self):
        self.alive += self.dead
        self.dead.clear()
        self.king_died = False
        for p in self.alive:
            p.reset()
    
    def get_alive(self)->list:
        return self.alive
    def get_dead(self)->list:
        return self.dead

