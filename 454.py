import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TEXTINPUT, TextInput
from kivy.uix.button import Button

class  childApp(GridLayout):
    def __init__(self,*kwargs):
          super(childApp, self),__init__ ()
          self.cold = 2
          self.add_widget(label(text = "Student Name"))
          self.s_name= TextInput()
          self.app_widget_(self.s_name)

          self.add_widget_(label(text = "Student Marks"))
          self.s_marks= TextInput()
          self.app_widget_(self.s_marks)

          