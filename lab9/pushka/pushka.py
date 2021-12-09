import math
from random import choice
import random as ra
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
u = 450
v = 400
v2 = 0
u2 = 0

uu = 100
vv = 100
uu2 = 0
vv2 = 0
radius_chidori = 60
stadia_igri = 0
s_chot = 0
gt = -1  # приращение скорости за кадр

yo = pygame.image.load('yo.png')
yo1 = pygame.transform.scale(yo, (40, 20))

JABLOKO = pygame.image.load('trgt.png')

FON = pygame.image.load('bckgrnd.jpg')
FON = pygame.transform.scale(FON, (800, 600))

P = pygame.image.load('player1.png')
P1 = pygame.transform.scale(P, (40, 72))

S = pygame.image.load('player2.png')
S1 = pygame.transform.scale(S, (110, 70))

RAS = pygame.image.load('ggg.png')
RAS1 = pygame.transform.scale(RAS, (40, 40))

CHI = pygame.image.load('chi.jpg')
CHI1 = pygame.transform.scale(CHI, (220, 120))

ghost = pygame.image.load('ssssss.png')

gmovr = pygame.image.load('gmovr.jpg')
gmovr = pygame.transform.scale(gmovr, (800, 600))


class Ball:
    def __init__(self, screen: pygame.Surface, x=v, y=u):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME вроде пофиксил

        if (self.x < (800 - self.r) and self.x > self.r):
            self.x += self.vx
            self.vx = self.vx * 0.99
        else:
            self.vx = - self.vx
            self.x = self.x + 2 * self.vx

        if (self.y < (600 - self.r) and self.y > self.r):
            self.y += self.vy
            self.vy = self.vy - gt
            self.vy = self.vy * 0.95
        else:
            self.vy = - 0.9 * self.vy
            self.y = self.y + 0.9 * self.vy

    def draw(self):
        yo = pygame.transform.rotate(yo1, -math.atan((self.vy) / (self.vx)) * self.x)
        self.screen.blit(yo, (self.x - 20, self.y - 10))

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r - 10) ** 2:
            return True
        else:  # fixe me вроде пофиксил
            return False


