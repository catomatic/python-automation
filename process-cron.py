#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import smtplib
import sys
import locale
from subprocess import call, Popen, PIPE

encoding = locale.getdefaultlocale()[1]

services = [
    ('apache2', 'apache2'),
    ('mysqld', 'mysql'),
    ('postgres', 'postgresql'),
    ('master', 'postfix')
]


class Email(object):
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
        super(Email, self).__init__()


class SendSuccessEmail(Email):
    def __init__(self, *args):
        self.sender = 'user@localhost'
        self.receivers = ['user@localhost']
        self.message = '''Subject: All processes running

        The following processes were already running or started
        automatically:
        {0}
        '''.format(args)
        super(Email, self).__init__()


class Action:
    fail_list = []
    success_list = []

    def __init__(self):
        self.fail_list = self.fail_list
        self.success_list = self. success_list

    def check(self):
        for process_name, service_name in services:
            p = Popen(['ps', '-C', process_name], stdout=PIPE)
            output, error = p.communicate()
            if process_name not in output.decode(encoding):
                self.fail_list.append(service_name)
            if process_name in output.decode(encoding):
                self.success_list.append(service_name)


class Start(Action):

    def __init__(self):
        Action.__init__(self)

    def do_action(self):
        if len(self.fail_list) > 0:
            for service in self.fail_list:
                call(['sudo', 'service', service, 'start'])


class Notify(Action):

    def __init__(self):
        Action.__init__(self)

    def do_action(self):
        if len(self.fail_list) > 0:
            SendFailEmail(self.fail_list).send_email()
        else:
            SendSuccessEmail(self.success_list).send_email()


def main():
    if sys.argv[1] == 'start':
        Start().check()
        Start().do_action()
    elif sys.argv[1] == 'notify':
        Notify().check()
        Notify().do_action()


if __name__ == '__main__':
    main()
