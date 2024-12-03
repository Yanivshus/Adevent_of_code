import re

dont = []

def find_indexes(content):
    global dont

    matches_dont = re.finditer("don't\(\)", content)
    dont = [match.start() for match in matches_dont]

def get_total(file):
    total = 0
    matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", file)
    for res in matches:
        ls_without_rest = res[4:len(res)-1].split(",")
        #print(ls_without_rest)
        total += int(ls_without_rest[0]) * int(ls_without_rest[1])
    return total


def main():
    global dont
    file = open("input.txt", "r").read()
    find_indexes(file)
    matches = re.findall(r"do\(\)(.*?)(?:don't\(\)|$)", file)
    total = 0

    total += get_total(file[0:dont[0]])

    for i in matches:
        total += get_total(i)
    print(total)



if __name__ == '__main__':
    main()