# entities/robot.py

import pygame

class Robot:
    def __init__(self, game, position):
        self.game = game
        self.position = pygame.Vector2(position)
        self.speed = game.settings.robot_speed
        self.current_task = "Idle"  # Track the robot's current task

        # Placeholder for robot appearance
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))  # Green square for the robot

    def update(self):
        # Logic for updating robot's position and task handling
        pass

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def assign_task(self, task):
        # Assign a new task to the robot
        self.current_task = task
        print(f"Robot assigned to {task}")
