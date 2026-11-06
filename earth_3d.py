
from vpython import *
import random

# ==============================
# 🌌 SPACE SCENE
# ==============================

scene.title = "🌍 ULTIMATE 3D SPACE EXPLORER"
scene.width = 1100
scene.height = 700
scene.background = vector(0, 0, 0)
scene.caption = "\n🌍 SPACE EXPLORER | Drag to rotate | Scroll to zoom\n"

scene.camera.pos = vector(0, 0, 13)
scene.camera.axis = vector(0, 0, -13)

# ==============================
# ✨ STAR FIELD
# ==============================

stars = []

for i in range(500):
    star = sphere(
        pos=vector(
            random.uniform(-30, 30),
            random.uniform(-30, 30),
            random.uniform(-30, 30)
        ),
        radius=random.uniform(0.015, 0.045),
        color=color.white,
        emissive=True
    )
    stars.append(star)

# ==============================
# ☀️ SUN
# ==============================

sun = sphere(
    pos=vector(-12, 5, -8),
    radius=2,
    color=color.orange,
    emissive=True
)

distant_light(
    direction=vector(1, -1, 1),
    color=color.white
)

# ==============================
# 🌍 EARTH
# ==============================

earth = sphere(
    pos=vector(0, 0, 0),
    radius=3,
    texture=textures.earth,
    shininess=0.9
)

# Atmosphere
atmosphere = sphere(
    pos=vector(0, 0, 0),
    radius=3.13,
    color=vector(0.1, 0.5, 1),
    opacity=0.10
)

# Extra blue glow
glow = sphere(
    pos=vector(0, 0, 0),
    radius=3.25,
    color=vector(0, 0.4, 1),
    opacity=0.035
)

# ==============================
# 🌙 MOON
# ==============================

moon = sphere(
    pos=vector(5, 0, 0),
    radius=0.55,
    color=vector(0.75, 0.75, 0.8),
    shininess=0.8
)

moon_orbit = ring(
    pos=vector(0, 0, 0),
    axis=vector(0, 1, 0),
    radius=5,
    thickness=0.012,
    color=color.white,
    opacity=0.35
)

# ==============================
# 🪐 SATURN
# ==============================

saturn = sphere(
    pos=vector(9, 2, -3),
    radius=1.1,
    color=vector(0.9, 0.65, 0.35),
    shininess=0.7
)

saturn_ring = ring(
    pos=saturn.pos,
    axis=vector(0.3, 1, 0.2),
    radius=1.8,
    thickness=0.3,
    color=vector(0.9, 0.7, 0.4),
    opacity=0.7
)

# ==============================
# ☄️ COMETS
# ==============================

comets = []

for i in range(4):
    comet = sphere(
        pos=vector(
            random.uniform(-15, 15),
            random.uniform(-10, 10),
            random.uniform(-10, 10)
        ),
        radius=0.12,
        color=color.cyan,
        emissive=True
    )
    comets.append(comet)

# ==============================
# 🌀 ANIMATION
# ==============================

angle = 0
star_timer = 0

while True:

    rate(60)

    # Earth rotation
    earth.rotate(
        angle=0.003,
        axis=vector(0, 1, 0),
        origin=vector(0, 0, 0)
    )

    # Moon orbit
    angle += 0.008

    moon.pos = vector(
        5 * cos(angle),
        0.7 * sin(angle),
        5 * sin(angle)
    )

    # Saturn rotation
    saturn.rotate(
        angle=0.003,
        axis=vector(0, 1, 0)
    )

    # Keep Saturn ring centered
    saturn_ring.pos = saturn.pos

    # Comet movement
    for comet in comets:
        comet.pos.x += 0.08

        if comet.pos.x > 18:
            comet.pos.x = -18
            comet.pos.y = random.uniform(-10, 10)
            comet.pos.z = random.uniform(-10, 10)

    # Twinkling stars
    star_timer += 1

    if star_timer % 20 == 0:
        for star in random.sample(stars, 30):
            star.radius = random.uniform(0.015, 0.05)






# for runing progrimming
# python --version
# python -m ensurepip --upgrade
# python main.py
# python --version
