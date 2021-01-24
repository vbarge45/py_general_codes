import time
import winsound
from win10toast import ToastNotifier

#Note:
#Need to install win10toast

def timer(message,minutes):
    notificator = ToastNotifier()
    notificator.show_toast("Alarm",f"Alarm will go off in {minutes} minutes...", duration=50)
    time.sleep(minutes*60)
    winsound.Beep(frequency=2500,duration=1000)
    notificator.show_toast(f"Alarm",message,duration=50)

if __name__ == "__main__":
    message = "Post in github"
    minute = 1
    timer(message,minute)
