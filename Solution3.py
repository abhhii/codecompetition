def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)



n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))
#dict of dicts to store slope b/w each pair of points like point: dict()
slopes = dict()
res = 0
for i in range(len(points)):
    slopes = dict()
    same_points, m = 0,0
    for j in range(i+1, len(points)):
        # print("x1 =", points[j][0], " x2 = ", points[i][0])
        # print("y1 =", points[j][1], " y2 = ", points[i][1])
        x = points[j][0] - points[i][0]
        y = points[j][1] - points[i][1]

        if x == 0 and y==0:
            same_points+=1
            continue
        hcf = gcd(x,y)
        # print("hcf is", hcf)
        if hcf != 0:
            x = x//hcf
            y = y//hcf
        # print("x is", x, " and y is", y)
        # print("And slopes is", slopes)
        if x in slopes.keys():
            if y in slopes[x].keys():
                slopes[x][y] = slopes[x][y] + 1
            else:
                slopes[x][y] = 1
        else:
            d = dict()
            d[y] = 1
            slopes[x] = d
        # print("Now slopes is", slopes)
        m = max(m, slopes[x][y])
        # print("same_points", same_points, "m is", m)

    res = max(res, m+ same_points + 1 )
print(res)
