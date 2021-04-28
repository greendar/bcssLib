
def returnChoiceFromList(listIn):
    """This function will return a choice from a list and the remaining list
    with the choice removed.
    We are assuming that the list is made up of strings.
    Note that to account for 0 indexing we are subtracting 1 when we assign the
    variable choice
    """

    count = 1
    for item in listIn:
        capItem = item.capitalize()  # what if it is not a string?
        print(f'{count}. ', capItem)
        count += 1
    getChoice = int(input('\nWhich would you like to choose?: '))
    choice = listIn[getChoice - 1]
    listIn.remove(choice)
    return choice, listIn



if __name__ == "__main__":
    myList = ['Apple', 'Carrot', 'dragon']
    a, myList = returnChoiceFromList(myList)
    print(a, myList)
