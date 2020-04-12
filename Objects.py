import pygame



class Player:
    turn = None
    move = ''

    def __init__(self):
        pass


class rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if (self.x, self.y) == (175, 175):
            self.index = 1
        elif (self.x, self.y) == (175, 225):
            self.index = 2
        elif (self.x, self.y) == (175, 275):
            self.index = 3
        elif (self.x, self.y) == (225, 175):
            self.index = 4
        elif (self.x, self.y) == (225, 225):
            self.index = 5
        elif (self.x, self.y) == (225, 275):
            self.index = 6
        elif (self.x, self.y) == (275, 175):
            self.index = 7
        elif (self.x, self.y) == (275, 225):
            self.index = 8
        elif (self.x, self.y) == (275, 275):
            self.index = 9

    def draw(self, win):
        pygame.draw.rect(win, (200, 200, 200), (self.x, self.y))

    def isclicked(self, a):

        if (a[0] in range(self.x, self.x + 50)) and (a[1] in range(self.y, self.y + 50)):
            return True
        else:
            return False


class Game:
    players = [Player(), Player()]
    id = None
    moveCount = 0
    ready = None
    p1 = []
    p2 = []
    coordinates = [(175, 175), (175, 225), (175, 275), (225, 175), (225, 225), (225, 275), (275, 175), (275, 225), (275, 275)]
    winners = [(1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 6, 9), (4, 5, 6), (7, 8, 9), (3, 5, 7)]
    win_player = ''

    def __init__(self, id1):
        self.id = id1
        self.cross = pygame.image.load('cross.jpg')
        self.circle = pygame.image.load('circle.png')
        self.rectangles = [rectangle(175, 175), rectangle(175, 225), rectangle(175, 275), rectangle(225, 175), rectangle(225, 225), rectangle(225, 275), rectangle(275, 175), rectangle(275, 225), rectangle(275, 275)]

    def draw(self,win):
        win.fill((255, 255, 255))
        for rectangle_ in self.rectangles:
            rectangle_.draw(win)
        for p in self.p1:
            self.draw_cross(self.rectangles[p-1], win)
        for p in self.p2:
            self.draw_ccircle(self.rectangles[p-1], win)
    def draw_cross(self, rect, win):
        win.blit(self.cross, (rect.x, rect.y))

    def draw_circle(self, rect, win):
        win.blit(self.circle, (rect.x, rect.y))

    def check_win_p1(self):
        count = 0
        for winner in self.winners:
            for a1 in self.p1:
                if a1 in winner:
                    count =+1
            if count == 3:
                return True

            else:
                count = 0

        return False

    def check_win_p2(self):
        count = 0
        for winner in self.winners:
            for a1 in self.p2:
                if a1 in winner:
                    count = +1
            if count == 3:
                return True

            else:
                count = 0

        return False