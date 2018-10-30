import sched, time
from plyer import notification

BREAK_TIME = 120*60

s = sched.scheduler(time.time, time.sleep)

def notify_break():
    notification.notify(
        title="BreakNot",
        message="Get up from that chair."
    )
    input("Press Enter when the break is terminated...")
    reschedule()

def reschedule():
    s.enter(BREAK_TIME, 1, notify_break)

if __name__ == '__main__':
    reschedule()
    s.run()