import pygame
from pygame.constants import NOEVENT

gravity = 0.2


class DuckSprite:
    def __init__(self, img, target_position):
        self.cur_patch_num = 0
        self.anim_frame_count = 0
        self.image = img
        self.position = target_position

    def update(self):
        if self.anim_frame_count >= 0:
            self.anim_frame_count = (self.anim_frame_count + 1) % 60
            self.cur_patch_num = self.anim_frame_count // 6

    def draw(self, targer_surface):
        patch_rect = (self.cur_patch_num * 50, 0, 50, self.image.get_height())
        targer_surface.blit(self.image, self.position, patch_rect)

    def handle_click(self):
        self.anim_frame_count = -self.anim_frame_count - 1

    def contains_point(self, pt):
        (my_x, my_y) = self.position
        my_width = 50
        my_height = self.image.get_height()
        (x, y) = pt
        return (x >= my_x and x < my_x + my_width and \
                y >= my_y and y < my_y + my_height)


class QueenSprite:
    def __init__(self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.position = (x, 0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        (x, y) = self.position
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn
        dist_to_go = target_y - new_y_pos
        if dist_to_go < 0:
            self.y_velocity = int(-0.90 * self.y_velocity)
            new_y_pos = target_y + dist_to_go
        self.position = (x, new_y_pos)

    def draw(self, target_surface):
        target_surface.blit(self.image, self.position)

    def contains_point(self, point):
        (my_x, my_y) = self.position
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = point
        return (x >= my_x and x < my_x + my_width) and \
               (y >= my_y and y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -3


def draw_board(the_board):
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]
    n = len(the_board)
    surface_size = 480
    square_size = surface_size // n
    surface_size = n * square_size
    surface = pygame.display.set_mode((surface_size, surface_size))

    ball = pygame.image.load('ball.png')
    ball_offset = (square_size - ball.get_width()) // 2
    all_sprites = []
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,
                              (col * square_size + ball_offset, row * square_size + ball_offset))
        all_sprites.append(a_queen)
    my_clock = pygame.time.Clock()

    # duck_sprite_sheet = pygame.image.load('duke_spritesheet.png')
    # duck1 = DuckSprite(duck_sprite_sheet, (square_size * 2, 0))
    # duck2 = DuckSprite(duck_sprite_sheet, (square_size * 5, square_size))
    # all_sprites.append(duck1)
    # all_sprites.append(duck2)
    while True:
        ev = pygame.event.poll()
        if ev.type != pygame.NOEVENT:
            print(ev)
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            if key == 27:
                break
            if key == ord('r'):
                colors[0] = (255, 0, 0)
            elif key == ord('g'):
                colors[0] = (0, 255, 0)
            elif key == ord('b'):
                colors[0] = (0, 0, 255)
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict['pos']
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break
        for row in range(n):
            color_index = row % 2
            for col in range(n):
                for col in range(n):
                    the_square = (col * square_size, row * square_size, square_size, square_size)
                    surface.fill(colors[color_index], the_square)
                    color_index = (color_index + 1) % 2
        for sprite in all_sprites:
            sprite.update()
        for sprite in all_sprites:
            sprite.draw(surface)
        my_clock.tick(60)
        pygame.display.flip()

    pygame.quit()


# def draw_board(the_board):
#     pygame.init()
#     colors = [(255, 0, 0), (0, 0, 0)]
#     n = len(the_board)
#     surface_size = 480
#     square_size = surface_size // n
#     surface_size = n * square_size
#     surface = pygame.display.set_mode((surface_size, surface_size))
#     ball = pygame.image.load('ball.png')
#     ball_offset = (square_size - ball.get_width()) // 2
#     all_sprites = []
#     for (col, row) in enumerate(the_board):
#         a_queen = QueenSprite(ball,
#                               (col * square_size + ball_offset, row * square_size + ball_offset))
#         all_sprites.append(a_queen)
#     my_clock = pygame.time.Clock()
#
#     while True:
#         ev = pygame.event.poll()
#         if ev.type != pygame.NOEVENT:
#             print(ev)
#         if ev.type == pygame.QUIT:
#             break
#         if ev.type == pygame.KEYDOWN:
#             key = ev.dict['key']
#             if key == 27:
#                 break
#             if key == ord('r'):
#                 colors[0] = (255, 0, 0)
#             elif key == ord('g'):
#                 colors[0] = (0, 255, 0)
#             elif key == ord('b'):
#                 colors[0] = (0, 0, 255)
#         if ev.type == pygame.MOUSEBUTTONDOWN:
#             posn_of_click = ev.dict['pos']
#             for sprite in all_sprites:
#                 if sprite.contains_point(posn_of_click):
#                     sprite.handle_click()
#                     break
#         for row in range(n):
#             color_index = row % 2
#             for col in range(n):
#                 for col in range(n):
#                     the_square = (col * square_size, row * square_size, square_size, square_size)
#                     surface.fill(colors[color_index], the_square)
#                     color_index = (color_index + 1) % 2
#         for sprite in all_sprites:
#             sprite.update()
#         for sprite in all_sprites:
#             sprite.draw(surface)
#         my_clock.tick(60)
#         pygame.display.flip()
#
#     pygame.quit()


if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
