def codes (code1, code2):
    """
    function create post codes beetwean 2 codes inproved
    code1 - post code 1
    code2 - post code 2
    """
    codesList = []
    firstCode = int(code1[0:2]+code1[3:6])
    secondCode = int(code2[0:2]+code2[3:6])


    if int(firstCode) > int(secondCode):
        codbox = ()
        for code in range(secondCode+1,firstCode):
            codebox = str(firstCode-1)
            codesList.append(codebox[0:2]+ "-" +codebox[2:5])
            firstCode-=1
        return(codesList)

    elif int(firstCode) < int(secondCode):
        codbox = ()
        for code in range(firstCode+1,secondCode):
            codebox = str(secondCode-1)
            codesList.append(codebox[0:2]+ "-" +codebox[2:5])
            secondCode-=1
        return(codesList)
    else:
        return("Codes are same or aren't numbers ")
