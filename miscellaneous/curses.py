'''
show how to use curse
'''

import curses
import time
stdscr = curses.initscr()
stdscr.addstr(5,10,'abv',curses.A_REVERSE)
# to control start show
while 1:
    c = stdscr.getch()
    if c == ord('b'):break
    
for i in range(100,110):
	time.sleep(1)
	stdscr.refresh()
	stdscr.addstr(10,10,chr(i)*10)
	
curses.endwin()
