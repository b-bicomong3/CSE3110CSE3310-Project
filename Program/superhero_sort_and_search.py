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
    :return: CHOICE
    """
    print("""
    1. Show list of all heroes
    2. Filter list
    3. Search for hero
    4. Exit
    """)

    CHOICE = input("> ")
    CHOICE = int(CHOICE)
    return CHOICE


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


def filterSearch():
    """
    gives user options to filter through list
    :return: CHOICE
    """
    print("""
Search by:
    1. Identity
    2. Align
    3. Eye Color
    4. Hair Color
    5. Existence
    6. Appearances
    7. First Appearance
    8. Year
    9. Brand
    """)

    CHOICE_ONE = input("> ")
    CHOICE_ONE = int(CHOICE_ONE)

    if CHOICE_ONE == 1:
        print("""
Search by:
    1. Public Identity
    2. Secret Identity
    3. No Dual Identity
    4. All     
        """)
    elif CHOICE_ONE == 2:
        print("""
Search by:
    1. Good Characters
    2. Bad Characters
    3. Neutral Characters
    4. All
        """)
    elif CHOICE_ONE == 3:
        print("""
Search by:
    1. Brown Eyes
    2. Blue Eyes
    3. Black Eyes
    4. Green Eyes
    5. Red Eyes
    6. Other Eye Colors
    7. All    
        """)
    elif CHOICE_ONE == 4:
        print("""
Search by:
    1. Brown Hair
    2. Black Hair
    3. Blond Hair
    4. Red Hair
    5. Other Hair Colors
    6. All    
        """)
    elif CHOICE_ONE == 5:
        print("""
Search by:
    1. Living Characters
    2. Deceased Characters
    3. All
        """)
    elif CHOICE_ONE == 7:
        print("""
Search by:
    1. Jan
    2. Feb
    3. Mar
    4. Apr
    5. May
    6. Jun
    7. Jul
    8. Aug
    9. Sep
    10. Oct
    11. Nov
    12. Dec
    13. All        
        """)
    elif CHOICE_ONE == 9:
        print("""
Search by:
    1. Marvel
    2. DC
    3. All
        """)

    if CHOICE_ONE != 6 or 8:
        CHOICE_TWO = input("> ")
        CHOICE_TWO = int(CHOICE_TWO)
    else:
        CHOICE_TWO = 0

    return CHOICE_ONE, CHOICE_TWO


## -- PROCESSING

def insertionSort(LIST):
    """
    splits the list into a sorted and unsorted half and then takes the lowest index of the unsorted section and places it in its relative position in the sorted section.
    :param LIST:
    :return:
    """
    for i in range(1, len(LIST)):
        IND_VALUE = LIST[i]  # Saving the value of the lowest index in unsorted
        SORTED_IND = i - 1  # Identify largest of sorted section

        while SORTED_IND >= 0 and IND_VALUE < LIST[SORTED_IND]:
            # While traversing tail-to-head in the sorted section
            LIST[SORTED_IND + 1] = LIST[SORTED_IND]
            SORTED_IND = SORTED_IND - 1
        LIST[SORTED_IND + 1] = IND_VALUE  # Places value in correct index


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


def filterID(SELECT, LIST):
    """
    filters using ID as filter
    :param SELECT:
    :param LIST:
    :return:
    """
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == "Public Identity":
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == "Secret Identity":
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == "No Dual Identity":
                FOUND.append(RAWARR[i])
    if SELECT != 4:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
         Superhero ID: {NEW_LIST[0]}
         Name: {NEW_LIST[1]}
         ID: {NEW_LIST[2]}""")

        print(f"There are {len(FOUND)} superheros with a {NEW_LIST[2]}")
    else:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         ID: {RAWARR[i][2]}""")


def filterAlign(SELECT, LIST):
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == "Good Characters":
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == "Bad Characters":
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == "Neutral Characters":
                FOUND.append(RAWARR[i])
    if SELECT != 4:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
        Superhero ID: {NEW_LIST[0]}
        Name: {NEW_LIST[1]}
        ALIGN: {NEW_LIST[3]}""")

        print(f"There are {len(FOUND)} {NEW_LIST[3]}")
    else:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == "":
                RAWARR[i].insert(3, "UNKNOWN")
            print(f"""
        Superhero ID: {RAWARR[i][0]}
        Name: {RAWARR[i][1]}
        ALIGN: {RAWARR[i][3]}""")


def filterEyes(SELECT, LIST):
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == "Brown Eyes":
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == "Blue Eyes":
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == "Black Eyes":
                FOUND.append(RAWARR[i])
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == "Green Eyes":
                FOUND.append(RAWARR[i])
    elif SELECT == 5:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == "Red Eyes":
                try:
                    FOUND.append(RAWARR[i])
                except IndexError:
                    continue
    elif SELECT == 6:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] != "Brown Eyes" and RAWARR[i][4] != "Blue Eyes" and RAWARR[i][4] != "Black Eyes" and \
                    RAWARR[i][4] != "Green Eyes" and RAWARR[i][4] != "Red Eyes":
                FOUND.append(RAWARR[i])
    if SELECT != 7:
        for i in range(len(FOUND)):
            try:
                if FOUND[i][4] == "":
                    FOUND[i].insert(4, "UNKNOWN")
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
         Superhero ID: {NEW_LIST[0]}
         Name: {NEW_LIST[1]}
         Eyes: {NEW_LIST[4]}""")

        if SELECT != 6:
            print(f"There are {len(FOUND)} superheros with {NEW_LIST[4]}")
        else:
            print(f"There are {len(FOUND)} superheros with other eye colors")
    else:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         ID: {RAWARR[i][4]}""")

def filterHair(SELECT, LIST):

def filterExistence(SELECT, LIST):

def filterFirstApperance(SELECT, LIST):

def filterBrand(SELECT, LIST):
## --- MAIN PROGRAM --- ##

if __name__ == "__main__":
    intro()
    RAWARR, HEADERS = getRawData('../comicBookCharData_mixed.csv')
    # rawArr is a 2D arrays holding all the Superhero data
    # headers is a variable that holds the List of all the column headers.
    insertionSort(RAWARR)

    while True:
        SELECT = menu()

        if SELECT == 1:
            for i in range(len(RAWARR)):
                print(f"""
    ID: {RAWARR[i][0]} 
    NAME: {RAWARR[i][1]}""")
        elif SELECT == 2:
            CHOICE_ONE, CHOICE_TWO = filterSearch()
            if CHOICE_ONE == 1:
                filterID(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 2:
                filterAlign(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 3:
                filterEyes(CHOICE_TWO, RAWARR)
        elif SELECT == 3:
            FOUND = search(RAWARR)
            display(FOUND)
        elif SELECT == 4:
            exit()
        else:
            print("Please enter a valid number")
