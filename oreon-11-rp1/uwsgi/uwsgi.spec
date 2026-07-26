%global source0_hash a48bb0365542b738a5e7a2a7031488e756f9256bb5bf30d2fc5f7bb8f55138b9

# Documentation sources:
%global commit 5784c30866a94942a5200db4d5f6c2850afb1caa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global docrepo uwsgi-docs

# The default compile options of uwsgi and php disagree in subtle ways,
# leading to potential crashes when uwsgi loads the php module, and php itself
# loads certain of its own modules.
#
# The "proper" solution for this would be to change the way php is compiled.
# In the interim, disabling PIE for uwsgi, and enabling PIC for the main
# uwsgi executable can work around the issue.
#
# See https://bugzilla.redhat.com/show_bug.cgi?id=2203863
%undefine _hardened_build

%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_moddir: %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}

# This is primarily built for fedora, make it easy right now
%if 0%{?fedora}
%bcond_without go
%bcond_without python3
%bcond_without python3_greenlet
%bcond_without ruby19
%bcond_without tuntap
%bcond_without zeromq
%bcond_without perl
%bcond_with perlcoro
%bcond_without glusterfs
%bcond_without php
%bcond_without pq
%bcond_without gloox
%bcond_without geoip
%bcond_without ruby_rack
# javapackages-tools retired (apache-ivy orphanage)
%bcond_with java
# Fedora httpd includes mod_proxy_uwsgi
# https://bugzilla.redhat.com/show_bug.cgi?id=1574335
%bcond_with mod_proxy_uwsgi
#mono
%ifarch %{mono_arches}
%bcond_without mono
%else
%bcond_with mono
%endif
# mongodblibs
# mongo-cxx-driver-legacy broken in rawhide rhbz#1675407
%bcond_with mongodblibs
# v8-314 retired
%bcond_with v8
#mongodblibs dependency
%if %{without mongodblibs}
%bcond_with gridfs
%else
%bcond_without gridfs
%endif
#Fedora endif
%endif

# epel8 builds pretty similar to Fedora for now
%if 0%{?rhel} == 8
%bcond_without go
%bcond_without python3
%bcond_without python3_greenlet
%bcond_without ruby19
%bcond_without tuntap
%bcond_without zeromq
%bcond_without perl
%bcond_without perlcoro
%bcond_without glusterfs
%bcond_without php
%bcond_without pq
%bcond_without gloox
%bcond_without geoip
%bcond_without ruby_rack
# javapackages-tools retired (apache-ivy orphanage)
%bcond_with java
# Fedora httpd includes mod_proxy_uwsgi
# https://bugzilla.redhat.com/show_bug.cgi?id=1574335
%bcond_with mod_proxy_uwsgi
#mono
%ifarch %{mono_arches}
%bcond_without mono
%else
%bcond_with mono
%endif
# mongodblibs
# mongo-cxx-driver-legacy broken in rawhide rhbz#1675407
%bcond_with mongodblibs
# v8-314 retired
%bcond_with v8
#mongodblibs dependency
%if %{without mongodblibs}
%bcond_with gridfs
%else
%bcond_without gridfs
%endif
#EL8 endif
%endif

%if 0%{?rhel} == 9
%bcond_without go
%bcond_without python3
# EPEL9 does not have python-greenlet-devel any more
%bcond_with python3_greenlet
%bcond_without ruby19
%bcond_without tuntap
# EPEL9 doesn't have zeromq yet
%bcond_with zeromq
%bcond_without perl
# EPEL9 doesn't have perl-Coro yet
%bcond_with perlcoro
# EPEL9 doesn't have glusterfs yet
%bcond_with glusterfs
%bcond_without php
%bcond_without pq
%bcond_without ruby_rack
# EPEL9 doesn't have gloox yet
%bcond_with gloox
# EPEL9 doesn't have GeoIP yet
%bcond_with geoip
# javapackages-tools retired (apache-ivy orphanage)
%bcond_with java
# Fedora httpd includes mod_proxy_uwsgi
# https://bugzilla.redhat.com/show_bug.cgi?id=1574335
%bcond_with mod_proxy_uwsgi
#mono
%ifarch %{mono_arches}
%bcond_without mono
%else
%bcond_with mono
%endif
# mongodblibs
# mongo-cxx-driver-legacy broken in rawhide rhbz#1675407
%bcond_with mongodblibs
# v8-314 retired
%bcond_with v8
#mongodblibs dependency
%if %{without mongodblibs}
%bcond_with gridfs
%else
%bcond_without gridfs
%endif

# EL9 has multiple python3 versions
%bcond_without python3_alternate1
%if %{with python3_alternate1}
%global python3_alternate1_pkgname python3.11
%global __python3_alternate1 python3.11
%global python3_alternate1_sitelib %(RPM_BUILD_ROOT= %{__python3_alternate1} -Ic "import sysconfig; print(sysconfig.get_path('purelib', vars={'platbase': '%{_prefix}', 'base': '%{_prefix}'}))")
%global python3_alternate1_version 3.11
%global python3_alternate1_version_nodots 311
%endif
%bcond_without python3_alternate2
%if %{with python3_alternate2}
%global python3_alternate2_pkgname python3.12
%global __python3_alternate2 python3.12
%global python3_alternate2_sitelib %(RPM_BUILD_ROOT= %{__python3_alternate2} -Ic "import sysconfig; print(sysconfig.get_path('purelib', vars={'platbase': '%{_prefix}', 'base': '%{_prefix}'}))")
%global python3_alternate2_version 3.12
%global python3_alternate2_version_nodots 312
%endif
%bcond_without python3_alternate3
%if %{with python3_alternate3}
%global python3_alternate3_pkgname python3.13
%global __python3_alternate3 python3.13
%global python3_alternate3_sitelib %(RPM_BUILD_ROOT= %{__python3_alternate3} -Ic "import sysconfig; print(sysconfig.get_path('purelib', vars={'platbase': '%{_prefix}', 'base': '%{_prefix}'}))")
%global python3_alternate3_version 3.13
%global python3_alternate3_version_nodots 313
%endif
#EL9 endif
%endif

%if 0%{?rhel} == 10
# EPEL10 does not have gcc-go
%bcond_with go
%bcond_without python3
# EPEL10 does not have python-greenlet-devel any more
%bcond_with python3_greenlet
%bcond_without ruby19
%bcond_without tuntap
# EPEL10 doesn't have zeromq yet
%bcond_with zeromq
%bcond_without perl
# EPEL10 doesn't have perl-Coro yet
%bcond_with perlcoro
# EPEL10 doesn't have glusterfs yet
%bcond_with glusterfs
%bcond_without php
%bcond_without pq
%bcond_without ruby_rack
# EPEL10 doesn't have gloox yet
%bcond_with gloox
# EPEL10 doesn't have GeoIP yet
%bcond_with geoip
# javapackages-tools retired (apache-ivy orphanage)
%bcond_with java
# Fedora httpd includes mod_proxy_uwsgi
# https://bugzilla.redhat.com/show_bug.cgi?id=1574335
%bcond_with mod_proxy_uwsgi
#mono
# EPEL10 doesn't have mono yet
%ifarch %{mono_arches}
%bcond_with mono
%else
%bcond_with mono
%endif
# mongodblibs
# mongo-cxx-driver-legacy broken in rawhide rhbz#1675407
%bcond_with mongodblibs
# v8-314 retired
%bcond_with v8
#mongodblibs dependency
%if %{without mongodblibs}
%bcond_with gridfs
%else
%bcond_without gridfs
%endif

# EL10 has multiple python3 versions
%bcond_without python3_alternate1
%if %{with python3_alternate1}
%global python3_alternate1_pkgname python3.12
%global __python3_alternate1 python3.12
%global python3_alternate1_sitelib %(RPM_BUILD_ROOT= %{__python3_alternate1} -Ic "import sysconfig; print(sysconfig.get_path('purelib', vars={'platbase': '%{_prefix}', 'base': '%{_prefix}'}))")}
%global python3_alternate1_version 3.12
%global python3_alternate1_version_nodots 312
%endif
#EL9 endif
%endif

%global manual_py_compile 1

# Turn off byte compilation so it doesn't try
# to auto-optimize the code in /usr/src/uwsgi
%if %{manual_py_compile} == 1
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%endif

