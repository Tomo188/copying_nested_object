def copyObject(arr):
    temp = {}
    for element in arr:
        if type(arr[element]) is dict:
            temp[element] = copyObject(arr[element])
        else:
            temp[element] = arr[element]
    return temp
