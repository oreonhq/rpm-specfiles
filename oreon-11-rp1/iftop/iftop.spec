%global source0_hash f733eeea371a7577f8fe353d86dd88d16f5b2a2e702bd96f5ffb2c197d9b4f97

Summary:        Command line tool that displays bandwidth usage on an interface
Name:           iftop
Version:        1.0
Release:        0.38.pre4%{?dist}
# {ip,sll,tcp}.h are BSD-4-Clause-UC, rest is GPL-2.0-or-later
License:        GPL-2.0-or-later AND BSD-4-Clause-UC
URL:            http://www.ex-parrot.com/~pdw/%{name}/
Source0:        http://www.ex-parrot.com/~pdw/%{name}/download/%{name}-%{version}pre4.tar.gz
Patch0:         iftop-1.0-ncursesw.patch
Patch1:         iftop-1.0-git20181003.patch
Patch2:         iftop-1.0-gcc10.patch
Patch3:         iftop-configure-c99.patch
Patch4:         iftop-function-args.patch
BuildRequires:  gcc, make, ncurses-devel, libpcap-devel

%description
iftop does for network usage what top(1) does for CPU usage. It listens to
network traffic on a named interface and displays a table of current bandwidth
usage by pairs of hosts. Handy for answering the question "why is our ADSL link
so slow?".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}pre4
%patch -P0 -p1 -b .ncursesw
touch -c -r configure.ac{.ncursesw,}
%patch -P1 -p1 -b .git20181003
%patch -P2 -p1 -b .gcc10
%patch -P3 -p1 -b .c99
%patch -P4 -p1 -b .fargs
# Avoid re-running autoconf.
touch -r aclocal.m4 configure*

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README TODO
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.*

%changelog
%autochangelog
