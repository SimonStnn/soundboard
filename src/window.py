import sys
import time
import logging
from typing import Callable
import pygame

from soundboard import SoundBoard

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)


EventType = Callable[[], None]


class Display:
    x = 0
    y = 0
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    soundboard = SoundBoard()
    buttons: list["Button"] = []

    def __init__(self, *, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        pygame.display.set_mode((width, height))
        pygame.init()
        pygame.display.set_caption("Soundboard")

    def resize(self, width: int | None, height: int | None):
        if width is None:
            width = self.width
        if height is None:
            height = self.height

        self.width = width
        self.height = height
        pygame.display.set_mode((width, height))

    def _render(self):
        Display.screen.fill(white)

        # Render buttons in grid of 4 x 2
        for button in self.buttons:
            button.draw()

    def add_button(self, button: "Button"):
        self.buttons.append(button)

    def run(self):
        while True:
            for event in pygame.event.get():
                match (event.type):
                    case pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    case pygame.MOUSEBUTTONDOWN:
                        # Find the clicked button
                        for button in self.buttons:
                            if button.rect.collidepoint(event.pos):
                                button.on_click()
                                break
                    case _:
                        pass

            # Render
            self._render()

            pygame.display.flip()
            time.sleep(0.01)


# Button class
class Button:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        *,
        font_size: int = 36,
        on_click_sound: str,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = text
        self.on_click_sound = on_click_sound

    def draw(self):
        pygame.draw.rect(Display.screen, white, self.rect)
        pygame.draw.rect(Display.screen, black, self.rect, 2)

        text_surface = self.font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        Display.screen.blit(text_surface, text_rect)

    def on_click(self):
        logging.debug(f"Clicked sound button: {self.text}, {self.on_click_sound}")
        Display.soundboard.play(self.on_click_sound)
