
def sort(width, height, length, mass):
    bulky = True if (width * height * length) >= 1000000 else False
    heavy = True if mass >= 20 else False

    if (bulky and heavy):
        return "REJECTED"
    elif (bulky or heavy):
        return "SPECIAL"
    else:
        return "STANDARD"
