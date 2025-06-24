WIDTH = 400
HEIGHT = 300

INFO_WIDTH = int(HEIGHT // 1.5)
INFO_HEIGHT = INFO_WIDTH
GAP = INFO_HEIGHT // 60
KEY_WIDTH = INFO_WIDTH // 8
KEY_HEIGHT = KEY_WIDTH
SPACE_KEY_WIDTH = 3 * KEY_WIDTH
ENTER_KEY_WIDTH = 2 * KEY_WIDTH
ENTER_KEY_HIGHT = 2 * KEY_HEIGHT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (22, 65, 221)
RED = (255, 0, 0)
GRAY = (150, 150, 150)
ORANGE = (255, 165, 0)

FPS = 60

IMAGE_SIZE = (5 * HEIGHT // 12, HEIGHT // 2)

BUTTON_WIDTH = WIDTH // 15
BUTTON_HEIGHT = BUTTON_WIDTH

SPRITES = {
    "sonic" : {
        "running" : ".//visuals//sonic//running_sonic",
        "waiting" : ".//visuals//sonic//waiting_sonic"
    },
    "shadow" : {
        "running" : ".//visuals//shadow//running_shadow",
        "waiting" : ".//visuals//shadow//waiting_shadow"
    },
    "tails" : {
        "running" : ".//visuals//tails//running_tails",
        "waiting" : ".//visuals//tails//waiting_tails"
    }
}