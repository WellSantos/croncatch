from croniter import croniter
import datetime
from crontab import CronTab


cron = CronTab(tabfile='1.tab')


for job in cron:
    sch = job.schedule(date_from=datetime.datetime.now())
    proximo = sch.get_next()
    today = datetime.datetime.now()
    hoje = today.strftime('%Y-%m-%d %H:%M:%S')
    print "Job: ",job
    print "Next Run: ",proximo
    print "Proximo(tipo): ",(type(proximo))
    print "Hoje: ",hoje
    print "Today: ",today
    print "Today(tipo): ",(type(today))
    
    
    if proximo < today:
        print "Hoje",today
    else:
        print "Amanha",proximo
    print "---------------------------------------"
