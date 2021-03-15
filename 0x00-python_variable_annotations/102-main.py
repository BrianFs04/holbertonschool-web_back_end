#!/usr/bin/env python3

zoom_array = __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)
print(zoom_array([12, 72, 91], 3))
