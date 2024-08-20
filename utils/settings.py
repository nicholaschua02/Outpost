# utils/settings.py

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (30, 30, 30)
        
        # Frame rate
        self.fps = 60

        # Resource limits (example values, can be adjusted)
        self.starting_metal = 100
        self.starting_energy_crystals = 50
        self.starting_bio_mass = 30
        
        # Robot settings
        self.robot_speed = 2  # Movement speed of robots
        
        # Enemy settings
        self.enemy_speed = 1  # Base speed of enemies
        self.enemy_spawn_rate = 30  # Frames between enemy spawns
        
        # Room settings
        self.room_cost_metal = 20
        self.room_cost_energy = 10
        self.room_cost_bio = 5

        # Wave settings
        self.time_between_waves = 60  # Seconds between waves
