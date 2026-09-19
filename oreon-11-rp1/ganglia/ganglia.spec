%global source0_hash 5333fedf34169356cf2a27ceb122cedb29c3131ae0d87e5fb735fc2afad8c9c7

%global gangver     3.7.2
%global webver      3.7.6

%global systemd         1
%global _hardened_build 1

%global with_python     1
%if 0%{?rhel} == 7
%global py2             1
%else
%global py3             1
%endif

%if 0%{?fedora} || 0%{?rhel} > 9
%global pcre2           1
%global autoconf_fix    1
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%global tirpc           1
%global php_xml         1
%endif

%if 0%{?fedora}  > 42
%global sysusers        1
%else
%global legacy_users    1
%endif

%if 0%{?fedora} || 0%{?rhel} > 6
%global httpd24         1
%endif

Summary:            Distributed Monitoring System
Name:               ganglia
Version:            %{gangver}
Release:            63%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                https://github.com/ganglia
Source0:            http://downloads.sourceforge.net/sourceforge/ganglia/ganglia-%{version}.tar.gz
Source1:            https://github.com/ganglia/ganglia-web/archive/%{webver}/ganglia-web-%{webver}.tar.gz
Source2:            gmond.service
Source3:            gmetad.service
Source4:            ganglia-httpd24.conf.d
Source5:            ganglia-httpd.conf.d
Source6:            conf.php
Source7:            ganglia.sysusers.conf
Patch0:             ganglia-3.7.2-185ab6.patch
Patch1:             ganglia-3.7.2-gcc14-cast.patch
Patch10:            ganglia-3.7.2-tirpc-hack.patch
Patch20:            ganglia-web-3.7.2-path.patch
Patch21:            ganglia-web-3.7.6-pr-379.patch
Patch22:            ganglia-web-3.7.6-php8.patch
Patch23:            0001-Sanitize-input-for-timezone.patch
Patch24:            0002-Validate-that-the-supplied-timezone-is-a-valid-timez.patch
Patch30:            ganglia-gmond-python2to3.patch
Patch31:            0002-2to3-pass.patch
Patch32:            0003-Ruff-pass.patch
Patch33:            0004-Use-raw-strings.patch
Patch34:            0005-First-loop-might-contain-non-integer-input.patch
Patch35:            0001-Fix-return-value-from-mod_python-init.patch
Patch40:            ganglia-3.7.2-autoconf-python3.patch
Patch50:            ganglia-3.7.2-pcre2.patch
%if 0%{?systemd}
BuildRequires:      systemd
%endif
%if 0%{?tirpc}
BuildRequires:      rpcgen
BuildRequires:      libtirpc-devel
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      libtool
%endif
BuildRequires:      apr-devel >= 1
BuildRequires:      cyrus-sasl-devel
BuildRequires:      expat-devel
BuildRequires:      freetype-devel
BuildRequires:      gcc
BuildRequires:      libconfuse-devel
BuildRequires:      libmemcached-devel
BuildRequires:      libpng-devel
BuildRequires:      make
%if 0%{?pcre2}
BuildRequires:      pcre2-devel
%else
BuildRequires:      pcre-devel
%endif
%{?py2:BuildRequires:      python2-devel}
%{?py3:BuildRequires:      python3-devel}
BuildRequires:      rrdtool-devel
BuildRequires:      rsync
BuildRequires:      /usr/bin/pod2man
BuildRequires:      /usr/bin/pod2html
%description
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

%package            web
Summary:            Ganglia Web Frontend
Version:            %{webver}
Requires:           rrdtool
Requires:           php
Requires:           php-gd
Requires:           %{name}-gmetad = %{gangver}-%{release}
%if 0%{?php_xml}
Requires:           php-xml
%endif
%description        web
This package provides a web frontend to display the XML tree published
by ganglia, and to provide historical graphs of collected
metrics. This website is written in the PHP.

