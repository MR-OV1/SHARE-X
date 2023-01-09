import os,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    print('\033[1;32m[•] Congrats! Your Device Support This Tools')
    os.system('xdg-open https://www.facebook.com/groups/1087082191981905/?ref=share_group_link')

import s2
