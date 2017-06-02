from PointMass import GridPoint
from Vector3 import TripleVector


class GridSpring:

    def __init__(self, end1=GridPoint(), end2=GridPoint(), stiffness=0, damping=0):
        self.end1 = end1
        self.end2 = end2
        self.stiffness = stiffness
        self.damping = damping
        self.target_length = end1.position.distance_between(end2.position) * .95

    def update(self):

        x = self.end1.position - self.end2.position
        length = x.magnitude()

        if length <= self.target_length:
            return

        x = (x.div_s(length)) * (length - self.target_length)
        dv = self.end2.velocity - self.end1.velocity
        force = self.stiffness * x - dv * self.damping

        self.end1.apply_force(-force)
        self.end2.apply_force(force)