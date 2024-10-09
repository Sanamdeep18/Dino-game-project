import pyautogui
from PIL import ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Detect birds (above mid height)
    for i in range(250, 300):  # Y-axis range (bird height)
        for j in range(500, 650):  # X-axis range (distance in front of the dino)
            if data[i, j] < 100:  # Obstacle detected
                hit("down")  # Duck to avoid bird
                return

    # Detect cacti (on the ground)
    for i in range(300, 400):  # Y-axis range (ground level)
        for j in range(500, 650):  # X-axis range (distance in front of the dino)
            if data[i, j] < 100:  # Obstacle detected
                hit("up")  # Jump to avoid cactus
                return
    return

if __name__ == "__main__":
    print("Dino game starting in 3 seconds...")
    time.sleep(3)

    while True:
        # Capture screenshot of the game
        image = ImageGrab.grab().convert('L')  # Convert the image to grayscale
        data = image.load()

        isCollide(data)
