# core/game.py

import pygame
from core.wave_manager import WaveManager
from core.event_manager import EventManager
from entities.robot import Robot
from entities.room import Room
from screens.main_menu import MainMenu
from screens.pause_menu import PauseMenu
from screens.game_over import GameOverScreen
from utils.settings import Settings

class Game:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.clock = pygame.time.Clock()

        # Initialize game components
        self.wave_manager = None
        self.event_manager = None
        self.robots = None
        self.rooms = None
        self.resources = None

        self.running = False
        self.paused = False

        # Initialize screens
        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.game_over_screen = GameOverScreen(self)

    def run(self):
        # Show the main menu and wait for the player to start the game
        self.main_menu.run()

        # Start the game loop once "Start Game" is selected
        self.start_new_game()
        while self.running:
            if self.paused:
                self.pause_menu.run()
            else:
                self._handle_events()
                self._update()
                self._draw()

            self.clock.tick(self.settings.fps)

    def start_new_game(self):
        # Reset game state
        self.wave_manager = WaveManager(self)
        self.event_manager = EventManager(self)
        self.robots = [Robot(self, (100, 100)) for _ in range(5)]  # Example: start with 5 robots
        self.rooms = [Room(self, "Hub", (300, 300))]  # Start with a central hub room
        self.resources = {
            "metal": self.settings.starting_metal,
            "energy": self.settings.starting_energy_crystals,
            "bio_mass": self.settings.starting_bio_mass
        }

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def game_over(self):
        self.game_over_screen.run()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause()

            # Handle other events like input, building, etc.

    def _update(self):
        # Update game logic
        self.wave_manager.update()
        self.event_manager.update()
        for robot in self.robots:
            robot.update()
        for room in self.rooms:
            room.update()

    def _draw(self):
        self.screen.fill(self.settings.bg_color)
        for room in self.rooms:
            room.draw(self.screen)
        for robot in self.robots:
            robot.draw(self.screen)

        # Draw HUD, etc.
        pygame.display.flip()
