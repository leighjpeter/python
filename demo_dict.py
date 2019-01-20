#!/usr/bin/env python3
# -*- coding: utf-8 -*-
alien_0 = {
    'color':'green',
    'point':5
}

print(alien_0['color'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print("Original x-position: " + str(alien_0['x_position']))
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position:' + str(alien_0['x_position']) )


for key, value in alien_0.items():
    print("\nKey:" + key)
    print('Value:' + str(value))

favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

print(favorite_languages.keys())
print(favorite_languages.values())


if 'erin' not in favorite_languages.keys() :
    print("Erin, please take our poll!")

# 字典列表
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
print('you ordered a '+ pizza['crust'] + '-crust pizza ' +
'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert', 'last': 'einstein', 'location': 'princeton', 
    },
    'mcurie': {
        'first': 'marie', 'last': 'curie', 'location': 'paris', 
    },
}

for username, userinfo in users.items():
    print("\nUsername:"+username)
    full_name = userinfo['first'] + ' ' +userinfo['last']
    print("\tFull name:" + full_name.title())
    print("\tLocation:" + userinfo['location'].title())

# OrderedDict模块可以记录添加的顺序，兼具列表和字典的优点
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['phil'] = 'php'
favorite_languages['sarah'] = 'java'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

f={'jen':'python','sarah':'java','phil':'php'}

print(f)