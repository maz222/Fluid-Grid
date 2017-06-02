from Vector3 import TripleVector


class GridPoint:

    def __init__(self, position=TripleVector(0, 0, 0), inverse_mass=0):
        self.position = position
        self.inverse_mass = inverse_mass

        self.velocity = TripleVector(0, 0, 0)
        self.acceleration = TripleVector(0, 0, 0)
        self.damping = 0.98

    def apply_force(self, force):
        self.acceleration += force * self.inverse_mass

    def increase_damping(self, factor):
        self.damping *= factor

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = TripleVector(0, 0, 0)

        if self.velocity.magnitude() ** 2 < 0.001 * 0.001:
            self.velocity = TripleVector(0, 0, 0)

        self.velocity *= self.damping
        self.damping = 0.98

    def __str__(self):
        return "(" + str(self.position.x) + " " + str(self.position.y) + ")"



