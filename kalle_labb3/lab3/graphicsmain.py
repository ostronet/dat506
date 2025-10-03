from gamemodel import *
from graphics import *


class GameGraphics:
    def __init__(self, game):
        self.game = game

        # open the window
        self.win = GraphWin("Cannon game" , 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)

        #drawing the line
        p1 = Point(-110,0)
        p2 = Point(110,0)
        l12 = Line(p1,p2)
        l12.setFill("black")
        l12.draw(self.win)

        
        self.draw_cannons = [self.drawCanon(0), self.drawCanon(1)] #Dessa drawCanon och drawScore är endast använda en gång i början! Sedan kör man de
        self.draw_scores  = [self.drawScore(0), self.drawScore(1)] #genom update score.
        self.draw_projs   = [None, None]

    def drawCanon(self,playerNr):
        #drawing the cannons
        playr = self.game.players[playerNr]
        col = playr.getColor()
        p1 = Point(playr.getX() - self.game.cannonSize / 2, 0)
        p2 = Point(playr.getX() + self.game.cannonSize/ 2, self.game.cannonSize)
        rec12 = Rectangle(p1,p2)

        rec12.setFill(col); rec12.draw(self.win)
        
        return rec12

    def drawScore(self,playerNr):
        # draw the score
        playr = self.game.players[playerNr]
        
        tp = Point(playr.getX(), -5)
        text = Text(tp,str(playr.getScore()))
        text.draw(self.win)
        
        return text

    def fire(self, angle, vel):
        player = self.game.getCurrentPlayer()
        proj = player.fire(angle, vel)

        circle_X = proj.getX()
        circle_Y = proj.getY()

        
        if self.draw_projs[self.game.current_player] is not None:
            self.draw_projs[self.game.current_player].undraw()

        # draw the projectile (ball/circle)
        p = Point(circle_X, circle_Y)
        circle = Circle(p,self.game.ballSize)
        self.draw_projs[self.game.current_player] = circle 
        circle.setFill(str(player.color))      #sparar projektilen i listan av projektiler
        circle.draw(self.win)
        
        

        while proj.isMoving():
            proj.update(1/50)

            # move is a function in graphics. It moves an object dx units in x direction and dy units in y direction
            circle.move(proj.getX() - circle_X, proj.getY() - circle_Y)

            circle_X = proj.getX()
            circle_Y = proj.getY()

            update(50)

        return proj

    def updateScore(self,playerNr):
    
        self.draw_scores[playerNr].undraw()
        self.draw_scores[playerNr] = self.drawScore(playerNr)

    def play(self):
        while True:
            player = self.game.getCurrentPlayer()
            oldAngle,oldVel = player.getAim()
            wind = self.game.getCurrentWind()

            # InputDialog(self, angle, vel, wind) is a class in gamegraphics
            inp = InputDialog(oldAngle,oldVel,wind)
            # interact(self) is a function inside InputDialog. It runs a loop until the user presses either the quit or fire button
            if inp.interact() == "Fire!": 
                angle, vel = inp.getValues()
                inp.close()
            elif inp.interact() == "Quit":
                exit()
            
            player = self.game.getCurrentPlayer()
            other = self.game.getOtherPlayer()
            proj = self.fire(angle, vel)
            distance = other.projectileDistance(proj)

            if distance == 0.0:
                player.increaseScore()
                self.updateScore(self.game.getCurrentPlayerNumber())
                self.explode(self.game.getOtherPlayer())
                self.game.newRound()

            self.game.nextPlayer()

    def explode(self,otherPlayer):
        explosion_radius = 0.1
        while explosion_radius < 2 * self.game.cannonSize:
            p = Point(otherPlayer.getX(),self.game.cannonSize/2)
            explosion = Circle(p,explosion_radius); explosion.setFill(self.game.getCurrentPlayer().getColor())
            explosion.draw(self.win)
            update(50)
            explosion_radius += 0.1
            explosion.undraw()
            
#vinden uppdaterar bara när man träffar och det är alltid blå som börjar efter att vinden uppdateras
class InputDialog:
    def __init__ (self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Wind").draw(win)
        self.height = Text(Point(3,3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a,v

    def close(self):
        self.win.close()


class Button:

    def __init__(self, win, center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0


GameGraphics(Game(11,2)).play()
