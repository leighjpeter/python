#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import log_core
import yaml
import logging.config
import os

def setup_logging(default_path='config.yaml', default_level=logging.INFO):
	path = default_path
	if os.path.exists(path):
		with open(path, 'r', encoding='utf-8') as f:
			config = yaml.load(f)
			logging.config.dictConfig(config)
	else:
		logging.basicConfig(level=default_level)

def log():
	logging.debug('Start')
	logging.info('Exec')
	logging.info('Finished')

if __name__ == '__main__':
	yaml_path = 'config.yaml'
	setup_logging(yaml_path)
	log()
	log_core.run()