After installing the lighttpd http server on the server, follow the following steps:

1. install `flup` via pip (necessary for running lighttpd). Note that if you are using Python 2.7, the new version of flup does not include a module which is fundamental for running the up. In order to enable this, the only choice is to install a different version of flup, i.e. 

   ```
   pip2 install flup==1.0.3.dev-20110405
   ```

1. copy the `lighttpd.conf` file in `/etc/lighttpd`;
1. copy the `conf-available/10-fastcgi-spar.conf in `/etc/lightpd/conf-available`;
1. enable the fastcgi by calling:
 
   ```
   lighttpd-enable-mod fastcgi
   lighttpd-enable-mod fastcgi-spar
   ```
1. make executable (permission 755) all the directories that are accessed by the web.py application used, and readable the files they contain that are used by the same application;
1. make the file sparontologies_log.txt writable to the group "www-data";
1. run the server by calling `/etc/init.d/lighttpd start`.

Use `/etc/init.d/lighttpd stop` for stopping the service, and `/etc/init.d/lighttpd force-reload` for reloading the service (if it is still running).

Since the web application of SPAR creates some files, i.e. the one for the log, it is important that the user www-data has write permission in the directory where the log is stored.