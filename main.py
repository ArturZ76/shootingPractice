import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.wav")
    
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, targets_group,True)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

def reset_game():
    global score
    score = 0
    targets_group.empty()
    for _ in range(20):
        new_target = Target("target.png", random.randrange(50, screen_width - 50), random.randrange(50, screen_height - 50))
        targets_group.add(new_target)

class GameState():
    def __init__(self):
        self.state = "intro"
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "main_game"

        screen.blit(background, (0,0,))
        text_surface = font.render("Ready?", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        screen.blit(background, (0,0,))
        targets_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        
        pygame.display.flip()
    
    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()



pygame.init()
clock = pygame.time.Clock()
game_state = GameState()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ready")
font = pygame.font.SysFont("Arial", 64)

screen_width = 1380
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
ready_text = pygame.image.load
pygame.mouse.set_visible(False)



game_font = pygame.font.SysFont("Arial", 100)

crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

targets_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target.png", random.randrange(10, screen_width - 10), random.randrange(10, screen_height -10))
    targets_group.add(new_target)
    

while True:

    game_state.state_manager()

    clock.tick(60)

