def File_open(file):
    try:
        with open('windows.txt', 'r') as infile:
            for line in infile:
                print(line, end="")
    except Exception as e:
        print("An unexpected error occured with details: " + str(e))
        return None


File_open('windows.txt')

# except PermissionError