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
        self.selected_room_type = None  # Track the selected room type

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._handle_robot_menu_click(mouse_pos)
                self._handle_room_menu_click(mouse_pos)

    def _handle_robot_menu_click(self, mouse_pos):
        for index, robot in enumerate(self.robots):
            icon_rect = pygame.Rect(50 + index * 60, self.settings.screen_height - 50, 40, 40)
            if icon_rect.collidepoint(mouse_pos):
                # Open task assignment menu or directly assign a task
                robot.assign_task("New Task")  # Example task assignment

    def _handle_room_menu_click(self, mouse_pos):
        room_types = ["Generator", "Mine", "Bio Lab", "Turret"]
        for index, room_type in enumerate(room_types):
            button_rect = pygame.Rect(self.settings.screen_width - 150, 100 + index * 60, 140, 40)
            if button_rect.collidepoint(mouse_pos):
                # Handle room selection
                self.selected_room_type = room_type
                print(f"Selected room type: {room_type}")

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

        # Draw HUD - Resources at top right
        self._draw_resources()

        # Draw Robot management menu
        self._draw_robot_menu()

        # Draw Room selection menu
        self._draw_room_menu()

        # Draw Timer and Progress Bar for next wave
        self._draw_wave_timer()

        pygame.display.flip()

    def _draw_resources(self):
        font = pygame.font.Font(None, 36)
        metal_text = font.render(f"Metal: {self.resources['metal']}", True, (255, 255, 255))
        energy_text = font.render(f"Energy: {self.resources['energy']}", True, (255, 255, 255))
        bio_mass_text = font.render(f"Bio Mass: {self.resources['bio_mass']}", True, (255, 255, 255))
        self.screen.blit(metal_text, (self.settings.screen_width - 150, 10))
        self.screen.blit(energy_text, (self.settings.screen_width - 150, 40))
        self.screen.blit(bio_mass_text, (self.settings.screen_width - 150, 70))

    def _draw_robot_menu(self):
        font = pygame.font.Font(None, 24)
        for index, robot in enumerate(self.robots):
            # Draw robot icons (placeholder: small squares)
            icon_rect = pygame.Rect(50 + index * 60, self.settings.screen_height - 50, 40, 40)
            pygame.draw.rect(self.screen, (0, 255, 0), icon_rect)

            # Display robot's current task
            task_text = font.render(f"Task: {robot.current_task}", True, (255, 255, 255))
            self.screen.blit(task_text, (50 + index * 60, self.settings.screen_height - 90))

    def _draw_room_menu(self):
        font = pygame.font.Font(None, 24)
        room_types = ["Generator", "Mine", "Bio Lab", "Turret"]
        for index, room_type in enumerate(room_types):
            # Draw room type buttons
            button_rect = pygame.Rect(self.settings.screen_width - 150, 100 + index * 60, 140, 40)
            pygame.draw.rect(self.screen, (100, 100, 100), button_rect)

            # Display room type text
            room_text = font.render(room_type, True, (255, 255, 255))
            self.screen.blit(room_text, (self.settings.screen_width - 140, 110 + index * 60))

    def _draw_wave_timer(self):
        # Calculate time remaining
        time_remaining = max(0, self.settings.time_between_waves - self.wave_manager.time_since_last_wave)
        
        # Draw timer text
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Next Wave: {int(time_remaining)}s", True, (255, 255, 255))
        self.screen.blit(timer_text, (self.settings.screen_width // 2 - 80, 10))
        
        # Draw progress bar
        progress_bar_width = 200
        progress = (self.wave_manager.time_since_last_wave / self.settings.time_between_waves) * progress_bar_width
        pygame.draw.rect(self.screen, (200, 200, 200), 
                         pygame.Rect(self.settings.screen_width // 2 - 100, 50, progress_bar_width, 20))
        pygame.draw.rect(self.screen, (0, 255, 0), 
                         pygame.Rect(self.settings.screen_width // 2 - 100, 50, progress, 20))
