import math
from pygame.draw import *
from random import choice
from random import randint
import pygame
import sys
pygame.font.init()



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

g = 10

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.dt = 0.08
        self.color = choice(GAME_COLORS)
        self._live = 1

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.x - self.r >= 0 and WIDTH - self.x >= self.r and self.y - self.r >= 0 and self.y + self.r <= HEIGHT:
            self.x += self.vx
            self.y -= self.vy
            self.vy -= g * self.dt
        if self.x - self.r <= 0 or WIDTH - self.x <= self.r and self.y - self.r >= 0 and self.y + self.r <= HEIGHT:
            if WIDTH - self.x <= self.r:
                self.x = WIDTH - self.r
            if self.x - self.r <= 0:
                self.x = self.r
            self.vx *= (-0.5)
            self.vy *= 0.5
            self.x += self.vx
            self.y -= self.vy
            self.vy -= g * self.dt
        if self.x - self.r >= 0 and WIDTH - self.x >= self.r and self.y - self.r <= 0 or self.y + self.r >= HEIGHT:
            if self.y - self.r <= 0:
                self.y = 0 + self.r
            if self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
            self.vy *= (-0.5)
            self.vx *= 0.5
            self.x += self.vx
            self.y -= self.vy
            self.vy -= g * self.dt
        if self.x - self.r <= 0 or WIDTH - self.x <= self.r and self.y - self.r <= 0 or self.y + self.r >= HEIGHT:
            if self.y - self.r <= 0:
                self.y = 0 + self.r
            if self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
            if WIDTH - self.x <= self.r:
                self.x = WIDTH - self.r
            self.vy *= (-0.5)
            self.vx *= (-0.5)
            self.x += self.vx
            self.y -= self.vy
            self.vy -= g * self.dt 

    def live(self):
        if abs(self.vx)<= 0.001:
            self._live = 0

    def draw(self):
        if self._live == 1:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        else:
            return

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME

        if abs(self.x-obj.x) <= self.r + obj.r and abs(self.y - obj.y) <= self.r + obj.r:
            return True

        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.weight = 40
        self.height = 5
        self.point = 0

    def fire2_start(self, event, obj):
        if obj.live == 1:
            self.f2_on = 1
        else:
            return

    def fire2_end(self, event, obj):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        if obj.live == 1:
            global balls, bullet
            bullet += 1
            new_ball = Ball(self.screen)
            new_ball.r += 5
            self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_ball)
            self.f2_on = 0
            self.f2_power = 10
            self.point += 1
            print(self.point)
        else:
            return

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        pygame.draw.polygon(
            self.screen, self.color,
            [
                (20 - int(self.height * math.sin(-self.an)), 450 - int(self.height * math.cos(-self.an))), 
                (20 + int((self.weight * math.cos(-self.an) - self.height * math.sin(-self.an))), 450 - int((self.weight * math.sin(-self.an) + self.height * math.cos(-self.an)))),
                (int(self.weight * math.cos(-self.an) + self.height * math.sin(-self.an)) + 20, 450 - int((self.weight * math.sin(-self.an) + self.height * math.cos(-self.an)) - 2 * self.height * math.cos(-self.an))),
                (20 + int(self.height * math.sin(-self.an)), 450 + int(self.height * math.cos(-self.an)))
            ]
        )
        
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.color = RED
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(10, 50)
        color = self.color = RED

    def hit(self, dpoints=1):
        """Попадание шарика в цель."""
        self.points += dpoints
        #print('очки:', self.points)

    def draw(self):
        if self.live == 1:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

        else:
            return

    def live(self, a):
        self.live = int(a)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
bullet = 0
balls = []

font = pygame.font.SysFont('arial', 30)

pygame.display.update()
clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

target.live(int(1))
target.new_target()
target.draw()

while not finished:
    
    screen.fill(WHITE)

    text1 = font.render(str(target.points), 1, (0, 0, 0))
    screen.blit(text1, (10, 10))
    pygame.display.update()

    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event, target)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event, target)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        b.live()

        if b.hittest(target) and target.live ==  1 and b._live == 1:
            target.live = 0
            target.draw()
            target.hit()
            print('очки:', target.points)          
          
            
        if balls[-1]._live == 0 and target.live == 0:
            for i in range(5000):
                text2 = font.render("Вы уничтожили цель за "+ str(gun.point) + " выстрелов", 1, (0, 0, 0))
                screen.blit(text2, (100, 10))
                pygame.display.update()
                i += 1

            gun.point = 0

            target.live = 1
            target.new_target()
            target.draw()

    gun.power_up()

    '''text1 = f1.render(str(target.point, True, (255, 255, 255))
    sc.blit(text1, (10, 10))'''

pygame.quit()