# J.M.S Corp
#Jhosep R, Mario Q, Sewmi G
# Statue of Gold
from gamelib import*
game=Game(800,600,"Statue of Gold")
bk=Image("1.jpg",game) 
bk.resizeTo(800,600)
game.setBackground(bk)

statue=Image("st45.png",game)
statue.resizeBy(-50)
statue.moveTo(400,400)

feo=Image("d23.png",game)
feo.setSpeed(4,60)
feo.resizeBy(-75)

cr=Image("cp2.png",game)
cr.setSpeed(100,80)
cr.resizeBy(-75)

logo=Image("logo.png",game)
logo.moveTo(400,300)

f=Font(black,48,green,"Comic Sans MS")
f1=Font(red,20,white,"Imapct")

#Title screen - game loop

while not game.over:
      game.processInput()
      bk.draw()
      #game.scrollBackground("left",2)
      logo.draw()
      game.update(30) 
      if keys.Pressed[K_SPACE]:
           game.over=True
           game.update(30)

game.over=False


#Level 1 - game loop

while not game.over:
      game.processInput()
      bk.draw()
      feo.move(True)
      cr.moveTo(mouse.x,mouse.y)
      statue.draw()
      #if  feo.collidedWith(statue):

      game.drawText("X   "+ str(game.score),100,530,f) 
      game.displayScore()

      #game.drawText("Statue's Health   "+ str(game.score),100,530,f) 
      #game.displayScore()

      #if feo.collidedWith(statue):
         #-feo.moveTo(randint.x, randint.y)  

      if feo.collidedWith(mouse) and mouse.LeftClick:
        feo.resizeBy(-2)
        x = randint(feo.width,game.width-feo.width)
        y = randint(feo.height,game.height-feo.height)
        feo.moveTo(x,y)
        feo.speed += 2        
        game.score += 10

        if feo.collidedWith(statue):
            game.score -= 10  

    

      
      
      game.update(30)

game.over = True




game.quit()

