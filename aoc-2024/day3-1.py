import re

def main():
    file = open("input.txt", "r").read()
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", file)

    total = 0
    for res in matches:
        ls_without_rest = res[4:len(res)-1].split(",")
        #print(ls_without_rest)
        total += int(ls_without_rest[0]) * int(ls_without_rest[1])
    print(total)





if __name__ == '__main__':
    main()