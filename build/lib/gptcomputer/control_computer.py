import pyautogui
import pyautogui

def control_computer(gpt_output):
    actions = gpt_output.split('\n')
    for action in actions:
        if action.startswith('Type:'):
            text = action[5:].strip()
            pyautogui.write(text)
        elif action.startswith('Move mouse to:'):
            coords = action[14:].strip().split(',')
            x = int(coords[0].strip())
            y = int(coords[1].strip())
            pyautogui.moveTo(x, y)
        elif action.startswith('Click mouse at:'):
            coords = action[15:].strip().split(',')
            x = int(coords[0].strip())
            y = int(coords[1].strip())
            pyautogui.click(x, y)
