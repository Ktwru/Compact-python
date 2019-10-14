def tail(matrix):
    for i in matrix:
        print(i)

def spiral(lenght):
    if lenght == 1:
        return [[1]], 1
    matrix_side = round(lenght ** 0.5)                                          #snake matrix side calculation
    if matrix_side < lenght ** 0.5:
        matrix_side += 1

    if matrix_side % 2 == 0:
        matrix_side += 1

    matrix = [[0 for x in range(matrix_side)] for y in range(matrix_side)]    #snake matrix building

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
            num += 1
            y += 1
            matrix[y][x] = num
            if num == lenght:
                #tail(matrix)
                return matrix, matrix_side
        for downside in range(side):
            num += 1
            x += 1
            matrix[y][x] = num
            if num == lenght:
                #tail(matrix)
                return matrix, matrix_side
        for rightside in range(side):
            num += 1
            y -= 1
            matrix[y][x] = num
            if num == lenght:
                #tail(matrix)
                return matrix, matrix_side
        for upside in range(side):
            num += 1
            x -= 1
            matrix[y][x] = num
            if num == lenght:
                #tail(matrix)
                return matrix, matrix_side
        side += 2

    print('matrix side:', matrix_side, 'x:', x, "y:", y, 'ops:', ops)


print(spiral(1))

