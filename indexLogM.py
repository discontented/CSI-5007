def indexLogM(symbolArray, start, end):
    if(symbolArray[start] == 0 & symbolArray[end] == 0):
        return indexLogM(symbolArray, end, min(2*end, symbolArray.length))
    if (symbolArray[start] == 0 & symbolArray[end] == 1):
        return