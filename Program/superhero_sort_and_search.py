# superhero_sort_and_search

"""
Title: Superhero Sort and Search
Author: Beatrix Bicomong
Date-created: 19-09-2022
"""

### --- LIST AND DICTIONARIES --- ###


FILTER = ("Identity", "Align", "Eye Color", "Hair Color", "Existence", "Appearances", "First Appearance", "Year", "Brand")
ID = ("Public Identity", "Secret Identity", "No Dual Identity", "All")
ALIGN = ("Good Characters", "Bad Characters", "Neutral Characters", "All")
EYES = ("Brown Eyes", "Blue Eyes", "Black Eyes", "Green Eyes", "Red Eyes", "Other Eye Colors", "All")
HAIR = ("Brown Hair", "Black Hair", "Blond Hair", "Red Hair", "Other Hair Colors", "Bald/No Hair", "All")
EXISTENCE = ("Living Characters", "Deceased Characters", "All")
BRAND = ("Marvel", "DC", "All")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "All")
MONTHS_FULL = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
MONTHS_TRY = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}


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


def editRawData(file):
    """
    edits through raw data for blanks in list and inserts "UNKNOWN"
    :param file: list
    :return: list
    """
    for i in range(len(RAWARR)):
        for j in range(len(RAWARR[i])):
            if RAWARR[i][j] == "":
                RAWARR[i].insert(j, "UNKNOWN")
    return RAWARR


def editMonths(file):
    """
    edits through months in the list and converts to one common layout
    :param file: list
    :return: list
    """
    global MONTHS, MONTHS_FULL, MONTHS_TRY
    for i in range(len(RAWARR)):
        TEMP = RAWARR[i][8].split("-")
        if TEMP[0] in MONTHS:
            MONTH_TEMP = MONTHS_TRY[TEMP[0]]
            YEAR_TEMP = int(TEMP[1]) + 1900
            LIST_TEMP = str(YEAR_TEMP), MONTH_TEMP
            NEW_VALUE = ", ".join(LIST_TEMP)
            RAWARR[i][8] = NEW_VALUE

    return RAWARR


def intro():
    """
    shows the title of the program
    :return: None
    """
    print("Welcome to Superhero Sort and Search")


## --- INPUTS

