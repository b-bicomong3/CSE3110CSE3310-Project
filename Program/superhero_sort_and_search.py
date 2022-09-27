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


def search(LIST, VALUE):
    """
    search Linearly through the list to end a value
    :param LIST: list (int)
    :param VALUE: int
    :return: bool
    """

    if "D" in VALUE or "M" in VALUE:
        while True:
            if len(VALUE) != 4:
                VALUE = VALUE[:1] + "0" + VALUE[1:]
            else:
                break

    if len(LIST) > 0:
        if LIST[0][0] == VALUE:
            return LIST[0]
        else:
            return search(LIST[1:], VALUE)
    else:
        return False

## -- PROCESSING

def quickSort(LIST, FIRST_INDEX, LAST_INDEX):
    """
    assign the first value as the pivot and place it in its correct location
    :param LIST: list (int)
    :param FIRST_INDEX: (int)
    :param LAST_INDEX: (int)
    :return: None
    """
    if FIRST_INDEX < LAST_INDEX:  # tests that the list is one or more

        PIVOT_VALUE = LIST[FIRST_INDEX]

        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False
        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                LEFT_INDEX += 1

            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE:
                RIGHT_INDEX -= 1

            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1)
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)


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
    quickSort(RAWARR, 0, len(RAWARR) - 1)

    while True:
        SELECT = menu()

        if SELECT == 1:
            for i in range(len(RAWARR)):
                print(f"""
    ID: {RAWARR[i][0]} 
    NAME: {RAWARR[i][1]}""")
        elif SELECT == 2:
            SEARCH = input("What is the Superhero ID? ")
            FOUND = search(RAWARR, SEARCH)
            if not FOUND:
                print("Please enter a valid value")
            else:
                display(FOUND)
        else:
            exit()
