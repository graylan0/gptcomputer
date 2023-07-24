import tkinter as tk
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import threading
import logging
import concurrent.futures

from .ai_state import AIState
from .control_computer import control_computer
from .ai_answer import AI_answer
from .utils import capture_screenshot, convert_image_to_ascii

def main():
    # Initialize AI models and tokenizer
    model1 = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-125M')
    tokenizer1 = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-125M')

    model2 = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-125M')
    tokenizer2 = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-125M')

    tokenizer1.add_special_tokens({'pad_token': '[PAD]'})
    model1.config.pad_token_id = tokenizer1.pad_token_id
    model1.cuda()

    tokenizer2.add_special_tokens({'pad_token': '[PAD]'})
    model2.config.pad_token_id = tokenizer2.pad_token_id
    model2.cuda()

    time_limit = 50
    max_length = 1889

    logging.basicConfig(filename='ai_controls.log', level=logging.INFO)

    # Create instances of AIState for each model
    ai_state1 = AIState()
    ai_state2 = AIState()

    # Create the Tkinter GUI
    root = tk.Tk()
    root.configure(background='black')

    ascii_display_label = tk.Label(root, text="ASCII Art Display", bg="black", fg="green")
    ascii_display_label.pack()
    ascii_display = tk.Text(root, height=20, width=80, bg="black", fg="green")
    ascii_display.pack()

    message_label = tk.Label(root, text="Enter Message", bg="black", fg="green")
    message_label.pack()
    message = tk.StringVar()
    entry = tk.Entry(root, textvariable=message, bg="black", fg="green")
    entry.pack()

    action_log_label = tk.Label(root, text="Action Log", bg="black", fg="green")
    action_log_label.pack()
    action_log = tk.Text(root, height=10, width=80, bg="black", fg="green")
    action_log.pack()

    def on_message():
        # Read previous thoughts from thoughts.txt
        try:
            with open('thoughts.txt', 'r') as f:
                prev_thoughts = f.read().strip()
        except FileNotFoundError:
            with open('thoughts.txt', 'w') as f:
                f.write('')
            prev_thoughts = ''

        screenshot_size = capture_screenshot()
        ascii_art = convert_image_to_ascii("screenshot.png")

        ascii_display.delete(1.0, tk.END)
        ascii_display.insert(tk.END, ascii_art)

        boot_prompt = "This is a computer. You can interact with it by moving the mouse, clicking, typing, etc."
        init_prompt = "Here is the current state of the computer: " + ascii_art + ". The screen resolution is: " + str(screenshot_size)
        activity_prompt = "You have completed " + str(time_limit) + " cycles. Your previous thoughts were: " + prev_thoughts + ". The new message is: " + message.get()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(AI_answer, model1, tokenizer1, ai_state1, boot_prompt, init_prompt, activity_prompt, 1000)
            future2 = executor.submit(AI_answer, model2, tokenizer2, ai_state2, boot_prompt, init_prompt, activity_prompt, 1000)

            gpt_output1 = future1.result()
            gpt_output2 = future2.result()

        control_computer(gpt_output1)
        control_computer(gpt_output2)

        # Write current thoughts to thoughts.txt
        with open('thoughts.txt', 'w') as f:
            f.write(prev_thoughts + ' ' + gpt_output1 + ' ' + gpt_output2)

        action_log.insert(tk.END, gpt_output1 + '\n')
        action_log.insert(tk.END, gpt_output2 + '\n')

    button = tk.Button(root, text="Send", command=on_message, bg="black", fg="green")
    button.pack()

    energy = '#008000'  # Green
    orb_size = 'XXX'  # Medium orb
    energy_label = tk.Label(root, text="Energy:", bg="black", fg=energy)
    energy_label.pack()

    orb_size_label = tk.Label(root, text="Orb Size: " + orb_size, bg="black", fg="green")
    orb_size_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
