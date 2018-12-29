#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

print('Hello pandas')

# title() strip() lstrip() rstrip()
name = 'ada live'
print(name.title())

first_name = "ada"
last_name = "lovelace "

print(last_name.strip())

print(first_name + ' ' + last_name)

print('Hello,'+ first_name.title()+'!')

print('Languages:\n\tPython\n\tC\n\tJavaScript')

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)
cars.reverse()
print(cars)

print(list(range(2,11,2)))