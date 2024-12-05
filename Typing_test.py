import curses
from curses import wrapper
import time
import random

def start_screen(standardscreen):
    standardscreen.clear()
    standardscreen.addstr("Welcome to the Typing Speed test")
    standardscreen.addstr("\n Press any key to begin!")
    standardscreen.refresh()
    standardscreen.getkey()

'''def load_text():
    with open("Text_Typingtest.txt", "r") as file:
        lines=file.readlines()
        return random.choice(lines).strip()'''

def display_text(standardscreen, target, current, wpm=0):
    standardscreen.addstr(target)
    standardscreen.addstr(1, 0, f"WPM : {wpm}" )
        
    for i,char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        standardscreen.addstr(0, i, char, color)

def wpmtst(standardscreen):
    target_text="a quick brown fox jumped over the lazy dog."
    current_text = []
    wpm = 0
    start_time = time.time()
    standardscreen.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60))/5)
        
        standardscreen.clear()
        display_text(standardscreen, target_text, current_text, wpm)
        standardscreen.refresh()

        if "".join(current_text) == target_text:
            standardscreen.nodelay(False)
            break

        try:
            key = standardscreen.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        
        if key in ("KEY_BAKCSPACE", '\b', "x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
        

def main(standardscreen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(standardscreen)
    
    while True:
        wpmtst(standardscreen)
        standardscreen.addstr(2, 0, "You have successfully completed the text, press <escape key> to quit and any other key to continue")
        key = standardscreen.getkey()
         
        if ord(key) == 27:
            break

wrapper(main)