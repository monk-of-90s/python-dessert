import pygame


class QueenSprite:
    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        self.position = target_posn

    def update(self):
        return

    def draw(self, target_surface):
        target_surface.blit(self.image, self.position)


def draw_board(the_board):
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]
    n = len(the_board)
    surface_size = 480
    square_size = surface_size // n
    surface_size = n * square_size
    surface = pygame.display.set_mode((surface_size, surface_size))
    for row in range(n):
        color_index = row % 2
        for col in range(n):
            for col in range(n):
                the_square = (col * square_size, row * square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                color_index = (color_index + 1) % 2
    ball = pygame.image.load('ball.png')
    ball_offset = (square_size - ball.get_width()) // 2
    all_sprites = []
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,
                              (col * square_size + ball_offset, row * square_size + ball_offset))
        all_sprites.append(a_queen)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        for sprite in all_sprites:
            sprite.update()
        for sprite in all_sprites:
            sprite.draw(surface)
        pygame.display.flip()

    pygame.quit()


#
# def draw_board(the_board):
#     pygame.init()
#     colors = [(255, 0, 0), (0, 0, 0)]
#     n = len(the_board)
#     surface_size = 480
#     square_size = surface_size // n
#     surface_size = n * square_size
#     surface = pygame.display.set_mode((surface_size, surface_size))
#     for row in range(n):
#         color_index = row % 2
#         for col in range(n):
#             for col in range(n):
#                 the_square = (col * square_size, row * square_size, square_size, square_size)
#                 surface.fill(colors[color_index], the_square)
#                 color_index = (color_index + 1) % 2
#     ball = pygame.image.load('ball.png')
#     ball_offset = (square_size - ball.get_width()) // 2
#     while True:
#         ev = pygame.event.poll()
#         if ev.type == pygame.QUIT:
#             break
#         for (col, row) in enumerate(the_board):
#             surface.blit(ball, (col * square_size + ball_offset, row * square_size + ball_offset))
#         pygame.display.flip()
#
#     pygame.quit()
#

if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
