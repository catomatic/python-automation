#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import smtplib
from subprocess import call, Popen, PIPE


def send_fail_email(*args):
    sender = 'user@localhost'
    receivers = ['user@localhost']
    message = '''Subject: Failed Process Notice

    The following processes failed to start automatically:
    {0}
    '''.format(args)

    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(sender, receivers, message)


def send_success_email():
    sender = 'user@localhost'
    receivers = ['user@localhost']
    message = '''Subject: All processes running

    No processes failed to start automatically.'''

    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(sender, receivers, message)


def notify_fail():
    services = [
        ('apache2', 'apache2'),
        ('mysqld', 'mysql'),
        ('postgres', 'postgresql'),
        ('master', 'postfix')
    ]
    fail_list = []
    for process_name, service_name in services:
        p = Popen(['ps', '-C', process_name], stdout=PIPE)
        output, error = p.communicate()
        if process_name not in output:
            fail_list.append(process_name)
    if len(fail_list) > 0:
        send_fail_email(fail_list)
    else:
        send_success_email()


notify_fail()
