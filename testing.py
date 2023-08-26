import datetime

ieri = datetime.date(2023, 8, 25)
azi = datetime.datetime.now()
print(ieri.strftime('%d/%m/%y'))
with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'\nData: {ieri.strftime("%d/%m/%y")} | Ora: 19:00')
    fisier.writelines(f'\nData: {azi.strftime("%d/%m/%y")} | Ora: {azi.hour}:{azi.minute}')
