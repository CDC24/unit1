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
    print ("Matzo balls")

elif num == 4:
     print ("Matzo balls")


