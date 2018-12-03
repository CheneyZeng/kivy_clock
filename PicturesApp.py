
import os
os.environ['KIVY_GL_BACKEND']='angle_sdl2'

from kivy import Config
Config.set('graphics','multisamples','0')
import kivy
kivy.require('1.9.1')

import glob
import webbrowser

from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)
    


class MyImage(ButtonBehavior, Image):        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            webbrowser.open(App.get_running_app().web)
    
class PicturesApp(App):
    folder = StringProperty()
    web = StringProperty()

    def build(self):

        # the root is created in pictures.kv
        root = self.root
               
        # get any files into images directory
        curdir = self.folder
        for filename in glob.glob(curdir):
            try:
                # load the image
                picture = Picture(source=filename, rotation=randint(-30, 30))
                # add to the main field
                root.add_widget(picture)
            except Exception as e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)

                
    def on_pause(self):
        return True

    
        
#if __name__ == '__main__':
    #PicturesApp(folder = 'images/*.png', web = 'https://www.baidu.com/').run()
