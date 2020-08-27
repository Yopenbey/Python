import datetime

data=datetime.datetime.now()
nasc=datetime.datetime(1978,3,7)

print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))
print(nasc.strftime("%A"))

%a texto da semana abreviado
%A texto da semana
%w numero do dia da semana
%d numero do dia do mes
%b texto do mes abreviado
%B texto do mes
%m numero do mes
%y ano com dois digitos
%Y ano com quatro digitos
%H horario 00 - 23
%I horario 00 - 12
%p horario AM / PM
%M minutos
%S segundos
%f microsegundos
%j dia do ano 365
%W numero da semana do ano