import customtkinter
from abc import ABC, abstractmethod
# Interface?

class Widget(ABC):

    @abstractmethod
    def draw_widget(self):
        pass

    @abstractmethod
    def update_widget(self):
        pass