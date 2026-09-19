%global source0_hash e076a51180ab3bc9642fe01f23b1fe97096c7a40088123a23868465a9227dfc9

# TODO: Split monitors and alerts into subpackages
#       they drag in way too many dependencies

%global moncgi_version 1.52
%global fixlib sed 's,/usr/lib,%{_libdir},g'

Name:           mon
Summary:        General-purpose resource monitoring system
Version:        1.2.0
Release:        43%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kernel.org/software/mon/

Source0:        ftp://ftp.kernel.org/pub/software/admin/mon/mon-%{version}.tar.bz2
Source1:        ftp://ftp.kernel.org/pub/software/admin/mon/contrib/cgi-bin/mon.cgi/mon.cgi-%{moncgi_version}.tar.bz2
Source2:        ftp://ftp.kernel.org/pub/software/admin/mon/contrib/all-alerts.tar.bz2

Source3:        mon.cf
Source4:        mon.service
Source5:        userfile

Patch0:         mon-1.2.0-perl.patch
Patch1:         mon-1.2.0-uucp.patch
# Use libtirpc instead of rpc/rpc.h from glibc, bug #1675405
Patch2:         mon-1.2.0-Port-to-libtirpc.patch
Patch3:         mon-1.2.0-fix_signal.patch

Requires:       perl(Authen::PAM)
Requires:       iputils
Requires:       fping
Requires:       traceroute
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  dos2unix
BuildRequires:  perl-generators
# pkgconfig(libtirpc) for Port-to-libtirpc.patch, bug #1675405,
# <https://sourceforge.net/p/mon/patches/11/>
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  systemd-units

%description
Mon is a general-purpose resource monitoring system.  It can be used
to monitor network service availability, server problems,
environmental conditions (i.e., the temperature in a room) or other
things. Mon can be used to test the condition and/or to trigger an
action upon failure of the condition.  Mon keeps the testing and
action-taking tasks as separate, stand-alone programs.

Mon is very extensible.  Monitors and alerts are not a part of mon, but
the distribution comes with a handful of them to get you started. This
means that if a new service needs monitoring, or if a new alert is
required, the mon server will not need to be changed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 2
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Filter out unwanted requires
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '
        /perl(Math::TrulyRandom)/d
        /perl(Net::hostent)/d
'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
for F in CHANGES doc/README.syslog.monitor
do
        iconv -f ISO-8859-1 -t UTF-8 $F >tmp
        touch --reference $F tmp
        mv tmp $F
done

dos2unix -q -k alerts/sms/sms.alert

make %{?_smp_mflags} -C mon.d \
        CFLAGS="%{optflags} -DUSE_VENDOR_CF_PATH=1"

%install
install -d -m0755 %{buildroot}%{_bindir}             \
        %{buildroot}%{_mandir}/man{1,8}/             \
        %{buildroot}%{_libdir}/mon/{alert.d,mon.d}/  \
        %{buildroot}%{_sysconfdir}/mon/              \
        %{buildroot}%{_unitdir}                    \
        %{buildroot}%{_localstatedir}/www/cgi-bin/   \
        %{buildroot}%{_localstatedir}/lib/mon/{log.d,state.d}/

install -p -m0755 mon clients/moncmd clients/monshow clients/skymon/skymon %{buildroot}%{_bindir}
install -p -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

install -p -m0755 mon.d/*.wrap mon.d/*.monitor %{buildroot}%{_libdir}/mon/mon.d/
install -p -m0755 alert.d/* %{buildroot}%{_libdir}/mon/alert.d/
install -p -m0755 alerts/*/*.alert %{buildroot}%{_libdir}/mon/alert.d/

install -d %{buildroot}%{_sysconfdir}/mon
%{fixlib} etc/auth.cf >%{buildroot}%{_sysconfdir}/mon/auth.cf
%{fixlib} %{SOURCE3} >%{buildroot}%{_sysconfdir}/mon/mon.cf
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/mon.service
install -Dp -m0600 %{SOURCE5} %{buildroot}%{_sysconfdir}/mon/userfile

install -Dp -m0755 mon.cgi-%{moncgi_version}/mon.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/mon.cgi

# Fix permissions in examples documentation files
chmod -x mon.cgi-1.52/mon.cgi                   \
        clients/skymon/skymon                   \
        mon.cgi-1.52/util/moncgi-appsecret.pl   \
        doc/README.snmpdiskspace.monitor        \
        utils/cf-to-hosts                       \
        clients/batch-example                   \
        utils/syslog.monitor

# Fix library path in examples
%{fixlib} -i etc/*.cf

%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable mon.service > /dev/null 2>&1 || :
    /bin/systemctl stop mon.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart mon.service >/dev/null 2>&1 || :
fi

%triggerun -- mon < 1.2.0-10
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply mon
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save mon >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del mon >/dev/null 2>&1 || :
/bin/systemctl try-restart mon.service >/dev/null 2>&1 || :

%files
%license COPYING COPYRIGHT
%doc CHANGES CREDITS README TODO doc/README.*
%doc KNOWN-PROBLEMS utils/ VERSION
%doc alerts/*/*.README mon.cgi-1.52/
%doc clients/{skymon,batch-example} etc/*.cf etc/example.m4 etc/example.monshowrc
%config(noreplace) %{_sysconfdir}/mon/
%{_unitdir}/*
%{_mandir}/man?/*
%{_localstatedir}/www/cgi-bin/mon.cgi
%{_bindir}/*
%{_localstatedir}/lib/mon/
%dir %{_libdir}/mon
%{_libdir}/mon/alert.d
%dir %{_libdir}/mon/mon.d
%{_libdir}/mon/mon.d/*.monitor
%attr(2755, root, uucp) %{_libdir}/mon/mon.d/dialin.monitor.wrap

# These packages are not in EPEL
%if 0%{?rhel} <= 5
# perl(Expect)
%exclude %{_libdir}/mon/mon.d/dialin.monitor
# perl(Authen::Radius)
%exclude %{_libdir}/mon/mon.d/radius.monitor
%endif

# These are not in Fedora either
# perl(AOL::TOC)
%exclude %{_libdir}/mon/alert.d/aim.alert
# perl(Filesys::DiskSpace)
%exclude %{_libdir}/mon/mon.d/freespace.monitor

%changelog
%autochangelog
