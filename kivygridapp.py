
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 23:11:09 2021

@author: Vinamra Yadav
"""


import time

from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout


Window.size = (400, 700)


KV = '''

#....

'''



class IncrediblyCrudeClock(Label):
    def update(self, *args):
        self.text = time.asctime()

class IncrediblyCrudeClock1(Label):
    def update(self, *args):
        t = time.gmtime()
        self.text = time.asctime(t)


class TimeApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        layout = MDBoxLayout(orientation='vertical')

        crudeclock1 = IncrediblyCrudeClock()
        Clock.schedule_interval(crudeclock1.update, 1)
        layout.add_widget(crudeclock1)
        layout.add_widget(Button(text='INDIA',
                                 background_color =(0,1,0,1)))


        crudeclock2 = IncrediblyCrudeClock1()
        Clock.schedule_interval(crudeclock2.update, 1)
        layout.add_widget(crudeclock2)
        layout.add_widget(Button(text='LONDON',
                                 background_color =(0, 1, 0, 1)))


        return layout

root = TimeApp()
root.run()

class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name="main_screen"))

        self.main_str = Builder.load_string(helper_string)

    def build(self):
        screen = Screen()
        screen.add_widget(self.main_str)
        return screen


if __name__ == '__main__':
    MainApp().run()
