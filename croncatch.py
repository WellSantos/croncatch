from croniter import croniter
import datetime
from crontab import CronTab



cron = CronTab(tabfile='schedule.tab')

def convert_time():
    valid=False
    while not valid:
        date_time = raw_input("Type \"HH:MM\" time format: ")
        try:
            dt1 = datetime.datetime.today()
            dt2 = dt1
            dt3 = str(dt2)
            date_full = dt3.split(' ')[0] + " " + date_time
            format = '%Y-%m-%d %H:%M'
            datetime_str = datetime.datetime.strptime(date_full, format) 
            return datetime_str 
            valid=True
        except:
            print "Please, Type HH::MM time format!\n"
    return datetime_str
    
user_input = convert_time() 

print "-----------------------------------------"
for job in cron:
    sch = job.schedule(date_from=user_input)
    next_event = sch.get_next()
    ne1 = next_event.strftime('%Y-%m-%d %H:%M')
    ne2 = ne1.split(' ')[1]
    j = job.command

    
    today = datetime.datetime.today()
    t1 = today.strftime('%Y-%m-%d %H:%M:%S')
    t2 = t1.split(' ')[0]
    t3 = datetime.datetime.strftime(next_event,'%Y-%m-%d')

    if t2 == t3:
       print ne2," Today - ",j
    else:
        print ne2," Tomorow - ",j
    print "-----------------------------------------"