%package            gmetad
Summary:            Ganglia Metadata collection daemon
Requires:           %{name} = %{gangver}-%{release}
%if 0%{?systemd}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%else
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service
%endif
%description        gmetad
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmetad daemon aggregates monitoring data from several clusters to
form a monitoring grid. It also keeps metric history using rrdtool.

%package            gmond
Summary:            Ganglia Monitoring daemon
Requires:           %{name} = %{gangver}-%{release}
%if 0%{?systemd}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%else
Requires(post):     /sbin/chkconfig
Requires(preun):    /sbin/chkconfig
Requires(preun):    /sbin/service
%endif
%description        gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmond daemon provides the ganglia service within a single cluster
or Multicast domain.

%if 0%{?py2}
%package            python2-gmond
Summary:            Ganglia Monitor daemon python DSO and metric modules
Requires:           ganglia-gmond
Requires:           python2
%{?python_provide:%python_provide python2-gmond}
# Remove before F30
Provides:           ganglia-python = %{version}-%{release}
%description        python2-gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This package provides the gmond python DSO and python gmond modules,
which can be loaded via the DSO at gmond daemon start time.
%endif

%if 0%{?py3}
%package            python3-gmond
Summary:            Ganglia Monitor daemon python3 DSO and metric modules
Requires:           ganglia-gmond
Requires:           python3
%{?python_provide:%python_provide python3-gmond}
Provides:           gmond-python = %{version}-%{release}
%description        python3-gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This package provides the gmond python DSO and python gmond modules,
which can be loaded via the DSO at gmond daemon start time.
%endif

%package            devel
Summary:            Ganglia Library
Requires:           %{name} = %{gangver}-%{release}
Requires:           apr-devel
Requires:           libconfuse-devel
%description        devel
The Ganglia Monitoring Core library provides a set of functions that
programmers can use to build scalable cluster or grid applications

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 30 -p1
%{?py3:%patch -P 31 -p1}
%{?py3:%patch -P 32 -p1}
%{?py3:%patch -P 33 -p1}
%{?py3:%patch -P 34 -p1}
%{?py3:%patch -P 35 -p1}
%patch -P 40 -p1
%if 0%{?tirpc}
%patch -P 10 -p1
%endif
%if 0%{?pcre2}
%patch -P 50 -p1
%endif
# fix broken systemd support
install -m 0644 %{SOURCE2} gmond/gmond.service.in
install -m 0644 %{SOURCE3} gmetad/gmetad.service.in
# web part
%setup -q -T -D -a 1
mv ganglia-web-%{webver} web
pushd web
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
popd

%build
touch Makefile.am

%if 0%{?tirpc}
aclocal -I m4
autoheader
automake --add-missing --copy --foreign 2>/dev/null
libtoolize --automake --copy
automake --add-missing --copy --foreign
autoconf -f || exit 1
%endif

%if 0%{?autoconf_fix}
pushd libmetrics
aclocal -I m4
autoheader
automake --add-missing --copy --foreign 2>/dev/null
libtoolize --automake --copy
automake --add-missing --copy --foreign
autoconf -f || exit 1
popd
%endif

export CFLAGS="%{optflags} -fcommon"
%configure \
    --enable-setuid=ganglia \
    --enable-setgid=ganglia \
    --with-gmetad \
    --with-memcached \
    --disable-static \
    --enable-shared \
    --with-libpcre=yes \
%if 0%{?with_python}
    --enable-python \
%if 0%{?py2}
    --with-python=%{__python2} \
%endif
%if 0%{?py3}
    --with-python=%{__python3} \
%endif
%else
    --disable-python \
%endif
    --sysconfdir=%{_sysconfdir}/ganglia

# Remove rpaths
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

## Default to run as user ganglia instead of nobody
%{__perl} -pi.orig -e 's|nobody|ganglia|g' \
    gmond/gmond.conf.html ganglia.html gmond/conf.pod

