from toast.scene_graph import Scene
from toast.bitmap_font import BitmapFont
from toast.text import Text
from toast.resource_loader import ResourceLoader

from examples.demo_game import DemoGame

class NewScene(Scene):
    def __init__(self):
        super(NewScene, self).__init__()
        
        # Read the alphabet string from a file.
        alphaArray = open('Data\\anomaly.dat','r').readline()
        # Define the font dimensions
        fontDimension = (32,32)
        # Create bitmap font object
        font = BitmapFont(ResourceLoader.load('Data\\anomaly.png'), fontDimension, alphaArray)
        
        # Create the text object
        text = Text(font,'Basic Text')
        # Set the text object's position
        text.position = (0, 88)
        
        self.add(text)

game = DemoGame((640, 480), NewScene)
game.run()
