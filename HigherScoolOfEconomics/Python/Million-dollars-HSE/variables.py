import pygame as pg

color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_grey = (18, 18, 18)
color_light_gray = (169, 169, 169)
color_blue = (0, 0, 255)
color_yellow = (246, 202, 9)
color_red = (255, 0, 0)
color_pure_green = (0, 255, 0)
color_bright_blue = (0, 151, 255)
color_dark_blue = (0, 0, 50)
color_transparent = (255, 255, 255, 0)
color_pink = (255, 184, 255)
color_inky = (0, 255, 255)
color_clyde = (255, 184, 82)
color_food = (248, 176, 144)

color_light_orange = (250, 168, 67)
color_orange = (190, 107, 5)
color_dark_orange = (88, 47, 0)

color_light_retro_wave = (248, 135, 255)
color_middle_retro_wave = (151, 0, 204)
color_dark_retro_wave = (50, 20, 80)
color_line_retro_wave = (30, 180, 250)

color_dark_green = (0, 50, 0)
color_green = (0, 150, 20)
color_light_green = (150, 200, 0)

hot_keys = {
    "Confirmation": pg.K_RETURN,
    "ReplayCurrent": pg.K_c,
    "ReplayDefault": pg.K_o,
    "ReplayGenerated": pg.K_g,
    "Mute": pg.K_m,
    "Pause": pg.K_p,
    "ToSettings": pg.K_SPACE,
    "ToRecords": pg.K_TAB,
    "GoBack": pg.K_BACKSPACE,
    "Up": pg.K_w,
    "Right": pg.K_d,
    "Down": pg.K_s,
    "Left": pg.K_a
}

default_hot_keys = {
    "Confirmation": pg.K_RETURN,
    "ReplayCurrent": pg.K_c,
    "ReplayDefault": pg.K_o,
    "ReplayGenerated": pg.K_g,
    "Mute": pg.K_m,
    "Pause": pg.K_p,
    "ToSettings": pg.K_LCTRL,
    "ToRecords": pg.K_TAB,
    "GoBack": pg.K_BACKSPACE,
    "Up": pg.K_w,
    "Right": pg.K_d,
    "Down": pg.K_s,
    "Left": pg.K_a
}
