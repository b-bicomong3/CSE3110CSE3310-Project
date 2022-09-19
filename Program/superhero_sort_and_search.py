# superhero_sort_and_search

"""
Title: Superhero Sort and Search
Author: Beatrix Bicomong
Date-created: 19-09-2022
"""


## --- SUBROUTINE -- ##

def getRawData(fileName):
    import csv
    TEMPLI = []
    FILE = open(fileName)
    TEXT = csv.reader(FILE)
    for line in TEXT:
        TEMPLI.append(line)
    VAR = TEMPLI.pop(0)
    return TEMPLI, VAR


def intro():
    print("Welcome to Superhero Sort and Search")


## --- INPUTS

def menu():
    """
    displays user menu
    :return:
    """
    print("""
    1. Show list of heroes
    2. Search for hero
    3. Exit
    """)

    CHOICE = input("> ")

    try:
        CHOICE = int(CHOICE)
        return CHOICE
    except ValueError:
        print("Please enter a valid number")
        return menu()


def search(LIST):
    """
    searches for hero's id
    :param LIST: list
    :return: list
    """
    VALUE = input("What is the Superhero ID? ")

    for i in range(len(RAWARR)):
        if RAWARR[i][0] == VALUE:
            FOUND = RAWARR.pop(i)
            return FOUND
    if RAWARR[i][0] != VALUE:
        print("Entry is invalid!")
        return search(LIST)


## -- PROCESSING

def selectionSort(LIST):
    """
    compares the current index value with the rest of the set. It will find the
    lowest value in the set and place it in the lowest index of the unsorted part of the list.
    :param LIST: list (int)
    :return: None
    """
    for i in range(len(LIST) - 1):  # for each place in the list (except the last)
        MIN_IND = i  # assume the index w/ lowest value is i
        for j in range(i + 1, len(LIST)):  # for each place after i (includes the last)
            if LIST[j] < LIST[MIN_IND]:  # test if subsequent value is less than the current assumed minimum
                MIN_IND = j  # update the index of the current assumed min value
        if LIST[MIN_IND] < LIST[i]:  # test if minimum value is not at the start of the unsorted list
            # swaps the min value with the lowest index in the unsorted part of the list
            TEMP = LIST[i]
            LIST[i] = LIST[MIN_IND]
            LIST[MIN_IND] = TEMP


## -- OUTPUTS

def display(HERO):
    """
    displays hero's information
    :param HERO:
    :return: None
    """
    print(f"""
    Superhero ID: {HERO[0]}
    Name: {HERO[1]}
    ID: {HERO[2]}
    ALIGN: {HERO[3]}
    EYE: {HERO[4]}
    HAIR: {HERO[5]}
    ALIVE: {HERO[6]}
    APPEARANCES: {HERO[7]}
    FIRST APPEARANCE: {HERO[8]}
    YEAR: {HERO[9]}
    Brand: {HERO[10]}
""")


## --- MAIN PROGRAM --- ##

if __name__ == "__main__":
    intro()
    RAWARR, HEADERS = getRawData('../comicBookCharData_mixed.csv')
    # rawArr is a 2D arrays holding all the Superhero data
    # headers is a variable that holds the List of all the column headers.
    selectionSort(RAWARR)

    while True:
        SELECT = menu()

        if SELECT == 1:
            for i in range(len(RAWARR)):
                print(RAWARR[i][:2])
        elif SELECT == 2:
            FOUND = search(RAWARR)
            display(FOUND)
        else:
            exit()
