import tkinter as tk
from tkinter import filedialog, ttk, END
from constants import DEFAULT_TIME_1, DEFAULT_TIME_2, DEFAULT_TIME_3
import json

class Config_window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Config Window")

        self.window_width = 300
        self.window_height = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
        #self.root.configure(bg='white')

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
        self.root.rowconfigure(10, weight=1)
        self.root.rowconfigure(11, weight=1)
        self.root.rowconfigure(12, weight=1)
        self.root.rowconfigure(13, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
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
        study_label = ttk.Label(self.root, text="Study time")
        study_label.grid(column=0, row=0, padx=5, pady=0, columnspan=3)

        hour_label = ttk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=0)

        self.hour_spin_box_study = ttk.Spinbox(self.root, from_=0, to=24)
        self.hour_spin_box_study.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=0, columnspan=2)

        # minutes
        minute_label = ttk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=0)

        self.minute_spin_box_study = ttk.Spinbox(self.root, from_=0, to=60)
        self.minute_spin_box_study.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=0, columnspan=2)

        # seconds
        seconds_label = ttk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=0)

        self.second_spin_box_study = ttk.Spinbox(self.root, from_=0, to=60)
        self.second_spin_box_study.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=0, columnspan=2)
        # # #

        # rest boxes
        rest_label = ttk.Label(self.root, text="Rest time")
        rest_label.grid(column=0, row=5, padx=5, pady=0, columnspan=3)

        hour_label = ttk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=0)

        self.hour_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=24)
        self.hour_spin_box_rest.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=0, columnspan=2)

        # minutes
        minute_label = ttk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=0)

        self.minute_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=60)
        self.minute_spin_box_rest.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=0, columnspan=2)

        # seconds
        seconds_label = ttk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=8, sticky=tk.EW, padx=5, pady=0)

        self.second_spin_box_rest = ttk.Spinbox(self.root, from_=0, to=60)
        self.second_spin_box_rest.grid(column=1, row=8, sticky=tk.EW, padx=5, pady=0, columnspan=2)
        # # #


        # time picker
        self.button_30_15 = ttk.Button(self.root, text=f"{DEFAULT_TIME_1[0]}/{DEFAULT_TIME_1[1]}", width=10, command=self.change_time_1)
        self.button_30_15.grid(column=0, row=10, padx=0, pady=2)
        self.button_40_15 = ttk.Button(self.root, text=f"{DEFAULT_TIME_2[0]}/{DEFAULT_TIME_2[1]}", width=10, command=self.change_time_2)
        self.button_40_15.grid(column=1, row=10, padx=0, pady=2)
        self.button_40_20 = ttk.Button(self.root, text=f"{DEFAULT_TIME_3[0]}/{DEFAULT_TIME_3[1]}", width=10, command=self.change_time_3)
        self.button_40_20.grid(column=2, row=10, padx=0, pady=2)
        # # #

        self.choose_alarm = ttk.Button(self.root, text="Select alarm", command=self.select_alarm, width=17)
        self.choose_alarm.grid(column=0, row=12, padx=5, pady=0, columnspan=3)

        self.config_button = ttk.Button(self.root, text="Update", command=self.change_config_button_clicked, width=17)
        self.config_button.grid(column=0, row=13, padx=5, pady=0, columnspan=3)

        self.insert_time_in_cels_when_open(h_study, m_study, s_study, h_rest, m_rest, s_rest)

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

    def change_time(self, minutes_study, munites_rest):
        self.hour_spin_box_study.delete(0, END)
        self.hour_spin_box_study.insert(0, 0)
        self.minute_spin_box_study.delete(0, END)
        self.minute_spin_box_study.insert(0, minutes_study)
        self.second_spin_box_study.delete(0, END)
        self.second_spin_box_study.insert(0, 0)

        self.hour_spin_box_rest.delete(0, END)
        self.hour_spin_box_rest.insert(0, 0)
        self.minute_spin_box_rest.delete(0, END)
        self.minute_spin_box_rest.insert(0, munites_rest)
        self.second_spin_box_rest.delete(0, END)
        self.second_spin_box_rest.insert(0, 0)

    def change_time_1(self):
        self.change_time(*DEFAULT_TIME_1)
    
    def change_time_2(self):
        self.change_time(*DEFAULT_TIME_2)

    def change_time_3(self):
        self.change_time(*DEFAULT_TIME_3)

    def select_alarm(self):
        file_path = filedialog.askopenfilename(title="Select Alarm",
                                    initialdir="./audio/alarms", 
                                    filetypes=[("All Files", ("*.mp3", "*.wav")), ("MP3", ("*.mp3")), ("WAV", "*.wav*")])
        if file_path:
            self.alarm_path = file_path
        # self.alarm_path cant be None except audio/alarms is empty
        # save the old alarm_path if no audio is selected

    def insert_time_in_cels_when_open(self, h_study, m_study, s_study, h_rest, m_rest, s_rest):
        self.hour_spin_box_study.delete(0, END)
        self.hour_spin_box_study.insert(0, h_study)
        self.minute_spin_box_study.delete(0, END)
        self.minute_spin_box_study.insert(0, m_study)  
        self.second_spin_box_study.delete(0, END)
        self.second_spin_box_study.insert(0, s_study) 

        self.hour_spin_box_rest.delete(0, END)
        self.hour_spin_box_rest.insert(0, h_rest)
        self.minute_spin_box_rest.delete(0, END)
        self.minute_spin_box_rest.insert(0, m_rest)  
        self.second_spin_box_rest.delete(0, END)
        self.second_spin_box_rest.insert(0, s_rest)         

    def show(self):
        self.root.mainloop()