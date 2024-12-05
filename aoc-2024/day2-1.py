def check_rules(ls : list):
    check = False
    if (ls[0] - ls[1]) < 0:
        check = True

    for i in range(0,len(ls)-1):
        diff = ls[i] - ls[i+1]
        if abs(diff) >= 1 and abs(diff) <= 3:
            state_diff = False
            if diff < 0:
                state_diff = True
            
            if state_diff != check:
                return False
        else:
            return False
    return True




S
def main():
    file = open("day2-input.txt").readlines()
    total = 0
    for line in file:
        line = line[0:len(line)-1]
        line = line.split(" ")

        num_ls = [int(x) for x in line]

        res = check_rules(num_ls)
        if res == True:
            total += 1
    print(total)









if __name__ == "__main__":
    main()
