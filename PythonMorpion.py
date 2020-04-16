import pygame
import sys

# Variables

board = ["-", "-", "-",
		"-", "-", "-",
		"-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

	#Affiche le tableau initial
	display_board()

	while game_still_going:

		handle_turn(current_player)

		check_if_game_over()

		flip_player()


def handle_turn(player):
	position = input("Choisis une position de 1 à 9 :\n")
	position = int(position) - 1

	board[position] = "X"
	display_board()

def check_if_game_over():
	check_if_win()
	check_if_tie()

def check_if_win():

	return

def check_if_tie():
	return

def flip_player():
	return

play_game()