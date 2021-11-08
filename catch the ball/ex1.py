import pygame
from pygame.draw import *
from random import randint
from random import choice
import sys
pygame.font.init()

COLOR = [(127, 127, 127), (255, 0, 255), (255, 255, 255)]
FPS = 20
height = 800
weight = 1200
score = 0
screen = pygame.display.set_mode((weight, height))
screen.fill((255, 255, 255))


class Ball:

	def __init__(self):
		'''
		Задаёт основные парметры шарика
		'''
		self.x = randint(100, 700)
		self.y = randint(50, 300)
		self.v_x = randint(-20, 20)
		self.v_y = randint(-20, 20)
		self.r = randint(10, 50)
		self.color = choice(COLOR)


	def draw(self, surface):
		'''
		Рисует шарик
		'''
		circle(surface, self.color, (self.x, self.y), self.r)

	def move(self):
		'''
		Задаёт движение шариков
		'''
		self.x += self.v_x
		self.y += self.v_y

	def collision(self):
		'''
		Задаёт отражение шариков от стенок
		'''
		if self.x <= self.r or self.x >= weight - self.r and self.y >= self.r :			
			self.v_x *= -1
			self.x += self.v_x
			self.y += self.v_y

		if self.y <= self.r or self.y >= height - self.r and self.x >=self.r :
			self.v_y *= -1
			self.x += self.v_x
			self.y += self.v_y

	def event(self, event, score):
		'''
		Проверяет клик по шарику и считает баллы
		'''
		pos_x, pos_y = event.pos
		r1 = ((pos_x - self.x)**2 + (pos_y - self.y)**2)**(1/2)
		if r1 <= self.r:
			score += 1
			print(score)
		return score

class Square:

	def __init__(self):
		self.a = randint(20, 40)
		self.x = randint(100, 700)
		self.y = randint(50, 300)
		self.vx = randint(-20, 20)
		self.vy = randint(-20, 20)
		self.color = choice(COLOR)

	def draw(self, surface):
		rect(surface, self.color, (self.x, self.y, self.a, self.a))

	def move(self):
		self.y += self.vy
		self.x += self.vx

	def collision(self):
		if self.x <= 0 or self.x >= weight - self.a and self.y >= 0 and self.y <= height - self.a:
			if self.x < 0:
				self.x = 0
				self.vx *= (-1)
			if self.x > weight - self.a:
				self.x = weight - self.a
				self.vx *= (-1)

		if self.x >=0 and self.x <= weight - self.a and self.y <= 0 or self.y >= height - self.a:
			if self.y < 0:
				self.y = 0
				break
				#self.vy *= (-1)
			if self.y > height - self.a:
				self.y = height - self.a
				break
			self.vy *= (-1)

		if self.x <= 0 or self.x >= weight - self.a and self.y <= 0 or self.y >= height - self.a:
			if self.x < 0:
				self.x = 0
				self.vy *= (-1)
				self.vx *= (-1) 
			if self.x > weight - self.a:
				self.x = weight - self.a
				self.vy *= (-1)
				self.vx *= (-1) 
			if self.y < 0:
				self.y = 0
				self.vy *= (-1)
				self.vx *= (-1) 
			if self.y > height - self.a:
				self.y = height - self.a 
				self.vy *= (-1)
				self.vx *= (-1)

	#def 
			
					

ball = Ball()
pool = [Ball() for _ in range(10)]
square = Square()
pool2 = [Square() for _ in range(10)]

f1 = pygame.font.Font(None, 50)
text1 = f1.render('score', True, (255, 255, 255))
screen.blit(text1, (10, 10))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            for ball in pool:
    	        score = ball.event(event, score)

    for i in range(10):
    	pool[i].draw(screen)
    	pool[i].collision()
    	pool[i].move()
    for i in range(10):
    	pool2[i].draw(screen)
    	pool2[i].collision()
    	pool2[i].move()
    	print(pool2[i].vy, pool2[i].vx, pool2[i].x, pool2[i].y)
    
    pygame.display.update()
    screen.fill((0, 0, 0))
    text1 = f1.render(str(score), True, (255, 255, 255))
    screen.blit(text1, (10, 10))

pygame.quit()