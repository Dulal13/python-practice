with open('poem.txt') as f:
    data = f.read().lower()

    if 'twinkle' in data:
        print("Found")
    else:
        print('Not found')