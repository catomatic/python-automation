#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import smtplib
import sys
from subprocess import call, Popen, PIPE


class Email:
    def __init__(self):
        self.sender = sender
        self.receivers = receivers
        self.message = message

    def send_email(self):
        smtp = smtplib.SMTP('localhost')
        smtp.sendmail(self.sender, self.receivers, self.message)


class SendFailEmail(Email):
    def __init__(self, *args):
        self.sender = 'user@localhost'
        self.receivers = ['user@localhost']
        self.message = '''Subject: Failed Process Notice

        The following processes failed to start automatically:
        {0}
        '''.format(args)


class SendSuccessEmail(Email):
    def __init__(self, *args):
        self.sender = 'user@localhost'
        self.receivers = ['user@localhost']
        self.message = '''Subject: All processes running

        The following processes were already running or started
        automatically:
        {0}
        '''.format(args)


def notify():
    services = [
        ('apache2', 'apache2'),
        ('mysqld', 'mysql'),
        ('postgres', 'postgresql'),
        ('master', 'postfix')
    ]
    fail_list = []
    success_list = []
    for process_name, service_name in services:
        p = Popen(['ps', '-C', process_name], stdout=PIPE)
        output, error = p.communicate()
        if process_name not in output:
            fail_list.append(process_name)
        if process_name in output:
            success_list.append(process_name)
    if len(fail_list) > 0:
        SendFailEmail(fail_list).send_email()
    else:
        SendSuccessEmail(success_list).send_email()


notify()