# Set %%__python to the newest possible version
%if %{with python3}
%global __python %{__python3}
%else
%if %{with python3_alternate1}
%global __python %{__python3_alternate1}
%else
%if %{with python3_alternate2}
%global __python %{__python3_alternate2}
%else
%if %{with python3_alternate3}
%global __python %{__python3_alternate3}
%else
%if %{with python2}
%global __python %{__python2}
%else
%global __python /usr/bin/true
%endif
%endif
%endif
%endif
%endif

Name:           uwsgi
Version:        2.0.31
Release:        6%{?dist}
Summary:        Fast, self-healing, application container server
# uwsgi is licensed under GPLv2 with a linking exception
# docs are licensed under MIT
# Automatically converted from old format: GPLv2 with exceptions and MIT - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions AND LicenseRef-Callaway-MIT
URL:            https://github.com/unbit/uwsgi

ExcludeArch:    %{ix86}

Source0:        https://github.com/unbit/uwsgi/archive/refs/tags/%{version}.tar.gz
Source1:        fedora.ini
Source2:        uwsgi.service
Source3:        emperor.ini
Source4:        https://github.com/unbit/%{docrepo}/archive/%{commit}/%{docrepo}-%{shortcommit}.tar.gz
Source5:        README.Fedora
Source7:        uwsgi.tmpfiles
Source8:        uwsgi.sysusers

# When adding patches please add to the end, don't
# reuse intermediate numbers
Patch0:         uwsgi_trick_chroot_rpmbuild.patch
Patch1:         uwsgi_fix_rpath.patch
Patch2:         uwsgi_ruby20_compatibility.patch
Patch3:         uwsgi_fix_lua.patch
# https://github.com/unbit/uwsgi/issues/882
Patch5:         uwsgi_fix_mongodb.patch
Patch6:         uwsgi_v8-314_compatibility.patch
Patch7:         uwsgi_fix_mono.patch
Patch13:        uwsgi_fix_chroot_chdir.patch
Patch14:        uwsgi_python312-2.patch

BuildRequires:  curl, libxml2-devel, libuuid-devel, jansson-devel
BuildRequires:  libyaml-devel, ruby-devel
BuildRequires:  libxcrypt-devel
%if %{with tcp_wrappers}
BuildRequires:  tcp_wrappers-devel
%endif
%if %{with python2}
BuildRequires:  python2-devel
%if %{with python2_greenlet}
BuildRequires:  python-greenlet-devel
%endif
%endif
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
%endif
%if %{with python3_greenlet}
BuildRequires:  python%{python3_pkgversion}-greenlet-devel
%endif
%if %{with python3_alternate1}
BuildRequires:  %{python3_alternate1_pkgname}-devel
%endif
%if %{with python3_alternate2}
BuildRequires:  %{python3_alternate2_pkgname}-devel
%endif
%if %{with python3_alternate3}
BuildRequires:  %{python3_alternate3_pkgname}-devel
%endif
%if %{with glusterfs}
BuildRequires:  glusterfs-devel, glusterfs-api-devel
%endif
BuildRequires:  lua-devel, ruby, pcre2-devel
%if %{with php}
BuildRequires:  php-devel, php-embedded
%endif
BuildRequires:  libedit-devel, krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  bzip2-devel, gmp-devel, pam-devel
BuildRequires:  sqlite-devel, libcap-devel
BuildRequires:  httpd-devel, libcurl-devel
BuildRequires:  libstdc++-devel
%if %{with gloox}
BuildRequires:  gloox-devel
%endif
BuildRequires:  libevent-devel, zlib-devel
%if %{with geoip}
BuildRequires:  GeoIP-devel
%endif
BuildRequires:  openldap-devel, boost-devel
BuildRequires:  libattr-devel, libxslt-devel
%if %{with perl}
BuildRequires:  perl-devel, perl-ExtUtils-Embed
%if %{with perlcoro}
BuildRequires: perl-Coro
%endif
%endif
%if %{with zeromq}
BuildRequires:  zeromq-devel
%endif
%if %{with go}
BuildRequires:  gcc-go
%endif
BuildRequires:  systemd-devel, systemd-units
%if %{with mono}
BuildRequires:  mono-devel, mono-web, glib2-devel
%endif
%if %{with v8}
%if 0%{?fedora}
BuildRequires:  v8-314-devel
%else
BuildRequires:  v8-devel
%endif
%endif
%if %{with mongodblibs}
%if 0%{?fedora}
BuildRequires:  mongo-cxx-driver-legacy-devel
%else
BuildRequires:  mongo-cxx-driver-devel
%endif
%endif
%if %{with pq}
BuildRequires:  libpq-devel
%endif

%if 0%{?fedora}
BuildRequires:  libargon2-devel
Obsoletes:      uwsgi-router-access <= 2.0.16
%endif

Obsoletes:      uwsgi-loggers <= 1.9.8-1
Obsoletes:      uwsgi-routers <= 2.0.6
Obsoletes:      uwsgi-plugin-erlang <= 1.9.20-1
Obsoletes:      uwsgi-plugin-admin <= 2.0.6

%{?systemd_requires}

%filter_requires_in %{_usrsrc}
%filter_provides_in %{_usrsrc}
%filter_provides_in %{_libdir}/uwsgi/.*\.so$
%filter_setup

%description
uWSGI is a fast (pure C), self-healing, developer/sysadmin-friendly
application container server.  Born as a WSGI-only server, over time it has
evolved in a complete stack for networked/clustered web applications,
implementing message/object passing, caching, RPC and process management.
It uses the uwsgi (all lowercase, already included by default in the Nginx
and Cherokee releases) protocol for all the networking/interprocess
communications.  Can be run in preforking mode, threaded,
asynchronous/evented and supports various form of green threads/co-routine
(like uGreen and Fiber).  Sysadmin will love it as it can be configured via
command line, environment variables, xml, .ini and yaml files and via LDAP.
Being fully modular can use tons of different technology on top of the same
core.

%package -n uwsgi-devel
Summary:    uWSGI - Development header files and libraries
Requires:   uwsgi = %{version}-%{release}

%description -n uwsgi-devel
This package contains the development header files and libraries
for uWSGI extensions

%if %{with python2}
%package -n python2-uwsgidecorators
Summary:        Python 2 decorators providing access to the uwsgi API
Requires:       uwsgi = %{version}-%{release}
Requires:       uwsgi-plugin-python2 = %{version}-%{release}
Obsoletes:      python-uwsgidecorators < 2.0.16-4
Provides:       python-uwsgidecorators = %{version}-%{release}

%description -n python2-uwsgidecorators
The uwsgidecorators Python 2 module provides higher-level access to the uWSGI API.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-uwsgidecorators
Summary:        Python %{python3_version} decorators providing access to the uwsgi API
Requires:       uwsgi = %{version}-%{release}
Requires:       uwsgi-plugin-python%{python3_pkgversion} = %{version}-%{release}
%if 0%{?rhel} == 7
Obsoletes:      python3-uwsgidecorators < 2.0.16-4
Provides:       python3-uwsgidecorators = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-uwsgidecorators
The uwsgidecorators Python %{python3_version} module provides higher-level
access to the uWSGI API.
%endif

%if %{with python3_alternate1}
%package -n %{python3_alternate1_pkgname}-uwsgidecorators
Summary:        Python %{python3_alternate1_version} decorators providing access to the uwsgi API
Requires:       uwsgi = %{version}-%{release}
Requires:       uwsgi-plugin-python%{python3_alternate1_version_nodots} = %{version}-%{release}

%description -n %{python3_alternate1_pkgname}-uwsgidecorators
The uwsgidecorators Python %{python3_alternate1_version} module provides
higher-level access to the uWSGI API.
%endif

%if %{with python3_alternate2}
%package -n %{python3_alternate2_pkgname}-uwsgidecorators
Summary:        Python %{python3_alternate2_version} decorators providing access to the uwsgi API
Requires:       uwsgi = %{version}-%{release}
Requires:       uwsgi-plugin-python%{python3_alternate2_version_nodots} = %{version}-%{release}

%description -n %{python3_alternate2_pkgname}-uwsgidecorators
The uwsgidecorators Python %{python3_alternate2_version} module provides
higher-level access to the uWSGI API.
%endif

