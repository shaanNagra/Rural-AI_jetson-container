#!/usr/bin/env python


import sys
from jtop import jtop, JtopException
import os
import psutil
import csv
import argparse

def transfer(ip, logfilename, path="", recursive=False, remote_path="/home/shaan/Documents/"):
    import paramiko
    from paramiko import SSHClient
    from scp import SCPClient
    
    print("SENDING")
    
    portt='22'
    usern='shaan'
    passw='thefireflyisgr8'

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.load_system_host_keys()
    # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, 
            username=usern,
            password=passw)
    
    scp = SCPClient(ssh.get_transport())
    scp.put(str(path) + str(logfilename),
            recursive = recursive, 
            remote_path = remote_path
        )
    scp.close()
    print("SENT")

def jetson_logger(logfilename):
    parser = argparse.ArgumentParser(description='Simple jtop logger')
    # Standard file to store the logs
    # parser.add_argument('--file', action="store", dest="file", default=str(logfilename))
    # args = parser.parse_args()

    # print("Simple jtop logger")
    # print("Saving log on {file}".format(file=args.file))

    try:
        with jtop() as jetson:
            # Make csv file and setup csv
            with open(logfilename, 'w') as csvfile:
                stats = jetson.stats
                # Initialize cws writer
                writer = csv.DictWriter(csvfile, fieldnames=stats.keys())
                # Write header
                writer.writeheader()
                # Write first row
                writer.writerow(stats)
                # Start loop
                while jetson.ok():
                    stats = jetson.stats
                    # Write row
                    writer.writerow(stats)
                    print("Log at {time}".format(time=stats['time']))
    except JtopException as e:
        print(e)
    except KeyboardInterrupt:
        print("Closed with CTRL-C")
    except IOError:
        print("I/O error")
    
if len(sys.argv) == 3:
    path = "/home/jetson1/"
    logfilename = sys.argv[1]+".csv"
    ip = sys.argv[2]
    jetson_logger(logfilename)
    transfer(ip, logfilename, path)

elif len(sys.argv) ==2:
    logfilename = sys.argv[1]+".csv"
    ip = sys.argv[2]
    jetson_logger(logfilename)
    
else:    
    print("arguments")
    print("filename, ip")


