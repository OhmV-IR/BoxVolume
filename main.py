invalidinput = True
while(invalidinput):
    sides = input("What is the side length of the box(m): ")
    depth = input("What is the depth of the box(m): ")
    invalidinput = False
    try: 
        sides = float(sides)
        depth = float(depth)
    except:
        print("error converting input to float please try again")
        invalidinput = True
volume = sides * 4 * depth
print('volume: ' +str(volume) + 'm³')
print("cube area: " + str(sides * 4) + 'm²')