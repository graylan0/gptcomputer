import pyautogui
import logging

def control_computer(action):
    global energy, orb_size
    try:
        if action.startswith('move_mouse'):
            x, y = map(int, action.split()[1:])  # Extract the coordinates from the action string
            pyautogui.moveTo(x, y)
            logging.info(f'Moved mouse to ({x}, {y})')
            energy = '#800080'  # Purple
            orb_size = 'XX'  # Small orb
        # Handle other actions...
    except Exception as e:
        logging.error(f'Error performing action: {e}')
