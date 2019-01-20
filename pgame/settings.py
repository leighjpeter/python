#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Settings():
	"""存储设置的类"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		# ship's speed
		self.ship_speed_factor = 5
		self.ship_limit = 3
		# bullet setting
		self.bullet_speed_factor = 5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 10
		# alien speed
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 100
		self.fleet_direction = 1