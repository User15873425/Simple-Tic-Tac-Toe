def player():
    return 'X' if counter % 2 != 0 else 'O'


def printer():
    print(''.join(field[0][:]))
    print(' '.join(field[1][:]))
    print(' '.join(field[2][:]))
    print(' '.join(field[3][:]))
    print(''.join(field[4][:]))


def win():
    for i in range(1, 4):
        if field[i][0] == field[i][1] == field[i][2] != ' ':
            return True
    for j in range(1, 4):
        if field[0][j] == field[1][j] == field[2][j] != ' ':
            return True
    if field[1][1] == field[2][2] == field[3][3] != ' ':
        return True
    if field[1][3] == field[2][2] == field[3][1] != ' ':
        return True
    return False


cells = list(('|' + ' ' * 3 + '|') * 3)
field = []
while cells:
    field.append(cells[:5])
    cells = cells[5:]
field = [list('-' * 9)] + field + [list('-' * 9)]
counter = 0

printer()

while counter < 10:
    try:
        a, b = input('Enter the coordinates: ').split()
        a = int(a)
        b = int(b)
    except ValueError:
        print('You should enter numbers!')
    else:
        if a < 1 or a > 3 or b < 1 or b > 3:
            print('Coordinates should be from 1 to 3!')
        elif field[a][b] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            counter += 1
            field[a][b] = player()
            printer()
            if win():
                print(f'{player()} wins')
                break
            elif counter == 9:
                print('Draw')
                break
