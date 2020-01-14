def convert(w,h,px):
    newpx = []
    asciiGrid = []
    
    for x in range(0, w):
        for y in range(0, h):
            color = px[x,y]
            newpx.append(color)
            if color <= 30:
                asciiGrid.append(" ▓ ")
            elif color > 30 and color < 60:
                asciiGrid.append(" @ ")
            elif color > 60 and color < 90:
                asciiGrid.append(" % ")
            elif color > 90 and color < 120:
                asciiGrid.append(" B ")
            elif color > 120 and color < 150:
                asciiGrid.append(" 0 ")
            elif color > 150 and color < 180:
                asciiGrid.append(" O ")
            elif color > 180 and color < 210:
                asciiGrid.append(" C ")
            elif color > 210 and color < 240:
                asciiGrid.append(" # ")
            else :
                asciiGrid.append("   ")

    asciiImg = ""
    
    # loop through the array of ASCII characters, adding a line break after every 150px
    for x in range(0, len(asciiGrid)):
        asciiImg += asciiGrid[x]
        if x % 150 == 0:
            asciiImg += "\n"
    return asciiImg
    print("ASCII conversion successful!")