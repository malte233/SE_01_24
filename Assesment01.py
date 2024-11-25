#safes the not 0 liquid
def find_top_non_zero(beaker):
    top = 0
    for value in beaker:
        if value != 0:
            top = value
    return top



def is_move_valid(move, beakers):
    source, target = map(int, move.split(" "))
    #get source & target beaker 
    src_beaker = beakers[source - 1]
    tgt_beaker = beakers[target - 1]
    #find the top luiqid 
    src_top = find_top_non_zero(src_beaker)
    tgt_top = find_top_non_zero(tgt_beaker)
    #leer
    if src_top == 0:
        return False
    #voll
    if tgt_beaker.count(0) == 0:
        return False
    if tgt_top == 0 or tgt_top == src_top:
        return True
    return False


#this are the 3 beakers
data = [[1, 0, 0], [2, 1, 2], [2, 1, 0]]

print("1: " + str(data[0]))
print("2: " + str(data[1]))
print("3: " + str(data[2]))

print("What is your move? Example move: '1 2' -> liquid from one poured into 2")

move=input()

print(move)

if is_move_valid(move, data):
    print("Move is legal.")
else:
    print("Move is not legal.")