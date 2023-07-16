import os
import sys

while 1:
    i = input("terminal<~$_ ")
    params = i.split()
    
    new_pid = os.fork()
    if new_pid == 0:
        print ("I am the child process")
        os.execvp(params[0], params)
        
    else:
        print("I am the Parent process")
        print("The child process id is ", new_pid)
        os.wait()
