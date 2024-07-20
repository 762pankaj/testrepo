def sq_dist(t1, t2):
    square_distance = 0
    for i in range(len(t1)):
        diff = t1[i] - t2[i]
        square_distance += diff**2
    return square_distance

print(int(sq_dist((5, 4, 2), (2, 3, 4))))
print(int(sq_dist((1, 2, 3, 4), (2, 3, 4, 5))))
