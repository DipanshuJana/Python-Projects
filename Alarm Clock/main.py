import datetime
import pygame
import sys
from plyer import notification

# main function
def main(hour, minute, second, period, alarm):

    # am/pm loic 
    if period == datetime.datetime.now().strftime('%p'):
        hour += 12

    while True:
        if hour ==  datetime.datetime.now().hour and minute == datetime.datetime.now().minute and second == datetime.datetime.now().second:
            print(f'Alarm at: {hour}:{minute}:{second} {period}')
            alarm.play(-1) # infinite loop sysntax for ringing the clock
            # notification syntax
            notification.notify(
                title = "Python Alarm Clock",
                message = f"You had set you alarm at {hour - 12} : {minute} : {second}0. Enter stop in the program to stop the alarm.",
                app_icon = "D:\\Productivity\\Python\\Projects\\Alarm Clock\\notification.ico",
                timeout = 5
            )
            # stop logic 
            if input() == 'Stop' or input() == 'stop':
                pygame.quit()
                sys.exit()

# initialize everything
if __name__ == '__main__':
    pygame.init()
    print ('HOUR : MINUTE: AM/PM')
    hour = int(input('PLEASE SET THE HOUR:'))
    minute = int(input('PLEASE SET THE MINUTE:'))
    second = int(input('PLEASE SET THE SECOND:'))
    period = input('PLEASE SET AM/PM:').upper()
    alarm = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Alarm Clock\\Alarm.mp3')
    main(hour, minute, second, period, alarm)