import random

grid_size = 5
monkey_position = [random.randint(0, grid_size - 1),random.randint(0, grid_size - 1)]
banana_position = [random.randint(0, grid_size - 1),random.randint(0, grid_size - 1)]

while monkey_position != banana_position:
	for i in range(grid_size):
		for j in range(grid_size):
			if [i,j] == monkey_position:
				print('M', end=' ')
			elif [i,j] == banana_position:
				print('B',end=' ')
			else:
				print('.', end=' ')
		print()

	move = input("Enter a move (left,right,up,down): ").lower()


	if move == "left" and monkey_position[1]>0:
		monkey_position[1] -= 1
	elif move == 'right' and monkey_position[1] < grid_size - 1:
		monkey_position[1] += 1
	elif move == "up" and monkey_position[0] > 0:
		monkey_position[0] -= 1
	elif move == "down" and monkey_position[0] < grid_size - 1:
		monkey_position[0] += 1
	else:
		print("Invalid move Try again")

print("Monkey reached the bananaa 🍌" )