%if %{with python3_alternate3}
%package -n %{python3_alternate3_pkgname}-uwsgidecorators
Summary:        Python %{python3_alternate3_version} decorators providing access to the uwsgi API
Requires:       uwsgi = %{version}-%{release}
Requires:       uwsgi-plugin-python%{python3_alternate3_version_nodots} = %{version}-%{release}

%description -n %{python3_alternate3_pkgname}-uwsgidecorators
The uwsgidecorators Python %{python3_alternate3_version} module provides
higher-level access to the uWSGI API.
%endif

%package -n uwsgi-docs
Summary:  uWSGI - Documentation
Requires: uwsgi

%description -n uwsgi-docs
This package contains the documentation files for uWSGI

%package -n uwsgi-plugin-common
Summary:  uWSGI - Common plugins for uWSGI
Requires: uwsgi = %{version}-%{release}

%description -n uwsgi-plugin-common
This package contains the most common plugins used with uWSGI. The
plugins included in this package are: cache, CGI, RPC, uGreen

# Stats pushers

%package -n uwsgi-stats-pusher-file
Summary:    uWSGI - File Stats Pusher for uWSGI
Requires:   uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-stats-pusher-file
This package contains the stats_pusher_file plugin for uWSGI

%if %{with mongodblibs}
%package -n uwsgi-stats-pusher-mongodb
Summary:    uWSGI - MongoDB Stats Pusher for uWSGI
Requires:   uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-stats-pusher-mongodb
This package contains the stats_pusher_mongodb plugin for uWSGI
%endif

%package -n uwsgi-stats-pusher-socket
Summary:    uWSGI - Socket Stats Pusher for uWSGI
Requires:   uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-stats-pusher-socket
This package contains the stats_pusher_socket plugin for uWSGI

%package -n uwsgi-stats-pusher-statsd
Summary:    uWSGI - StatsD Stats Pusher for uWSGI
Requires:   uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-stats-pusher-statsd
This package contains the stats_pusher_statsd plugin for uWSGI

%package -n uwsgi-stats-pusher-zabbix
Summary:    uWSGI - Zabbix Stats Pusher for uWSGI
Requires:   uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-stats-pusher-zabbix
This package contains the zabbix plugin for uWSGI

# Alarms

%package -n uwsgi-alarm-curl
Summary:  uWSGI - Curl alarm plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-alarm-curl
This package contains the alarm_curl alarm plugin for uWSGI

%if %{with gloox}
%package -n uwsgi-alarm-xmpp
Summary:  uWSGI - Curl alarm plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-alarm-xmpp
This package contains the alarm_xmpp alarm plugin for uWSGI
%endif

# Transformations

%package -n uwsgi-transformation-chunked
Summary:  uWSGI - Chunked Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-router-uwsgi = %{version}-%{release}

%description -n uwsgi-transformation-chunked
This package contains the transformation_chunked plugin for uWSGI

%package -n uwsgi-transformation-gzip
Summary:  uWSGI - GZip Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-router-uwsgi = %{version}-%{release}

%description -n uwsgi-transformation-gzip
This package contains the transformation_gzip plugin for uWSGI

%package -n uwsgi-transformation-offload
Summary:  uWSGI - Off-Load Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-router-uwsgi = %{version}-%{release}

%description -n uwsgi-transformation-offload
This package contains the transformation_offload plugin for uWSGI

%package -n uwsgi-transformation-template
Summary:  uWSGI - Template Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-router-uwsgi = %{version}-%{release}

%description -n uwsgi-transformation-template
This package contains the transformation_template plugin for uWSGI

%package -n uwsgi-transformation-tofile
Summary:  uWSGI - ToFile Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-router-uwsgi = %{version}-%{release}

%description -n uwsgi-transformation-tofile
This package contains the transformation_tofile plugin for uWSGI

%package -n uwsgi-transformation-toupper
Summary:  uWSGI - ToUpper Transformation plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-transformation-toupper
This package contains the transformation_toupper plugin for uWSGI

# Loggers

%package -n uwsgi-log-encoder-msgpack
Summary:  uWSGI - msgpack log encoder plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-log-encoder-msgpack
This package contains the msgpack log encoder plugin for uWSGI

%package -n uwsgi-logger-crypto
Summary:  uWSGI - logcrypto logger plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-logger-crypto
This package contains the logcrypto logger plugin for uWSGI

%package -n uwsgi-logger-file
Summary:   uWSGI - logfile logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-loggers <= 1.9.8-1
Provides:  uwsgi-loggers = %{version}-%{release}

%description -n uwsgi-logger-file
This package contains the logfile logger plugin for uWSGI

%package -n uwsgi-logger-graylog2
Summary:   uWSGI - Graylog2 logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-logger-graylog2
This package contains the graylog2 logger plugin for uWSGI

%if %{with mongodblibs}
%package -n uwsgi-logger-mongodb
Summary:   uWSGI - mongodblog logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-loggers <= 1.9.8-1
Provides:  uwsgi-loggers = %{version}-%{release}

%description -n uwsgi-logger-mongodb
This package contains the mongodblog logger plugin for uWSGI
%endif

%package -n uwsgi-logger-pipe
Summary:  uWSGI - logpipe logger plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-logger-pipe
This package contains the logcrypto logger plugin for uWSGI

%package -n uwsgi-logger-redis
Summary:   uWSGI - redislog logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-loggers <= 1.9.8-1
Provides:  uwsgi-loggers = %{version}-%{release}

%description -n uwsgi-logger-redis
This package contains the redislog logger plugin for uWSGI

%package -n uwsgi-logger-rsyslog
Summary:   uWSGI - rsyslog logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-rsyslog <= 1.9.8-1
Provides:  uwsgi-plugin-rsyslog = %{version}-%{release}

%description -n uwsgi-logger-rsyslog
This package contains the rsyslog logger plugin for uWSGI

%package -n uwsgi-logger-socket
Summary:   uWSGI - logsocket logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-loggers <= 1.9.8-1
Provides:  uwsgi-loggers = %{version}-%{release}

%description -n uwsgi-logger-socket
This package contains the logsocket logger plugin for uWSGI

%package -n uwsgi-logger-syslog
Summary:   uWSGI - syslog logger plugin
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-syslog <= 1.9.8-1
Provides:  uwsgi-plugin-syslog = %{version}-%{release}

%description -n uwsgi-logger-syslog
This package contains the syslog logger plugin for uWSGI

%package -n uwsgi-logger-systemd
Summary:  uWSGI - systemd journal logger plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-logger-systemd
This package contains the systemd journal logger plugin for uWSGI

%if %{with zeromq}
%package -n uwsgi-logger-zeromq
Summary:  uWSGI - ZeroMQ logger plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, zeromq

%description -n uwsgi-logger-zeromq
This package contains the ZeroMQ logger plugin for uWSGI
%endif

# Plugins

%package -n uwsgi-plugin-airbrake
Summary:  uWSGI - Plugin for AirBrake support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-airbrake
This package contains the airbrake plugin for uWSGI

%package -n uwsgi-plugin-cache
Summary:  uWSGI - Plugin for cache support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-cache
This package contains the cache plugin for uWSGI

%package -n uwsgi-plugin-carbon
Summary:  uWSGI - Plugin for Carbon/Graphite support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-carbon
This package contains the Carbon plugin for uWSGI (to use in graphite)

%if %{with perl}
%package -n uwsgi-plugin-psgi
Summary:  uWSGI - Plugin for PSGI support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-psgi
This package contains the PSGI plugin for uWSGI

%if %{with perlcoro}
%package -n uwsgi-plugin-coroae
Summary:  uWSGI - Plugin for PERL Coro support
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-plugin-psgi = %{version}-%{release}, perl-Coro

%description -n uwsgi-plugin-coroae
This package contains the coroae plugin for uWSGI
%endif
%endif

%package -n uwsgi-plugin-cheaper-busyness
Summary:  uWSGI - Plugin for Cheaper Busyness algos
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-cheaper-busyness
This package contains the cheaper_busyness plugin for uWSGI

%package -n uwsgi-plugin-cplusplus
Summary:  uWSGI - Plugin for C++ support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-cplusplus
This package contains the cplusplus plugin for uWSGI

%package -n uwsgi-plugin-curl-cron
Summary:  uWSGI - Plugin for CURL Cron support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-curl-cron
This package contains the curl_cron plugin for uWSGI

%package -n uwsgi-plugin-dumbloop
Summary:  uWSGI - Plugin for Dumb Loop support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-dumbloop
This package contains the dumbloop plugin for uWSGI

