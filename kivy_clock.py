from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TestWidget(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        
        return TestWidget()

    
if __name__ == "__main__":
    TestApp().run()