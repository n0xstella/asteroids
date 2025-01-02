import pygame

class MusicManager:
    def __init__(self):
        pygame.mixer.init()

        # Dictionaries for BGM and SFX
        self.music = {
            "game_start_bgm": "assets/audio/game_start.mp3",
            "game_over_bgm": "assets/audio/game_over.mp3",
        }
        self.sounds = {
            "firing_laser_sfx": pygame.mixer.Sound("assets/audio/firing_laser_sfx.mp3"),
        }

    def play_bgm(self, bgm_key, loop=False):
        # Play background music.
        if bgm_key in self.music:
            try:
                pygame.mixer.music.load(self.music[bgm_key])
                loops = -1 if loop else 0
                pygame.mixer.music.play(loops=loops)
            except pygame.error as e:
                print(f"Error loading BGM '{bgm_key}': {e}")
        else:
            print(f'BGM "{bgm_key}" not found!')

    def stop_bgm(self):
        #Stop the currently playing background music.
        pygame.mixer.music.stop()

    def play_sound(self, sound_key):
        #Play a sound effect.
        if sound_key in self.sounds:
            try:
                pygame.mixer.Sound.set_volume(self.sounds[sound_key], 0.2)
                self.sounds[sound_key].play()
            except pygame.error as e:
                print(f"Error playing sound '{sound_key}': {e}")
        else:
            print(f'Sound "{sound_key}" not found!')

    def stop_all_sounds(self):
        # Stop all currently playing sound effects.
        pygame.mixer.stop()