%{__perl} -pi.orig -e 's|.*setuid_username.*|setuid_username ganglia|' \
    gmetad/gmetad.conf.in

## Don't have initscripts turn daemons on by default
%{__perl} -pi.orig -e 's|2345|-|g' gmond/gmond.init gmetad/gmetad.init

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

## Create directory structures
%{?with_python:mkdir -p %{buildroot}%{_libdir}/ganglia/python_modules}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/rrds

## Install services
%if 0%{?systemd}
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/gmond.service
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/gmetad.service
%else
install -Dp -m 0755 gmond/gmond.init %{buildroot}%{_sysconfdir}/init.d/gmond
install -Dp -m 0755 gmetad/gmetad.init %{buildroot}%{_sysconfdir}/init.d/gmetad
%endif

## Build default gmond.conf from gmond using the '-t' flag
LD_LIBRARY_PATH=lib/.libs gmond/gmond -t | %{__perl} -pe 's|nobody|ganglia|g' \
    > %{buildroot}%{_sysconfdir}/ganglia/gmond.conf

%if 0%{?with_python}
## Python bits
# Copy the python metric modules and .conf files
mkdir -p %{buildroot}%{_sysconfdir}/ganglia/conf.d
cp -p gmond/python_modules/conf.d/*.pyconf %{buildroot}%{_sysconfdir}/ganglia/conf.d/
cp -p gmond/modules/conf.d/*.conf %{buildroot}%{_sysconfdir}/ganglia/conf.d/
cp -p gmond/python_modules/*/*.py %{buildroot}%{_libdir}/ganglia/python_modules/
%endif

## Web bits
pushd web
make install DESTDIR=%{buildroot}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/ganglia/conf.php
ln -s ../../..%{_sysconfdir}/%{name}/conf.php \
    %{buildroot}%{_datadir}/%{name}/conf.php
popd

## httpd config
%if 0%{?httpd24}
install -Dp -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
%else
install -Dp -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
%endif

## Various clean up after install:

## Don't install the status modules and example.conf
rm -f %{buildroot}%{_sysconfdir}/ganglia/conf.d/{modgstatus,example}.conf

## Disable the diskusage module until it is configured properly
## mv %{buildroot}%{_sysconfdir}/ganglia/conf.d/diskusage.pyconf \
##   %{buildroot}%{_sysconfdir}/ganglia/conf.d/diskusage.pyconf.off

## Remove unwanted files from web dir
rm -rf %{buildroot}%{_datadir}/%{name}/{Makefile*,debian,ganglia-web.spec*,ganglia-web}
rm -rf %{buildroot}%{_datadir}/%{name}/{conf_default.php.in,version.php.in}
rm -rf %{buildroot}%{_localstatedir}/lib/%{name}-web/conf/sql

## Included as doc
rm -rf %{buildroot}%{_datadir}/%{name}/{README,TODO,AUTHORS,COPYING}

