#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:52:48 2019

@author: davinpc
"""

f = open('data.txt','r')
data = f.read()
print(data)
print(' ')
menu = '1. New Staff \n2. Delete Staff \n3. View Summary Data \n4. Save & Exit'
print(menu)
choice = str(input('Input Choice: '))
if choice == '1':
    print('New Staff')
    staff_id = str(input('Input ID [SXXXX]: '))
    number = [0,1,2,3,4,5,6,7,8,9]
    for x in number:
        if staff_id != 'S' + str(x) + str(x) + str(x) + str(x):
            staff_id = str(input('Input ID [SXXXX]: '))
        break
    staff_name = input('Input Name [0...20]: ')
    if len(staff_name) > 20:
        staff_name = input('Input Name [0...20]: ')
    staff_position = input('Input Position [Staff/Officer/Manager]: ')
    staff_position = staff_position.lower()
    if staff_position != 'staff':
        if staff_position != 'officer':
            if staff_position != 'manager':
                staff_position = input('Input Position [Staff/Officer/Manager]: ')
                