%package -n uwsgi-plugin-dummy
Summary:  uWSGI - Plugin for Dummy support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-dummy
This package contains the dummy plugin for uWSGI

%if %{with ruby_rack}
%package -n uwsgi-plugin-fiber
Summary:  uWSGI - Plugin for Ruby Fiber support
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-plugin-rack = %{version}-%{release}

%description -n uwsgi-plugin-fiber
This package contains the fiber plugin for uWSGI
%endif

%if %{with go}
%package -n uwsgi-plugin-gccgo
Summary:  uWSGI - Plugin for GoLang support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-gccgo
This package contains the gccgo plugin for uWSGI
%endif

%if %{with geoip}
%package -n uwsgi-plugin-geoip
Summary:  uWSGI - Plugin for GeoIP support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-geoip
This package contains the geoip plugin for uWSGI
%endif

%if %{with python2}
%package -n uwsgi-plugin-python2-gevent
Summary:  uWSGI - Plugin for Python 2 GEvent support
Requires: uwsgi-plugin-python2 = %{version}-%{release}
Obsoletes: uwsgi-plugin-gevent < 2.0.16-4
Provides: uwsgi-plugin-gevent = %{version}-%{release}

%description -n uwsgi-plugin-python2-gevent
This package contains the Python 2 gevent plugin for uWSGI
%endif

%if %{with python3}
%package -n uwsgi-plugin-python%{python3_pkgversion}-gevent
Summary:  uWSGI - Plugin for Python %{python3_version} GEvent support
Requires: uwsgi-plugin-python%{python3_pkgversion} = %{version}-%{release}

%description -n uwsgi-plugin-python%{python3_pkgversion}-gevent
This package contains the Python %{python3_version} gevent plugin for uWSGI
%endif

%if %{with python3_alternate1}
%package -n uwsgi-plugin-python%{python3_alternate1_version_nodots}-gevent
Summary:  uWSGI - Plugin for Python %{python3_alternate1_version} GEvent support
Requires: uwsgi-plugin-python%{python3_alternate1_version_nodots} = %{version}-%{release}, libevent

%description -n uwsgi-plugin-python%{python3_alternate1_version_nodots}-gevent
This package contains the Python %{python3_alternate1_version} gevent plugin for uWSGI
%endif

%if %{with python3_alternate2}
%package -n uwsgi-plugin-python%{python3_alternate2_version_nodots}-gevent
Summary:  uWSGI - Plugin for Python %{python3_alternate2_version} GEvent support
Requires: uwsgi-plugin-python%{python3_alternate2_version_nodots} = %{version}-%{release}, libevent

%description -n uwsgi-plugin-python%{python3_alternate2_version_nodots}-gevent
This package contains the Python %{python3_alternate2_version} gevent plugin for uWSGI
%endif

%if %{with python3_alternate3}
%package -n uwsgi-plugin-python%{python3_alternate3_version_nodots}-gevent
Summary:  uWSGI - Plugin for Python %{python3_alternate3_version} GEvent support
Requires: uwsgi-plugin-python%{python3_alternate3_version_nodots} = %{version}-%{release}, libevent

%description -n uwsgi-plugin-python%{python3_alternate3_version_nodots}-gevent
This package contains the Python %{python3_alternate3_version} gevent plugin for uWSGI
%endif

%if %{with glusterfs}
%package -n uwsgi-plugin-glusterfs
Summary:  uWSGI - Plugin for GlusterFS support
Requires: uwsgi-plugin-common = %{version}-%{release}, glusterfs-api

%description -n uwsgi-plugin-glusterfs
This package contains the glusterfs plugin for uWSGI
%endif

%if %{with python2}
%if %{with python2_greenlet}
%package -n uwsgi-plugin-python2-greenlet
Summary:  uWSGI - Plugin for Python 2 Greenlet support
Requires: python-greenlet, uwsgi-plugin-python2 = %{version}-%{release}
Obsoletes: uwsgi-plugin-greenlet < 2.0.16-4
Provides: uwsgi-plugin-greenlet = %{version}-%{release}

%description -n uwsgi-plugin-python2-greenlet
This package contains the Python 2 greenlet plugin for uWSGI
%endif
%endif

%if %{with python3_greenlet}
%package -n uwsgi-plugin-python%{python3_pkgversion}-greenlet
Summary:  uWSGI - Plugin for Python %{python3_version} Greenlet support
Requires: python%{python3_pkgversion}-greenlet, uwsgi-plugin-python%{python3_pkgversion} = %{version}-%{release}

%description -n uwsgi-plugin-python%{python3_pkgversion}-greenlet
This package contains the Python %{python3_version} greenlet plugin for uWSGI
%endif

%if %{with gridfs}
%package -n uwsgi-plugin-gridfs
Summary:  uWSGI - Plugin for GridFS support
Requires: uwsgi-plugin-common = %{version}-%{release}, libmongodb

%description -n uwsgi-plugin-gridfs
This package contains the gridfs plugin for uWSGI
%endif

%if %{with java}
%package -n uwsgi-plugin-jvm
Summary:  uWSGI - Plugin for JVM support
BuildRequires: java-devel
Requires: uwsgi-plugin-common = %{version}-%{release}, java-headless, jpackage-utils

%description -n uwsgi-plugin-jvm
This package contains the JVM plugin for uWSGI

%package -n uwsgi-plugin-jwsgi
Summary:  uWSGI - Plugin for JWSGI support
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-plugin-jvm = %{version}-%{release}

%description -n uwsgi-plugin-jwsgi
This package contains the jwsgi plugin for uWSGI
%endif

%package -n uwsgi-plugin-ldap
Summary:  uWSGI - Plugin for LDAP support
Requires: uwsgi-plugin-common = %{version}-%{release}, openldap

%description -n uwsgi-plugin-ldap
This package contains the ldap plugin for uWSGI

%package -n uwsgi-plugin-lua
Summary:  uWSGI - Plugin for LUA support
Requires: lua, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-lua
This package contains the lua plugin for uWSGI

%if %{with zeromq}
%package -n uwsgi-plugin-mongrel2
Summary:  uWSGI - Plugin for Mongrel2 support
Requires: uwsgi-plugin-common = %{version}-%{release}, zeromq

%description -n uwsgi-plugin-mongrel2
This package contains the mongrel2 plugin for uWSGI
%endif

%if %{with mono}
%package -n uwsgi-plugin-mono
Summary:  uWSGI - Plugin for Mono / .NET support
Requires: uwsgi-plugin-common = %{version}-%{release}, mono-web

%description -n uwsgi-plugin-mono
This package contains the mono plugin for uWSGI
%endif

%package -n uwsgi-plugin-nagios
Summary:  uWSGI - Plugin for Nagios support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-nagios
This package contains the nagios plugin for uWSGI

%package -n uwsgi-plugin-notfound
Summary:  uWSGI - Plugin for notfound support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-notfound
This package contains the notfound plugin for uWSGI

%package -n uwsgi-plugin-pam
Summary:  uWSGI - Plugin for PAM support
Requires: uwsgi-plugin-common = %{version}-%{release}, pam

%description -n uwsgi-plugin-pam
This package contains the PAM plugin for uWSGI

%if %{with php}
%package -n uwsgi-plugin-php
Summary:  uWSGI - Plugin for PHP support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-php
This package contains the PHP plugin for uWSGI
%endif

%package -n uwsgi-plugin-pty
Summary:  uWSGI - Plugin for PTY support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-pty
This package contains the pty plugin for uWSGI

%if %{with python2}
%package -n uwsgi-plugin-python2
Summary:  uWSGI - Plugin for Python 2 support
Requires: python2, uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-python < 2.0.16-4
Provides: uwsgi-plugin-python = %{version}-%{release}

%description -n uwsgi-plugin-python2
This package contains the Python 2 plugin for uWSGI
%endif

%if %{with python3}
%package -n uwsgi-plugin-python%{python3_pkgversion}
Summary:  uWSGI - Plugin for Python %{python3_version} support
Requires: python%{python3_pkgversion}, uwsgi-plugin-common = %{version}-%{release}
%if 0%{?rhel} == 7
Obsoletes: uwsgi-plugin-python3 < 2.0.16-4
Provides: uwsgi-plugin-python3 = %{version}-%{release}
%endif

