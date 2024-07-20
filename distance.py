"""def sq_dist(t1, t2):
    x = int(t1[0]-t2[0])
    y = int(t1[1]-t2[1])
    z = int(t1[2]-t2[2])
    square_distance = (x*x+y*y+z*z)
    return square_distance
print(int(sq_dist((5, 4, 2), (2, 3, 4))))"""
def sq_dist(t1, t2):
    square_distance = 0
    for i in range(len(t1)):
        diff = t1[i] - t2[i]
        square_distance += diff**2
    return square_distance

print(int(sq_dist((5, 4, 2), (2, 3, 4))))
print(int(sq_dist((1, 2, 3, 4), (2, 3, 4, 5))))
