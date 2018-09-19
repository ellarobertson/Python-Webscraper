import apscheduler

from datetime import datetime

from apscheduler.scheduler import Scheduler

print('in scheduler')

def job_function():
    email = EmailMsg(12.99,11.99,'Ligma','ella.a.robertson@gmail.com')
    print('Automated')

sched = Scheduler(standalone = True)
sched.add_interval_job(job_function, minutes=1)
sched.start()
