import sys
import pygame
from bullet import Bullet
# def check_events(ship):
# 	"""响应按键事件"""

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 		elif event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_RIGHT:
# 				ship.moving_right = True
# 			elif event.key == pygame.K_LEFT:
# 				ship.moving_left = True

# 		elif event.type == pygame.KEYUP:
# 			if event.key == pygame.K_RIGHT:
# 				ship.moving_right = False
# 			elif event.key == pygame.K_LEFT:
# 				ship.moving_left = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship) 

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕图像"""
	#每次循环都重新绘制屏幕
	screen.fill(ai_settings.bgcolor)
	ship.blitme()

	#在外星人后面重新绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()


	#让最近的绘制可见
	pygame.display.flip()