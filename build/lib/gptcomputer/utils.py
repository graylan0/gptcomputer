import pyautogui
import ascii_magic
from ascii_magic import AsciiArt
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return screenshot.size

def convert_image_to_ascii(image_path):
    output = ascii_magic.from_image_path(image_path)
    return ascii_magic.to_terminal(output)

def convert_image_to_ascii(image_path):
    my_art = AsciiArt.from_image(image_path)
    ascii_art = my_art.to_terminal()
    return ascii_art