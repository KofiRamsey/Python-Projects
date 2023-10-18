import os

# path
path = "D:\\gtavcars\\gta\\CARS"

obj = os.scandir(path)

# List all files and directories in the specified path
# print("Files and Directories in '% s':" % path)
for entry in obj:
    if entry.is_dir() or entry.is_file():
        print(f'		<Item>dlcpacks:/{entry.name}/</Item>')
