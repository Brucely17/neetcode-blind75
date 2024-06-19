# using set to solve


def containsDuplicate(array):
    setarray=set(array)

    if len(setarray)!=len(array):
        return True
    return False

print(containsDuplicate([1,2,3,1]))