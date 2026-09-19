%global source0_hash bfbf8e2dc381954ede81f871f88002fa68869a8990a780f50dfb3992775b236a

Summary: An NFS traffic monitoring tool
Name: nfswatch
Version: 4.99.14
Release: 3%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://nfswatch.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc libpcap-devel ncurses-devel libtirpc-devel

%description
Nfswatch is a command-line tool for monitoring NFS traffic.
Nfswatch can capture and analyze the NFS packets on a particular
network interface or on all interfaces.

Install nfswatch if you need a program to monitor NFS traffic.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
make STRIP= MANSUF=8 DESTDIR=${RPM_BUILD_ROOT} BINDIR=%{_sbindir} install

%files
%doc	LICENSE README
%{_sbindir}/nfswatch
%{_sbindir}/nfslogsum
%{_mandir}/man8/*

%changelog
%autochangelog
