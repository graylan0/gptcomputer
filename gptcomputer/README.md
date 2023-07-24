# gptcomputer
This Python script is a part of a larger project that uses the GPT-Neo model from the transformers library to interact with a computer interface. The script creates a GUI (Graphical User Interface) using the Tkinter library, and uses the GPT-Neo model to generate responses based on user input. The responses are then used to control the computer.

## Summary

1. **Initialization**: The script starts by importing necessary libraries and modules. It then initializes two instances of the GPT-Neo model and its tokenizer.

2. **AI State Creation**: Two instances of an AIState class are created. This class likely contains the state of the AI, including its current thoughts and actions.

3. **GUI Creation**: A GUI is created using Tkinter. This includes an ASCII art display, a message entry field, an action log, and labels for energy and orb size.

4. **Message Handling**: A function `on_message()` is defined to handle user messages. When a message is entered, the function captures a screenshot, converts it to ASCII art, and generates a prompt for the AI. The AI then generates a response using the GPT-Neo model in a separate thread. The response is used to control the computer and is logged in the action log.

5. **Main Loop**: The script enters the Tkinter main loop, which waits for user interaction.

## Directory structure
```
gptcomputer/
│
├── gptcomputer/
│   ├── __init__.py
│   ├── __main__.py  # This script
│   ├── ai_state.py
│   ├── control_computer.py
│   ├── ai_answer.py
│   └── utils.py
│
├── gptcomputer.egg-info/
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   └── top_level.txt
│
├── build/
│   ├── bdist.win-amd64/
│   └── lib/
│       └── gpt_computer/
│
├── dist/
│   └── gptcomputer-0.1-py3-none-any.whl
│
├── setup.py
└── ai_controls.log
```