def menu():
    """
    displays user menu
    :return: CHOICE (int)
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

    if "D" in VALUE or "M" in VALUE:
        while True:
            if len(VALUE) != 4:
                VALUE = VALUE[:1] + "0" + VALUE[1:]
            else:
                break

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
    global FILTER, ID, ALIGN, EYES, HAIR, EXISTENCE, BRAND, MONTHS

    print("Search by:")
    for i in range(len(FILTER)):
        print(f"{i + 1}. {FILTER[i]}")

    CHOICE_ONE = input("> ")
    CHOICE_ONE = int(CHOICE_ONE)

    if CHOICE_ONE == 1:
        print("Search by:")
        for i in range(len(ID)):
            print(f"{i + 1}. {ID[i]}")
    elif CHOICE_ONE == 2:
        print("Search by:")
        for i in range(len(ALIGN)):
            print(f"{i + 1}. {ALIGN[i]}")
    elif CHOICE_ONE == 3:
        print("Search by:")
        for i in range(len(EYES)):
            print(f"{i + 1}. {EYES[i]}")
    elif CHOICE_ONE == 4:
        print("Search by:")
        for i in range(len(HAIR)):
            print(f"{i + 1}. {HAIR[i]}")
    elif CHOICE_ONE == 5:
        print("Search by:")
        for i in range(len(EXISTENCE)):
            print(f"{i + 1}. {EXISTENCE[i]}")
    elif CHOICE_ONE == 7:
        print("Search by:")
        for i in range(len(MONTHS)):
            print(f"{i + 1}. {MONTHS[i]}")
    elif CHOICE_ONE == 9:
        print("Search by:")
        for i in range(len(BRAND)):
            print(f"{i + 1}. {BRAND[i]}")

    if CHOICE_ONE == 6 and CHOICE_ONE == 8:
        CHOICE_TWO = 0
    elif CHOICE_ONE == 0:
        CHOICE_TWO = -1
    else:
        CHOICE_TWO = input("> ")
        CHOICE_TWO = int(CHOICE_TWO)

    return CHOICE_ONE, CHOICE_TWO


## -- PROCESSING

def insertionSort(LIST):
    """
    splits the list into a sorted and unsorted half and then takes the lowest index of the unsorted section and places it in its relative position in the sorted section.
    :param LIST: list
    :return: None
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
    :param HERO: list
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
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global ID
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == ID[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == ID[1]:
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][2] == ID[2]:
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
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         ID: {RAWARR[i][2]}""")


def filterAlign(SELECT, LIST):
    """
    filters using alignment as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global ALIGN
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == ALIGN[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == ALIGN[1]:
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][3] == ALIGN[2]:
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
        Align: {NEW_LIST[3]}""")

        print(f"There are {len(FOUND)} {NEW_LIST[3]}")
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            print(f"""
        Superhero ID: {RAWARR[i][0]}
        Name: {RAWARR[i][1]}
        Align: {RAWARR[i][3]}""")


def filterEyes(SELECT, LIST):
    """
    filters using eye color as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global EYES
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == EYES[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == EYES[1]:
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == EYES[2]:
                FOUND.append(RAWARR[i])
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == EYES[3]:
                FOUND.append(RAWARR[i])
    elif SELECT == 5:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] == EYES[4]:
                FOUND.append(RAWARR[i])
    elif SELECT == 6:
        for i in range(len(RAWARR)):
            if RAWARR[i][4] != EYES[0] and RAWARR[i][4] != EYES[1] and RAWARR[i][4] != EYES[2] and \
                    RAWARR[i][4] != EYES[3] and RAWARR[i][4] != EYES[4]:
                FOUND.append(RAWARR[i])
    if SELECT != 7:
        for i in range(len(FOUND)):
            try:
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
    elif SELECT == 7:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         Eyes: {RAWARR[i][4]}""")


def filterHair(SELECT, LIST):
    """
    filters using hair color as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global HAIR
    TEMP = HAIR[5].split("/")
    BALD = TEMP[0]
    NO_HAIR = TEMP[1]

    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] == HAIR[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] == HAIR[1]:
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] == HAIR[2]:
                FOUND.append(RAWARR[i])
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] == HAIR[3]:
                FOUND.append(RAWARR[i])
    elif SELECT == 5:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] != HAIR[0] and RAWARR[i][5] != HAIR[1] and RAWARR[i][5] != HAIR[2] and \
                    RAWARR[i][5] != HAIR[3]:
                FOUND.append(RAWARR[i])
    elif SELECT == 6:
        for i in range(len(RAWARR)):
            if RAWARR[i][5] == BALD or RAWARR[i][5] == NO_HAIR:
                FOUND.append(RAWARR[i])
    if SELECT != 7:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
         Superhero ID: {NEW_LIST[0]}
         Name: {NEW_LIST[1]}
         Hair: {NEW_LIST[5]}""")

        if SELECT != 7 and SELECT != 6:
            print(f"There are {len(FOUND)} superheros with {NEW_LIST[5]}")
        elif SELECT == 6:
            print(f"There are {len(FOUND)} superheroes with no hair")
        else:
            print(f"There are {len(FOUND)} superheros with other hair colors")
    elif SELECT == 7:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         Hair: {RAWARR[i][5]}""")


