import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time

    score_surface = test_font.render(f'{current_time} s',False,'Black')
    score_rect = score_surface.get_rect(midright = (1000,250))
    screen.blit(score_surface, score_rect)
    return current_time

def display_endscore():
    score_message = test_font.render(f'Score: {score} s',False,'Black')
    score_rect = score_message.get_rect(center = ((500,120)))
    screen.blit(score_message, score_rect)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(tube_surface,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > - 150]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True




pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Adnan's FlappyRobot")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Minecraft.ttf',35)
game_active = True
start_time = 0
score = 0
highscore = 0
jump_sound = pygame.mixer.Sound('audio/jump.wav')

bg_surface = pygame.image.load('graphics/background.png')

text_surface = test_font.render('Flappy-Robot',False,'Black')
text_rect = text_surface.get_rect(center = (500,50))

lose_text = test_font.render('Game Over',False,'Black')
lose_rect = lose_text.get_rect(center = (500,50))

tap_text = test_font.render('Tap Space to restart',False,'Black')
tap_rect = tap_text.get_rect(center = (500,400))

tube_surface = pygame.image.load('graphics/tubeboth.png').convert_alpha()
tube_rect = tube_surface.get_rect(topleft = (500,330))

tube2_surface = pygame.image.load('graphics/tubedown.png').convert_alpha()
tube2_rect = tube2_surface.get_rect(bottomleft = (500,180))

obstacle_rect_list = []

player_fall = pygame.image.load('graphics/player2.png').convert_alpha()
player_surface = player_fall
player_jump = pygame.image.load('graphics/playerjump.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (170,100))
gravity = 0

player_head = pygame.image.load('graphics/playerhead.png')
player_head_scaled = pygame.transform.scale(player_head,(200,200))
player_head_rect = player_head_scaled.get_rect(center = ((500,250)))




obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,2000)

while True:         # lässt das Fenster dauerhaft laufen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # schließt das Fesnter beim drücken auf 'x'
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_surface = player_jump
                    gravity = -7
                    jump_sound.play()
            if event.type == pygame.KEYUP:
                player_surface = player_fall

            if event.type == obstacle_timer:
                temp = randint(200,450)
                temp2 = temp-150
                coordinate_x = randint(1000,1100)
                #obstacle_rect_list.append([(obsatcle_rect_list.append(tube_surface.get_rect(topleft = (coordinate_x,temp)))),obsatcle_rect_list.append(tube2_surface.get_rect(bottomleft = (coordinate_x,temp2)))])
                obstacle_rect_list.append(tube_surface.get_rect(topleft = (coordinate_x,temp)))
                obstacle_rect_list.append(tube2_surface.get_rect(bottomleft = (coordinate_x,temp2)))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True


    if game_active:

        screen.blit(bg_surface,(0,0))

        pygame.draw.rect(screen,'Pink',text_rect)
        screen.blit(text_surface,text_rect)

        gravity += 0.5
        player_rect.y += gravity
        screen.blit(player_surface, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect,obstacle_rect_list)

        if highscore <= 0:
            highscore = 0
        score = display_score()
        if player_rect.top > 500:
            game_active = False

    else:
        screen.fill((94, 129,162))
        start_time = int(pygame.time.get_ticks()/1000)
        player_rect.top = 100
        obstacle_rect_list.clear()
        gravity = 0
        screen.blit(player_head_scaled, player_head_rect)
        screen.blit(lose_text,lose_rect)
        screen.blit(tap_text,tap_rect)
        display_endscore()
        if highscore <= score:
            highscore_message = test_font.render(f'New Highscore: {score} s',False,'Black')
            highscore_rect = highscore_message.get_rect(bottomleft = ((0,500)))
            screen.blit(highscore_message, highscore_rect)
            highscore = score
        else:
            highscore_message = test_font.render(f'Highscore: {highscore} s',False,'Black')
            highscore_rect = highscore_message.get_rect(bottomleft = ((0,500)))
            screen.blit(highscore_message, highscore_rect)











    pygame.display.update()
    clock.tick(60)



