#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	ship = Ship(ai_settings, screen)
	# alien = Alien(ai_settings, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	# 创建外星人群
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, aliens)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, ai_settings, screen, ship, aliens)
			gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)

		gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()