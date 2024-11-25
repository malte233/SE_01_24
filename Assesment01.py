# liquid highst 
def find_top_non_zero(beaker):
    top = 0
    for value in beaker:
        if value != 0:
            top = value
    return top



def is_move_valid(move, beakers):
    source, target = map(int, move.split(" "))
    #access beaker 
    src_beaker = beakers[source - 1]
    tgt_beaker = beakers[target - 1]
    #find the top luiqid 
    src_top = find_top_non_zero(src_beaker)
    tgt_top = find_top_non_zero(tgt_beaker)
    #empty
    if src_top == 0:
        return False
    #full
    if tgt_beaker.count(0) == 0:
        return False
    if tgt_top == 0 or tgt_top == src_top:
        return True
    return False


#function should execute liquid pouring 
def make_move(move, data):
    source, target = map(int, move.split(" "))
    #access beaker 
    src_beaker = data[source - 1]
    tgt_beaker = data[target - 1]
   
    src_top = find_top_non_zero(src_beaker)
    zero_count = tgt_beaker.count(0)
    #pour liquid 
    tgt_beaker[3 - zero_count] = src_top

    src_beaker_non_zero_count = src_beaker.count(1,2,3)
    tgt_beaker[src_beaker_non_zero_count - 1] = 0

    #if i would have more time i would have done the following to complete exercices2

    #reconstrunct data array with changed beakers

    #give back changed data array
    return



data = [[1, 0, 0], [2, 1, 2], [2, 1, 0]]

while True:

    print("\nCurrent Beakers:")
    print("1:", data[0])
    print("2:", data[1])
    print("3:", data[2])
    print("What is your move? Example move: '1 2' -> liquid from 1 poured into 2")


    move = input()
    print("You chose:"+move)
    
    if is_move_valid(move, data):
        print("Move is legal.")
        data = make_move(move, data)
    else:
        print("Move is not legal.")

