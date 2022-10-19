def game_with_cells(m, n):
    if m>=2 and n>=2:
        if m*n%4 == 0:
            num = m*n//4
        elif m*n%2 == 0 and m*n%4 != 0:
            num = m*n//4 + m%n//2
        else :
            num = (m//22)(n//22)/4 + m//2+n//2 + m*n%2
    if m>1 or n>1:
        if (m%2 == 0 and n<2) or (n%2 == 0 and m<2):
            num = m*n//2
        elif m%2 != 0 and n%2 != 0:
            num = m*n//2 + m%n
    else:
        num = 1
    return num
print(game_with_cells(2,2))