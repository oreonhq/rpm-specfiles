%global source0_hash 8599063b7c398f9cfef7a9ec699659b25b1c14d2bc0f535aed05ce32b7d9f507

Summary: Interface statistics
Name: ifstat
Version: 1.1
Release: 50%{?dist}
License: GPL-2.0-or-later
URL: http://gael.roualland.free.fr/ifstat/
Source0: http://gael.roualland.free.fr/ifstat/ifstat-%{version}.tar.gz
Patch0: ifstat-destdir.patch
Patch1: ifstat-UTF8.patch
Patch2: ifstat-configure-snmp-c99.patch
BuildRequires: pkgconfig(netsnmp)
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf

%description
ifstat(1) is a little tool to report interface activity like vmstat/iostat do.
In addition, ifstat can poll remote hosts through SNMP if you have the ucd-snmp
library. It will also be used for localhost if no other known method works (You
need to have snmpd running for this though).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
autoconf
%configure --enable-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/ifstat %{buildroot}%{_bindir}/ifstat-ifstat
mv %{buildroot}%{_mandir}/man1/ifstat.1 %{buildroot}%{_mandir}/man1/ifstat-ifstat.1

%files
%doc COPYING HISTORY README TODO
%{_mandir}/man1/ifstat-ifstat.1*
%{_bindir}/ifstat-ifstat

%changelog
%autochangelog
