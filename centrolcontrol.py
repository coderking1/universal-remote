import os
from gpiozero import Button
#at gpio two
button1 = Button(2)
#at gpio three
button2 = Button(3)
#at gpio four
button3 = Button(4)
#run(main)
if button1.wait_for_press():
    os.system("python carremote.py")
if button2.wait_for_press():
    os.system("python tv.py")
if button3.wait_for_press():
    os.system("python aircon.py")
if button1.wait_for_press() and button3.wait_for_press():
    os.system("python main.py")
