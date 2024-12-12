from dataclasses import dataclass, field
from typing import Set, Tuple


@dataclass
class Region:
    plot_type: str
    plots: Set[Tuple[int, int]] = field(default_factory=set)

    @property
    def area(self) -> int:
        return len(self.plots)

    @property
    def sides(self):
        sides = 0

        corner_upper_left = [[0, -1], [-1, -1], [-1, 0]]
        corner_upper_right = [[-1, 0], [-1, 1], [0, 1]]
        corner_lower_right = [[0, 1], [1, 1], [1, 0]]
        corner_lower_left = [[1, 0], [1, -1], [0, -1]]

        corners = [corner_upper_left, corner_upper_right, corner_lower_right, corner_lower_left]

        for point in self.plots:
            for corner in corners:
                direction = corner[0]
                adjacent1 = (point[0] + direction[0], point[1] + direction[1]) in self.plots

                direction = corner[1]
                diagonal = (point[0] + direction[0], point[1] + direction[1]) in self.plots

                direction = corner[2]
                adjacent2 = (point[0] + direction[0], point[1] + direction[1]) in self.plots

                if (adjacent1 == adjacent2) and (not adjacent1 or not diagonal):
                    sides += 1
        return sides

    @property
    def price(self) -> int:
        return self.area * self.sides

    def plot_is_adjacent(self, point: Tuple[int, int]) -> bool:
        x1, y1 = point
        for plot in self.plots:
            x2, y2 = plot
            if abs(x1 - x2) + abs(y1 - y2) == 1:
                return True
        else:
            return False

    def region_is_adjacent(self, region2) -> bool:
        for plot in region2.plots:
            if self.plot_is_adjacent(plot):
                return True
        return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.plot_type=}, {self.plots=}, {self.area=}, {self.sides=}, {self.price=})"

map = [[i for i in row.strip()] for row in open("day12_input.txt")]

regions = []

for i, row in enumerate(map):
    for j, plot_type in enumerate(row):
        updated_region = None
        for region in regions:
            if region.plot_type == plot_type and region.plot_is_adjacent((i, j)):
                region.plots.add((i, j))
                updated_region = region
                break
        else:
            new_region = Region(plot_type=plot_type)
            new_region.plots.add((i, j))
            regions.append(new_region)

        # Merge adjacent regions
        if updated_region:
            for region in regions:
                if region is not updated_region and region.plot_type == updated_region.plot_type and region.region_is_adjacent(updated_region):
                    updated_region.plots = region.plots.union(updated_region.plots)
                    region.plots = set()

# Remove blank regions
regions = [region for region in regions if region.area > 0]


total = sum(region.price for region in regions)
print(total)