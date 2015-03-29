#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

from subprocess import call, Popen, PIPE


def start_process():
    services = [
        ('apache2', 'apache2'),
        ('mysqld', 'mysql'),
        ('postgres', 'postgresql'),
        ('master', 'postfix')
    ]
    for process_name, service_name in services:
        p = Popen(['ps', '-C', process_name], stdout=PIPE)
        output, error = p.communicate()
        if process_name not in output:
            call(['service', service_name, 'start'])
            print '{0}: {1} down, start attempted'.format(process_name, 
                service_name)
        else:
            print '{0}: {1} already running'.format(process_name, service_name)


start_process()
