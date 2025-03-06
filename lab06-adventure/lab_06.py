
class Room:
    """
    Room class
    """
    def __init__(self,description,north,east,south,west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []

    receiver = Room("You are in the receiver",1,None,None,None)
    kitchen = Room("You are in the kitchen",None,1,None,None)
    hall = Room("You are in the hall",4,3,0,2)
    restroom = Room("You are in the restroom",None,4,3,None)
    living_room = Room("You are in the living room",None,5,1,None)
    bathroom = Room("You are in the bathroom",5,None,None,1)

    room_list += [receiver]
    room_list += [hall]
    room_list += [kitchen]
    room_list += [bathroom]
    room_list += [living_room]
    room_list += [restroom]

    current_room = 0
    next_room = 0
    nope = "You can't go that way"
    done = True
    while done:
        print(room_list[current_room].description)
        action = str(input("Where to go now?\n"))
        if action=="N" or action=="n" or action=="North" or action=="NORTH" or action=="north":
            if room_list[current_room].north is None:
                print(nope)
            else:
                next_room = room_list[current_room].north
        elif action=="S" or action=="s" or action=="South" or action=="SOUTH" or action=="south":
            if room_list[current_room].south is None:
                print(nope)
            else:
                next_room = room_list[current_room].south
        elif action=="E" or action=="e" or action=="East" or action=="EAST" or action=="east":
            if room_list[current_room].east is None:
                print(nope)
            else:
                next_room = room_list[current_room].east
        elif action=="W" or action=="w" or action=="West" or action=="WEST" or action=="west":
            if room_list[current_room].west is None:
                print(nope)
            else:
                next_room = room_list[current_room].west
        elif action=="Exit" and current_room == 0:
            print("Bye bye!")
            done = False
        elif action == "Exit" and current_room != 0:
            print("You need to be in the receiver!")
        else:
            print("Invalid entry")
        current_room = next_room
main()