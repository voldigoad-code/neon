def add_ancii_art(ancii_list, stdscr, y, x):
    for i in ancii_list:
        stdscr.addstr(y, x, i)
        y += 1
    stdscr.getch()
    stdscr.refresh()