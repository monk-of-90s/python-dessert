import pygame, cards


class HandHolding5(cards.Hand):
    def __init__(self, *args, **kwargs):
        super(HandHolding5, self).__init__(*args, **kwargs)
        self.image = pygame.image.load('cards.png')

    def draw(self, targer_surface):
        for card in self.cards:
            # rect = (self.cards.index(card) * 61, 0, 61, 80)
            rect = ((card.rank - 1) * 61, ((card.suit + 1) % 4) * 80, 61, 80)
            targer_surface.blit(self.image, (self.cards.index(card) * 61, 0), rect)


deck = cards.Deck()
deck.shuffle()
hand = HandHolding5('Tom')
deck.deal([hand], 5)
print(hand)

pygame.init()
surface_height = 80
surface_width = 60 * 5
surface = pygame.display.set_mode((surface_width, surface_height))
hand.draw(surface)
pygame.display.flip()

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
pygame.quit()