%description -n uwsgi-plugin-python%{python3_pkgversion}
This package contains the Python %{python3_version} plugin for uWSGI
%endif

%if %{with python3_alternate1}
%package -n uwsgi-plugin-python%{python3_alternate1_version_nodots}
Summary:  uWSGI - Plugin for Python %{python3_alternate1_version} support
Requires: %{python3_alternate1_pkgname}, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-python%{python3_alternate1_version_nodots}
This package contains the Python %{python3_alternate1_version} plugin for uWSGI
%endif

%if %{with python3_alternate2}
%package -n uwsgi-plugin-python%{python3_alternate2_version_nodots}
Summary:  uWSGI - Plugin for Python %{python3_alternate2_version} support
Requires: %{python3_alternate2_pkgname}, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-python%{python3_alternate2_version_nodots}
This package contains the Python %{python3_alternate2_version} plugin for uWSGI
%endif

%if %{with python3_alternate3}
%package -n uwsgi-plugin-python%{python3_alternate3_version_nodots}
Summary:  uWSGI - Plugin for Python %{python3_alternate3_version} support
Requires: %{python3_alternate3_pkgname}, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-python%{python3_alternate3_version_nodots}
This package contains the Python %{python3_alternate3_version} plugin for uWSGI
%endif

%if %{with ruby_rack}
%package -n uwsgi-plugin-rack
Summary:  uWSGI - Ruby rack plugin
Requires: rubygem-rack, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-rack
This package contains the rack plugin for uWSGI
%endif

%package -n uwsgi-plugin-rbthreads
Summary:  uWSGI - Ruby native threads support plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, ruby

%description -n uwsgi-plugin-rbthreads
This package contains the rbthreads plugin for uWSGI

%if %{with java}
%package -n uwsgi-plugin-ring
Summary:  uWSGI - Clojure/Ring request handler support plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, uwsgi-plugin-jvm = %{version}-%{release}, clojure

%description -n uwsgi-plugin-ring
This package contains the ring plugin for uWSGI
%endif

%package -n uwsgi-plugin-rpc
Summary:  uWSGI - Plugin for RPC support
Requires: rrdtool, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-rpc
This package contains the RPC plugin for uWSGI

%package -n uwsgi-plugin-rrdtool
Summary:  uWSGI - Plugin for RRDTool support
Requires: rrdtool, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-rrdtool
This package contains the RRD Tool plugin for uWSGI

%package -n uwsgi-plugin-ruby
Summary:  uWSGI - Plugin for Ruby support
Requires: ruby, uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-ruby
This package contains the ruby19 plugin for uWSGI

%package -n uwsgi-plugin-spooler
Summary:  uWSGI - Plugin for Remote Spooling support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-spooler
This package contains the spooler plugin for uWSGI

%package -n uwsgi-plugin-sqlite3
Summary:  uWSGI - SQLite3 plugin
Requires: uwsgi-plugin-common = %{version}-%{release}, sqlite

%description -n uwsgi-plugin-sqlite3
This package contains the sqlite3 plugin for uWSGI

%package -n uwsgi-plugin-ssi
Summary:  uWSGI - Server Side Includes plugin
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-ssi
This package contains the ssi plugin for uWSGI

%if %{with python2}
%package -n uwsgi-plugin-python2-tornado
Summary:  uWSGI - Plugin for Tornado (Python 2) support
Requires: uwsgi-plugin-common = %{version}-%{release}, python-tornado
Obsoletes: uwsgi-plugin-tornado < 2.0.16-4
Provides: uwsgi-plugin-tornado = %{version}-%{release}

%description -n uwsgi-plugin-python2-tornado
This package contains the tornado (Python 2) plugin for uWSGI
%endif

%if %{with python3}
%package -n uwsgi-plugin-python%{python3_pkgversion}-tornado
Summary:  uWSGI - Plugin for Tornado (Python %{python3_version}) support
Requires: uwsgi-plugin-common = %{version}-%{release}, python%{python3_pkgversion}-tornado

%description -n uwsgi-plugin-python%{python3_pkgversion}-tornado
This package contains the tornado (Python %{python3_version}) plugin for uWSGI
%endif

%package -n uwsgi-plugin-ugreen
Summary:  uWSGI - Plugin for uGreen support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-ugreen
This package contains the uGreen plugin for uWSGI

%if %{with v8}
%package -n uwsgi-plugin-v8
Summary:  uWSGI - Plugin for v8 support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-v8
This package contains the v8 plugin for uWSGI
%endif

%package -n uwsgi-plugin-webdav
Summary:  uWSGI - Plugin for WebDAV support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-webdav
This package contains the webdav plugin for uWSGI

%package -n uwsgi-plugin-xattr
Summary:  uWSGI - Plugin for Extra Attributes support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-xattr
This package contains the xattr plugin for uWSGI

%package -n uwsgi-plugin-xslt
Summary:  uWSGI - Plugin for XSLT transformation support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-xslt
This package contains the xslt plugin for uWSGI

%package -n uwsgi-plugin-zergpool
Summary:  uWSGI - Plugin for zergpool support
Requires: uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-plugin-zergpool
This package contains the zergpool plugin for uWSGI

# Routers

%if %{with tcp_wrappers}
%package -n uwsgi-router-access
Summary:   uWSGI - Plugin for router_access router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-access
This package contains the router_access plugin for uWSGI
%endif

%package -n uwsgi-router-basicauth
Summary:   uWSGI - Plugin for Basic Auth router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-basicauth
This package contains the basicauth plugin for uWSGI

%package -n uwsgi-router-cache
Summary:   uWSGI - Plugin for Cache router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-cache
This package contains the cache router plugin for uWSGI

%package -n uwsgi-router-expires
Summary:   uWSGI - Plugin for Expires router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-expires
This package contains the expires router plugin for uWSGI

%package -n uwsgi-router-fast
Summary:   uWSGI - Plugin for FastRouter support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-fastrouter <= 2.0.6
Provides:  uwsgi-plugin-fastrouter = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-fast
This package contains the fastrouter (proxy) plugin for uWSGI

%package -n uwsgi-router-forkpty
Summary:   uWSGI - Plugin for ForkPTY router support
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-router-forkpty
This package contains the ForkPTY router plugin for uWSGI

%package -n uwsgi-router-hash
Summary:   uWSGI - Plugin for Hash router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-hash
This package contains the hash router plugin for uWSGI

%package -n uwsgi-router-http
Summary:   uWSGI - Plugin for HTTP router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-http
This package contains the http router plugin for uWSGI

%package -n uwsgi-router-memcached
Summary:   uWSGI - Plugin for Memcached router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-memcached
This package contains the memcached router plugin for uWSGI

%package -n uwsgi-router-metrics
Summary:   uWSGI - Plugin for Metrics router support
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-router-metrics
This package contains the metrics router plugin for uWSGI

%package -n uwsgi-router-radius
Summary:   uWSGI - Plugin for Radius router support
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-router-radius
This package contains the metrics router plugin for uWSGI

%package -n uwsgi-router-raw
Summary:   uWSGI - Plugin for Raw Router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-rawrouter <= 2.0.6
Provides:  uwsgi-plugin-rawrouter = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-raw
This package contains the Raw router plugin for uWSGI

%package -n uwsgi-router-redirect
Summary:   uWSGI - Plugin for Redirect router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-redirect
This package contains the redirect router plugin for uWSGI

%package -n uwsgi-router-redis
Summary:   uWSGI - Plugin for Redis router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-redis
This package contains the redis router plugin for uWSGI

%package -n uwsgi-router-rewrite
Summary:   uWSGI - Plugin for Rewrite router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-rewrite
This package contains the rewrite router plugin for uWSGI

%package -n uwsgi-router-spnego
Summary:   uWSGI - Plugin for SPNEgo router support
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-router-spnego
This package contains the spnego router plugin for uWSGI

%package -n uwsgi-router-ssl
Summary:   uWSGI - Plugin for SSL router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Obsoletes: uwsgi-plugin-sslrouter <= 2.0.6
Provides:  uwsgi-plugin-sslrouter = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-ssl
This package contains the SSL router plugin for uWSGI

%package -n uwsgi-router-static
Summary:   uWSGI - Plugin for Static router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-static
This package contains the Static router plugin for uWSGI

