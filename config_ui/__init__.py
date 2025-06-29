import tkinter as tk
from tkinter import filedialog
import json

class Config_window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Config Window")

        self.window_width = 250
        self.window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)

        #self.root.attributes('-alpha', 0.95)
        self.root.attributes('-topmost', 1)

        self.root.iconbitmap('./icon.ico')

        # rows and columns
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=1)
        self.root.rowconfigure(8, weight=1)
        self.root.rowconfigure(9, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        # # #

        # read from the config file
        with open("./config.json", "r") as file:
            content = file.read()
            data = json.loads(content)

            study_seconds = data["study_time"]
            rest_seconds = data["rest_time"]
            self.alarm_path = data["alarm"] # default alarm path 
        
        h_study = study_seconds // 3600
        m_study = (study_seconds - h_study * 3600) // 60
        s_study = study_seconds - h_study * 3600 - m_study * 60
        h_rest = rest_seconds // 3600
        m_rest = (rest_seconds - h_rest * 3600) // 60
        s_rest = rest_seconds - h_rest * 3600 - m_rest * 60
        # # # 

        # study boxes
        # hour
        study_label = tk.Label(self.root, text="Study time")
        study_label.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

        hour_label = tk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=0)

        hour_current_value = tk.StringVar(value=h_study)
        self.hour_spin_box_study = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        self.hour_spin_box_study.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=0)

        # minutes
        minute_label = tk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=0)

        minute_current_value = tk.StringVar(value=m_study)
        self.minute_spin_box_study = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        self.minute_spin_box_study.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=0)

        # seconds
        seconds_label = tk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=0)

        second_current_value = tk.StringVar(value=s_study)
        self.second_spin_box_study = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        self.second_spin_box_study.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=0)
        # # #

        # rest boxes
        rest_label = tk.Label(self.root, text="Rest time")
        rest_label.grid(column=0, row=4, padx=5, pady=5, columnspan=2)

        hour_label = tk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=0)

        hour_current_value = tk.StringVar(value=h_rest)
        self.hour_spin_box_rest = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        self.hour_spin_box_rest.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=0)

        # minutes
        minute_label = tk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=0)

        minute_current_value = tk.StringVar(value=m_rest)
        self.minute_spin_box_rest = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        self.minute_spin_box_rest.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=0)

        # seconds
        seconds_label = tk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=0)

        second_current_value = tk.StringVar(value=s_rest)
        self.second_spin_box_rest = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        self.second_spin_box_rest.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=0)
        # # #

        self.choose_alarm = tk.Button(self.root, text="Select alarm", command=self.select_alarm)
        self.choose_alarm.grid(column=0, row=8, padx=5, pady=5, columnspan=2)

        self.config_button = tk.Button(self.root, text="Update Config File", command=self.change_config_button_clicked)
        self.config_button.grid(column=0, row=9, padx=5, pady=5, columnspan=2)

    def change_config_button_clicked(self):
        try:
            study_hours = int(self.hour_spin_box_study.get())
            study_minutes = int(self.minute_spin_box_study.get())
            study_seconds = int(self.second_spin_box_study.get())

            study_time = study_hours * 3600 + study_minutes * 60 + study_seconds

            if study_time > 24 * 3600:
                study_time = 24 * 3600
        except (KeyError, TypeError, ValueError):
            study_time = 0
        
        try:
            rest_hours = int(self.hour_spin_box_rest.get())
            rest_minutes = int(self.minute_spin_box_rest.get())
            rest_seconds = int(self.second_spin_box_rest.get())

            rest_time = rest_hours * 3600 + rest_minutes * 60 + rest_seconds

            if rest_time > 24 * 3600:
                rest_time =  24 * 3600
        except (KeyError, TypeError, ValueError):
            rest_time = 0      

        dict_time = {
            "study_time" : study_time,
            "rest_time" : rest_time,
            "alarm" : self.alarm_path
        }

        with open("config.json", "w") as outfile:
            json.dump(dict_time, outfile)

    def select_alarm(self):
        file_path = filedialog.askopenfilename(title="Select Alarm",
                                    initialdir="./audio/alarms", 
                                    filetypes=[("All Files", ("*.mp3", "*.wav")), ("MP3", ("*.mp3")), ("WAV", "*.wav*")])
        self.alarm_path = file_path

    def show(self):
        self.root.mainloop()