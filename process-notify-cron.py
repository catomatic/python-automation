#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import smtplib
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
    def __init__(self):
        self.sender = 'user@localhost'
        self.receivers = ['user@localhost']
        self.message = '''Subject: All processes running

        No processes failed to start automatically.'''


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
        SendFailEmail().send_email(fail_list)
    else:
        SendSuccessEmail().send_email()


notify_fail()
