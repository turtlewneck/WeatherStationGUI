from customtkinter import *
import tkinter as tk
import threading
from tkdial import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import random
import time
from TemperatureWidget import TemperatureWidget
import math

'''DARK MODE BACKGROUND = gray14'''
'''LIGHT MODE BACKGROUND = gray92'''

class Application(CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        random.seed(5)

        '''INITIALIZE READFILE CLASS'''
        self.read_from_file = ReadFile(self)

        # self.frame = CTkFrame(self)
        # self.frame.pack(expand=True, fill=BOTH)

        self.btn = CTkButton(master=self, text="Toggle mode!", corner_radius=10, command=self.handle_toggle_mode)
        self.btn.place(relx=0.5, rely=0.5, anchor="center")
        print("help ", self.cget("fg_color"))
    

        self.label = CTkLabel(master=self, text="CTkLabel", fg_color="transparent")
        self.label.place(relx=0.1, rely=0.1, anchor=E)
        

        '''INITIALIZATION OF CANVAS'''
        self.canvas = tk.Canvas(self, width=150, height=350)
        self.canvas.pack()
        

        '''READING VALUES FROM FILE'''
        self.read_from_file.read_file()


        '''TEMPERATURE SECTION'''
        '''This is an example usage of temperature class'''
        # temp = TemperatureWidget(self)
        # temp.draw_widget(50)

        self.update_temperature()


        '''WIND SECTION'''
        self.wind_rose = WindRoseCanvas(self, size=300)
        self.wind_rose.pack()


        '''MAIN LOOP - END OF THE PROGRAM'''
        self.mainloop()
        
    
    def handle_toggle_mode(self):
        if self._get_appearance_mode() == "light":
            self._set_appearance_mode("dark")
            self.btn.configure(require_redraw=True, bg_color="gray14")
        else:
            self._set_appearance_mode("light")
            self.btn.configure(require_redraw=True, bg_color="gray92")

    def update_temperature(self):
        temp = random.randint(0, 100)
        data = list(map(int, self.read_from_file.data_sheet))
        # data = self.read_from_file.data_sheet
        print("DATA inside update: ", data)
        # self.draw_temperature_bar(data[len(data)-1])
        self.draw_temperature_bar(temp)
        self.after(1000, self.update_temperature)

    def draw_temperature_bar(self, temp, max_temp=100):
        self.canvas.delete("all")
        bar_height = 300
        bar_width = 30
        x_offset = 60
        y_offset = 20

        # Draw temperature scale lines and labels
        for i in range(0, max_temp + 1, 10):
            y = bar_height - (i / max_temp) * bar_height + y_offset
            self.canvas.create_line(x_offset, y, x_offset + bar_width + 10, y, fill="gray")
            self.canvas.create_text(x_offset - 10, y, text=f"{i}°C", anchor="e")

        # Draw bar background
        self.canvas.create_rectangle(x_offset, y_offset, x_offset + bar_width, y_offset + bar_height, fill="lightgray", outline="black")

        # Draw filled temperature level
        fill_height = (temp / max_temp) * bar_height
        self.canvas.create_rectangle(x_offset, y_offset + bar_height - fill_height,
                                x_offset + bar_width, y_offset + bar_height,
                                fill="red")


class WindRoseCanvas(tk.Canvas):
    def __init__(self, parent, size=200, **kwargs):
        super().__init__(parent, width=size, height=size, bg='white', highlightthickness=0, **kwargs)
        self.size = size
        self.center = size / 2
        self.arrow_length = size * 0.4
        self.draw_base()

    def draw_base(self):
        # Compass lines (N-S, E-W)
        self.create_line(self.center, 0, self.center, self.size, fill='gray')
        self.create_line(0, self.center, self.size, self.center, fill='gray')

        # Direction labels
        font = ("Arial", 10, "bold")
        self.create_text(self.center, 10, text="N", font=font)
        self.create_text(self.center, self.size - 10, text="S", font=font)
        self.create_text(10, self.center, text="W", font=font)
        self.create_text(self.size - 10, self.center, text="E", font=font)

        self.update_direction()

    def draw_arrow(self, degrees: float):
        self.delete("arrow")
        radians = math.radians(degrees - 90)
        x = self.center + self.arrow_length * math.cos(radians)
        y = self.center + self.arrow_length * math.sin(radians)

        self.create_line(
            self.center, self.center, x, y,
            arrow=tk.LAST, fill='blue', width=3, tags="arrow"
        )

    def update_direction(self):
        dir = random.randint(0, 360)
        self.draw_arrow(dir)
        self.after(1000, self.update_direction)

        # Convert to radians and rotate -90° to make 0° = North


class ReadFile():
    def __init__(self, application):
        self.application = application
        self.last_read = 0
        self.iterator = 0
        self.data_sheet = []
    def read_file(self):
        try:
            with open(".\data.txt", "r") as file:
                contents = file.readlines()
                for line in contents:
                    self.data_sheet.append(line)
                    # self.iterator += 1
                    # if self.iterator%2 == 0:
                    #     break 
                    
                print("whatever man: ", self.data_sheet)
                file.close()
        except FileNotFoundError:
            print("File not found")
        self.application.after(5000, self.read_file)

        

class WeatherData:
    def __init__(self):
        self.rain_mm: float | None = None
        self.wind_direction: float | None = None
        self.wind_speed: float | None = None
        self.temperature: float | None = None
        self.humidity: float | None = None
        self.sound_intensity: float | None = None
        self.solar_intensity: float | None = None
    


Application("Weather Station", (600, 800))

# app = CTk()
# app.geometry("600x800")

# set_appearance_mode("dark")

# btn = CTkButton(master=app, text="Click here to get instant retardation", corner_radius=10)
# btn.place(relx=0.5, rely=0.5, anchor="center")

# app.mainloop()


# import customtkinter as ctk
# import random

# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.geometry("300x400")

# # Frame to hold the bar and labels
# frame = ctk.CTkFrame(app)
# frame.pack(pady=20, padx=20)

# # Temperature scale (labels)
# label_frame = ctk.CTkFrame(frame, width=40)
# label_frame.grid(row=0, column=0, sticky="n")

# for i in reversed(range(0, 110, 10)):
#     lbl = ctk.CTkLabel(label_frame, text=f"{i}°", width=40)
#     lbl.pack()

# # Progress bar (vertical)
# progress = ctk.CTkProgressBar(frame, orientation="vertical", height=300, width=20, progress_color="red")
# progress.grid(row=0, column=1, padx=10)

# # Current temperature label
# temp_label = ctk.CTkLabel(app, text="Temperature: 0°C", font=("Arial", 16))
# temp_label.pack(pady=10)

# # Update function
# def update_temperature():
#     temp = random.randint(0, 100)
#     progress.set(temp / 100)
#     temp_label.configure(text=f"Temperature: {temp}°C")
#     app.after(1000, update_temperature)  # Call this again in 1 second

# # Start updating
# update_temperature()

# app.mainloop()