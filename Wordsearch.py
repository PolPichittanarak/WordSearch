import random


class coordinates:
	def __init__(self):
		self.x = 0
		self.y = 0




def build_grid(size):
	grid = []
	for line in range(size):
		row = []
		for cell in range(size):
			ran_ascii = random.randint(65, 90)
			character = chr(ran_ascii)
			row.append(character)
		grid.append(row)
	return grid

def print_grid(grid):
	for row in grid:
		for cell in row:
			print(cell, end = " | ")
		print()
		print("-"* (4*len(row)))
		
def enter_words():
	words = []
	print("enter one word at a time \nenter stop once you are done (the word 'stop' is invalid)")
	userword = ""
	while userword != "stop":
		userword = input("Enter a word :").upper()
		if userword.isdigit():
			print("only string type input is allowed")
			continue
		words.append(userword)
	return words

def load_words_from_file():
	words = []
	filename = input("Enter filename:")
	wordfile = open(filename, "r")
	file_content = wordfile.readlines()
	for line in file_content:
		words.append(line.upper())
	return words

def load_words():
	userchoice = input("would you like to type in words of your choice or load from the file (1 or 2)")
	if userchoice == "1":
		words = load_words()
	elif userchoice == "2":
		words = load_words_from_file()
	return words

	
def add_word_to_grid(grid, word, x_origin, y_origin, direction, protected_cells):
	#InitX = x_origin
	#InitY = y_origin
	protected_cells = protected_cells
	
	for count, letter in enumerate(word):
		for y, row in grid:
			for x, cell in row:
				if y == y_origin and x == x_origin:
					grid[y.origin][x.origin] = letter
					prot_cell = [y.origin, x.origin]
					protected_cells.append(prot_cell)
				if direction == "horizontal":
					x_origin += 1
				elif direction == "vertical":
					y_origin += 1
				elif direction == "diagonal":
					x_origin += 1
					y_origin += 1
	return_list = [grid, protected_cells]
	return return_list
				

def attempt_word_setting(word, grid):
	current_row = size
	current_column = size
	for letter in word:
		for indexY, row in enumerate(grid):
			for indexX, cell in enumerate(row):
				if cell == letter:
					letter_x = indexX
					letter_y = indexY
					if letter_x > current_column or letter_y > current_row:
						return False
					
				indices = [indexY, indexX]
				if indices in protected_cells:
					if letter != cell:
						return False
	return True


protected_cells = []
size = 10
grid = build_grid(size)
print_grid(grid)
