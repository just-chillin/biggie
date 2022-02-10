#!/usr/local/bin/python3

import os
import random
import string
from subprocess import Popen
import signal
import sys

def main(argv):
    if len(argv) > 1 and argv[1] == "pause":
        signal.pause()
        return
        
    arg_count = int(os.getenv('ARG_COUNT', 10))
    arg_len = int(os.getenv('ARG_LEN', 100))
    proc_count = int(os.getenv('PROC_COUNT', 1))
    
    file_path = os.path.realpath(__file__)
    procs = []
    for i in range(proc_count):
        cmd = get_cmd(arg_count, arg_len)
        print("starting {} {}".format(file_path, cmd))
        procs.append(Popen([file_path, *cmd]))
    
    for p in procs:
        p.wait()

def get_cmd(arg_count, arg_len):
    args = ['pause']
    for _ in range(arg_count):
        a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=arg_len))
        args.append(a)
    return args
    
if __name__ == '__main__':
    main(sys.argv)