import os
import sys
from netaddr import *
import threading

def handle_ip_generation():
    counter = 0
    for ip in IPNetwork('0.0.0.0/24'):
        counter += 1

        sys.stdout.write("Gen[%d]\r\n" % counter)

        file = open("D:\out.txt", "a").write(str(ip) + "\r\n")


def handle_cleanup():

    array = open("D:\out.txt", "r").read().split("\r\n")
    open("D:\out.txt", "w").write("")
    file = open("D:\out.txt", "a")

    for i in range(0, len(array)):
        if (array[i].split(".")[0] is not "0"):
            file.write("%s\r\n" % array[i])

    # close the file
    file.close()

handle_ip_generation()
handle_cleanup()
