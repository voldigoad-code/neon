import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

class NewMenu:
    def __init__(self, stdscr, options_list):
        self.options_list = options_list
        self.current_option_index = 0
        self.stdscr = stdscr
        self.y, self.x = self.stdscr.getmaxyx()
    def display_menu(self):
        self.stdscr.refresh()
        playing = True
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.WHITE_AND_BLACK = curses.color_pair(1)

        while playing:
            coord_for_menu = [self.y//2, self.x//2]
            for i in range(len(self.options_list)):
                if self.current_option_index == i:
                    self.stdscr.addstr(coord_for_menu[0] + i, coord_for_menu[1], self.options_list[i], self.WHITE_AND_BLACK)
                else:
                    self.stdscr.addstr(coord_for_menu[0] + i, coord_for_menu[1], self.options_list[i])


            key = self.stdscr.getkey()
            if key == "KEY_DOWN":
                self.current_option_index += 1
            elif key == "KEY_UP":
                self.current_option_index -= 1
            elif key == "KEY_ENTER":
                playing = False
                return self.current_option_index