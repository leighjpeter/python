#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""Alien的类"""
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True;
		elif self.rect.left <= 0:
			return True;

	def update(self):
		"""向左或向右移动外星人"""
		self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
		self.rect.x = self.x

	def  blitme(self):
		self.screen.blit(self.image, self.rect)