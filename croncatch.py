from croniter import croniter
import datetime
from crontab import CronTab


cron = CronTab(tabfile='1.tab')


for job in cron:
    sch = job.schedule(date_from=datetime.datetime.now())
    next_event = sch.get_next()
    ne1 = next_event.strftime('%Y-%m-%d %H:%M')
    ne2 = ne1.split(' ')[1]
    
    today = datetime.datetime.today()
    t1 = today.strftime('%Y-%m-%d %H:%M:%S')
    t2 = t1.split(' ')[0]
    t3 = datetime.datetime.strftime(next_event,'%Y-%m-%d')

  
    # print ne2
    # print "Job: ",job
    # print "Next Run: ",next_event
    
    if t2 == t3:
       print ne2," Today - ",job
    else:
        print ne2," Tomorow - ",job
    print "---------------------------------------"