%package -n uwsgi-router-tuntap
Summary:   uWSGI - Plugin for TUN/TAP router support
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-router-tuntap
This package contains the tuntap router plugin for uWSGI

%package -n uwsgi-router-uwsgi
Summary:   uWSGI - Plugin for uWSGI router support
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-uwsgi
This package contains the uwsgi router plugin for uWSGI

%package -n uwsgi-router-xmldir
Summary:   uWSGI - Plugin for XMLDir router rupport
Requires:  uwsgi-plugin-common = %{version}-%{release}
Provides:  uwsgi-routers = %{version}-%{release}

%description -n uwsgi-router-xmldir
This package contains the xmldir router plugin for uWSGI

# Emperors

%package -n uwsgi-emperor-amqp
Summary:   uWSGI - Plugin for AMQP emperor rupport
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-emperor-amqp
This package contains the AMQP emperor plugin for uWSGI

%if %{with pq}
%package -n uwsgi-emperor-pg
Summary:   uWSGI - Plugin for Postgres emperor rupport
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-emperor-pg
This package contains the Postgres emperor plugin for uWSGI
%endif

%if %{with zeromq}
%package -n uwsgi-emperor-zeromq
Summary:   uWSGI - Plugin for ZeroMQ emperor rupport
Requires:  uwsgi-plugin-common = %{version}-%{release}

%description -n uwsgi-emperor-zeromq
This package contains the ZeroMQ emperor plugin for uWSGI
%endif

# The rest

%if %{with mod_proxy_uwsgi}
%package -n mod_proxy_uwsgi
Summary:  uWSGI - Apache2 proxy module
Requires: uwsgi = %{version}-%{release}, httpd

%description -n mod_proxy_uwsgi
Fully Apache API compliant proxy module
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -p %{SOURCE1} buildconf/
echo "plugin_dir = %{_libdir}/uwsgi" >> buildconf/fedora.ini
cp -p %{SOURCE5} README.Fedora
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%if 0%{?fedora}
%patch -P5 -p1
%endif
%if %{with v8} && 0%{?fedora}
%patch -P6 -p1
%endif
%if %{with mono}
%patch -P7 -p1
%endif
%patch -P13 -p1
%patch -P14 -p1

%build
CFLAGS="%{optflags} -Wno-error -Wno-unused-but-set-variable -fPIC" %{__python} uwsgiconfig.py --verbose --build fedora.ini
%if %{with python2}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python2} uwsgiconfig.py --verbose --plugin plugins/python fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python2} uwsgiconfig.py --verbose --plugin plugins/gevent fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python2} uwsgiconfig.py --verbose --plugin plugins/tornado fedora
%endif
%if %{with python3}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3} uwsgiconfig.py --verbose --plugin plugins/python fedora python%{python3_pkgversion}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3} uwsgiconfig.py --verbose --plugin plugins/gevent fedora python%{python3_pkgversion}_gevent
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3} uwsgiconfig.py --verbose --plugin plugins/tornado fedora python%{python3_pkgversion}_tornado
%endif
%if %{with python3_alternate1}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate1} uwsgiconfig.py --verbose --plugin plugins/python fedora python%{python3_alternate1_version_nodots}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate1} uwsgiconfig.py --verbose --plugin plugins/gevent fedora python%{python3_alternate1_version_nodots}_gevent
%endif
%if %{with python3_alternate2}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate2} uwsgiconfig.py --verbose --plugin plugins/python fedora python%{python3_alternate2_version_nodots}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate2} uwsgiconfig.py --verbose --plugin plugins/gevent fedora python%{python3_alternate2_version_nodots}_gevent
%endif
%if %{with python3_alternate3}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate3} uwsgiconfig.py --verbose --plugin plugins/python fedora python%{python3_alternate3_version_nodots}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3_alternate3} uwsgiconfig.py --verbose --plugin plugins/gevent fedora python%{python3_alternate3_version_nodots}_gevent
%endif
%if %{with mongodblibs}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/mongodblog fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable -std=gnu++11 -Wno-error" %{__python2} uwsgiconfig.py --verbose --plugin plugins/stats_pusher_mongodb fedora
%endif
%if %{with mono}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/mono fedora
%endif
%if %{with php}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/php fedora
%endif
%if %{with v8}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/v8 fedora
%endif
%if %{with go}
# In EL* distributions, the gccgo compiler needs to be explicitly used to
# compile Go code, gcc will not work. However, gccgo can compile C code,
# so use that instead
%if 0%{?rhel}
CC="gccgo" CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/gccgo fedora
%else
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/gccgo fedora
%endif
%endif
%if %{with ruby19}
%if %{with ruby_rack}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/fiber fedora
%endif
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/rbthreads fedora
%endif
%if %{with tuntap}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/tuntap fedora
%endif
%if %{with perl}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/psgi fedora
%if %{with perlcoro}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/coroae fedora
%endif
%endif
%if %{with zeromq}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/logzmq fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/mongrel2 fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/emperor_zeromq fedora
%endif
%if %{with python2_greenlet}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/greenlet fedora
%endif
%if %{with python3_greenlet}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/greenlet fedora python%{python3_pkgversion}_greenlet
%endif
%if %{with glusterfs}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/glusterfs fedora
%endif
%if %{with gridfs}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/gridfs fedora
%endif
%if %{with java}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/jvm fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/jwsgi fedora
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/ring fedora
%endif
%if %{with gloox}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/alarm_xmpp fedora
%endif
%if %{with geoip}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/geoip fedora
%endif
%if %{with ruby_rack}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/rack fedora
%endif
%if %{with tcp_wrappers}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/router_access fedora
%endif
%if %{with mod_proxy_uwsgi}
%{_httpd_apxs} -Wc,-Wall -Wl -c apache2/mod_proxy_uwsgi.c
%endif
%if %{with pq}
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python} uwsgiconfig.py --verbose --plugin plugins/emperor_pg fedora
%endif

%install
install -d %{buildroot}%{_sysconfdir}/uwsgi.d
install -d %{buildroot}%{_usrsrc}/uwsgi/%{version}
install -d %{buildroot}%{_includedir}/uwsgi
install -d %{buildroot}%{_libdir}/uwsgi
%if %{with mono}
install -d %{buildroot}%{_monogacdir}
%endif
mkdir docs
tar -C docs/ --strip-components=1 -xvzf %{SOURCE4}
tar -C %{buildroot}%{_usrsrc}/uwsgi/%{version} --strip-components=1 -xvzf %{SOURCE0}
cp %{SOURCE1} %{buildroot}%{_usrsrc}/uwsgi/%{version}/buildconf/
cp docs/Changelog-%{version}.rst CHANGELOG
rm -f docs/.gitignore
echo "%{commit}, i.e. this:" >> README.Fedora
echo "https://github.com/unbit/%{docrepo}/tree/%{commit}" >> README.Fedora
install -D -p -m 0755 uwsgi %{buildroot}%{_sbindir}/uwsgi
install -p -m 0644 *.h %{buildroot}%{_includedir}/uwsgi
install -p -m 0755 *_plugin.so %{buildroot}%{_libdir}/uwsgi
%if %{with python2}
install -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python2_sitelib}/uwsgidecorators.py
%if %{manual_py_compile} == 1
%py_byte_compile %{__python2} %{buildroot}%{python2_sitelib}/uwsgidecorators.py
%endif
%endif
%if %{with python3}
install -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python3_sitelib}/uwsgidecorators.py
%if %{manual_py_compile} == 1
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}/uwsgidecorators.py
%endif
%endif
%if %{with python3_alternate1}
install -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python3_alternate1_sitelib}/uwsgidecorators.py
%if %{manual_py_compile} == 1
%py_byte_compile %{__python3_alternate1} %{buildroot}%{python3_alternate1_sitelib}/uwsgidecorators.py
%endif
%endif
%if %{with python3_alternate2}
install -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python3_alternate2_sitelib}/uwsgidecorators.py
%if %{manual_py_compile} == 1
%py_byte_compile %{__python3_alternate2} %{buildroot}%{python3_alternate2_sitelib}/uwsgidecorators.py
%endif
%endif
%if %{with python3_alternate3}
install -D -p -m 0644 uwsgidecorators.py %{buildroot}%{python3_alternate3_sitelib}/uwsgidecorators.py
%if %{manual_py_compile} == 1
%py_byte_compile %{__python3_alternate3} %{buildroot}%{python3_alternate3_sitelib}/uwsgidecorators.py
%endif
%endif
%if %{with java}
install -D -p -m 0644 plugins/jvm/uwsgi.jar %{buildroot}%{_javadir}/uwsgi.jar
%endif
%if %{with mono}
gacutil -i plugins/mono/uwsgi.dll -f -package uwsgi -root %{buildroot}/usr/lib
%endif
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/uwsgi.ini
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/uwsgi.service
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/uwsgi.conf
%if %{with mod_proxy_uwsgi}
install -D -p -m 0755 apache2/.libs/mod_proxy_uwsgi.so %{buildroot}%{_httpd_moddir}/mod_proxy_uwsgi.so
%endif

