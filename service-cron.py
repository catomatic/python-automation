#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import sys
from subprocess import call, check_output


def actions(action):
    def wrap(function):
        def wrapped_function(service):
            sc = call(['service', function(service), action])
            return sc
        return wrapped_function
    return wrap


@actions(sys.argv[1])
def service_action(service):
    return service


def run_actions():
    options = ['stop', 'start', 'restart', 'status']
    if sys.argv[1] in options:
        service_action('apache2')
        service_action('mysql')
        service_action('postgresql')
    else:
        return None


run_actions()
