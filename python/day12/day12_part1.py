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
    def perimeter(self) -> int:
        perimeter = 0

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for point in self.plots:
            perimeter += 4

            for direction in directions:
                check_point = point[0] + direction[0], point[1] + direction[1]
                if check_point in self.plots:
                    perimeter -= 1

        return perimeter

    @property
    def price(self) -> int:
        return self.area * self.perimeter

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
        return f"{self.__class__.__name__}({self.plot_type=}, {self.plots=}, {self.area=}, {self.perimeter=}, {self.price=})"

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