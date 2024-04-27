import pygame
from pygame import mixer

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ping Pong")

# Player 1
player1Y = 260
player1YChange = 0
def player1(y):
    pygame.draw.rect(window,(255,255,255),(20,y,10,100))

# Player 2
player2Y = 260
player2YChange = 0
def player2(y):
    pygame.draw.rect(window,(255,255,255),(770,y,10,100))

# Ball
ballX = 390
ballY = 300
ballXChange = 0.1
ballYChange = 0.1
ballRunning = False
def ball(x,y):
    pygame.draw.circle(window , (255,255,255) , (x,y) , 10)

# Score
score1 = 0
score2 = 0
font = pygame.font.Font("freesansbold.ttf" , 20)
def score(score1,score2):
    sc = font.render("Player 1: " + str(score1) + "   Player 2: " + str(score2) , True , "white")
    window.blit(sc, (300 , 20))

running = True
while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1YChange = -0.1
            if event.key == pygame.K_s:
                player1YChange = 0.1
            if event.key == pygame.K_UP:
                player2YChange = -0.1
            if event.key == pygame.K_DOWN:
                player2YChange = 0.1
            if event.key == pygame.K_SPACE:
                ballRunning = True
            if event.key == pygame.K_r:
                score1 = 0
                score2 = 0
                ballX = 390
                ballY = 300
                ballRunning = False
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1YChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2YChange = 0
            

     

    player1Y += player1YChange
    player2Y += player2YChange

    if ballRunning == True:
        ballY += ballYChange
        ballX += ballXChange

    # Boundary restrictions

    # Players
    if player1Y < 0:
        player1Y = 0
    if player1Y > 500:
        player1Y = 500
    if player2Y < 0:
        player2Y = 0
    if player2Y > 500:
        player2Y = 500

    # Ball Contact with the Boundary
    if ballY < 10:
        ballYChange *= -1
        ballY = 10
    if ballY > 590 :
        ballYChange *= -1
        ballY = 590

    # Ball beating the player
    if ballX < 10:
        score2 += 1
        ballX = 40
        ballY = 300
        ballXChange *= -1
        ballRunning = False
    if ballX > 790 :
        score1 += 1
        ballX = 760
        ballY = 300
        ballXChange *= -1
        ballRunning = False

    # Contact of Ball and Player
    if (ballY < player1Y +100 and ballY > player1Y) and (ballX > 28 and ballX<30):
        ballXChange *= -1
        ballX = 30
        # collision_sound = mixer.Sound('laser.wav')
        # collision_sound.play()
    if (ballY < player2Y +100 and ballY > player2Y) and (ballX > 770 and ballX<772):
        ballXChange *= -1
        ballX = 770
        # collision_sound = mixer.Sound('laser.wav')
        # collision_sound.play()

    

    player1(player1Y)
    player2(player2Y)
    ball(ballX,ballY)
    score(score1,score2)
    pygame.display.update()
