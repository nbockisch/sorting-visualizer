from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
import matplotlib.animation as animation 
import numpy as np
import random
import tkinter as tk
import time

from algorithms import *

class Gui():
    def __init__(self): 
        self.window = None
        self.delay = None # Time to delay between showing sorting steps in sec
        self.playback_i = 0
        self.is_paused = False

        # GUI elements
        self.algos = {
            "Bubble Sort" : Bubble,
            "Merge Sort" : Merge,
            "Quick Sort" : Quick,
            "Insertion Sort" : Insertion,
            "Selection Sort" : Selection
        }
        self.algo_sel = None
        self.algo_menu = None
        self.nums_size = None

        # Plot elements
        self.fig = None
        self.plot = None
        self.bar = None
        self.g_canvas = None

        # Data
        self.nums = random.sample(range(1, 11), 10)
        self.backup = np.copy(self.nums)
        self.algo = None # Holds the sorted array and steps for playback

    def update_graph(self, frame = (Operator.NONE, 0, 0)):
        self.plot.clear()
        self.plot.axis('off')

        # Update data to reflect the current frame
        if (frame[0] == Operator.SWAP):
            self.nums[frame[1]], self.nums[frame[2]] = self.nums[frame[2]], self.nums[frame[1]]
        elif (frame[0] == Operator.INS):
                self.nums[frame[1]] = frame[2]

        # Set colors of the bars to reflect comparison or swapping
        self.bar = self.plot.bar(np.arange(0, len(self.nums), 1), self.nums)
        color = "blue"

        if (frame[0] == Operator.COMP):
            color = "magenta"
        elif (frame[0] == Operator.SWAP or frame[0] == Operator.INS):
            color = "red"

        if (frame[0] == Operator.SWAP or frame[0] == Operator.COMP):
            self.bar.patches[frame[1]].set_color(color)
            self.bar.patches[frame[2]].set_color(color)
        elif (frame[0] == Operator.INS):
            self.bar.patches[frame[1]].set_color(color)

        # Refresh canvas to draw new plot
        self.g_canvas.draw()
        self.g_canvas.flush_events()

    def run_sort(self, *args): 
        self.reset_sort()
        self.algo = self.algos[self.algo_sel.get()](np.copy(self.nums))
        self.algo.sort()

    def play_sort(self):
        if (not self.algo): return
        self.is_paused = False

        while self.playback_i < len(self.algo.frames) and not self.is_paused:
            self.update_graph(self.algo.frames[self.playback_i])
            time.sleep(1 / self.delay.get())
            self.playback_i += 1

    def step_forward(self):
        if (not self.algo): return

        if self.playback_i < len(self.algo.frames):
            self.playback_i += 1
            self.update_graph(self.algo.frames[self.playback_i])

    def step_backward(self):
        if (not self.algo): return

        if self.playback_i > 0:
            self.playback_i -= 1
            self.update_graph(self.algo.frames[self.playback_i])

    def pause_sort(self):
        self.is_paused = True

    def reset_sort(self):
        if (self.algo):
            self.is_paused = True
            self.nums = np.copy(self.backup)
            self.playback_i = 0

            self.update_graph()

    def resize_nums(self, event):
        self.algo = None
        self.nums = random.sample(range(1, self.nums_size.get() + 1), 
                                  self.nums_size.get())
        self.backup = np.copy(self.nums)
        self.playback_i = 0
        self.update_graph()
        self.run_sort()

    # function to create and display the gui
    def start_gui(self):
        rows = 2
        columns = 6

        self.window = tk.Tk()

        self.window.title("Sorting Visualizer")

        # Gui elements
        self.algo_sel = tk.StringVar()
        self.algo_sel.set(list(self.algos.keys())[0])
        self.algo_menu = tk.OptionMenu(self.window, self.algo_sel, *self.algos,
                                       command=self.run_sort)
        self.run_sort() # Enable playing sort from the start

        self.nums_size = tk.IntVar(self.window)
        nums_slider = tk.Scale(self.window, from_=10, to=100, label="Size",
                               orient="horizontal", variable=self.nums_size, 
                               command=self.resize_nums)

        self.delay = tk.DoubleVar(self.window)
        delay_slider = tk.Scale(self.window, from_=1, to=1000, 
                                label="Speed", resolution=0.01, 
                                orient="horizontal", variable=self.delay)

        play_btn = tk.Button(self.window, text="Play Sort",
                                  command = self.play_sort)

        pause_btn = tk.Button(self.window, text="Pause Sort",
                                  command = self.pause_sort)

        reset_btn = tk.Button(self.window, text="Reset Sort",
                                  command = self.reset_sort)

        # Embed the graph in the window
        self.fig = Figure(figsize = (5, 5), dpi=100)
        self.plot = self.fig.add_subplot(1,1,1)
        self.plot.axis('off')
        self.plot.bar(np.arange(0, len(self.nums), 1), self.nums)
        self.g_canvas = FigureCanvasTkAgg(self.fig, master = self.window)
        self.g_canvas.draw()

        # Make gui elements resize with the window
        for i in range(columns):
            self.window.grid_columnconfigure(i, weight=1)
            
        for i in range(rows):
            self.window.grid_rowconfigure(i, weight=1)

        # Display all the gui elements in the window
        self.algo_menu.grid(row=0, column=0, sticky="NSEW")
        nums_slider.grid(row=0, column=1, sticky="NSEW")
        delay_slider.grid(row=0, column=2, sticky="NSEW")
        play_btn.grid(row=0, column=3, sticky="NSEW")
        pause_btn.grid(row=0, column=4, sticky="NSEW")
        reset_btn.grid(row=0, column=5, sticky="NSEW")
        self.g_canvas.get_tk_widget().grid(row=1, column=0, columnspan=6, sticky="NSEW")

        self.window.mainloop()
