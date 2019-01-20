#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

#### 说明备注
# pygame.sprite.groupcollide(bullets, aliens, True, True) 可以检测两个编组的成员之间的碰撞
# pygame.sprite.spritecollideany(ship, aliens) 可以检测飞船和外星人之间的碰撞
###

def check_keydown_events(ship, event, screen, ai_settings, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ship, screen, ai_settings, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(ship, event, screen, ai_settings, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets, aliens):
	# 检视键盘鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(ship, event, screen, ai_settings, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(ship, event, screen, ai_settings, bullets)

def update_bullets(bullets, ai_settings, screen, ship, aliens):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0 :
			bullets.remove(bullet)
	check_bullet_alien_collisions(bullets, ai_settings, screen, ship, aliens)

def check_bullet_alien_collisions(bullets, ai_settings, screen, ship, aliens):
	# 检查是否有子弹击中了外星人
	# 如果是这样就删除相应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ship, screen, ai_settings, bullets):
	if len(bullets) < ai_settings.bullet_allowed :
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算屏幕可以容纳多少行外星人"""
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height ) 
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
	for number_rows in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, number_rows)

def check_fleet_edges(ai_settings, aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			check_fleet_direction(ai_settings, aliens)
			break

def check_fleet_direction(ai_settings, aliens):
	"""将整群外星人下移,并改变它们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	screen_rect = screen.get_rect()
	if screen_rect.bottom < aliens.rect.bottom:
		hit_ship(ai_settings, stats, screen, ship, aliens, bullets)

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	# 检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		hit_ship(ai_settings, stats, screen, ship, aliens, bullets)
	# 检测外星人是否到达底端
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def hit_ship(ai_settings, stats, screen, ship, aliens, bullets):
	# 飞船-1
	stats.ship_left -= 1
	if stats.ship_left < 0:
		stats.game_active = False
	# 清空外星人和子弹
	aliens.empty()
	bullets.empty()

	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()

	sleep(0.5)

def update_screen(ai_settings, screen, ship, bullets, aliens):
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	# aliens.blitme()
	aliens.draw(screen)

	# 让最近绘制的屏幕可见
	pygame.display.flip()