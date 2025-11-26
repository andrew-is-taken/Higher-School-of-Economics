import tkinter as tk
import random

root = tk.Tk()
root.title("2048")


def init_table():
    """Creates the table"""
    return [[0] * 4 for _ in range(4)]


def spawn_new_digit(table):
    """Spawns 2 or 4 in a free space"""
    pool = [(i, j) for i in range(4) for j in range(4) if table[i][j] == 0]
    if pool:
        pos = random.choice(pool)
        table[pos[0]][pos[1]] = random.choice([2, 4])


def combine(row):
    """Moves all digits from the row to the right and combines them if it finds two similar values"""
    temp = [i for i in row if i != 0]
    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            temp[i + 1] *= 2
            temp[i] = 0
    mem = [i for i in temp if i != 0]
    temp = [0] * (4 - len(mem))
    temp += mem
    return temp


def combine_reversed(row):
    """Moves all digits from the row to the left and combines them if it finds two similar values"""
    temp = [i for i in row if i != 0]
    for i in range(len(temp) - 1, 0, -1):
        if temp[i] == temp[i - 1]:
            temp[i - 1] *= 2
            temp[i] = 0
    temp = [i for i in temp if i != 0]
    temp += [0] * (4 - len(temp))
    return temp


def change(table, direction):
    """Determines if the table changed after user's input"""
    changed = False
    if direction in ['W', 'S']:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(table[j][i])
            row_comb = combine(row) if direction == 'S' else combine_reversed(row)
            if row != row_comb:
                changed = True
            for x in range(4):
                table[x][i] = row_comb[x]
    else:
        for i in range(4):
            row = table[i]
            row_comb = combine(row) if direction == 'D' else combine_reversed(row)
            if row != row_comb:
                changed = True
            table[i] = row_comb
    return changed


def update_table(table):
    """Updates the table after user's input"""
    for i in range(4):
        for j in range(4):
            temp = table[i][j]
            col = 'black'
            if 4 < temp <= 16:
                col = 'blue'
            elif 16 < temp <= 64:
                col = 'green'
            elif 64 < temp <= 256:
                col = 'orange'
            label = tk.Label(root, text=str(temp) if temp != 0 else '', font=('Times', 20, 'bold'), fg=col,
                             width=4, height=2, relief='sunken')
            label.grid(row=i, column=j, padx=5, pady=5)


def end_game():
    """Creates new label to indicate that the game has ended"""
    label = tk.Label(root, text='GG', font=('Times', 20, 'bold'))
    label.grid(row=5, columnspan=4)


def start_game():
    """Creates new table, spawns two digits and binds user input to functions"""
    table = init_table()
    spawn_new_digit(table)
    spawn_new_digit(table)
    update_table(table)

    def w_pressed(event):
        """When user presses W"""
        changed_table = change(table, 'W')
        process_input(changed_table)

    def a_pressed(event):
        """When user presses A"""
        changed_table = change(table, 'A')
        process_input(changed_table)

    def s_pressed(event):
        """When user presses S"""
        changed_table = change(table, 'S')
        process_input(changed_table)

    def d_pressed(event):
        """When user presses D"""
        changed_table = change(table, 'D')
        process_input(changed_table)

    def process_input(changed_table):
        """Updates the table and spawns new digit if user pressed button and the game is not ended
        or stops the game if user can't do any more moves"""
        if changed_table:
            spawn_new_digit(table)
            update_table(table)
        else:
            if not horizontally_available(table) and not vertically_available(table):
                end_game()

    def horizontally_available(table):
        """Checks if user still can play by pressing A/D"""
        for i in range(4):
            for j in range(3):
                if table[i][j] == table[i][j + 1]:
                    return True
        return False

    def vertically_available(table):
        """Checks if user still can play by pressing W/S"""
        for i in range(3):
            for j in range(4):
                if table[i][j] == table[i + 1][j]:
                    return True
        return False

    root.bind('w', w_pressed)
    root.bind('a', a_pressed)
    root.bind('s', s_pressed)
    root.bind('d', d_pressed)
    root.mainloop()


if __name__ == '__main__':
    start_game()
