
import subprocess
from time import  time
import os


def wc(filename):
    proc = subprocess.Popen(['C:\\Users\\y57b\\UnixTools\\wc.exe', filename])
    return proc

def python_ext(files):
    return (f for f in files if f[-3:] == '.py')

start = time()
procs = []
for root, dirs, files in os.walk("."):  
    for filename in python_ext(files):
        proc = wc(filename)
        procs.append(proc)

for proc in procs:
    proc.communicate()
end = time()
print('Finished in %.3f seconds' % (end - start))