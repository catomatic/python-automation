## Python Automation Scripts

### Start Services

Source file: process-start-cron.py

Written to run as a cron job, attempts to start down services based on process name. Uses the "ps" command to determine if a process is running.

### Status Notify

Source file: process-notify-cron.py

Written to run as a cron job, determines if a service (based on process name, using "ps") is down and sends an email if it is. Also sends an email if no services are determined to be down. Designed to be used in conjunction with process-start-cron.py. Set this to run a short period of time after process-start-cron.py. Note: I have postfix in here, but if postfix is down then obviously no email will be sent.

### Start Services and Notify

Source file: process-cron.py

Class-based combo of process-notify-cron.py and process-start-cron.py.

### Start, Stop, Restart, Status

Source file: service-cron.py

Takes arguments to stop, start, restart, or get status of all services in the if statement; suitable for cron use. Uses decorators, just for fun. I primarily use this to stop all the webserver services at once.

#### Updates

04/01/2015: Added service-cron.py