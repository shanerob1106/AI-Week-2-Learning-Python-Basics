
# Collecting the length and width of each room
r1length = int(input("Please enter length of room 1: "))
r1width = int(input("Please enter width of room 1: "))

r2length = int(input("Please enter length of room 2: "))
r2width = int(input("Please enter width of room 2: "))

r3length = int(input("Please enter length of room 3: "))
r3width = int(input("Please enter width of room 3: "))

r4length = int(input("Please enter length of room 4: "))
r4width = int(input("Please enter width of room 4: "))

# calculating area of each room 
room1 = r1length * r1width
room2 = r2length * r2width
room3 = r3length * r3width
room4 = r4length * r4width

# Sum of all areas to find total footage of the house
house = room1 + room2 + room3 + room4

# Final output of all rooms
print("Room one area: ", room1)
print("Room two area: ", room2)
print("Room three area: ", room3)
print("Room four area: ", room4)
print("Total house area: ", house)