install -m0644 -D %{SOURCE8} %{buildroot}%{_sysusersdir}/uwsgi.conf

%post
%systemd_post uwsgi.service

%preun
%systemd_preun uwsgi.service

%postun
%systemd_postun uwsgi.service

%files
%{_sbindir}/uwsgi
%config(noreplace) %{_sysconfdir}/uwsgi.ini
%{_unitdir}/uwsgi.service
%{_tmpfilesdir}/uwsgi.conf
%dir %{_sysconfdir}/uwsgi.d
%doc README README.Fedora CHANGELOG
%license LICENSE
%{_sysusersdir}/uwsgi.conf

%files -n uwsgi-devel
%{_includedir}/uwsgi
%{_usrsrc}/uwsgi

%if %{with python2}
%files -n python2-uwsgidecorators
%{python2_sitelib}/uwsgidecorators.py*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-uwsgidecorators
%{python3_sitelib}/uwsgidecorators.py
%{python3_sitelib}/__pycache__/uwsgidecorators.cpython-%{python3_version_nodots}*.py*
%endif

%if %{with python3_alternate1}
%files -n %{python3_alternate1_pkgname}-uwsgidecorators
%{python3_alternate1_sitelib}/uwsgidecorators.py
%{python3_alternate1_sitelib}/__pycache__/uwsgidecorators.cpython-%{python3_alternate1_version_nodots}*.py*
%endif

%if %{with python3_alternate2}
%files -n %{python3_alternate2_pkgname}-uwsgidecorators
%{python3_alternate2_sitelib}/uwsgidecorators.py
%{python3_alternate2_sitelib}/__pycache__/uwsgidecorators.cpython-%{python3_alternate2_version_nodots}*.py*
%endif

%if %{with python3_alternate3}
%files -n %{python3_alternate3_pkgname}-uwsgidecorators
%{python3_alternate3_sitelib}/uwsgidecorators.py
%{python3_alternate3_sitelib}/__pycache__/uwsgidecorators.cpython-%{python3_alternate3_version_nodots}*.py*
%endif

%files -n uwsgi-docs
%doc docs

%files -n uwsgi-plugin-common
%dir %{_libdir}/uwsgi
%{_libdir}/uwsgi/http_plugin.so
%{_libdir}/uwsgi/cgi_plugin.so

# Stats pushers

%files -n uwsgi-stats-pusher-file
%{_libdir}/uwsgi/stats_pusher_file_plugin.so

%if %{with mongodblibs}
%files -n uwsgi-stats-pusher-mongodb
%{_libdir}/uwsgi/stats_pusher_mongodb_plugin.so
%endif

%files -n uwsgi-stats-pusher-socket
%{_libdir}/uwsgi/stats_pusher_socket_plugin.so

%files -n uwsgi-stats-pusher-statsd
%{_libdir}/uwsgi/stats_pusher_statsd_plugin.so

%files -n uwsgi-stats-pusher-zabbix
%{_libdir}/uwsgi/zabbix_plugin.so

# Alarms

%files -n uwsgi-alarm-curl
%{_libdir}/uwsgi/alarm_curl_plugin.so

%if %{with gloox}
%files -n uwsgi-alarm-xmpp
%{_libdir}/uwsgi/alarm_xmpp_plugin.so
%endif

# Transformations

%files -n uwsgi-transformation-chunked
%{_libdir}/uwsgi/transformation_chunked_plugin.so

%files -n uwsgi-transformation-gzip
%{_libdir}/uwsgi/transformation_gzip_plugin.so

%files -n uwsgi-transformation-offload
%{_libdir}/uwsgi/transformation_offload_plugin.so

%files -n uwsgi-transformation-template
%{_libdir}/uwsgi/transformation_template_plugin.so

%files -n uwsgi-transformation-tofile
%{_libdir}/uwsgi/transformation_tofile_plugin.so

%files -n uwsgi-transformation-toupper
%{_libdir}/uwsgi/transformation_toupper_plugin.so

# Loggers

%files -n uwsgi-log-encoder-msgpack
%{_libdir}/uwsgi/msgpack_plugin.so

%files -n uwsgi-logger-crypto
%{_libdir}/uwsgi/logcrypto_plugin.so

%files -n uwsgi-logger-file
%{_libdir}/uwsgi/logfile_plugin.so

%files -n uwsgi-logger-graylog2
%{_libdir}/uwsgi/graylog2_plugin.so

%if %{with mongodblibs}
%files -n uwsgi-logger-mongodb
%{_libdir}/uwsgi/mongodblog_plugin.so
%endif

%files -n uwsgi-logger-pipe
%{_libdir}/uwsgi/logpipe_plugin.so

%files -n uwsgi-logger-redis
%{_libdir}/uwsgi/redislog_plugin.so

%files -n uwsgi-logger-rsyslog
%{_libdir}/uwsgi/rsyslog_plugin.so

%files -n uwsgi-logger-socket
%{_libdir}/uwsgi/logsocket_plugin.so

%files -n uwsgi-logger-syslog
%{_libdir}/uwsgi/syslog_plugin.so

%files -n uwsgi-logger-systemd
%{_libdir}/uwsgi/systemd_logger_plugin.so

%if %{with zeromq}
%files -n uwsgi-logger-zeromq
%{_libdir}/uwsgi/logzmq_plugin.so
%endif

# Plugins

%files -n uwsgi-plugin-airbrake
%{_libdir}/uwsgi/airbrake_plugin.so

%files -n uwsgi-plugin-cache
%{_libdir}/uwsgi/cache_plugin.so

%files -n uwsgi-plugin-carbon
%{_libdir}/uwsgi/carbon_plugin.so

%if %{with perl}
%files -n uwsgi-plugin-psgi
%{_libdir}/uwsgi/psgi_plugin.so

%if %{with perlcoro}
%files -n uwsgi-plugin-coroae
%{_libdir}/uwsgi/coroae_plugin.so
%endif
%endif

%files -n uwsgi-plugin-cheaper-busyness
%{_libdir}/uwsgi/cheaper_busyness_plugin.so

%files -n uwsgi-plugin-cplusplus
%{_libdir}/uwsgi/cplusplus_plugin.so

%files -n uwsgi-plugin-curl-cron
%{_libdir}/uwsgi/curl_cron_plugin.so

%files -n uwsgi-plugin-dumbloop
%{_libdir}/uwsgi/dumbloop_plugin.so

%files -n uwsgi-plugin-dummy
%{_libdir}/uwsgi/dummy_plugin.so

%if %{with ruby19}
%if %{with ruby_rack}
%files -n uwsgi-plugin-fiber
%{_libdir}/uwsgi/fiber_plugin.so
%endif
%endif

%if %{with go}
%files -n uwsgi-plugin-gccgo
%{_libdir}/uwsgi/gccgo_plugin.so
%endif

%if %{with geoip}
%files -n uwsgi-plugin-geoip
%{_libdir}/uwsgi/geoip_plugin.so
%endif

%if %{with python2}
%files -n uwsgi-plugin-python2-gevent
%{_libdir}/uwsgi/gevent_plugin.so
%endif

%if %{with python3}
%files -n uwsgi-plugin-python%{python3_pkgversion}-gevent
%{_libdir}/uwsgi/python%{python3_pkgversion}_gevent_plugin.so
%endif

%if %{with python3_alternate1}
%files -n uwsgi-plugin-python%{python3_alternate1_version_nodots}-gevent
%{_libdir}/uwsgi/python%{python3_alternate1_version_nodots}_gevent_plugin.so
%endif

%if %{with python3_alternate2}
%files -n uwsgi-plugin-python%{python3_alternate2_version_nodots}-gevent
%{_libdir}/uwsgi/python%{python3_alternate2_version_nodots}_gevent_plugin.so
%endif

