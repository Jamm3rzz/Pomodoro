import time
from pygame import mixer
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

BG_COLOR = "#0b0f1a" # Full caps names for signifying the variable won't change values a "constant"
TEXT_COLOR = "#33ffff" # Snake case for variables ssss LMAOO
HIGHLIGHT_COLOR = "#aa11ff"
ACCENT_COLOR = "#FFA500"

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
        self.root.title("Quantime")
        self.root.geometry("600x400")
        self.root.configure(bg="black") # Just a base color...

        icon = tk.PhotoImage(file=ICON_PATH)

        #self.background_label = tk.Label(self.root, image=bg_image)
        #self.background_label.image = bg_image
        #self.background_label.place(x=-2, y=-2) # Need to put -2...?

        self.root.iconphoto(False, icon)

    def _setup_widgets(self) -> None: # I decided to not use grid & just lock window size & place these bc it looked awful & bothered me.
        canvas = tk.Canvas(self.root, bg="black", highlightthickness=0, bd=0)

        self.time_work_entry = tk.Entry(canvas, 
            background=BG_COLOR, 
            foreground=TEXT_COLOR, 
            border=0,
            font=("Helvetica", 9, "italic")
            )
        self.time_work_entry.insert(END, "Work time")
        self.time_play_entry = tk.Entry(canvas,
            background=BG_COLOR, 
            foreground=TEXT_COLOR, 
            border=0,
            font=("Helvetica", 9, "italic")
            )
        self.time_play_entry.insert(END, "Play time")

        self.progress_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            mode="determinate",
            length=300,
        )

        start_button = tk.Button(
            self.root,
            text="Start",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            command=lambda: self.start_timer(0),
            highlightthickness=0,
            border=0,
            font=("Helvetica", 9, "italic")
        )

        bg = Image.open(BACKGROUND_IMAGE_PATH).resize((600, 400))
        bg_image = ImageTk.PhotoImage(bg)
        canvas.bg_image = bg_image

        # This is where I'm actually placing everything!
        # Also I'll be moving all of these bc IK my app looks like ass rn... but I just taught myself git & it's 2am gimme a break.
        canvas.pack(fill="both", expand=True)
        canvas.create_image(300, 200, image=bg_image)
        canvas.create_text(300, 50, text="Quantime", font=("Helvetica", 25, "bold", "italic"), fill=TEXT_COLOR)
        self._rounded_rect(110, 280, 500, 320, canvas=canvas, radius=45, fill=BG_COLOR)
        canvas.create_window(130, 300, window=start_button)
        canvas.create_window(300, 150, window=self.time_work_entry)
        canvas.create_window(300, 200, window=self.time_play_entry)
        canvas.create_window(300, 300, window=self.progress_bar)

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

    def _rounded_rect(self, x1: int, y1: int, x2: int, y2: int, canvas, radius=25, **kwargs) -> tk.Canvas.create_polygon: # Next time i'm using pyqt6.
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

def main() -> None:
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()