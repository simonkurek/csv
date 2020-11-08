import sys
import os

if len(sys.argv) != 2:
    print('Error: Invalid argument')
    print('Correct usage: "csv filename"')
else:
    filename = sys.argv[1]
    os.system(f'column -s, -t < {filename} | less -#2 -N -S')
