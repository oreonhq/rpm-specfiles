# Replace all occurrences of /srv/trac with your trac root below
# and uncomment the respective SetEnv and PythonOption directives.
WSGIScriptAlias /trac /var/www/cgi-bin/trac.wsgi

<Directory /var/www/>
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
# <LocationMatch /cgi-bin/trac\.f?cgi>
#     SetEnv TRAC_ENV /opt/trac/hn-aci
# </LocationMatch>
# <IfModule mod_python.c>
# <Location /cgi-bin/trac.cgi>
#     SetHandler mod_python
#     PythonHandler trac.web.modpython_frontend
#     #PythonOption TracEnv /srv/trac
# </Location>
# </IfModule>
