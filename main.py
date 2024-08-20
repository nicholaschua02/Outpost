# main.py

import pygame
from core.game import Game
from utils.settings import Settings

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Outpost")

    game = Game(screen, settings)
    game.run()

if __name__ == "__main__":
    main()
