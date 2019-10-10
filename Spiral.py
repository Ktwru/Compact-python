
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


    for op in range(ops):                                                       #spiral matrix
        x -= 1
        y -= 1
        for leftside in range(side):
            num+=1
            y+=1
            matrix[y][x]=num
        for downside in range(side):
            num+=1
            x+=1
            matrix[y][x]=num
        for rightside in range(side):
            num+=1
            y-=1
            matrix[y][x]=num
        for upside in range(side):
            num+=1
            x-=1
            matrix[y][x]=num
        side+=2

    print('matrix side:', matrix_side, 'x:', x, "y:", y, 'ops:', ops)


    for i in matrix:
        print(i)


print(spiral(13))

