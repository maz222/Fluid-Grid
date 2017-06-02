from PointMass import GridPoint
from Spring import GridSpring
from Vector3 import TripleVector

class Grid:

    # bottom corner = [x, y]
    def __init__(self, bottom_corner, width, height, x_spacing, y_spacing, string_strength=.28):
        self.bottom_corner = bottom_corner
        self.width = width
        self.height = height
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing

        spring_list = []

        points = []
        fixed_points = []

        col = 0
        for y in range(0, self.height, self.y_spacing):
            if y >= len(points):
                points.append([])
                fixed_points.append([])
                print(len(points))
            for x in range(0, self.width, self.x_spacing):
                points[col].append(GridPoint(TripleVector
                                             (self.bottom_corner[0] + x, self.bottom_corner[1] + y, 0), 1))
                fixed_points[col].append(GridPoint(TripleVector
                                                   (self.bottom_corner[0] + x, self.bottom_corner[1] + y, 0), 0))
            col += 1

        self.points = points
        self.fixed_points = fixed_points

        for y in range(0, len(self.points)):
            for x in range(0, len(self.points[y])):
                if x == 0 or y == 0 or x == len(self.points[y]) - 1 or y == len(self.points) - 1:
                    spring_list.append(GridSpring(self.fixed_points[y][x], self.points[y][x], 0.1, 0.1))
                elif x % 3 == 0 and y % 3 == 0:
                    spring_list.append(GridSpring(self.fixed_points[y][x], self.points[y][x], .002, .002))

                stiffness = string_strength
                damping = .06

                if x > 0:
                    spring_list.append(GridSpring(self.points[y][x-1], self.points[y][x], stiffness, damping))
                if y > 0:
                    spring_list.append(GridSpring(self.points[y-1][x], self.points[y][x], stiffness, damping))

        self.springs = spring_list

    # force = Vector3 (directed force ONLY)
    # force = float (all others)
    # position = Vector3
    # radius = float

    def apply_directed_force(self, force, position, radius):
        for col in self.points:
            for mass in col:
                if position.distance_between(mass.position)**2 < radius**2:
                    mass.apply_force(10 * force.div_s(10 + position.distance_between(mass.position)))

    def apply_implosive_force(self, force, position, radius):
        for col in self.points:
            for mass in col:
                dist2 = position.distance_between(mass.position)**2
                if dist2 < radius**2:
                    mass.apply_force(10 * force * (position - mass.position).div_s(100 + dist2))
                    mass.increase_damping(.6)

    def apply_explosive_force(self, force, position, radius):
        for col in self.points:
            for mass in col:
                dist2 = position.distance_between(mass.position)**2
                if dist2 < radius**2:
                    mass.apply_force(100 * force * (mass.position - position).div_s(10000 + dist2))
                    mass.increase_damping(.6)

    def update(self):
        for spring in self.springs:
            spring.update()
        for col in self.points:
            for point in col:
                point.update()

    def __str__(self):
        string = ""
        for i in range(len(self.points)):
            for j in range(len(self.points[i])):
                string += " " + str(self.points[i][j]) + " "
            string += "\n"
        return string



