from enum import Enum
from dataclasses import dataclass

class LocationType(Enum):
    WALL = "#"
    OBJECT = "O"
    LEFT_BOX = "["
    RIGHT_BOX = "]"
    ROBOT = "@"
    EMPTY = "."

@dataclass
class Location:
    x: int
    y: int
    type: LocationType

    @property
    def gps_coordinates(self):
        if self.type == LocationType.LEFT_BOX:
            return self.x * 100 + self.y
        else:
            return 0

class Room:
    def __init__(self, room_input):
        self.room_input = room_input
        self.locations = []
        self.robot_location = None
        self.parse_room_input()

    def parse_room_input(self):
        for i, row in enumerate(self.room_input.split("\n")):
            r = []
            for j, col in enumerate(row):
                match col:
                    case LocationType.ROBOT.value:
                        self.robot_location = Location(i, j*2, LocationType.ROBOT)
                        r.append(Location(i, j*2, LocationType.ROBOT))
                        r.append(Location(i, j*2+1, LocationType.EMPTY))
                    case LocationType.OBJECT.value:
                        r.append(Location(i, j*2, LocationType.LEFT_BOX))
                        r.append(Location(i, j*2+1, LocationType.RIGHT_BOX))
                    case LocationType.WALL.value:
                        r.append(Location(i, j*2, LocationType.WALL))
                        r.append(Location(i, j*2+1, LocationType.WALL))
                    case LocationType.EMPTY.value:
                        r.append(Location(i, j*2, LocationType.EMPTY))
                        r.append(Location(i, j*2+1, LocationType.EMPTY))

            self.locations.append(r)

    def can_move(self, location, direction):
        new_location = self.get_new_location(location, direction)
        match self.locations[new_location.x][new_location.y].type, direction:
            case LocationType.EMPTY, _:
                return True
            case LocationType.LEFT_BOX, "^" | "v":
                right_box = self.locations[new_location.x][new_location.y + 1]
                return self.can_move(new_location, direction) and self.can_move(right_box, direction)
            case LocationType.RIGHT_BOX, "^" | "v":
                left_box = self.locations[new_location.x][new_location.y - 1]
                return self.can_move(new_location, direction) and self.can_move(left_box, direction)
            case LocationType.LEFT_BOX | LocationType.RIGHT_BOX, "<" | ">":
                return self.can_move(new_location, direction)
            case LocationType.WALL, _:
                return False

    def move_location(self, old_location, direction):
        new_location = self.get_new_location(old_location, direction)
        match self.locations[new_location.x][new_location.y].type, direction:
            case LocationType.EMPTY, _:
                self.locations[new_location.x][new_location.y] = new_location
                self.locations[old_location.x][old_location.y].type = LocationType.EMPTY
            case LocationType.LEFT_BOX, "^" | "v":
                self.move_location(self.locations[new_location.x][new_location.y], direction)
                self.locations[new_location.x][new_location.y] = new_location
                self.locations[old_location.x][old_location.y].type = LocationType.EMPTY

                # Right Box
                self.move_location(self.locations[new_location.x][new_location.y + 1], direction)
            case LocationType.RIGHT_BOX, "^" | "v":
                self.move_location(self.locations[new_location.x][new_location.y], direction)
                self.locations[new_location.x][new_location.y] = new_location
                self.locations[old_location.x][old_location.y].type = LocationType.EMPTY

                # Left Box
                self.move_location(self.locations[new_location.x][new_location.y - 1], direction)
            case LocationType.LEFT_BOX | LocationType.RIGHT_BOX, "<" | ">":
                self.move_location(self.locations[new_location.x][new_location.y], direction)
                self.locations[new_location.x][new_location.y] = new_location
                self.locations[old_location.x][old_location.y].type = LocationType.EMPTY
            case LocationType.WALL, _:
                raise Exception("Hit Wall")
        return new_location

    def get_new_location(self, location, direction):
        match direction:
            case ">":
                return Location(location.x + 0, location.y + 1, location.type)
            case "v":
                return Location(location.x + 1, location.y + 0, location.type)
            case "<":
                return Location(location.x + 0, location.y - 1, location.type)
            case "^":
                return Location(location.x - 1, location.y + 0, location.type)

    def move_robot(self, direction):
        if self.can_move(self.robot_location, direction):
            self.robot_location = self.move_location(self.robot_location, direction)

    def display_room(self):
        for location in self.locations:
            print("".join([l.type.value for l in location]))

    def sum_gps_coordinates(self):
        total = 0
        for row in self.locations:
            for col in row:
                total += col.gps_coordinates
        return total

room_input, directions_input = open("day15_input.txt").read().split("\n\n")
directions_input = directions_input.replace("\n", "")

room = Room(room_input)

for d in directions_input:
    room.move_robot(d)

print(room.sum_gps_coordinates())