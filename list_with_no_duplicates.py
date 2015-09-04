#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
print a list with no duplicates
"""

#  Author:
#    Johan Chassaing
#
#  License:
#    GPL
#
#  Dependencies:
#    python
#

list_to_check = ['cat', 'cat', 'cat', 'ls', 'ls', 'ls']
no_dup_list = []

for item in list_to_check:
    if item not in no_dup_list:
        no_dup_list.append(item)

print no_dup_list
