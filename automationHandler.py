import apscheduler

from datetime import datetime

from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

def job_function():
    execfile(main.py)

# Schedule job_function to be called every two hours
sched.add_interval_job(job_function, minutes=1)
