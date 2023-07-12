import pygame as py
from pygame.locals import *

class Application:

	def __init__(self):
		py.init()
		self.screen = py.display.set_mode((540, 340))
        Application.running = True

	def play(self):
		# this will run until the window is visible
		while Application.running:
			for event in py.event.get():
				if event.type == QUIT:
				    Application.running = False
		py.quit()

if __name__ == '__main__':
    Application().play()
