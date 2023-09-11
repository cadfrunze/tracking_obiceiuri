from datetime import datetime

minute = datetime.now().minute
ora = datetime.now().hour
zi = datetime.now().day
luna = datetime.now().month
an = datetime.now().year

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'Data: {zi}/{luna}/{an} | Ora: {ora}:{minute}')