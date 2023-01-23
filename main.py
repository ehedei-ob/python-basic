from time import strftime

hours = int(strftime('%H'))
minutes = int(strftime('%M'))

if hours < 19:
    print(f'Quedan {18-hours} horas y {59-minutes} minutos para irse a casa')
else:
    print('Es hora de irse a casa')

