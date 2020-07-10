import pygame as py



class ship(py.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = py.image.load("ship.png")
    self.image = py.transform.smoothscale(self.image, (40, 40))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.image = py.transform.rotate(self.image, -90)
    self.speed = py.math.Vector2(0,0)



  def update(self):
    self.rect.move_ip(self.speed)



  def reset(self, pos):
    self.rect.center = pos



  def checkReset(self, endPos):
    if self.rect.center[0] > endPos:
      return True
    else:
      return False