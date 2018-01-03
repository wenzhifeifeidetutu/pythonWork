import sys

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf 

from pygame.sprite import Group



def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")

	# #设置背景颜色
	# bg_color = (230, 230, 230)

	#创造一艘飞船
	ship = Ship(ai_settings, screen)

	#创造一个用于储存子弹的编组
	bullets = Group()


	while True:
		

		# #监视键盘和鼠标事件
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		# gf.check_events(ship)
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()

		#删除已经消失的子弹
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))

		#重新绘制屏幕		
		# screen.fill(ai_settings.bgcolor)
		# ship.blitme()

		# #让最近绘制屏幕可见
		# pygame.display.flip()
		# gf.update_screen(ai_settings, screen, ship)
		gf.update_screen(ai_settings, screen, ship, bullets)




run_game()