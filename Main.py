import pygame
import sys

pygame.init()


def main():
    window = pygame.display.set_mode((900, 600))
    window.fill((202, 151, 39))
    f1 = pygame.font.Font('PixelFont.ttf', 36)

    pygame.draw.rect(window, (255, 255, 255), (700, 150, 150, 50))
    pygame.draw.rect(window, (0, 0, 0), (700, 150, 150, 50), 5)
    text1 = f1.render('Button', 0, (0, 0, 0))
    window.blit(text1, (720, 160))

    pygame.draw.rect(window, (255, 255, 255), (50, 75, 50, 50))



    pygame.display.update()
    pressed = pygame.mouse.get_pressed()
    while True:
        pygame.time.delay(20)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return
            if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                window.blit(f1.render('click', 0, (0,0,0)), (i.pos[0]-20, i.pos[1]-10))
            if pygame.mouse.get_focused():
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(window, (0,0,0), pos, 5)
        pygame.display.update()






if __name__ == "__main__":
    main()