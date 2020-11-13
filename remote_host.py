#!/usr/bin/env python2
import paramiko
import time

class remote_host():
    def __init__(self, ip, port, user, pasw):
        self.ip   = ip
        self.port = int(port)
        self.user = user
        self.pasw = pasw

    def connect(self):
        self.c = paramiko.SSHClient()
        self.c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.c.connect(hostname = self.ip, username = self.user, password = self.pasw, port = self.port)
        return

    def close(self):
        self.c.close()

    def check_latency(self, repeat = 10):
        assert self.c.get_transport().is_active(), 'Can not connect'
        repeat = int(repeat)
        with self.c.invoke_shell() as ssh:
            r = []
            symbol = '!'
            for x in range(repeat):
                ts1 = time.time()
                ssh.send(symbol)
                while True:
                    data = ssh.recv(1024)
#                    print '*** DEBUG ***  ', data
                    if symbol in data:
                        ts2 = time.time()
                        rtt = (ts2 - ts1) * 1000
                        assert type(rtt) == float
                        r.append(rtt)
                        break
        print '\nStatistics for {}: '.format(self.ip)
        print '\tRTT max: {:.2f}ms\n\tRTT min: {:.2f}ms\n\tRTT avg: {:.2f}ms\n\n'.format(max(r), min(r), sum(r) / len(r))
