from croniter import croniter
import datetime
from crontab import CronTab



cron = CronTab(tabfile='1.tab')

def convert(date_time): 
    format = '%H:%M'
    datetime_str = datetime.datetime.strptime(date_time, format) 
    return datetime_str 
   

date_time = raw_input("hora: ")
agora = (convert(date_time)) 


for job in cron:
    sch = job.schedule(date_from=agora)
    next_event = sch.get_next()
    ne1 = next_event.strftime('%Y-%m-%d %H:%M')
    ne2 = ne1.split(' ')[1]
    
    today = datetime.datetime.today()
    t1 = today.strftime('%Y-%m-%d %H:%M:%S')
    t2 = t1.split(' ')[0]
    t3 = datetime.datetime.strftime(next_event,'%Y-%m-%d')

    if t2 == t3:
       print ne2," Today - ",job
    else:
        print ne2," Tomorow - ",job
    print "---------------------------------------"
