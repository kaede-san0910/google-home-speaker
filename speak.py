#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from getch import getch, pause

word = "こんにちわ"
cmd = 'node ~/python/dev/google_home_speaker/index.js こんにちわ'
cnt = 0
#subprocess.check_call(cmd.split(), shell=True)

while True:
    cnt = cnt + 1
    if cnt == 100:
        cnt = 0
    key = ord(getch())
    print("You pressed: %s (%d)" % (chr(key), key))
    if key == 116: # t
        subprocess.check_call('./lang/toyota.sh')
    elif key == 97: # a
        if cnt % 4 == 0:
            subprocess.check_call('./lang/audi.sh')
        elif cnt % 4 == 1:
            subprocess.check_call('./lang/amg.sh')
        elif cnt % 4 == 2:
            subprocess.check_call('./lang/alpha.sh')
        else:
            subprocess.check_call('./lang/aston-martin.sh')
    elif key == 98: # b
        subprocess.check_call('./lang/bmw.sh')
    elif key == 99: # c
        subprocess.check_call('./lang/chevrolet.sh')
    elif key == 104: # h
        if cnt % 2 == 0:
            subprocess.check_call('./lang/honda.sh')
        else:
            subprocess.check_call('./lang/hummer.sh')
    elif key == 106: # j
        subprocess.check_call('./lang/jeep.sh')
    elif key == 108: # l
        subprocess.check_call('./lang/lexus.sh')
    elif key == 109: # m
        if cnt % 3 == 0:
            subprocess.check_call('./lang/mercedes-benz.sh')
        elif cnt % 3 == 1:
            subprocess.check_call('./lang/mini.sh')
        else:
            subprocess.check_call('./lang/mazda.sh')
    elif key == 112: # p
        if cnt % 2 == 0:
            subprocess.check_call('./lang/peugeot.sh')
        elif cnt % 2 == 1:
            subprocess.check_call('./lang/porche.sh')
    elif key == 114: # r
        if cnt % 2 == 0:
            subprocess.check_call('./lang/renault.sh')
        elif cnt % 2 == 1:
            subprocess.check_call('./lang/renault.sh')
    elif key == 115: # s
        subprocess.check_call('./lang/subaru.sh')
    elif key == 118: # v
        subprocess.check_call('./lang/volks.sh')
    elif key == 122: # z
        subprocess.check_call('./lang/zzzz.sh')
#    elif key == 27: # ESC
#        break
    else:
        subprocess.check_call('./lang/error.sh')
pause()
