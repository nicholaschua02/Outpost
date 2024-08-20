# screens/pause_menu.py

import pygame

class PauseMenu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 74)
        self.options = ["Resume", "Main Menu", "Exit"]
        self.selected_index = 0

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for index, option in enumerate(self.options):
            color = (255, 255, 255) if index == self.selected_index else (100, 100, 100)
            text = self.font.render(option, True, color)
            screen.blit(text, (self.game.settings.screen_width // 2 - text.get_width() // 2, 
                               self.game.settings.screen_height // 2 + index * 100 - text.get_height() // 2))
        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                if self.selected_index == 0:
                    self.game.unpause()
                elif self.selected_index == 1:
                    self.game.show_main_menu()
                elif self.selected_index == 2:
                    pygame.quit()
                    exit()

    def run(self):
        while self.game.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.handle_input(event)
            self.draw(self.game.screen)
