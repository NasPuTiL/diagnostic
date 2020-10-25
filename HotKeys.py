from pynput.keyboard import Key, Listener
path = ""
def on_press(key):
    global path
    if key != Key.space:
        path += str(key)
    else:
        path += ' '

    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    print(path)


A

I AM LORD