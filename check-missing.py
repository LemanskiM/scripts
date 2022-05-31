
def missing (inputList,howManyElements):
    """
    Checking missing elements in incloude list in function
    list - list input to function
    howManyElements - size of list
    """
    list = []
    missingElementsList = []

    for i in range(howManyElements):
#create template list
        list.append(howManyElements)
        howManyElements-=1
    list.reverse()

    for j in list:
#checking missing int in template list
        if j in inputList:
            pass
        else:
            missingElementsList.append(j)
    return missingElementsList

print(missing([1,2,5,9,111,121,122,125],400))
#help(missing)
