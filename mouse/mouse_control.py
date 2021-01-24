from mouse import control_functions
import torch
accuracy_thrashold = 0.40                     # If accuracy is less than this, ignore it
click_thrashold = 0.60
class_names = ['Movement', 'SingleClick', 'RightClick', 'DoubleClick', 'FastMovement']


def control(xoxo, conf, cls):
    global accuracy_thrashold
    cur_x, cur_y, accuracy, type_selected = 0, 0, 0, -1
    if torch.is_tensor(xoxo[0]):
        cur_x, cur_y = (xoxo[0].item() + xoxo[2].item()) / 2, (xoxo[1].item() + xoxo[3].item()) / 2
        accuracy = conf.item()
        type_selected = int(cls.item())
    else:
        return

    print(f'Cur_x is: {cur_x}, cur_y is: {cur_y}, accuracy is: {accuracy}, type is: {type_selected}')

    # Ignore it if accuracy is less
    if (type_selected == 0 or type_selected == 4) and accuracy < accuracy_thrashold:
        return
    if type_selected != 0 and type_selected != 4 and accuracy < click_thrashold:
        return

    # class_name[0] = 'Movement'
    if type_selected == 0:
        control_functions.move_cursor(cur_x, cur_y, 0)
    # class_name[4] = 'FastMovement'
    elif type_selected == 4:
        control_functions.move_cursor(cur_x, cur_y, 1)
    # class_name[1] = 'SingleClick'
    elif type_selected == 1:
        control_functions.single_click_register()
    # class_name[3] = 'DoubleClick'
    elif type_selected == 3:
        control_functions.double_click_register()
    # class_name[2] = 'RightClick'
    elif type_selected == 2:
        control_functions.right_click_register()
    else:
        return
