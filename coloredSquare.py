#Caleb Callaway
#2/5/18
#coloredSquare.py- uses sprites to display colored squares




from ggame import *
red = Color(0xff0000, 1)
line = LineStyle(3,red)
rectangleRed = RectangleAsset(100,100,line,red)

yellow = Color(0xffff00, 1)
line = LineStyle(3,yellow)
rectangleYellow = RectangleAsset(100,100,line,yellow)

green = Color(0x00ff00, 1)
line = LineStyle(3,green)
rectangleGreen = RectangleAsset(100,100,line,green)

blue = Color(0x0000ff, 1)
line = LineStyle(3,blue)
rectangleBlue = RectangleAsset(100,100,line,blue)

from random import randint

num = randint (1,4)


if num == 1:
    Sprite(rectangleRed)
    myApp = App()
    myApp.run()

elif num == 2:
    Sprite(rectangleYellow)
    myApp = App()
    myApp.run()

elif num == 3:
    Sprite(rectangleGreen)
    myApp = App()
    myApp.run()

elif num == 4:
    Sprite(rectangleBlue)
    myApp = App()
    myApp.run()


