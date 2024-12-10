def find_first_empty(arr):
    for c in range(0,len(arr)):
        if arr[c] == '.':
            return c


def main():
    file = list(open("input.txt", "r").read())
    arr = [int(x) for x in file]
    narr = []
    i = 1
    curr_id = 0

    # mapping to opened form
    while i < len(arr):
        amount_block = arr[i-1]
        amount_space = arr[i]

        while amount_block > 0:
            narr.append(str(curr_id))
            amount_block -= 1

        if amount_space == 0:
            i += 2 # need to understand the problem with the i.
            curr_id += 1
            amount_block = arr[i]
            while amount_block > 0:
                narr.append(str(curr_id))
                amount_block -= 1

        while amount_space > 0:
            narr.append('.')
            amount_space -= 1

        i+=2
        curr_id += 1

    print(narr)
    print(" ")
    # now need to move all to side.
    j = len(narr) - 1
    while j > 0:
        ind_blank = find_first_empty(narr)

        if j <= ind_blank:
            break

        if narr[j] != '.':
            temp = narr[j]
            narr[j] = '.'
            narr[ind_blank] = temp
        j -= 1

    print(arr)
    print(" ")
    print(narr)

    total = 0
    for q in range(0,len(narr)):
        if narr[q] != '.':
            total += int(narr[q]) * q

    print(total)







if __name__ == '__main__':
    main()