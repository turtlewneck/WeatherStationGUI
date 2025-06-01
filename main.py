from customtkinter import *
import tkinter as tk
import threading
from tkdial import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import random
import time
from TemperatureWidget import TemperatureWidget

'''DARK MODE BACKGROUND = gray14'''
'''LIGHT MODE BACKGROUND = gray92'''

class Application(CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        random.seed(5)
        # self.place_bar()


        self.read_from_file = ReadFile(self)

        # self.frame = CTkFrame(self)
        # self.frame.pack(expand=True, fill=BOTH)

        self.btn = CTkButton(master=self, text="Toggle mode!", corner_radius=10, command=self.handle_toggle_mode)
        self.btn.place(relx=0.5, rely=0.5, anchor="center")
        print("GOWNO ", self.cget("fg_color"))

        self.dial = Dial(master=self, unit_length=8)
        self.dial.place(relx=0.1, rely=0.7, anchor=CENTER)


        bar = tb.Progressbar(master=self, bootstyle="danger-striped", length=300, maximum=100)
        bar.pack(pady=20)
        bar['value'] = 30 


        self.label = CTkLabel(master=self, text="CTkLabel", fg_color="transparent")
        self.label.place(relx=0.6, rely=0.1, anchor=E)

        # tempereature bar
        
        bar = CTkScrollbar(master=self, )
        bar.place(relx=0.4, rely=0.8, anchor=CENTER)
        
        # self.temperature_box = CTkSlider(master=self )
        # self.temperature_box.place(relx=0.1, rely=0.1, anchor=CENTER)
        self.canvas = tk.Canvas(self, width=150, height=350)
        self.canvas.pack()
        
        self.read_from_file.read_file()

        # works
        temp = TemperatureWidget(self)
        temp.draw_widget(50)

        self.update_temperature()
        # self.draw_temperature_bar(random.random())
        # while True:
        
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
        data = self.read_from_file.data_sheet
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
        
        # self.after(1000, self.draw_temperature_bar(random.random()))
        



class ReadFile():
    def __init__(self, application):
        self.application = application
        self.last_read = 0
        self.iterator = 0
        self.data_sheet = []
    def read_file(self):
        try:
            with open(".\data.txt", "r") as file:
                contents = file.read()
                for line in contents:
                    self.data_sheet.append(int(line))
                    self.iterator += 1
                    if self.iterator%2 == 0:
                        break 
                    
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
    


Application("dupa", (600, 800))

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