import pygame as py, random



class asteroid(py.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = py.image.load("asteroid.png")
    self.image = py.transform.smoothscale(self.image,(random.randint(0, 40), random.randint(0,40)))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = py.math.Vector2(0,3)
    rotation = random.randint(0,360)
    self.speed.rotate_ip(rotation)

def update(self):
  screen_info = py.diplay.Info()
  self.rect.move_ip(self.speed)
  rotation = random.randint(0, 360)
  self.speed.rotate_ip(rotation)
  self.image = py.transform.rotate(self.image, 180 - rotation)
  screen_info = py.display.Info()
  if self.rect.right >= screen_info.current_w or self.rect.left <= 0:
    self.speed[0] *= -1
    self.image = py.transform.flip(self.image, True, False)
    self.rect.move_ip(self.speed[0], 0)
  if self.rect.top <= 0 or self.rect.bottom >= screen_info.current_h:
    self.speed[1] *= -1
    self.image = py.transform.flip(self.image, False, True)
    self.rect.move_ip(0, self.speed[1])    