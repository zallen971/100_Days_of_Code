import random
import time
import os
import re
import msvcrt # Windoes-only library
import tkinter as tk
import textwrap



# generates random 50-word paragraph using a text corpus
def generate_paragraph():
    with open(r"C:\Users\zallen\Python_Coding\Typing_Test\text_file.txt", 'r') as f:
        text = f.read()
    words = text.split()
    random.shuffle(words)
    paragraph = []
    prev_word = None
    for word in words:
        if word != prev_word:
            paragraph.append(word)
            prev_word = word
        if len(paragraph) == 50:
            break

    return ' '.join(paragraph)

# cleans up the text
def clean_text(text):
    text = text.lower() # convert to lowercase
    text = text.strip() # remove the extra whitespace
    text = re.sub(r'\s+', ' ', text) # normalize whitespace
    text = re.sub(r'[^\w\s]', '', text) # remove punctuation
    return text

# GUI
class TypingTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.paragraph = generate_paragraph()
        self.cleaned_paragraph = clean_text(self.paragraph)

        # press the start button then begin typing label
        instructions_label = tk.Label(master, text="Press the start button then begin typing. Press Enter to end the test.\n")
        instructions_label.pack()

        # create a frame for buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10) # add padding around the frame

        self.label = tk.Label(master, text=self.cleaned_paragraph, wraplength=450, justify=tk.LEFT)
        self.label.pack()

        self.text_box = tk.Text(master, height=10, width=55, wrap=tk.WORD)
        self.text_box.pack()
        self.text_box.bind('<KeyRelease>', self.check_spelling) # bind key release to check spelling
        self.text_box.bind('<Return>', self.end_test) # bind 'Enter' keyt to end the test


        self.start_button = tk.Button(master, text="Start", command=self.start_test)
        self.start_button.pack(side=tk.LEFT, padx=25, pady=25) # pack start button to the left

        self.restart_button = tk.Button(master, text="Restart", command=self.restart_test)
        self.restart_button.pack(side=tk.RIGHT, padx=25, pady=25) # pack restart button to the right

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()


    def setup_test(self):
        self.paragraph = generate_paragraph()
        self.cleaned_paragraph = clean_text(self.paragraph)

        if hasattr(self, 'label'):
            self.label.config(text=self.cleaned_paragraph)
        else:
            self.label = tk.Label(self.master, text=self.cleaned_paragraph, wraplength=450, justify=tk.LEFT)
            self.label.pack()

        if hasattr(self, 'text_box'):
            self.text_box.delete("1.0", tk.END)
        else:
            self.text_box = tk.Text(self.master, height=10, width=55)
            self.text_box.pack()
            self.text_box.bind('<KeyRelease>', self.check_spelling) # bind key release to check spelling
            self.text_box.bind('<Return>', self.end_test) # bin Enter key to end the test

        self.start_time = None
    
    def start_test(self):
        self.start_time = time.time()
        self.text_box.focus()
        self.start_button.config(state=tk.DISABLED) # disable the start button

    def end_test(self, event):
        end_time = time.time()
        user_input = self.text_box.get("1.0", tk.END).strip() # get the content of the text box

        time_taken = end_time - self.start_time
        if time_taken == 0:
            time_taken = 0.01 # avoid division by zero

        words_per_min = (len(user_input.split()) / time_taken) * 60 # time taken in seconds

        # calculate the number of correctly typed words
        correct_words = 0
        user_words = user_input.split()
        paragraph_words = self.cleaned_paragraph.split()
        for i in range(min(len(user_words), len(paragraph_words))):
            if user_words[i] == paragraph_words[i]:
                correct_words += 1
        
        accuracy = (correct_words / len(paragraph_words)) * 100

        self.result_label.config(text=f"\nYour typing speed is: {words_per_min:.2f} WPM\nYour typing accuracy is: {accuracy:.2f}%")
        return "break"


    def check_spelling(self, event):
        # We only check spelling when the user types a space or punctuation, not every keystroke
        if event.keysym in ('space', 'Return', 'period', 'comma', 'question', 'exclam'):
            # Remove previous misspelled word highlights
            self.text_box.tag_remove('misspelled', '1.0', tk.END)

            # Get the current text input
            user_input = self.text_box.get("1.0", tk.END).strip()
            user_words = user_input.split()  # Split by spaces to get the typed words
            paragraph_words = self.cleaned_paragraph.split()  # Split the reference paragraph into words

            # Iterate through user words and check for misspelled ones
            current_index = '1.0'
            for i, word in enumerate(user_words):
                if i < len(paragraph_words) and word != paragraph_words[i]:
                    # Find the start index of the word
                    start_idx = self.text_box.search(word, current_index, stopindex=tk.END)
                    if start_idx:
                        # Calculate the end index based on the word's length
                        end_idx = self.text_box.index(f"{start_idx} + {len(word)}c")
                        # Tag the misspelled word to highlight it
                        self.text_box.tag_add('misspelled', start_idx, end_idx)

                    # Update the current index to the next word's start position
                    current_index = self.text_box.index(f"{start_idx} + {len(word)}c")

            # Make misspelled words red
            self.text_box.tag_config('misspelled', foreground='red')



    def restart_test(self):
        self.setup_test()
        self.start_button.config(state=tk.NORMAL) # Enable the start button
        self.result_label.config(text="")


# run the typing test
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()