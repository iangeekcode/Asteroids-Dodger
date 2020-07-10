import pygame as py, random, pandas as pd
from pygame. locals import *
from ship import *
from asteroid import *



py.init()
screen_info = py.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)



screen = py.display.set_mode(size)
clock = py.time.Clock()
color = (30, 0, 30)
screen.fill(color)


df = pd.read_csv('game_info.csv')
NumLevels = df['LevelNum'].max()
CurrentLevels = df['LevelNum'].min()
LevelData = df.iloc[CurrentLevels]




AsteroidCount = LevelData['AsteroidCount']
player = ship((LevelData['PlayerX'], LevelData['PlayerY']))
Asteroids = py.sprite.Group()


def init():
  global AsteroidCount, CurrentLevels, LevelData
  LevelData = df.iloc[CurrentLevels]
  player.reset((LevelData['PlayerX'], LevelData['PlayerY']))
  CurrentLevels  += 1
  AsteroidCount = LevelData['AsteroidCount']
  Asteroids.empty()
  player.reset
  for i in range(AsteroidCount):
    Asteroids.add(asteroid((random.randint(0 , 800), random.randint(0, 600))))



def win():
  font = py.font.SysFont(None, 70)
  text = font.rnder("You Survived!", True, (255, 0, 0))
  text_rect = text = text.get_rect()
  text_rect.center = (screen_info.current_w //2, screen_info.current_h //2)
  while True:
    screen.fill(color)
    screen.blit(text, text_rect)
    py.display.flip()



def main():
  global CurrentLevels
  init()
  while True:
    size = (width, height) = (screen_info.current_w), int(screen_info.current_h)
    while CurrentLevels <= NumLevels:
      clock.tick(60)
      for event in py.event.get():
        if event.type == py.KEYDOWN:
          if event.key == py.K_RIGHT:
            player.speed[0] = 5
          if event.key == py.K_LEFT:
            player.speed[0] = -5
          if event.key == py.K_UP:
            player.speed[1] = -5
          if event.key == py.K_DOWN:
            player.speed[1] = 5
        else:
          player.speed[0] = 0
          player.speed[1] = 0
      screen.fill(color)
      Asteroids.draw(screen)
      Asteroids.update()
      gets_hit = py.sprite.spritecollide(player, Asteroids, False)
      screen.blit(player.image, player.rect)
      if player.checkReset(screen_info.current_w):
        init()
      if CurrentLevels == NumLevels:
        break
        
      elif gets_hit:
        player.reset((20, 300))

      
      else:
        CurrentLevels += 1
        init()
      

     
  win()



if __name__=="__main__":
  main()