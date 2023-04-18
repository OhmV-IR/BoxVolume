invalidinput = True
while(invalidinput):
    sides = input("What is the side length of the box(m): ")
    depth = input("What is the depth of the box(m): ")
    invalidinput = False
    try: 
        sides = int(sides)
        depth = int(depth)
    except:
        print("error converting input to integer please try again")
        invalidinput = True
volume = sides * 4 * depth
print(str(volume) + 'm³')
print("cube area: " + str(sides * 4) + 'm²')