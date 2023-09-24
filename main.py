from api import process_file
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, Style

def main():

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])

    print(Style.BRIGHT + Fore.WHITE + "Selected file: ", file_path + Style.RESET_ALL)

    input1 = input(Style.BRIGHT + Fore.WHITE + "Press Enter to continue, or any text + Enter to cancel: " + Style.RESET_ALL)

    audio_file = open(file_path, "rb")

    if input1 != "":
        print(Fore.RED + "Canceled!" + Style.RESET_ALL)
        exit()

    print(Style.BRIGHT + Fore.WHITE + "Prompt guide: https://platform.openai.com/docs/guides/speech-to-text/prompting" + Style.RESET_ALL)
    prompt = input(Style.BRIGHT + Fore.WHITE + "(Optional) Input a prompt for the transcription: " + Style.RESET_ALL)

    print(Style.BRIGHT + Fore.CYAN + "Processing file:")
    print(file_path)

    if prompt != "":
        print("with prompt:" + Style.RESET_ALL)
        print(prompt + Style.RESET_ALL)
    else:
        print("with no prompt." + Style.RESET_ALL)

    final_summary = process_file(audio_file, prompt)

    print(Style.RESET_ALL + "\nFinal Summary:\n")
    print(final_summary)



if __name__ == "__main__":
    main()

