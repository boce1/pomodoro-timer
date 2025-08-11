from .default_audio import DEFAULT_ALARM_PATH
from path import resource_path

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
YELLOW = (255,255,50)

FPS = 60

IMAGE_SIZE = (5 * HEIGHT // 12, HEIGHT // 2)

BUTTON_WIDTH = WIDTH // 15
BUTTON_HEIGHT = BUTTON_WIDTH

SPRITES = {
    "sonic" : {
        "running" : resource_path("visuals", "sonic", "running_sonic"),
        "waiting" : resource_path("visuals", "sonic", "waiting_sonic")
    },
    "shadow" : {
        "running" : resource_path("visuals", "shadow", "running_shadow"),
        "waiting" : resource_path("visuals", "shadow", "waiting_shadow")
    },
    "tails" : {
        "running" : resource_path("visuals", "tails", "running_tails"),
        "waiting" : resource_path("visuals", "tails", "waiting_tails")
    },
    "super_sonic" : {
        "running" : resource_path("visuals", "super_sonic", "running_super_sonic"),
        "waiting" : resource_path("visuals", "super_sonic", "waiting_super_sonic")
    }
}

DEFAULT_TIME_1 = (30, 15)
DEFAULT_TIME_2 = (40, 15)
DEFAULT_TIME_3 = (40, 20)