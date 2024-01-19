import window


if __name__ == "__main__":
    display = window.Display()

    PADDING_X = 20
    PADDING_Y = 20
    WIDTH = 80
    HEIGHT = 80
    COLS = 4

    for i, sound in enumerate(display.soundboard.sounds):
        column = i % COLS
        row = i // COLS
        x = (2 * PADDING_X) + (column * PADDING_X) + (column * WIDTH)
        y = (2 * PADDING_Y) + (row * PADDING_Y) + (row * HEIGHT)

        button = window.Button(
            x,
            y,
            WIDTH,
            HEIGHT,
            sound[0].upper() + sound[1:3].lower(),
            on_click_sound=sound,
        )

        display.add_button(button)

    total_width = (COLS * WIDTH) + (3 * PADDING_X) + (COLS * PADDING_X)
    total_height = (
        ((len(display.soundboard.sounds) + COLS - 1) // COLS * HEIGHT)
        + (
            ((len(display.soundboard.sounds) + COLS - 1) // COLS - 1)
            * PADDING_Y
        )
        + (4 * PADDING_Y)
    )

    display.resize(total_width, total_height)
    display.run()
