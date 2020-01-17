#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())