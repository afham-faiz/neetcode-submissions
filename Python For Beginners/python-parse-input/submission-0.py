from typing import List

def read_integers() -> List[int]:
    line = input()
    integer_list = []
    string_list = line.split(",")
    for i in string_list:
        integer_list.append(int(i))
    return integer_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
