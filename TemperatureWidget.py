from Widget import Widget

class TemperatureWidget(Widget):
    def __init__(self, app):
        self.app = app
        # super().__init__()
    def draw_widget(self, temp, max_temp=100):
        self.app.canvas.delete("all")
        bar_height = 100
        bar_width = 30
        x_offset = 100
        y_offset = 100

        # Draw temperature scale lines and labels
        for i in range(0, max_temp + 1, 10):
            y = bar_height - (i / max_temp) * bar_height + y_offset
            self.app.canvas.create_line(x_offset, y, x_offset + bar_width + 10, y, fill="gray")
            self.app.canvas.create_text(x_offset - 10, y, text=f"{i}°C", anchor="e")

        # Draw bar background
        self.app.canvas.create_rectangle(x_offset, y_offset, x_offset + bar_width, y_offset + bar_height, fill="lightgray", outline="black")

        # Draw filled temperature level
        fill_height = (temp / max_temp) * bar_height
        self.app.canvas.create_rectangle(x_offset, y_offset + bar_height - fill_height,
                                x_offset + bar_width, y_offset + bar_height,
                                fill="red")
        
        # self.after(1000, self.draw_temperature_bar(random.random()))

    def update_widget(self):
        # need to add communication 
        data = self.read_from_file.data_sheet
        self.draw_widget(data[len(data)-1])
        self.after(1000, self.update_temperature)
        
    pass