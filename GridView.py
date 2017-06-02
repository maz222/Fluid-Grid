from Grid import Grid
from PointMass import GridPoint
from Vector3 import TripleVector

import pygame


class GridView:

    # cheating! doesn't actually transform - just ignores z completely
    @staticmethod
    def trans_vec(vec3):
        return vec3.x, vec3.y

    @staticmethod
    def draw(grid, surface):
        color = (0, 0, 0)
        width = 1
        if grid is not None:
            points = grid.points
            for y in range(len(points)):
                for x in range(len(points[y])):
                    start = GridView.trans_vec(points[y][x].position)
                    if x + 1 < len(points[y]):
                        end = GridView.trans_vec(points[y][x+1].position)
                        pygame.draw.line(surface, color, start, end, width)
                    if y + 1 < len(points):
                        end = GridView.trans_vec(points[y+1][x].position)
                        pygame.draw.line(surface, color, start, end, width)
