def draw_right_triangle(width):
    for i in range(1, width + 1):
        for j in range(i):
            print('*', end='')
        print()

# Take input from the user
base_height = int(input("Enter the arrow base height: "))
base_width = int(input("Enter the arrow base width: "))

arrow_head_width = int(input("Enter the arrow head width (larger than base width): "))
while arrow_head_width <= base_width:
    print("Arrow head width must be larger than base width.")
    arrow_head_width = int(input("Enter the arrow head width (larger than base width): "))

# Call the draw_rectangle function
draw_rectangle(base_height, base_width)

# Call the draw_right_triangle function
draw_right_triangle(arrow_head_width)
