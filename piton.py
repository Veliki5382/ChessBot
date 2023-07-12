import pygame as py
import chess

class Application:

    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((1600, 900))
        self.clock = py.time.Clock()
        self.is_running = True
        
        self.board = Board()
    
    def run(self):

        while(self.is_running == True):
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.is_running = False
            
            self.screen.fill("magenta")
            self.board.draw_board(self.screen)

            py.display.flip()

        py.quit()


class Board:

    def __init__(self):
        self.light_color = (255, 228, 138)
        self.dark_color = (133, 95, 30)
        self.tile_size = 96
        self.xOffset = 800 - 4 * self.tile_size
        self.yOffset = 450 - 4 * self.tile_size

    def draw_board(self, screen):
        
        for i in range(8):
            for j in range(8):
                tile = py.Rect(self.xOffset+i*self.tile_size, self.yOffset+j*self.tile_size, self.tile_size, self.tile_size)
                if i+j & 1:
                    py.draw.rect(screen, self.dark_color, tile)
                else:
                    py.draw.rect(screen, self.light_color, tile)


if __name__ == "__main__":
    
    app = Application()
    app.run()