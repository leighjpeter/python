#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# logging
# 可指定日志级别 debug,info,warning,error
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
