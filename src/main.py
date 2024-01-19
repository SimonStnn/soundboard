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

        button = window.Button(x, y, WIDTH, HEIGHT, sound)

        display.add_button(button)

    TOTAL_WIDTH = (COLS * WIDTH) + (3 * PADDING_X) + (COLS * PADDING_X)
    TOTAL_HEIGHT = (
        ((len(display.soundboard.sounds) + COLS - 1) // COLS * HEIGHT)
        + (((len(display.soundboard.sounds) + COLS - 1) // COLS - 1) * PADDING_Y)
        + (4 * PADDING_Y)
    )

    display.resize(TOTAL_WIDTH, TOTAL_HEIGHT)
    display.run()
