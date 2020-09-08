## Cristopher Jose Rodolfo Barrios Solis
## 18207

import numpy as np

from raytracer.gla import color
from raytracer.math import Math

class Material(object):
    def __init__(self, diffuse = color(1, 1, 1)):
        self.diffuse = diffuse

class Intersect(object):
    def __init__(self, distance):
        self.distance = distance

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

        self.Math = Math()

    def ray_intersect(self, orig, dir):
        L = self.Math.subtract(self.center, orig)
        tca = self.Math.dot(L, dir)

        l = self.Math.norm(L)

        d = (l**2 - tca**2) **0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d**2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        return Intersect(distance = t0)
