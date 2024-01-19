import os
import pygame


class SoundBoard:
    def __init__(self) -> None:
        self.__setup_output_device()

        self.sounds = os.listdir("./audio")

    def __setup_output_device(
        self, devicename: str | None = None, *, capture_devices: bool = False
    ):
        pygame.mixer.init()

    def play(self, file_path: str):
        # find best match
        file_path = file_path.lower()
        file_path = (
            sound for sound in self.sounds if file_path in sound.lower()
        ).__next__()

        pygame.mixer.music.load(os.path.join("./audio", file_path))
        pygame.mixer.music.play()

    def __delattr__(self, __name: str) -> None:
        self.__del__()

    def __del__(self) -> None:
        pygame.mixer.quit()
