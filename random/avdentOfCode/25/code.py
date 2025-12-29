"""
    array or list with 100 slots
    read in file
    for each line split into direction and steps
     if pointer == 0 add 1 to counter
      if direction == R pointer + steps
      else pointer - steps
      steps modulo 100 = steps

"""

# print(130 % 100)
# pointer = 30
# print(abs(pointer)% 100)
import json
# with open('/Users/user/repo/Notes/random/avdentOfCode/./25/data.txt', 'r') as file:
#     data = [item.replace("\n", "") for item in file]
#     dic = {"two":data}
# with open('/Users/user/repo/Notes/random/avdentOfCode/./25/data.json','w') as file:
#     json.dump(dic,file)

total = 0
pointer = 50
move = 0
direction = ''

def left(pointer, move):
    pointer = pointer - move
    if pointer < 0:
        pointer = abs(pointer)
        pointer = pointer % 100
        pointer = 100 - pointer
    return pointer

def right(pointer, move):
    pointer = pointer + move
    return pointer

def lorMove(string):
    LoR = string[0]
    move = int(string[1:])
    return LoR, move

with open ('/Users/user/repo/Notes/random/avdentOfCode/25/data.json', 'r') as f:
# with open ('./25/data.json', 'r') as f:
    fi= json.load(f)
    file = fi['one']
    for item in file:
        if pointer == 0:
            total = total + 1
        direction, move = lorMove(item)
        if direction == 'L':
            pointer = left(pointer, move)
        else:
            pointer = right(pointer, move)
        pointer = abs(pointer)
        pointer = pointer % 100
print(total)


#     print(type(fi))
# print(lorMove("r450"))