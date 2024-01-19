import window


if __name__ == "__main__":
    display = window.Display()

    padding = 20
    vertical_padding = 20
    width = 80
    height = 80
    columns = 4

    for i, sound in enumerate(display.soundboard.sounds):
        column = i % columns
        row = i // columns
        x = (2 * padding) + (column * padding) + (column * width)
        y = (2 * vertical_padding) + (row * vertical_padding) + (row * height)

        button = window.Button(
            x,
            y,
            width,
            height,
            sound[0].upper() + sound[1:3].lower(),
            on_click_sound=sound,
        )

        display.add_button(button)

    total_width = (columns * width) + (3 * padding) + (columns * padding)
    total_height = (
        ((len(display.soundboard.sounds) + columns - 1) // columns * height)
        + (
            ((len(display.soundboard.sounds) + columns - 1) // columns - 1)
            * vertical_padding
        )
        + (4 * vertical_padding)
    )

    display.resize(total_width, total_height)
    display.run()
