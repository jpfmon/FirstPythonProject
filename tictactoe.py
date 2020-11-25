ce = ["", "", "", "", "", "", "", "", ""]

s_1 = f"| {ce[0]} | {ce[1]} | {ce[2]} |"
s_2 = f"| {ce[3]} | {ce[4]} | {ce[5]} |"
s_3 = f"| {ce[6]} | {ce[7]} | {ce[8]} |"

turns = 0


def fill_strings(cells_updated):
    global s_1
    global s_2
    global s_3
    s_1 = f"| {ce[0]} | {ce[1]} | {ce[2]} |"
    s_2 = f"| {ce[3]} | {ce[4]} | {ce[5]} |"
    s_3 = f"| {ce[6]} | {ce[7]} | {ce[8]} |"


def reset_all():
    global ce
    global s_1
    global s_2
    global s_3
    ce = ["", "", "", "", "", "", "", "", ""]
    s_1 = f"| {ce[0]} | {ce[1]} | {ce[2]} |"
    s_2 = f"| {ce[3]} | {ce[4]} | {ce[5]} |"
    s_3 = f"| {ce[6]} | {ce[7]} | {ce[8]} |"


def check_not_used(index):
    if ce[index - 1] == "":
        return True
    else:
        return False


def playing_1():
    global ce
    global turns
    while True:
        selec = input("Jugador 1, Introduce tu seleccion: ")
        try:
            selec_index = int(selec)
            if (selec_index <= 0) or (selec_index >= 10):
                raise Exception
            if check_not_used(selec_index):
                ce[selec_index - 1] = "X"
                break
            else:
                print("Seleccion no valida, espacio ya ocupado")
        except:
            print("Por favor, un numero entre 1 y 9")
    turns += 1
    print(f"Turno: {turns}")
    tablero()


def playing_2():
    global ce
    global turns
    while True:
        selec = input("Jugador 2, Introduce tu seleccion: ")
        try:
            selec_index = int(selec)
            if (selec_index <= 0) or (selec_index >= 10):
                raise Exception
            if check_not_used(selec_index):
                ce[selec_index - 1] = "O"
                break
            else:
                print("Seleccion no valida, espacio ya ocupado")
        except:
            print("Por favor, un numero entre 1 y 9")
    turns += 1
    print(f"Turno: {turns}")
    tablero()


def check_elements_equal(row, sign):
    all_equals = True
    for element in row:
        if element != sign:
            all_equals = False
            break
        else:
            all_equals = True
    # print(all_equals)
    return all_equals


def create_rows(ce):
    row_1h = list(ce[:3:1])
    row_2h = list(ce[3:6:1])
    row_3h = list(ce[6::1])
    row_d1 = list(ce[::4])
    row_d2 = list(ce[2:7:2])
    row_1v = list(ce[:7:3])
    row_2v = list(ce[1:8:3])
    row_3v = list(ce[2::3])
    all_rows = [row_1h, row_2h, row_3h, row_d1, row_d2, row_1v, row_2v, row_3v]
    return all_rows


def check_winner_1(ce):
    global keep_playing
    # row_1h = list(ce[:3:1])
    # row_2h = list(ce[3:6:1])
    # row_3h = list(ce[6::1])
    # row_d1 = list(ce[::4])
    # row_d2 = list(ce[2:7:2])
    # row_1v = list(ce[:7:3])
    # row_2v = list(ce[1:8:3])
    # row_3v = list(ce[2::3])
    # all_rows = [row_1h,row_2h,row_3h,row_d1,row_d2,row_1v,row_2v,row_3v]
    all_rows = create_rows(ce)
    for item in all_rows:
        if check_elements_equal(item, "X"):
            keep_playing = False
            break


def check_winner_2(ce):
    global keep_playing
    # row_1h = list(ce[:3:1])
    # row_2h = list(ce[3:6:1])
    # row_3h = list(ce[6::1])
    # row_d1 = list(ce[::4])
    # row_d2 = list(ce[2:7:2])
    # row_1v = list(ce[:7:3])
    # row_2v = list(ce[1:8:3])
    # row_3v = list(ce[2::3])
    # all_rows = [row_1h, row_2h, row_3h, row_d1, row_d2, row_1v, row_2v, row_3v]
    all_rows = create_rows(ce)
    for item in all_rows:
        if check_elements_equal(item, "O"):
            keep_playing = False
            break


def tablero(*args):
    if len(args) > 0:
        index = 0
        for item in args:
            ce[index] = item
            index += 1
    fill_strings(ce)
    print(s_1) 
    print(s_2)
    print(s_3)


keep_playing = True

print("Para seleccionar donde colocar la ficha, introduce el numero correspondiente: ")
tablero(1, 2, 3, 4, 5, 6, 7, 8, 9)
print()
print("Comienza la partida")
reset_all()
tablero()
print("Empieza jugador 1 con 'X', luego jugador 2 con 'O'")

while keep_playing:
    if turns == 9:
        print("Empate!!")
        break
    playing_1()
    check_winner_1(ce)
    if keep_playing == False:
        print("Jugador 1 Gana!!")
        break
    if turns == 9:
        print("Empate!!")
        break
    playing_2()
    check_winner_2(ce)
    if keep_playing == False:
        print("Jugador 2 Gana!!")
        break
