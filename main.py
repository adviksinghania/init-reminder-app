import subprocess
import os

run = True
while run:
    text = input('What shall I remind you about? : ')
    local_time = float(input('In how many minutes? : '))
    local_time = local_time * 60
    path = os.getcwd()
    subprocess.Popen(f'python3 {path}/remind.py -t "{text}" -m {local_time}', shell=True)
    ask = input('Reminder saved. Do you want to continue ? (y/n) : ')
    if ask in {'y', 'yes', 'Yes', 'Y'}:
        continue
    elif ask in {'n', 'no', 'No', 'N'}:
        run = False

print('Exiting...')
