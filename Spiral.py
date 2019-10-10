
def spiral(lenght):
    # if type(n) != int or n<1:
    #     return []

    matrix_side = round(lenght ** 0.5)                                          #snake matrix side calculation
    if matrix_side < lenght ** 0.5:
        matrix_side += 1

    if matrix_side % 2 == 0:
        matrix_side += 1

    matrix = [['0' for x in range(matrix_side)] for y in range(matrix_side)]    #snake matrix building

    x = matrix_side//2                                                          #center
    y = x
    num=1
    matrix[y][x] = num

    ops = matrix_side//2
    side = 2

    y+=1
    for op in range(ops):
        x-=1
        y-=1
        for leftside in range(side):
            num+=1
            matrix[y+leftside][x]=num
        for downside in range(side):
            num+=1
            matrix[y+side-1][x+downside+1]=num
        for rightside in range(side):
            num+=1
            matrix[y+side-2-rightside][x+side]=num
        for upside in range(side):
            num+=1
            matrix[y-1][x+side-1-upside]=num
        side+=2

    print('matrix side:', matrix_side, 'x:', x, "y:", y, 'ops:', ops)

    # matrix = [[0 for j in range(n)] for i in range(n)]
    #
    # ops = (n//2)
    # num = 0
    # s = n - 1
    # x = 0
    # y = 0
    # for i in range(ops):
    #     for upside in range(s):
    #         num += 1
    #         matrix[y][x + upside] = num
    #     for rightside in range(s):
    #         num += 1
    #         matrix[y + rightside][x + s] = num
    #     for downside in range(s):
    #         num += 1
    #         matrix[y + s][x + s - downside] = num
    #     for leftside in range(s):
    #         num += 1
    #         matrix[y + s - leftside][x] = num
    #     x+=1
    #     y+=1
    #     s-=2
    #
    # if n%2:
    #     matrix[n//2][n//2]=n*n

    #for i in matrix:
    #    print(i)
    for i in matrix:
        print(i)


print(spiral(10))

