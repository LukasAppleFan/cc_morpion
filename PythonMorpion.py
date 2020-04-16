import pygame
import sys

joueur1 = 1
joueur2 = 2

tab = [[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' '],]

for row in tab:
	print(row)

tab[0][0] = 'x'

for row in tab:
	print(row)

value = input("Entrer en x :\n")

print(f'You entered {value}')
