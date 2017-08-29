import os
from gpiozero import Button
#at gpio two
button1 = Button(2)
#run(main)
if button1.wait_for_press():
    os.system("arduino IRtvSend\IRtvSend.ino")
if button1.wait_for_press() and button2.wait_for_press():
    os.system("python centrolcontrol.py")
