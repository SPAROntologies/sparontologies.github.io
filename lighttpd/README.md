After installing the lighttpd http server on the server, follow the following steps:

1. install `flup` via pip (necessary for running lighttpd)
1. copy the lighttpd.conf file in /etc/lighttpd;
1. copy the conf-available/10-fastcgi.conf in /etc/lightpd/conf-available;
1. enable the fastcgi by calling `lighttpd-enable-mod fastcgi`;
1. make executable (permission 755) all the directories that are accessed by the web.py application used, and readable the files they contain that are used by the same application;
1. create an empty file for the socket in `tmp` and assign it to www-data: `touch /tmp/fastcgi.socket-0; chown www-data:www-data /tmp/fastcgi.socket-0`
1. run the server by calling `/etc/init.d/lighttpd start`.

The error log is stored in `/var/log/lighttpd/error.log`. Use `/etc/init.d/lighttpd stop` for stopping the service, and `/etc/init.d/lighttpd force-reload` for reloading the service (if it is still running).

Since the web application of OpenCitations creates some files, i.e. the one for the log, it is important that the user www-data has write permission in the directory where the log is stored.