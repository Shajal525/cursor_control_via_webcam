import pyautogui
import time
prev_x = -1 
prev_y = 0
prev_time = 0
mouse_speed = 1       # Intensity of  mouse movement speed
fast_speed = 10
movement_thrashold = 8
time_thrashold = 1
pyautogui.PAUSE = 0     # Zero delay for movement
click_delay = 0.8


def move_cursor(cur_x, cur_y, is_fast):
    global prev_x, prev_y, mouse_speed, movement_thrashold, prev_time, time_thrashold
    cur_time = time.time()
    # If mouse is just selected
    if prev_x == -1 or (cur_time - prev_time) > time_thrashold:
        prev_x, prev_y = cur_x, cur_y
        prev_time = cur_time
        return

    # Ignore very slight movements
    if abs(cur_x-prev_x) + abs(cur_y-prev_y) < movement_thrashold:
        return

    # Move mouse
    x_move = (cur_x - prev_x) * mouse_speed
    y_move = (cur_y - prev_y) * mouse_speed
    dur = 1
    if is_fast:
        x_move = x_move * fast_speed
        y_move = y_move * fast_speed
        dur = 0
    cursor_x, cursor_y = pyautogui.position()
    if pyautogui.onScreen(cursor_x+x_move, cursor_y+y_move):
        
        pyautogui.moveRel(x_move, y_move, duration=0.0001 * dur)
        # pyautogui.moveTo(cursor_x+x_move, cursor_y+y_move, duration = time_dif/100)

    prev_x, prev_y = cur_x, cur_y


def single_click_register():
    # Ignore if movement not started yet
    if prev_x == -1:
        return
    print('Single click registered.')
    # pyautogui.PAUSE = 0.5
    # pyautogui.click(prev_x, prev_y)
    pyautogui.click(pyautogui.position(), duration=click_delay)
    # pyautogui.PAUSE = 0


def double_click_register():
    # Ignore if movement not started yet
    if prev_x == -1:
        return
    print('Double click registered.')
    # pyautogui.PAUSE = 0.5
    # pyautogui.click(prev_x, prev_y, clicks=2)
    pyautogui.click(pyautogui.position(), clicks=2, duration=click_delay)
    # pyautogui.PAUSE = 0


def right_click_register():
    # Ignore if movement not started yet
    if prev_x == -1:
        return
    print('Right click registered.')
    # pyautogui.PAUSE = 0.5
    # pyautogui.click(prev_x, prev_y, button='right')
    pyautogui.click(pyautogui.position(), button='right', duration=click_delay)
    # pyautogui.PAUSE = 0
