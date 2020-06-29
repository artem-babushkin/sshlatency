#!/usr/bin/env python2
import getpass
from remote_host import remote_host
import argparse

parser = argparse.ArgumentParser('Connect to SSH host. Send symbol, check it appearance in terminal. Calculate RTT')
parser.add_argument('-a', '--address', required = True , help = 'Host to connect' )
parser.add_argument('-p', '--port', default = 22, help = 'SSH port' )
parser.add_argument('-u', '--user', default = None, help = 'Usename')
parser.add_argument('-r', '--repeat', default = 10, help = 'Number of probes')

a = parser.parse_args().address
p = parser.parse_args().port
u = parser.parse_args().user
r = parser.parse_args().repeat

################################################################################

if not u:
    u = getpass.getuser()

host = remote_host(a, p, u, getpass.getpass('Enter password: '))
host.connect()
host.check_latency(r)
host.close()



################################################################################
