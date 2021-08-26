cel = int(input('Enter the temp in cel format : '))

def cel_to_far(cel):
    return (9*cel+160)/5

far = cel_to_far(cel)
print("Fahrenhite temp : ", far)