import sys
from standard import standard_func
import os

for file, dirs, files in os.walk('./data/'):
    for f in files:
        if f.endswith('.in'):
            with open('./data/' + f, 'r') as in_file:
                with open('./data/' + f[:-3] + '.out', 'w') as out_file:
                    old_stdin = sys.stdin
                    old_stdout = sys.stdout
                    sys.stdin = in_file
                    sys.stdout = out_file
                    standard_func()
                    sys.stdin = old_stdin
                    sys.stdout = old_stdout
                    in_file.close()
                    out_file.close()