%if %{with python3_alternate3}
%files -n uwsgi-plugin-python%{python3_alternate3_version_nodots}-gevent
%{_libdir}/uwsgi/python%{python3_alternate3_version_nodots}_gevent_plugin.so
%endif

%if %{with glusterfs}
%files -n uwsgi-plugin-glusterfs
%{_libdir}/uwsgi/glusterfs_plugin.so
%endif

%if %{with python2_greenlet}
%files -n uwsgi-plugin-python2-greenlet
%{_libdir}/uwsgi/greenlet_plugin.so
%endif

%if %{with python3_greenlet}
%files -n uwsgi-plugin-python%{python3_pkgversion}-greenlet
%{_libdir}/uwsgi/python%{python3_pkgversion}_greenlet_plugin.so
%endif

%if %{with gridfs}
%files -n uwsgi-plugin-gridfs
%{_libdir}/uwsgi/gridfs_plugin.so
%endif

%if %{with java}
%files -n uwsgi-plugin-jvm
%{_libdir}/uwsgi/jvm_plugin.so
%{_javadir}/uwsgi.jar

%files -n uwsgi-plugin-jwsgi
%{_libdir}/uwsgi/jwsgi_plugin.so
%endif

%files -n uwsgi-plugin-ldap
%{_libdir}/uwsgi/ldap_plugin.so

%files -n uwsgi-plugin-lua
%{_libdir}/uwsgi/lua_plugin.so

%if %{with zeromq}
%files -n uwsgi-plugin-mongrel2
%{_libdir}/uwsgi/mongrel2_plugin.so
%endif

%if %{with mono}
%files -n uwsgi-plugin-mono
%{_libdir}/uwsgi/mono_plugin.so
%{_monodir}/uwsgi/
%{_monogacdir}/uwsgi/
%endif

%files -n uwsgi-plugin-nagios
%{_libdir}/uwsgi/nagios_plugin.so

%files -n uwsgi-plugin-notfound
%{_libdir}/uwsgi/notfound_plugin.so

%files -n uwsgi-plugin-pam
%{_libdir}/uwsgi/pam_plugin.so

%if %{with php}
%files -n uwsgi-plugin-php
%{_libdir}/uwsgi/php_plugin.so
%endif

%files -n uwsgi-plugin-pty
%{_libdir}/uwsgi/pty_plugin.so

%if %{with python2}
%files -n uwsgi-plugin-python2
%{_libdir}/uwsgi/python_plugin.so
%endif

%if %{with python3}
%files -n uwsgi-plugin-python%{python3_pkgversion}
%{_libdir}/uwsgi/python%{python3_pkgversion}_plugin.so
%endif

%if %{with python3_alternate1}
%files -n uwsgi-plugin-python%{python3_alternate1_version_nodots}
%{_libdir}/uwsgi/python%{python3_alternate1_version_nodots}_plugin.so
%endif

%if %{with python3_alternate2}
%files -n uwsgi-plugin-python%{python3_alternate2_version_nodots}
%{_libdir}/uwsgi/python%{python3_alternate2_version_nodots}_plugin.so
%endif

%if %{with python3_alternate3}
%files -n uwsgi-plugin-python%{python3_alternate3_version_nodots}
%{_libdir}/uwsgi/python%{python3_alternate3_version_nodots}_plugin.so
%endif

%if %{with ruby_rack}
%files -n uwsgi-plugin-rack
%{_libdir}/uwsgi/rack_plugin.so
%endif

%if %{with ruby19}
%files -n uwsgi-plugin-rbthreads
%{_libdir}/uwsgi/rbthreads_plugin.so
%endif

%if %{with java}
%files -n uwsgi-plugin-ring
%{_libdir}/uwsgi/ring_plugin.so
%endif

%files -n uwsgi-plugin-rrdtool
%{_libdir}/uwsgi/rrdtool_plugin.so

%files -n uwsgi-plugin-rpc
%{_libdir}/uwsgi/rpc_plugin.so

%files -n uwsgi-plugin-ruby
%{_libdir}/uwsgi/ruby19_plugin.so

%files -n uwsgi-plugin-spooler
%{_libdir}/uwsgi/spooler_plugin.so

%files -n uwsgi-plugin-sqlite3
%{_libdir}/uwsgi/sqlite3_plugin.so

%files -n uwsgi-plugin-ssi
%{_libdir}/uwsgi/ssi_plugin.so

%if %{with python2}
%files -n uwsgi-plugin-python2-tornado
%{_libdir}/uwsgi/tornado_plugin.so
%endif

%if %{with python3}
%files -n uwsgi-plugin-python%{python3_pkgversion}-tornado
%{_libdir}/uwsgi/python%{python3_pkgversion}_tornado_plugin.so
%endif

%files -n uwsgi-plugin-ugreen
%{_libdir}/uwsgi/ugreen_plugin.so

%if %{with v8}
%files -n uwsgi-plugin-v8
%{_libdir}/uwsgi/v8_plugin.so
%endif

%files -n uwsgi-plugin-webdav
%{_libdir}/uwsgi/webdav_plugin.so

%files -n uwsgi-plugin-xattr
%{_libdir}/uwsgi/xattr_plugin.so

%files -n uwsgi-plugin-xslt
%{_libdir}/uwsgi/xslt_plugin.so

%files -n uwsgi-plugin-zergpool
%{_libdir}/uwsgi/zergpool_plugin.so

# Routers

%if %{with tcp_wrappers}
%files -n uwsgi-router-access
%{_libdir}/uwsgi/router_access_plugin.so
%endif

%files -n uwsgi-router-basicauth
%{_libdir}/uwsgi/router_basicauth_plugin.so

%files -n uwsgi-router-cache
%{_libdir}/uwsgi/router_cache_plugin.so

%files -n uwsgi-router-expires
%{_libdir}/uwsgi/router_expires_plugin.so

%files -n uwsgi-router-fast
%{_libdir}/uwsgi/fastrouter_plugin.so

%files -n uwsgi-router-forkpty
%{_libdir}/uwsgi/forkptyrouter_plugin.so

%files -n uwsgi-router-hash
%{_libdir}/uwsgi/router_hash_plugin.so

%files -n uwsgi-router-http
%{_libdir}/uwsgi/router_http_plugin.so

%files -n uwsgi-router-memcached
%{_libdir}/uwsgi/router_memcached_plugin.so

%files -n uwsgi-router-metrics
%{_libdir}/uwsgi/router_metrics_plugin.so

%files -n uwsgi-router-radius
%{_libdir}/uwsgi/router_radius_plugin.so

%files -n uwsgi-router-raw
%{_libdir}/uwsgi/rawrouter_plugin.so

%files -n uwsgi-router-redirect
%{_libdir}/uwsgi/router_redirect_plugin.so

%files -n uwsgi-router-redis
%{_libdir}/uwsgi/router_redis_plugin.so

%files -n uwsgi-router-rewrite
%{_libdir}/uwsgi/router_rewrite_plugin.so

%files -n uwsgi-router-spnego
%{_libdir}/uwsgi/router_spnego_plugin.so

%files -n uwsgi-router-ssl
%{_libdir}/uwsgi/sslrouter_plugin.so

%files -n uwsgi-router-static
%{_libdir}/uwsgi/router_static_plugin.so

%if %{with tuntap}
%files -n uwsgi-router-tuntap
%{_libdir}/uwsgi/tuntap_plugin.so
%endif

%files -n uwsgi-router-uwsgi
%{_libdir}/uwsgi/router_uwsgi_plugin.so

%files -n uwsgi-router-xmldir
%{_libdir}/uwsgi/router_xmldir_plugin.so

# Emperors

%files -n uwsgi-emperor-amqp
%{_libdir}/uwsgi/emperor_amqp_plugin.so

%if %{with pq}
%files -n uwsgi-emperor-pg
%{_libdir}/uwsgi/emperor_pg_plugin.so
%endif

%if %{with zeromq}
%files -n uwsgi-emperor-zeromq
%{_libdir}/uwsgi/emperor_zeromq_plugin.so
%endif

# The rest

%if %{with mod_proxy_uwsgi}
%files -n mod_proxy_uwsgi
%{_httpd_moddir}/mod_proxy_uwsgi.so
%endif

%changelog
%autochangelog
