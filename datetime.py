from datetime import datetime

data_em_texto = raw_input("data: ") #'16:10'
data = str(data_em_texto)
data_e_hora = datetime.strptime(data_em_texto, '%H:%M')

print "data em texto: ",data_em_texto
print (type(data_em_texto))
print "data: ",data
print (type(data))
print "data e hora: ",data_e_hora
print (type(data_e_hora))

