import pygame

# init
pygame.init()

# buat display surface object
windowX = 500
windowY = 500
window = pygame.display.set_mode((windowX, windowY))

# object game
# posisi
x = 250
y = 250

# ukuran
p = 20
l = 20

# kecepatan
s = 10

while True:
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 0:
        y -= s
    if keys[pygame.K_DOWN] and y < windowY - p:
        y += s
    if keys[pygame.K_LEFT] and x > 0:
        x -= s
    if keys[pygame.K_RIGHT] and x < windowX - l:
        x += s

    # update assets
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), (x, y, p, l))
    # render ke display atau layar
    pygame.display.update()

