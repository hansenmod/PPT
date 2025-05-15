degree = 90
dic = {"up": 0, "down": 0, "left": 0, "right": 0}
return_dis = 0
current_dic = 0
dic_flag = 0
flag = False
x = 0
y = 0
number = 0


def get_expect_dic(*argue) -> None:
    global degree
    direction_flag = int(degree / 90) % 4
    degree += 90
    return direction_flag


def f(x):
    dic[x] += 1


def final_dic(*argue):
    global return_dis
    global current_dic
    global dic_flag
    global flag
    """
    获取折返距离
    """

    if flag:
        return_dis = (
            dic["up"]
            if current_dic == 2
            else (
                dic["down"]
                if current_dic == 0
                else dic["left"] if current_dic == 3 else dic["right"]
            )
        )
        if return_dis != 0:
            (
                f("up")
                if dic_flag == 0
                else (
                    f("left")
                    if dic_flag == 1
                    else f("down") if dic_flag == 2 else f("right")
                )
            )
        flag = False

    if return_dis != 0:
        return_dis -= 1

        return current_dic

    else:
        dic_flag = get_expect_dic()
        current_dic = dic_flag
        flag = True
        (
            f("up")
            if dic_flag == 0
            else (
                f("left")
                if dic_flag == 1
                else f("down") if dic_flag == 2 else f("right")
            )
        )
        return dic_flag


def print_matrix(lenth):
    global number
    global x, y
    number = (lenth * lenth) - 1
    matrix = [[0 for _ in range(lenth)] for _ in range(lenth)]
    center_point = int((lenth - 1) / 2)
    x = center_point
    y = center_point
    matrix[x][y]=number
    while x != 0 or y != 0:
        flag = final_dic()
        print(flag)
        if flag == 0:
            x -= 1
        elif flag == 1:
            y -= 1
        elif flag == 2:
            x += 1
        elif flag == 3:
            y += 1
        number -= 1
        print(x, y, number)
        matrix[x][y] = number
        print(matrix)
    return matrix


if __name__ == "__main__":
    # 创建一个 3x3 的矩阵

    # 访问元素，例如第二行第三列：

    for item in print_matrix(5):
        print(" ".join(f"{x:3}" for x in item))
