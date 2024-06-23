import random

def generate_path(N, M):
	maze = {(i, j): 0 for i in range(N) for j in range(M)}
	path = [(0, 0)]
	while path[-1] != (N-1, M-1):
		x, y = path[-1]
		if x == N-1:
			path.append((x, y+1))
		elif y == M-1:
			path.append((x+1, y))
		else:
			if random.choice([0, 1]) == 0:
				path.append((x+1, y))
			else:
				path.append((x, y+1))
	for cell in path:
		maze[cell] = 2
	return maze

def add_obstacles(maze, min_obstacles, N, M):
	max_obstacles = N * M - 2  # excluding start and end points
	if min_obstacles > max_obstacles:
		raise ValueError("Minimum number of obstacles exceeds maximum possible.")
	for _ in range(min_obstacles):
		while True:
			x, y = random.randint(0, N-1), random.randint(0, M-1)
			if maze[(x, y)] == 0:
				maze[(x, y)] = 1
				break
	return maze

def set_obstacle(maze, N, M):
	while True:
		try:
			x, y = map(int, input("Enter coordinates to set obstacle (row column): ").split())
			if x < 0 or x >= N or y < 0 or y >= M:
				print("Coordinates are out of bounds.")
			elif maze[(x, y)] == 2:
				print("You cannot set obstacle on the path.")
			else:
				maze[(x, y)] = 1
				break
		except ValueError:
			print("Invalid input. Please enter integers separated by space.")
		except KeyError:
			print("Invalid coordinates. Please enter coordinates within the maze.")

def remove_obstacle(maze, N, M):
	while True:
		try:
			x, y = map(int, input("Enter coordinates to remove obstacle (row column): ").split())
			if x < 0 or x >= N or y < 0 or y >= M:
				print("Coordinates are out of bounds.")
			elif maze[(x, y)] == 2:
				print("You cannot remove obstacle from the path.")
			else:
				maze[(x, y)] = 0
				break
		except ValueError:
			print("Invalid input. Please enter integers separated by space.")
		except KeyError:
			print("Invalid coordinates. Please enter coordinates within the maze.")

def print_maze(maze, N, M):
	for i in range(N):
		for j in range(M):
			if maze[(i, j)] == 0:
				print(' ', end=' ')
			elif maze[(i, j)] == 1:
				print('X', end=' ')
			else:
				print('O', end=' ')
		print()

def main():
	try:
		filename = input("Enter the filename (grid77.txt or grid99.txt): ")
		with open(filename) as file:
			N, M = map(int, file.readline().split())
			maze = generate_path(N, M)
			print("Generated maze:")
			print_path(maze, N, M)
			min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
			maze = add_obstacles(maze, min_obstacles, N, M)
			print("Maze with obstacles:")
			print_path(maze, N, M)
			while True:
				print("\nOptions:")
				print("1. Set obstacle")
				print("2. Remove obstacle")
				print("3. Print maze")
				print("4. Exit")
				choice = int(input("Enter your choice: "))
				if choice == 1:
					set_obstacle(maze, N, M)
					print("Updated maze:")
					print_path(maze, N, M)
				elif choice == 2:
					remove_obstacle(maze, N, M)
					print("Updated maze:")
					print_path(maze, N, M)
				elif choice == 3:
					print("Current maze:")
					print_path(maze, N, M)
				elif choice == 4:
					print("Exiting program.")
					break
				else:
					print("Invalid choice. Please enter a number from 1 to 4.")
	except FileNotFoundError:
		print("File not found. Please enter a valid filename.")
	except ValueError:
		print("Invalid input. Please enter an integer.")
	except Exception as e:
		print("An error occurred:", e)

if __name__ == "__main__":
	main()
