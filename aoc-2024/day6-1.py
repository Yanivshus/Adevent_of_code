def get_position_of_player(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '>' or arr[i][j] == '<' or arr[i][j] == '^' or arr[i][j] == 'v':
                return i,j
    return -1,-1

def move_until_obstacle_left(arr,i,j):
    arr[i][j] = 'X'
    q = j
    while q >= 0 and arr[i][q] != '#':
        arr[i][q] = 'X'
        q -= 1
    if q >= 0:
        arr[i][q+1] = '^'

def move_until_obstacle_right(arr,i,j):
    arr[i][j] = 'X'
    q = j
    while q < len(arr[0]) and arr[i][q] != '#':
        arr[i][q] = 'X'
        q += 1

    if q < len(arr[0]):
        arr[i][q-1] = 'v'

def move_until_obstacle_up(arr,i,j):
    arr[i][j] = 'X'
    k = i
    while k >= 0 and arr[k][j] != '#':
        arr[k][j] = 'X'
        k -= 1

    if k >= 0:
        arr[k+1][j] = '>'

def move_until_obstacle_down(arr, i, j):
    arr[i][j] = 'X'
    k = i
    while k < len(arr) and arr[k][j] != '#':
        arr[k][j] = 'X'
        k += 1

    if k < len(arr):
        arr[k-1][j] = '<'

def print_grid(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j == len(arr[0])-1:
                print(arr[i][j])
            else:
                print(arr[i][j],end='')
    print("")

def count_x(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'X':
                total += 1

    return total


def main():
    file = open("input.txt").read().split("\n")
    arr = [list(x) for x in file]

    #print_grid(arr)

    while get_position_of_player(arr) != (-1, -1):
        i,j = get_position_of_player(arr)
        if arr[i][j] == '>':
            move_until_obstacle_right(arr,i, j)
        elif arr[i][j] == '<':
            move_until_obstacle_left(arr, i, j)
        elif arr[i][j] == 'v':
            move_until_obstacle_down(arr,i, j)
        elif arr[i][j] == '^':
            move_until_obstacle_up(arr,i, j)
        print_grid(arr)
    #print(arr)

    print(count_x(arr))



if __name__ == '__main__':
    main()