## House cleaning
rm -f %{buildroot}%{_libdir}/*.la

# Remove execute bit
chmod 0644 %{buildroot}%{_datadir}/%{name}/header.php
%{?with_python:chmod 0644 %{buildroot}%{_libdir}/%{name}/python_modules/*.py}
chmod 0644 %{buildroot}%{_datadir}/%{name}/css/smoothness/jquery-ui-1.10.2.custom.css
chmod 0644 %{buildroot}%{_datadir}/%{name}/css/smoothness/jquery-ui-1.10.2.custom.min.css

# Remove shebang
%{?with_python:sed -i '1{\@^#!@d}' %{buildroot}%{_libdir}/%{name}/python_modules/*.py}

# Sysusers
%if 0%{?sysusers}
install -m0644 -D %{SOURCE7} %{buildroot}%{_sysusersdir}/ganglia.conf
%endif

%if 0%{?legacy_users}
%pre
## Add the "ganglia" user
/usr/sbin/useradd -c "Ganglia Monitoring System" \
        -s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} ganglia 2> /dev/null || :
%endif

%if 0%{?systemd}
%post gmond
%systemd_post gmond.service

%preun gmond
%systemd_preun gmond.service

%postun gmond
%systemd_postun_with_restart gmond.service

%post gmetad
%systemd_post gmetad.service

%preun gmetad
%systemd_preun gmetad.service

%postun gmetad
%systemd_postun_with_restart gmetad.service

%else 

%post gmond
/sbin/chkconfig --add gmond

%post gmetad
/sbin/chkconfig --add gmetad

%preun gmetad
if [ "$1" = 0 ]; then
  /sbin/service gmetad stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del gmetad
fi

%preun gmond
if [ "$1" = 0 ]; then
  /sbin/service gmond stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del gmond
fi

%endif

# https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Scriptlet_to_replace_a_symlink_to_a_directory_with_a_directory
%pretrans web -p <lua>
path = "/usr/share/ganglia/lib/Zend"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/libganglia*.so.*
%dir %{_libdir}/ganglia
%{_libdir}/ganglia/*.so
%{?with_python:%exclude %{_libdir}/ganglia/modpython.so}
%if 0%{?sysusers}
%{_sysusersdir}/ganglia.conf
%endif

%files gmetad
%dir %{_localstatedir}/lib/%{name}
%attr(0755,ganglia,ganglia) %{_localstatedir}/lib/%{name}/rrds
%{_sbindir}/gmetad
%if 0%{?systemd}
%{_unitdir}/gmetad.service
%else
%{_sysconfdir}/init.d/gmetad
%endif
%{_mandir}/man1/gmetad.1*
%{_mandir}/man1/gmetad.py.1*
%dir %{_sysconfdir}/ganglia
%config(noreplace) %{_sysconfdir}/ganglia/gmetad.conf

%files gmond
%{_bindir}/gmetric
%{_bindir}/gstat
%{_sbindir}/gmond
%if 0%{?systemd}
%{_unitdir}/gmond.service
%else
%{_sysconfdir}/init.d/gmond
%endif
%{_mandir}/man5/gmond.conf.5*
%{_mandir}/man1/gmond.1*
%{_mandir}/man1/gstat.1*
%{_mandir}/man1/gmetric.1*
%dir %{_sysconfdir}/ganglia
%{?with_python:%dir %{_sysconfdir}/ganglia/conf.d}
%config(noreplace) %{_sysconfdir}/ganglia/gmond.conf
%{?with_python:%config(noreplace) %{_sysconfdir}/ganglia/conf.d/*.conf}
%{?with_python:%exclude %{_sysconfdir}/ganglia/conf.d/modpython.conf}

%if 0%{?py2}
%files python2-gmond
%dir %{_libdir}/ganglia/python_modules/
%{_libdir}/ganglia/python_modules/*.py*
%{_libdir}/ganglia/modpython.so*
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/*.pyconf*
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/modpython.conf
%endif

%if 0%{?py3}
%files python3-gmond
%dir %{_libdir}/ganglia/python_modules/
%{_libdir}/ganglia/python_modules/*.py*
%{_libdir}/ganglia/modpython.so*
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/*.pyconf*
%config(noreplace) %{_sysconfdir}/ganglia/conf.d/modpython.conf
%endif

%files devel
%{_bindir}/ganglia-config
%{_includedir}/*.h
%{_libdir}/libganglia*.so

%files web
%license web/COPYING
%doc web/AUTHORS web/README web/TODO
%config(noreplace) %{_sysconfdir}/%{name}/conf.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_datadir}/%{name}
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}-web/conf
%config(noreplace) %attr(0644,apache,apache) %{_localstatedir}/lib/%{name}-web/conf/*.json
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}-web/dwoo
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}-web/dwoo/cache
%dir %attr(0755,apache,apache) %{_localstatedir}/lib/%{name}-web/dwoo/compiled

%changelog
%autochangelog
