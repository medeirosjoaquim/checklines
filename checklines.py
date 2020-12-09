#!/usr/bin/python

import sys
import subprocess

#some colors
WARNING = '\033[93m'
MESSAGE_COLOR = '\033[96m'
OK = '\033[92m'
FAIL = '\033[91m'

diff_branch = sys.argv[1]
diff = subprocess.run(['git', 'diff', f'HEAD..{diff_branch}', '--numstat'], stdout=subprocess.PIPE)
diff = diff.stdout.decode('utf8')

diff_results = diff.splitlines()
processed_lines = []
changed_lines = 0;
for line in diff_results:
    processed_lines.append(line.strip().split())

for changed in processed_lines:
    changed_lines += int(changed[1])

print (MESSAGE_COLOR,'Total changed lines: ', changed_lines)

if changed_lines <= 200:
   print(OK, 'Your commits are S size')
elif changed_lines < 400:
   print(WARNING, 'Your commits are M size, do not exceed 400 lines')

if changed_lines > 400:
   print(FAIL, 'Your commits are L size, you are over the 400 lines change limit!')

