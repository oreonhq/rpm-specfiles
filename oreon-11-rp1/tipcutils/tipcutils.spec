%global source0_hash 76fba32a3fbc81fc2285e54154a06e79e2173c43aaa47d5eb3a1e572a0de7add

Name:       tipcutils
Version:    3.0.6
Release:    4%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://tipc.sourceforge.net/
Summary:    TIPC utilities package for Linux
Source0:    http://downloads.sourceforge.net/project/tipc/%{name}-%{version}.tgz

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libdaemon-devel
BuildRequires: libmnl-devel

%description
Tipcutils contains a variety of utility programs for use with Linux TIPC,
including:

1) TIPC pipe: A netcat like program for tipc.

2) tipclog: A simple userspace network event logger running as daemon that
logs link and node availability status.

3) tipc-link-watcher: A daemon keeping track of the status of TIPC nodes and
links in a cluster by using the topology service

4) net_topology_tracker: A daemon using the toplogy service to keep track of
the status of the overall cluster connectivity.  It connects to the topolgy
servers of all detected peer nodes, ans subscribes for their network view.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
head -n34 include/tipcc.h | tail -n25 | sed -e 's/ \* //g' -e 's/\*//g' > LICENSE

# undefined UIO_MAXIOV in iovec_client.c => skip it
sed -ie 's/ iovec / /g' test/Makefile.am

# tipc-trace needs Python2 => skip it
sed -ie 's/ tipc-trace//g' utils/Makefile.am

%build
./bootstrap
LDFLAGS="-fPIE" \
	%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_sbindir}/tipclog
%{_sbindir}/tipc-link-watcher
%{_bindir}/tipc-pipe
%{_mandir}/man1/tipc-pipe.1.gz
%doc LICENSE README

%check
make check

%changelog
%autochangelog
