
def returnChoiceFromList(listIn):
    """This function will return a choice from a list and the remaining list
    with the choice removed.
    We are assuming that the list is made up of strings.
    Note that to account for 0 indexing we are subtracting 1 when we assign the
    variable choice
    """
    count = 1
    for item in listIn:
        capItem = item.capitalize()  # what if it is not a string?/ capitalization nonPermanent
        print(f'{count}. ', capItem)
        count += 1
    getChoice = int(input('\nWhich would you like to choose?: '))
    choice = listIn[getChoice - 1]
    listIn.remove(choice)
    return choice, listIn

def returnChoiceFromListOfObjects(objListIn):
    """This function will return a choice from a list of objects and the remaining
    list of objects with the choice removed.

    It is assumed that the objects have a name attribute.
    """
    nameStrList = []
    for object in objListIn:
        nameStrList.append(object.name)

    choiceName, remList = returnChoiceFromList(nameStrList)
    # remove object that was chosen
    for object in objListIn:
        if object.name == choiceName:
            objListIn.remove(object)

    return choiceName, objListIn



if __name__ == "__main__":
    from delMe import *
    a = Student('Albert', 17, 2345)
    b = Student('Betty', 15, 5467)
    c = Student('Charles', 14, 6587)
    studentList = [a, b, c]
    choice, listOut = returnChoiceFromListOfObjects(studentList)
    print(choice)
    print()
    for student in listOut:
        print(student)
