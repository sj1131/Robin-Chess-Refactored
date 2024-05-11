from cccc import *

p_list = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook] + [Pawn] * 8

class Team:
    king:King
    def __init__(self, team) -> None:
        self.alive = []
        self.dead  = []
        self.attackable_pos = []
        self.team = team
        self.king_died = False
        ly = 7 if team == 1 else 0
        i  = 0
        for p in p_list:
            if p == Pawn and ly in [0, 7]:
                ly -= team
            tmp_p = p(team=team, lx=i, ly=ly)
            self.alive.append(tmp_p)
            if p == King:
                self.king = tmp_p
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

    def update_attackable(self, chessboard):
        self.attackable_pos.clear()
        for p in self.alive:
            p:Gameobject
            self.attackable_pos += p.getDxDy(chessboard=chessboard)

    #TODO: Maybe move to a new class
    def is_Check(self, attackable):
        for pos in attackable:
            if self.king.get_pos() == pos:
                return True
        return False

    def is_Checkmate(self, chessboard, attackable, ):
        #FIXME: checkmate code needed
        if not self.is_Check(attackable):
            return False
        for pos in self.king.getDxDy(chessboard):
            pass
    #TODO:

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
    def get_attackable(self):
        return self.attackable_pos

