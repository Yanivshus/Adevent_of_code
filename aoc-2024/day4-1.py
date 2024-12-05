def check_rules(arr, i, j):
    c = 0

    direction = [
        (0, -1),  # Left
        (0, 1),   # Right
        (1, 0),   # Down
        (-1, 0),  # Up
        (-1, -1), # Diagonal left up
        (-1, 1),  # Diagonal right up
        (1, -1),  # Diagonal left down
        (1, 1),   # Diagonal right down
    ]
    for di,dj in direction:
        try:
            if i + di*3 < 0 or i + di*3 > len(arr) or j + dj*3 < 0 or j +dj * 3 > len(arr[0]):
                continue
            if (arr[i][j] == 'X' and
                arr[i + di][j +dj] == 'M' and
                arr[i + di*2][j + dj*2] == 'A' and
                arr[i + di*3][j + dj*3] == 'S'
            ):
                c+=1
                print(i,j)

        except IndexError:
            pass

    return c


def main():
    file = open("input.txt", "r").read()
    arr = file.split("\n")
    #arr = arr[0:len(arr)-1]
    print(len(arr))
    total = 0

    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j] == 'X':
                total += check_rules(arr,i,j)
    print(total)





if __name__ == '__main__':
    main()