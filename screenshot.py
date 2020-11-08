import subprocess

filename = 'mainscript.py'

def foo():
    while True:
        try:
            p = subprocess.Popen('python ' + filename, shell=True).wait()
        except:
            pass
        else:
            break

foo()