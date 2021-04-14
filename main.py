from pygame import *



window = display.set_mode((1200,700))
background = transform.scale(image.load("12.jpg"), (1200,700))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,width, height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()   
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed











display.set_caption(" ")
background = transform.scale(image.load("12.jpg"), (1200,700))

game = True
finish = False
clock = time.Clock()

    

racket1 = Player('11.jpg', 100 , 200 , 4 , 50 , 150)
racket2 = Player('11.jpg', 1100 , 200 , 4 , 50 , 150)
ball = GameSprite('111.png', 200 , 200 , 4 , 50 , 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0)) 
lose2 =  font.render('PLAYER 2 LOSE', True ,(180 ,0 ,0))

run = True

speed_x = 3
speed_y = 3



FPS = 144
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        
        racket1.update_1()
        racket2.update_r()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()
        ball.reset()
        







    
    display.update()