def filterExistence(SELECT, LIST):
    """
    filters using existence as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global EXISTENCE
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][6] == EXISTENCE[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][6] == EXISTENCE[1]:
                FOUND.append(RAWARR[i])
    if SELECT != 3:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
         Superhero ID: {NEW_LIST[0]}
         Name: {NEW_LIST[1]}
         Existence: {NEW_LIST[6]}""")

        print(f"There are {len(FOUND)} superheros who are {NEW_LIST[6]}")
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         Existence: {RAWARR[i][6]}""")
    else:
        print("Please enter a valid number")


def filterFirstApperance(SELECT, LIST):
    """
    filters using first appearance as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global MONTHS, MONTHS_FULL, MONTHS_TRY
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[0] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[1] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 3:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[2] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 4:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[3] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 5:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[4] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 6:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[5] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 7:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[6] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 8:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[7] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 9:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[8] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 10:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[9] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 11:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[10] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    elif SELECT == 12:
        for i in range(len(RAWARR)):
            if MONTHS_FULL[11] in RAWARR[i][8]:
                FOUND.append(RAWARR[i])
    if SELECT != 13:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
        Superhero ID: {NEW_LIST[0]}
        Name: {NEW_LIST[1]}
        Date: {NEW_LIST[8]}""")

        TEMP = NEW_LIST[8]
        TEMP_MONTH = TEMP.split(", ")
        NEW_MONTH = TEMP_MONTH[1]

        print(f"There are {len(FOUND)} superheros who appeared in the month of {NEW_MONTH}")
    elif SELECT == 13:
        for i in range(len(RAWARR)):
            print(f"""
        Superhero ID: {RAWARR[i][0]}
        Name: {RAWARR[i][1]}
        Date: {RAWARR[i][8]}""")
    else:
        print("Please enter a valid number")


def filterBrand(SELECT, LIST):
    """
    filters using branding as filter
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    global BRAND
    FOUND = []
    if SELECT == 1:
        for i in range(len(RAWARR)):
            if RAWARR[i][10] == BRAND[0]:
                FOUND.append(RAWARR[i])
    elif SELECT == 2:
        for i in range(len(RAWARR)):
            if RAWARR[i][10] == BRAND[1]:
                FOUND.append(RAWARR[i])
    if SELECT != 3:
        for i in range(len(FOUND)):
            try:
                NEW_LIST = FOUND.pop(i)
            except IndexError:
                break
            print(f"""
         Superhero ID: {NEW_LIST[0]}
         Name: {NEW_LIST[1]}
         Brand: {NEW_LIST[10]}""")

        print(f"There are {len(FOUND)} superheros who are from {NEW_LIST[10]}")

    elif SELECT == 3:
        for i in range(len(RAWARR)):
            print(f"""
         Superhero ID: {RAWARR[i][0]}
         Name: {RAWARR[i][1]}
         Brand: {RAWARR[i][10]}""")


def filterOther(SELECT, LIST):
    """
    filters either using the year alone of the superhero or the amount of appearances of the superheros
    :param SELECT: int
    :param LIST: list
    :return: None
    """
    for i in range(len(RAWARR)):
        if CHOICE_ONE == 6:
            print(f"""
        Superhero ID: {RAWARR[i][0]}
        Name: {RAWARR[i][1]}
        Appearances: {RAWARR[i][7]}""")
        else:
            print(f"""
        Superhero ID: {RAWARR[i][0]}
        Name: {RAWARR[i][1]}
        Appearances: {RAWARR[i][9]}""")


## --- MAIN PROGRAM --- ##

if __name__ == "__main__":
    intro()
    RAWARR, HEADERS = getRawData('../comicBookCharData_mixed.csv')
    editRawData(RAWARR)
    editMonths(RAWARR)
    # rawArr is a 2D arrays holding all the Superhero data
    # headers is a variable that holds the List of all the column headers.
    insertionSort(RAWARR)

    while True:
        SELECT = menu()
        ### INPUTS
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
            elif CHOICE_ONE == 4:
                filterHair(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 5:
                filterExistence(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 7:
                filterFirstApperance(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 9:
                filterBrand(CHOICE_TWO, RAWARR)
            elif CHOICE_ONE == 6 or CHOICE_ONE == 8:
                filterOther(CHOICE_ONE, RAWARR)
        elif SELECT == 3:
            FOUND = search(RAWARR)
            display(FOUND)
        elif SELECT == 4:
            exit()
        else:
            print("Please enter a valid number")