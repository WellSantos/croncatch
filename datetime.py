import datetime
def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Type time: HH:MM ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%H:%M")
            isValid=True
            print d
            print(type(d))
        except:
            print "Type HH::MM time format!\n"
    return d
#test the function
print ObtainDate()

today = datetime.datetime.today()
tomorow = today + datetime.timedelta(days = 1)
print "Hoje: ",today
print "Amanha: ",tomorow