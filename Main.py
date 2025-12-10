import time
from pygame import mixer
import tkinter as tk
from tkinter import ttk
from tkinter import *

BG_COLOR = "#11bbdd" # Full caps names for signifying the variable won't change values a "constant"
TEXT_COLOR = "#002233" # Snake case for variables ssss LMAOO
HIGHLIGHT_COLOR = "#33ffff"

AUDIO_PATH = r"C:\Users\James\Documents\Mikubot\.venv\Include\Assets\taco-bell-bong-sfx.mp3"
BACKGROUND_IMAGE_PATH = r"Assets\Untitled design.png"
ICON_PATH = r"Assets\taco.png"

class PomodoroApp(): # Camel Case class names (I like camel case more than snake but snake is more readable </3)
    def __init__(self, root: tk.Tk):
        self.root = root

        self.elapsed = 0
        self.is_wait_time = False

        self._setup_audio() # Underscores before names to signal that the func is not meant for use outside class.
        self._setup_window() # Also snake case functions
        self._setup_widgets()

    def _setup_audio(self) -> None: # Already knew about specifying variables & return types :)
        mixer.init()
        mixer.music.load(AUDIO_PATH)

    def _setup_window(self) -> None: # Keep function names lowercase
        self.root.title("Pomodoro")
        self.root.geometry("600x400")

        bg_image = tk.PhotoImage(file=BACKGROUND_IMAGE_PATH)
        icon = tk.PhotoImage(file=ICON_PATH)

        self.background_label = tk.Label(self.root, image=bg_image)
        self.background_label.image = bg_image
        self.background_label.place(x=-2, y=-2) # Need to put -2...?

        self.root.iconphoto(False, icon)

    def _setup_widgets(self) -> None: # I decided to not use grid & just lock window size & place these bc it looked awful & bothered me.
        self.time_work_entry = ttk.Entry(self.root)
        self.time_play_entry = ttk.Entry(self.root)

        self.progress_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            mode="determinate",
            length=300
        )

        start_button = tk.Button(
            self.root,
            text="Start",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            command=lambda: self.start_timer(0)
        )

        # This is where I'm actually placing everything!
        # Also I'll be moving all of these bc IK my app looks like ass rn... but I just taught myself git & it's 2am gimme a break.
        self.time_work_entry.place(x=200, y=150)
        self.time_play_entry.place(x=200, y=200)
        start_button.place(x=260, y=250)
        self.progress_bar.place(x=150, y=300)

    def start_timer(self, remaining_seconds: int) -> None: # See? External function not internal :D no underscore in front good job James!!! 
        """Main timer loop, called every second using Tkinter's scheduler.""" # Use these to explain External function's use <3
        if remaining_seconds <= 0:
            self._cycle_phase()
            return

        self.elapsed += 1
        self.progress_bar["value"] = self.elapsed

        # Schedule next second
        self.root.after(
            1000,
            lambda: self.start_timer(remaining_seconds - 1)
        )
    
    def _cycle_phase(self) -> None:
        """Switch between Work and Play periods and restart timer."""
        self.elapsed = 0
        mixer.music.play()

        if self.is_wait_time:
            # Play time segment
            seconds = int(self.time_play_entry.get()) * 60
            self.is_wait_time = False
        else:
            # Work segment
            seconds = int(self.time_work_entry.get()) * 60
            self.is_wait_time = True

        self.progress_bar["maximum"] = seconds
        self.progress_bar["value"] = 0
        self.start_timer(seconds)

def main() -> None:
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()