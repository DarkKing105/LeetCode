asteroids = [5,10,-5]
min = min(asteroids)

for i in range(len(asteroids) -1, -1, -1):
    if asteroids[i] < 0:
        if asteroids[i-1] >= 0:
            asteroids.pop()
            asteroids.pop()

