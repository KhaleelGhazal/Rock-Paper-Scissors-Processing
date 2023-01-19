import sys

class Button:
    def __init__(self, rectX_, rectY_, rectW_, rectH_, rectC_):
        self.rectX = rectX_
        self.rectY = rectY_
        self.rectW = rectW_
        self.rectH = rectH_
        self.rectC = rectC_

    def display(self):
        noStroke()
        fill(*self.rectC)
        rect(self.rectX, self.rectY, self.rectW, self.rectH)

rock = None
paper = None
scissors = None

def displayGame(winner):
    background(10, 20, 100)
    textAlign(CENTER)
    fill(255)
    textSize(40)
    text("rock, paper, or scissors?",width/2,200)
    text("rock",100,400)
    text("paper",300,400)
    text("scissors",500,400)
    image(rock, 50, 425, 100, 100)
    image(paper, 250, 425, 100, 100)
    image(scissors, 450, 425, 100, 100)
    text("Winner: " + winner, width/2, 550)
    text("Score: Human " + str(userScore) + " - " + str(computerScore) + " Computer", width/2, 580)

def endGame():
    sys.exit()

buttons = [Button(0, 0, 0, 0, 0) for i in range(4)]
userScore = 0
computerScore = 0
gameOver = False
computerChoice = 0
gameOn = True
winner = ""

def setup():
    global rock, paper, scissors
    r = createFont("Arial", 40)
    textFont(r)
    background(10, 20, 100)
    size(800, 800)
    buttons[0] = Button(50, 400, 100, 100, (10, 20, 100))
    buttons[1] = Button(250, 400, 100, 100, (10, 20, 100))
    buttons[2] = Button(450, 400, 100, 100, (10, 20, 100))
    rock = loadImage("rock.png")
    paper = loadImage("paper.png")
    scissors = loadImage("scissors.png")
    
def checkWinner():
    global winner
    if userScore == 3:
        winner = "Human"
    elif computerScore == 3:
        winner = "Computer"
    if userScore == 3 or computerScore == 3:
        displayFinalScreen(winner)

def displayFinalScreen(winner):
    background(10, 20, 100)
    textAlign(CENTER)
    fill(255)
    textSize(40)
    text("Overall Winner: " + winner, width/2, height/2)
    text("Thank you for playing!", width/2, height/2 + 50)

def draw():
    for i in range(3):
        buttons[i].display()
    displayGame(winner)
    checkWinner()
    if userScore == 3 or computerScore == 3:
        noLoop()

def mousePressed():
    global userScore, computerScore, winner
    computerChoice = int(random(1, 4))
    if (mouseX >= 50 and mouseX <= 50+100 and mouseY >= 400 and mouseY <= 400+100):
        println("Human chooses rock")
        userChoice = 1
    elif (mouseX >= 250 and mouseX <= 250+100 and mouseY >= 400 and mouseY <= 400+100):
        println("Human chooses paper")
        userChoice = 2
    elif (mouseX >= 450 and mouseX <= 450+100 and mouseY >= 400 and mouseY <= 400+100):
        println("Human chooses scissors")
        userChoice = 3
    # check for tie
    if (userChoice == computerChoice):
        println("tie")
        winner = "Tie"
    # check for human win
    elif ((userChoice == 1 and computerChoice == 3) or
          (userChoice == 2 and computerChoice == 1) or
          (userChoice == 3 and computerChoice == 2)):
        println("Human wins!")
        userScore += 1
        winner = "Human"
    # check for computer win
    else:
        println("Computer wins!")
        computerScore += 1
        winner = "Computer"