class Ball2(Ball):
    def paint(self):
        self.screen.blit(RAS1, (self.x - 20, self.y - 20))


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 20
        self.wigth = 6
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.xp = 100
        self.xp2 = 100
        self.x = v
        self.y = u
        self.x2 = vv
        self.y2 = uu
        self.r = 20

    def draw_xp(self):
        pygame.draw.rect(screen, (255, 0, 0), (10, 570, 2 * self.xp, 10))
        pygame.draw.rect(screen, (0, 0, 0), (10, 570, 200, 10), 3)

    def draw_xp2(self):
        pygame.draw.rect(screen, (255, 0, 0), (390, 570, 2 * self.xp2, 10))
        pygame.draw.rect(screen, (0, 0, 0), (390, 570, 200, 10), 3)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.x = v
        new_ball.y = u
        new_ball.r += 5
        self.an = -math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.xp = self.xp - 5
        self.f2_on = 0
        self.f2_power = 10

    def fire2syr_end(self, event):
        """Выстрел расенганом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls2, bullet
        bullet += 1
        new_ball = Ball2(self.screen)
        new_ball.x = v
        new_ball.y = u
        new_ball.r += 5
        self.an = -math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls2.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] == v:
                self.an = 1.57
            else:
                self.an = -math.atan((event.pos[1] - u) / (event.pos[0] - v))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw1(self):
        """Рисуем пушку. Зависит от положения мыши."""
        global v2, u2
        self.screen.blit(P1, (v - 55, u - 38))
        v2 = v
        u2 = u

    # pygame.draw.polygon(self.screen, self.color, ([v, u],
    # [v + self.f2_power * math.cos(self.an), u - self.f2_power * math.sin(self.an)],
    # [v + self.f2_power * math.cos(self.an) + self.wigth * math.sin(self.an), u - self.f2_power * math.sin(self.an) + self.wigth * math.cos(self.an)],
    # [v + self.wigth * math.sin(self.an), u + self.wigth * math.cos(self.an)]))
    # FIXIT don't know how to do it вроде пофиксил

    def draw2(self):
        """Рисуем пушку. Зависит от положения мыши."""
        global vv2, uu2
        self.screen.blit(S1, (vv - 55, uu - 38))
        vv2 = vv
        uu2 = uu

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.x = ra.randint(0, 780)
        self.y = ra.randint(0, 550)
        self.r = 50
        self.points = 1
        self.live = 1
        self.color = choice(GAME_COLORS)

    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = ra.randint(0, 780)
        y = self.y = ra.randint(0, 550)
        r = self.r = ra.randint(20, 50)
        color = self.color = RED
        self.live = 1
        self.points = 1

    def move(self):
        self.x = self.x + ra.randint(-4, 4)
        self.y = self.y + ra.randint(-4, 4)

    def hit(self):
        """Попадание шарика в цель."""
        global s_chot
        s_chot += self.points

    def draw(self):
        JABLOKO1 = pygame.transform.scale(JABLOKO, (self.r, self.r))
        self.screen.blit(JABLOKO1, (self.x - 20, self.y - 10))


class Ghast:
    def __init__(self, screen):
        self.screen = screen
        self.x = ra.randint(0, 800)
        self.y = ra.randint(0, 600)
        self.r = 50
        self.speed = 1
        self.angle = math.atan2((self.y - u2), (self.x - v2))

    def move(self):
        self.x = self.x + self.speed * math.cos(math.atan2((u2 - self.y), (v2 - self.x)))
        self.y = self.y + self.speed * math.sin(math.atan2((u2 - self.y), (v2 - self.x)))

    def draw(self):
        ghost1 = pygame.transform.scale(ghost, (self.r + 20, self.r - 20))
        self.screen.blit(ghost1, (self.x - 25, self.y - 15))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0

balls = []
balls2 = []

clock = pygame.time.Clock()
gun = Gun(screen)
gun2 = Gun(screen)
target = Target(screen)
ghast = Ghast(screen)
finished = False

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков ', True, (255, 0, 0))

while not finished:

    if stadia_igri == 0:
        pygame.draw.rect(screen, (255, 0, 255), (100, 100, 600, 100))
        text01 = f1.render('SINGLE MODE', True, (0, 0, 0))
        screen.blit(text01, (300, 140))
        pygame.draw.rect(screen, (0, 255, 0), (100, 400, 600, 100))
        text02 = f1.render('PVP MODE', True, (0, 0, 0))
        screen.blit(text02, (330, 440))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 100 and event.pos[0] < 700 and event.pos[1] > 100 and event.pos[1] < 200):
                    stadia_igri = 1
                if (event.pos[0] > 100 and event.pos[0] < 700 and event.pos[1] > 400 and event.pos[1] < 500):
                    stadia_igri = 3
                    '''multiplayer ещё написать нужно'''
            if event.type == pygame.QUIT:
                finished = True

    if ((u2 - ghast.y) ** 2 + (v2 - ghast.x) ** 2) < 100 and stadia_igri == 1:
        stadia_igri = 2
    if ((u2 - ghast.y) ** 2 + (v2 - ghast.x) ** 2) < 100 and stadia_igri == 3:
        stadia_igri = 4

    if stadia_igri == 3:
        if gun.xp <= 0:
            stadia_igri = 4
        if gun2.xp2 <= 0:
            stadia_igri = 5
        screen.blit(FON, (0, 0))
        gun.draw1()
        gun2.x = vv
        gun2.y = uu
        gun2.draw2()

        clock.tick(FPS)
        for event in pygame.event.get():
            massiv_klavish = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                finished = True

            if massiv_klavish[pygame.K_n]:
                screen.blit(CHI1, (vv - 110, uu - 60))

                if (((v - vv) ** 2 + (u - uu) ** 2) < radius_chidori ** 2):
                    gun.xp = gun.xp - 8
                if (((ghast.x - vv) ** 2 + (ghast.y - uu) ** 2) < radius_chidori ** 2):
                    gun2.xp2 = gun2.xp2 + 1
                    if gun2.xp2 > 100:
                        gun2.xp2 = 100

            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    gun.fire2_end(event)
                if event.button == 3:
                    gun.fire2syr_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)
            if massiv_klavish[pygame.K_s]:
                u = u + 5
            if massiv_klavish[pygame.K_w]:
                u = u - 5
            if massiv_klavish[pygame.K_d]:
                v = v + 5
            if massiv_klavish[pygame.K_a]:
                v = v - 5

            if massiv_klavish[pygame.K_k]:
                uu = uu + 5
            if massiv_klavish[pygame.K_i]:
                uu = uu - 5
            if massiv_klavish[pygame.K_l]:
                vv = vv + 5
            if massiv_klavish[pygame.K_j]:
                vv = vv - 5

        for b in balls:
            b.move()
            b.draw()
            b.live = b.live - 1
            if b.live == 0:
                b.x = 1000
            if b.hittest(target) and target.live:
                target.live = 0
                gun.xp += 20
                if gun.xp > 100:
                    gun.xp = 100
                target.hit()
                target.new_target()
        for b2 in balls2:
            b2.move()
            b2.paint()
            b2.live = b2.live - 1
            if b2.live == 0:
                b2.x = 1000
            if b2.hittest(gun2):
                gun2.xp2 = gun2.xp2 - 5
                if gun.xp > 100:
                    gun.xp = 100
                b2.x = 10000
        gun.draw_xp()
        gun2.draw_xp2()
        ghast.draw()
        pygame.display.update()
        ghast.move()
        gun.power_up()

    if stadia_igri == 2:
        screen.blit(gmovr, (0, 0))
        screen.blit(text1, (230, 520))
        text2 = f1.render(str(s_chot), True, (255, 0, 0))
        screen.blit(text2, (500, 520))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    if stadia_igri == 1:
        if gun.xp <= 0:
            stadia_igri = 2
        screen.blit(FON, (0, 0))
        gun.draw1()
        gun.draw_xp()
        target.move()
        target.draw()
        ghast.draw()
        for b in balls:
            b.draw()
            b.live = b.live - 1
            if b.live == 0:
                b.x = 1000
        for b2 in balls2:
            b2.paint()
            b2.live = b2.live - 1
            if b2.live == 0:
                b2.x = 1000
        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            massiv_klavish = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    gun.fire2_end(event)
                if event.button == 3:
                    gun.fire2syr_end(event)
            elif event.type == pygame.MOUSEMOTION:
                gun.targetting(event)
            if massiv_klavish[pygame.K_s]:
                u = u + 5
            if massiv_klavish[pygame.K_w]:
                u = u - 5
            if massiv_klavish[pygame.K_d]:
                v = v + 5
            if massiv_klavish[pygame.K_a]:
                v = v - 5

        for b in balls:
            b.move()
            b.draw()
            if b.hittest(target) and target.live:
                target.live = 0
                gun.xp += 11
                if gun.xp > 100:
                    gun.xp = 100
                target.hit()
                target.new_target()
        for b2 in balls2:
            b2.move()

        ghast.move()
        gun.power_up()

    if stadia_igri == 4:
        screen.blit(gmovr, (0, 0))

        text2 = f1.render('player2 is the winner', True, (255, 0, 0))
        screen.blit(text2, (500, 520))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    if stadia_igri == 5:
        screen.blit(gmovr, (0, 0))

        text2 = f1.render('player1 is the winner', True, (255, 0, 0))
        screen.blit(text2, (500, 520))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
print(s_chot)
pygame.quit()
