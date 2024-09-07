import pygame 
from fighter import Fighter



pygame.init()

#create window
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED=(255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#load back-image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#function for drawing background
def draw_bg():
    scaled_bg=pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

def draw_health_bar(health,x,y):
    ratio = health/100
    pygame.draw.rect(screen,BLACK,(x+5,y+3,410,36))
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400 *ratio,30))


#instances of fighters
fighter_1 = Fighter(200,463)
fighter_2 = Fighter(1050,463)



#game loop
run = True
while run:
    clock.tick(FPS)

    #draw bg
    draw_bg()
    #show player stats
    draw_health_bar(fighter_1.health,20,30)
    draw_health_bar(fighter_2.health,1080,30)

    #move fighters
    fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)


    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 #update image   
    pygame.display.update()        

#exit game
pygame.quit()

