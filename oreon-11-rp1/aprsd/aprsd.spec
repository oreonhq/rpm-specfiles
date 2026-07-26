%global source0_hash 9aa7f89782d2df24fe6e3143f24c3eabfbe77d70526898e48c0057bd447cb1bd

%define uprel 15
Name: aprsd
Summary: Internet gateway and client access to amateur radio APRS packet data
Version: 2.2.5
Release: %{uprel}.6%{?dist}.41
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}-%{uprel}.tar.gz
Source1: aprsd.conf
Source2: aprsd.service
Source3: INIT.TNC
Source4: user.deny
Source5: welcome.txt
Source6: RESTORE.TNC
Source7: aprsd.logrotate
Patch0: aprsd-2.2.5-15-compile.patch
Patch1: aprsd-2.2.5-15-gcc43-port.patch
Patch2: aprsd-2.2.5-15-sysconfdir.patch
Patch3: aprsd-configure-c99.patch
URL: http://sourceforge.net/projects/aprsd/
BuildRequires:  gcc-c++
BuildRequires: libax25-devel
BuildRequires: systemd-units
BuildRequires: make
BuildRequires: libxcrypt-devel
#Requires (preun): /sbin/chkconfig
#Requires (preun): /sbin/service
#Requires (post): /sbin/chkconfig
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
APRSd is an APRS server program that uses amateur radio and internet
services to convey GPS mapping, weather, and positional data.
It has been developed by and for amateur radio enthusiasts to provide
real-time data in an easy to use package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{uprel}
%patch -P0 -p1 -b compile
%patch -P1 -p1 -b gccport
%patch -P2 -p1 -b sysconfdir
%patch -P3 -p1 -b configure-c99

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}" INSTALL="install -p"
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_sysconfdir}/aprsd
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/aprsd/aprsd.conf
install -m 755 %{SOURCE2} %{buildroot}%{_unitdir}/aprsd.service
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/aprsd/INIT.TNC
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/aprsd/user.deny
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/aprsd/welcome.txt
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/aprsd/RESTORE.TNC
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/logrotate.d/aprsd
mkdir -p %{buildroot}%{_localstatedir}
mkdir -p %{buildroot}%{_localstatedir}/log/aprsd

%post
#/sbin/chkconfig --add aprsd
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
#if [ $1 = 0 ]; then
# /sbin/service aprsd stop > /dev/null 2>&1
# /sbin/chkconfig --del aprsd
#fi
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable aprsd.service > /dev/null 2>&1 || :
    /bin/systemctl stop aprsd.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart aprsd.service >/dev/null 2>&1 || :
fi

%triggerun -- aprsd < 2.2.5-15.6.3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply aprsd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save aprsd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del aprsd >/dev/null 2>&1 || :
/bin/systemctl try-restart aprsd.service >/dev/null 2>&1 || :

%files
%{_bindir}/aprsd
%{_bindir}/aprspass
%{_unitdir}/aprsd.service
%dir %{_sysconfdir}/aprsd
%dir %{_localstatedir}/log/aprsd
%config(noreplace) %{_sysconfdir}/aprsd/*
%config(noreplace) %{_sysconfdir}/logrotate.d/aprsd
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc README
%doc doc/aprsddoc.html
%doc doc/ports.html
%doc doc/q.html
%doc doc/qalgorithm.html

%changelog
%autochangelog
