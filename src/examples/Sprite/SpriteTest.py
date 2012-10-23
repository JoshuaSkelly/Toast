from toast import Scene
from toast.image_sheet import ImageSheet
from toast.sprite import Sprite
from toast.resource_loader import ResourceLoader
from toast.animation import Animation

from examples.demo_game import DemoGame

class NewScene(Scene):
    def __init__(self):
        super(NewScene, self).__init__()
        
        self.clear_color = 98, 186, 221
        self.resolution = 640, 480
        
        dimension = 32, 37
        data = ResourceLoader.load('data//player_run.png')
        sheet = ImageSheet(data, dimension)
        
        interval = 60

        run = [(sheet[0], interval), 
               (sheet[1], interval), 
               (sheet[2], interval), 
               (sheet[3], interval), 
               (sheet[4], interval), 
               (sheet[5], interval), 
               (sheet[6], interval), 
               (sheet[7], interval)]
        
        for i in range(8):
            animation = Animation('run_cycle', run)
            animation.goto_and_play(i, 'run_cycle')
            
            staticSprite = Sprite(sheet[i])
            staticSprite.position = (i + 1) * 32, 68
            self.add(staticSprite)
            
            animatedSprite = Sprite(animation)
            animatedSprite.position = (i + 1) * 32, 132
            self.add(animatedSprite)

game = DemoGame((640, 480), NewScene)
game.run()