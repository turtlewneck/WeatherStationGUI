from customtkinter import *
import threading

'''DARK MODE BACKGROUND = gray14'''
'''LIGHT MODE BACKGROUND = gray92'''

class Application(CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # self.frame = CTkFrame(self)
        # self.frame.pack(expand=True, fill=BOTH)

        self.btn = CTkButton(master=self, text="Toggle mode!", corner_radius=10, command=self.handle_toggle_mode)
        self.btn.place(relx=0.5, rely=0.5, anchor="center")
        print("GOWNO ", self.cget("fg_color"))

        self.mainloop()
    
    def handle_toggle_mode(self):
        if self._get_appearance_mode() == "light":
            self._set_appearance_mode("dark")
            self.btn.configure(require_redraw=True, bg_color="gray14")
        else:
            self._set_appearance_mode("light")
            self.btn.configure(require_redraw=True, bg_color="gray92")


class ReadFile():
    def __init__(self):
        pass
    # def set_mode(self):
        

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