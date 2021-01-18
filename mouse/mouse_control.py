from mouse import control_functions
import torch
accuracy_thrashold = 0.40                     # If accuracy is less than this, ignore it
class_names = ['SingleClick', 'RightClick', 'DoubleClick', 'Movement']


def control(xoxo, conf, cls):
    global accuracy_thrashold
    cur_x, cur_y, accuracy, type_selected = 0, 0, 0, -1
    if torch.is_tensor(xoxo[0]):
        cur_x, cur_y = (xoxo[0].item() + xoxo[2].item()) / 2, (xoxo[1].item() + xoxo[3].item()) / 2
        accuracy = conf.item()
        type_selected = int(cls.item())
    else:
        return

    # Ignore it if accuracy is less
    if accuracy < accuracy_thrashold:
        return

    if class_names[type_selected] == 'Movement':
        control_functions.move_cursor(cur_x, cur_y)
    elif class_names[type_selected] == 'SingleClick':
        control_functions.single_click_register()
    elif class_names[type_selected] == 'DoubleClick':
        control_functions.double_click_register()
    elif class_names[type_selected] == 'RightClick':
        control_functions.right_click_register()
    else:
        return
