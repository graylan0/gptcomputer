import pyautogui
import ascii_magic

def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return screenshot.size

def convert_image_to_ascii(image_path):
    output = ascii_magic.from_image_path(image_path)
    return ascii_magic.to_terminal(output)
