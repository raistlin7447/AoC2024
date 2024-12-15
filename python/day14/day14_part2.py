from dataclasses import dataclass


@dataclass
class Robot:
    x_position: int
    y_position: int
    x_velocity: int
    y_velocity: int

    def set_location(self, map_x_size, map_y_size, time):
        x = (self.x_position + self.x_velocity * time) % map_x_size
        y = (self.y_position + self.y_velocity * time) % map_y_size
        self.x_position = x
        self.y_position = y
        return x, y

robots = []

lines = open("day14_input.txt").readlines()
for line in lines:
    position, velocity = line.split()
    position = position.replace("p=", "").split(",")
    velocity = velocity.replace("v=", "").split(",")
    new_robot = Robot(int(position[0]), int(position[1]), int(velocity[0]), int(velocity[1]))
    robots.append(new_robot)

num_robots = len(robots)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

max_x = 101
max_y = 103

for second in range(10000):
    for robot in robots:
        x_loc, y_loc = robot.set_location(max_x, max_y, 1)
        if 0 <= x_loc < max_x // 2 and 0 <= y_loc < max_y // 2:
            q1 += 1
        elif max_x // 2 < x_loc < max_x and 0 <= y_loc < max_y // 2:
            q2 += 1
        elif 0 <= x_loc < max_x // 2 and max_y // 2 < y_loc < max_y:
            q3 += 1
        elif max_x // 2 < x_loc < max_x and max_y // 2 < y_loc < max_y:
            q4 += 1

    map = [["." for j in range(max_x)]for i in range(max_y)]

    locations = set([(bot.x_position, bot.y_position) for bot in robots])
    if num_robots == len(locations):
        print(f"Candidate at {second+1} seconds.")
        for robot in robots:
            map[robot.y_position][robot.x_position] = "X"

        for i in map:
            print("".join(i))
