import os
from gpiozero import Button
#at gpio two
button1 = Button(2)
#at gpio three
button2 = Button(3)
#at gpio four
button3 = Button(4)
#at gpio ten
button4 = Button(10)
#at gpio nine
button5 = Button(9)
#run(main)
if button1.wait_for_press():
    os.system("arduino onair\onair.ino")
if button2.wait_for_press():
    os.system("arduino up\up.ino")
if button3.wait_for_press():
    os.system("arduino down\down.ino")
if button4.wait_for_press():
    os.system("arduino 26\26.ino")
if button5.wait_for_press():
    os.system("arduino offair\offair.ino")
if button1.wait_for_press() and button5.wait_for_press():
    os.system("python centrolcontrol.py")
