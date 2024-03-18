
puzzle_input = []
puzzle_output = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# tim kiem o trong de di chuyen
def check_zero(puzzle_input):
    for i in range(9):
        if puzzle_input[i] == 0:
            return i

def check_logic(puzzle_input):
    count = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if j == 9: break
            if puzzle_input[i] > puzzle_input[j] and puzzle_input[i] != 0 and puzzle_input[j] != 0:
                count+=1
    if count % 2 == 0:
        return True
    else:
        return False

def heuristic(puzzle_input):
    sum = 0
    # su dung cong thuc tinh khoang cach manhattan: (|x - (a - 1)%3| + |y - a//3|) voi x la vi tri dong hien tai, y la vi tri cot hien tai
    # ham heuristic la tong khoang cach manhattan cua trang thai
    for i in range(9):
        if puzzle_input[i] != 0:
            sum += abs(i % 3 - (puzzle_input[i] - 1) % 3) + abs(i//3 - (puzzle_input[i] - 1)//3)
    return sum
# ham nay giup chon ra gia tri heuristic nho nhat trong list cac trang thai
def min_heuristic(list_heuristics):
    min = float('inf')
    index = None
    for i in range(len(list_heuristics)):
        if(list_heuristics[i] < min):
            min = list_heuristics[i]
            index = i
        return index

def show_game(puzzle):
    print("""
 {}  {}  {} 
 {}  {}  {} 
 {}  {}  {} 
""".format(puzzle[0], puzzle[1], puzzle[2], puzzle[3], puzzle[4], puzzle[5], puzzle[6], puzzle[7],
                        puzzle[8]))

# su dung thuat toan Best First Search de tim kiem duong di

def AI_play_game(puzzle_input):
    open_list = []
    open_LIST = []
    closed_list = []
    heuristic_val = []
    count_x = 0
    open_list.append(puzzle_input)
    x = []
    x = open_list.pop(0)
    a = x[9]  # lay ra chi muc cua o trong(o so 0)
    while x[:9] != puzzle_output:
        if a % 3 != 0:  # left
            statespace1 = x.copy()
            temp = statespace1[a]
            statespace1[a] = statespace1[a - 1]
            statespace1[a - 1] = temp
            statespace1[9] = a - 1
            statespace1.append("L")

            if statespace1[:9] == puzzle_output:
                print("Các bước để giải quyết là: ")
                print(", ".join(statespace1[10:]))
                count_x = len(statespace1) - 10
                break
            else:
                if statespace1[:9] not in closed_list and statespace1[:9] not in open_LIST:
                    open_list.append(statespace1)  # for printing the steps
                    open_LIST.append(statespace1[:9])  # to prevent loops
                    heuristic_val.append(heuristic(statespace1[:9]))

        if a % 3 != 2:  # right
            statespace2 = x.copy()
            temp = statespace2[a]
            statespace2[a] = statespace2[a + 1]
            statespace2[a + 1] = temp
            statespace2[9] = a + 1
            statespace2.append("R")

            if statespace2[:9] == puzzle_output:
                print("Các bước để giải quyết là: ")
                print(", ".join(statespace2[10:]))
                count_x = len(statespace2) - 10
                break
            else:
                if statespace2[:9] not in closed_list and statespace2[:9] not in open_LIST:
                    open_list.append(statespace2)
                    open_LIST.append(statespace2[:9])
                    heuristic_val.append(heuristic(statespace2[:9]))

        if a != 0 and a != 1 and a != 2:  # up
            statespace3 = x.copy()
            temp = statespace3[a]
            statespace3[a] = statespace3[a - 3]
            statespace3[a - 3] = temp
            statespace3[9] = a - 3
            statespace3.append("U")

            if statespace3[:9] == puzzle_output:
                print("Các bước để giải quyết là: ")
                print(", ".join(statespace3[10:]))
                count_x = len(statespace3) - 10
                break
            else:
                if statespace3[:9] not in closed_list and statespace3[:9] not in open_LIST:
                    open_list.append(statespace3)
                    open_LIST.append(statespace3[:9])
                    heuristic_val.append(heuristic(statespace3[:9]))


        if a != 6 and a != 7 and a != 8:  # down
            statespace4 = x.copy()
            temp = statespace4[a]
            statespace4[a] = statespace4[a + 3]
            statespace4[a + 3] = temp
            statespace4[9] = a + 3
            statespace4.append("D")
            if statespace4[:9] == puzzle_output:
                print("\nCác bước để giải quyết là:- ")
                print(", ".join(statespace4[10:]))
                count_x = len(statespace4) - 10
                break
            else:
                if statespace4[:9] not in closed_list and statespace4[:9] not in open_LIST:
                    open_list.append(statespace4)
                    open_LIST.append(statespace4[:9])
                    heuristic_val.append(heuristic(statespace4[:9]))


        closed_list.append(x[:9])
        y = min_heuristic(heuristic_val)
        tem = heuristic_val.pop(y)
        x = open_list.pop(y)
        a = x[9]
    print("Số bước di chuyển là: ", count_x)
def input_number(puzzle_input):
    print("\nNhập trạng thái ban đầu: ")
    puzzle_input = list(map(int, input().split()))
    print("\nBảng trạng thái sau khi nhập:")
    show_game(puzzle_input)
    return puzzle_input


puzzle_input = input_number(puzzle_input)


while(check_logic(puzzle_input) == False):
    print("Trạng thái này không thể xử lí, hãy nhập lại: ")
    puzzle_input = input_number(puzzle_input)
zero = check_zero(puzzle_input)
if(check_logic(puzzle_input)):
    print("Trạng thái này có thể xử lí")
    print(heuristic(puzzle_input))
    puzzle_input.append(zero)
    AI_play_game(puzzle_input)


'''
if(check_logic(puzzle_input)):
    print("Trạng thái này có thể xử lí")
    puzzle_input.append(zero)
    AI_play_game(puzzle_input)

else:
    print("Trạng thái này không thể xử lí")
'''
