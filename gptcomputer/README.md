# gptcomputer
This Python script is a part of a larger project that uses the GPT-Neo model from the transformers library to interact with a computer interface. The script creates a GUI (Graphical User Interface) using the Tkinter library, and uses the GPT-Neo model to generate responses based on user input. The responses are then used to control the computer.

## Summary

1. **Initialization**: The script starts by importing necessary libraries and modules. It then initializes two instances of the GPT-Neo model and its tokenizer.

2. **AI State Creation**: Two instances of an AIState class are created. This class likely contains the state of the AI, including its current thoughts and actions.

3. **GUI Creation**: A GUI is created using Tkinter. This includes an ASCII art display, a message entry field, an action log, and labels for energy and orb size.

4. **Message Handling**: A function `on_message()` is defined to handle user messages. When a message is entered, the function captures a screenshot, converts it to ASCII art, and generates a prompt for the AI. The AI then generates a response using the GPT-Neo model in a separate thread. The response is used to control the computer and is logged in the action log.

5. **Main Loop**: The script enters the Tkinter main loop, which waits for user interaction.


## Installation

To install this Python package, you would typically follow these steps:

1. **Clone the repository**: If the package is hosted on a version control system like GitHub, you would first clone the repository to your local machine. You can do this with the command `git clone <repository-url>`, replacing `<repository-url>` with the URL of the repository.

2. **Navigate to the directory**: Use the command `cd <directory-name>` to navigate to the directory containing the setup.py file. In this case, it would be `cd gpt_computer`.

3. **Create a virtual environment (optional)**: It's often a good idea to create a virtual environment when installing Python packages to avoid conflicts with other packages. You can do this with the following commands:

   - `python3 -m venv env` to create the virtual environment. Replace `env` with the name you want to give to the environment.
   - `source env/bin/activate` (on Unix or MacOS) or `.\env\Scripts\activate` (on Windows) to activate the environment.

4. **Install the package**: Use the command `pip install .` to install the package. The `.` tells pip to look for the setup.py file in the current directory and install the package defined by it.

5. **Run the package**: After installation, you should be able to run the package using the command defined in the setup.py file. In this case, it would be `gptcomputer`.

Please note that this package requires Python 3 and pip, the Python package installer. If you don't have these installed, you will need to install them first. Also, the package seems to depend on the transformers library, which requires PyTorch or TensorFlow. Make sure you have one of these installed as well.

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
