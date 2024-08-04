import time, sys
indent = 0
indentIncreasing = True
anim = '***********'


try:
    while True:
        print(' ' * indent, end='')  #end will skip newline, printing anim right after
        print(anim) #newline
        time.sleep(0.1)

        if indentIncreasing: #increase num of spaces
            indent+=1
            if indent==20:
                indentIncreasing = False

        else: #decrease num of spaces
            indent-=1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()