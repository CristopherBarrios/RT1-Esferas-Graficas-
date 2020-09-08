## Cristopher Jose Rodolfo Barrios Solis
## 18207

import random

from raytracer.gla import Raytracer, color
from raytracer.object import Object, Texture
from raytracer.sphere import Sphere, Material

r = Raytracer(800, 800)

## colorsitos
blanco = Material(diffuse = color(1, 0.96, 0.96))
naranja = Material(diffuse = color(1, 0.65, 0))
negro = Material(diffuse = color(0.2, 0.2, 0.2))

## ojos
r.scene.append(Sphere([0.25, 2.2, -5], 0.10, negro))
r.scene.append(Sphere([-0.25, 2.2, -5], 0.10, negro))


##  nariz
r.scene.append(Sphere([0, 1.9, -5], 0.10, naranja))

##  boca
r.scene.append(Sphere([0.25, 1.6, -5], 0.07, negro))
r.scene.append(Sphere([-0.25, 1.6, -5], 0.07, negro))
r.scene.append(Sphere([0.1, 1.5, -5], 0.07, negro))
r.scene.append(Sphere([-0.1, 1.5, -5], 0.07, negro))

##  botones
r.scene.append(Sphere([0, 0.35, -3],  0.13, negro))
r.scene.append(Sphere([0, -0.15, -3], 0.18, negro))
r.scene.append(Sphere([0, -0.75, -3], 0.23, negro))

##  cuerpo
r.scene.append(Sphere([0, 2.5,  -7], 1.1, blanco))
r.scene.append(Sphere([0, 0.5,  -6], 1.32, blanco))
r.scene.append(Sphere([0, -2,  -8], 2.2, blanco))

r.rtRender()

r.glFinish('final.bmp')
