def pascal(rows):
    l = [1]
    for i in range(rows):
        print(*l)
        l = [sum(x) for x in zip([0]+row, row+[0])]
        
pascal(int(input()))