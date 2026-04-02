import tkinter as tk
import _tkinter
from tkinter import filedialog, ttk, END
from constants import DEFAULT_TIME_1, DEFAULT_TIME_2, DEFAULT_TIME_3, DEFAULT_TIME_4
import json
from path import resource_path

class Config_window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Config Window")

        # Window Setup
        self.window_width = 300
        self.window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
        self.root.attributes('-alpha', 0.97)
        self.root.attributes('-topmost', 1)

        try:
            icon = tk.PhotoImage(file=resource_path("icon.png"))
            self.root.iconphoto(True, icon)
        except _tkinter.TclError:
            print("Error: Couldn't load the icon.")

        # Row/Column Configuration
        # Reduced to 12 rows for a tighter layout
        for i in range(13):
            self.root.rowconfigure(i, weight=1)
        for i in range(3):
            self.root.columnconfigure(i, weight=1)

        # Map display strings to constants for the dropdown
        self.preset_map = {
            f"{DEFAULT_TIME_1[0]}/{DEFAULT_TIME_1[1]}": DEFAULT_TIME_1,
            f"{DEFAULT_TIME_2[0]}/{DEFAULT_TIME_2[1]}": DEFAULT_TIME_2,
            f"{DEFAULT_TIME_3[0]}/{DEFAULT_TIME_3[1]}": DEFAULT_TIME_3,
            f"{DEFAULT_TIME_4[0]}/{DEFAULT_TIME_4[1]}": DEFAULT_TIME_4,
        }

        # Data Loading
        with open(resource_path("config.json"), "r") as file:
            data = json.load(file)
            study_seconds = data.get("study_time", 0)
            rest_seconds = data.get("rest_time", 0)
            self.alarm_path = data.get("alarm", "")

        # UI - Study Time Section
        ttk.Label(self.root, text="Study Time", font=('Consolas', 10, 'bold')).grid(row=0, column=0, columnspan=3)
        
        ttk.Label(self.root, text="Hours:").grid(row=1, column=0, sticky=tk.W, padx=10)
        self.hour_spin_box_study = ttk.Spinbox(self.root, from_=0, to=24)
        self.hour_spin_box_study.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=5)

        ttk.Label(self.root, text="Minutes:").grid(row=2, column=0, sticky=tk.W, padx=10)
        self.minute_spin_box_study = ttk.Spinbox(self.root, from_=0, to=60)
        self.minute_spin_box_study.grid(row=2, column=1, columnspan=2, sticky=tk.EW, padx=5)

        ttk.Label(self.root, text="Seconds:").grid(row=3, column=0, sticky=tk.W, padx=10)
        self.second_spin_box_study = ttk.Spinbox(self.root, from_=0, to=60)
        self.second_spin_box_study.grid(row=3, column=1, columnspan=2, sticky=tk.EW, padx=5)

        # UI - Rest Time Section
        ttk.Label(self.root, text="Rest Time", font=('Consolas', 10, 'bold')).grid(row=4, column=0, columnspan=3, pady=(10, 0))

        ttk.Label(self.root, text="Hours:").grid(row=5, column=0, sticky=tk.W, padx=10)
        self.hour_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=24)
        self.hour_spin_box_rest.grid(row=5, column=1, columnspan=2, sticky=tk.EW, padx=5)

        ttk.Label(self.root, text="Minutes:").grid(row=6, column=0, sticky=tk.W, padx=10)
        self.minute_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=60)
        self.minute_spin_box_rest.grid(row=6, column=1, columnspan=2, sticky=tk.EW, padx=5)

        ttk.Label(self.root, text="Seconds:").grid(row=7, column=0, sticky=tk.W, padx=10)
        self.second_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=60)
        self.second_spin_box_rest.grid(row=7, column=1, columnspan=2, sticky=tk.EW, padx=5)

        # UI - Preset Dropdown
        ttk.Label(self.root, text="Presets:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=(10, 0))
        self.preset_combo = ttk.Combobox(self.root, values=list(self.preset_map.keys()), state="readonly")
        self.preset_combo.grid(row=8, column=1, columnspan=2, sticky=tk.EW, padx=5, pady=(10, 0))
        self.preset_combo.bind("<<ComboboxSelected>>", self.on_preset_changed)

        # UI - Action Buttons
        self.choose_alarm = ttk.Button(self.root, text="Select Alarm Audio", command=self.select_alarm)
        self.choose_alarm.grid(row=9, column=0, columnspan=3, pady=(15, 0), padx=20, sticky=tk.EW)

        self.config_button = ttk.Button(self.root, text="Update Config File", command=self.save_config)
        self.config_button.grid(row=10, column=0, columnspan=3, pady=5, padx=20, sticky=tk.EW)

        # Info Labels
        ttk.Label(self.root, text="After updating, focus main window", font=("Consolas", 7)).grid(row=11, column=0, columnspan=3)
        ttk.Label(self.root, text="and press ENTER to refresh timer", font=("Consolas", 7)).grid(row=12, column=0, columnspan=3)

        # Initialize boxes with current data
        self.fill_boxes(*self.split_seconds(study_seconds), *self.split_seconds(rest_seconds))

    def split_seconds(self, total_seconds):
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return h, m, s

    def fill_boxes(self, h_s, m_s, s_s, h_r, m_r, s_r):
        """Helper to batch update all spinboxes."""
        vals = [h_s, m_s, s_s, h_r, m_r, s_r]
        boxes = [self.hour_spin_box_study, self.minute_spin_box_study, self.second_spin_box_study,
                 self.hour_spin_box_rest, self.minute_spin_box_rest, self.second_spin_box_rest]
        for box, val in zip(boxes, vals):
            box.delete(0, END)
            box.insert(0, int(val))

    def on_preset_changed(self, event):
        """Handles dropdown selection by looking up values in the map."""
        times = self.preset_map.get(self.preset_combo.get())
        if times:
            # times is (study_min, rest_min) from constants
            self.fill_boxes(0, times[0], 0, 0, times[1], 0)

    def select_alarm(self):
        file_path = filedialog.askopenfilename(
            title="Select Alarm",
            initialdir=resource_path("audio", "alarms"),
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )
        if file_path:
            self.alarm_path = file_path

    def save_config(self):
        try:
            s_time = int(self.hour_spin_box_study.get())*3600 + int(self.minute_spin_box_study.get())*60 + int(self.second_spin_box_study.get())
            r_time = int(self.hour_spin_box_rest.get())*3600 + int(self.minute_spin_box_rest.get())*60 + int(self.second_spin_box_rest.get())
            
            # Cap at 24 hours
            s_time = min(s_time, 86400)
            r_time = min(r_time, 86400)

            config_data = {
                "study_time": s_time,
                "rest_time": r_time,
                "alarm": self.alarm_path
            }

            with open(resource_path("config.json"), "w") as outfile:
                json.dump(config_data, outfile, indent=4)
        except ValueError:
            print("Invalid input in time boxes.")

    def show(self):
        self.root.mainloop()