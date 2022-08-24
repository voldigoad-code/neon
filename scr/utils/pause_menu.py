import menu

from curses import wrapper

def pause_menu(stdscr):
    pause_menu_options = [
        "Resume",
        "Exit"
    ]

    pause_menu = menu.NewMenu(stdscr, pause_menu_options)
    return pause_menu.display_menu()
    
def start_pause_menu():
    wrapper(pause_menu)