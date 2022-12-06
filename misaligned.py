
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            num = i*5+j
            print(f'{num} | {major} | {minor}')
            
    return len(major_colors) * len(minor_colors), num


result, num = print_color_map()
print("All is well (maybe!)\n")
