%global source0_hash 7ad043c8cbb02743b5066822bd2aa1b3313d2675d235edea1db287e7138611ec

Name:		rootsh
Summary: 	Shell wrapper for auditing
Version:	1.5.3
Release:	38%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
Source0:	http://download.sourceforge.net/rootsh/%{name}-%{version}.tar.gz
# Bug filed upstream 
# http://sourceforge.net/tracker/index.php?func=detail&aid=1964114&group_id=110309&atid=656399
Patch0:		rootsh-1.5.3-open-needs-3-args.patch
Patch1:		rootsh-configure-c99.patch
URL:		http://sourceforge.net/projects/rootsh

BuildRequires: make
BuildRequires:  gcc
%description
Rootsh is a wrapper for shells which logs all echoed keystrokes and 
terminal output to a file and/or to syslog. Its main purpose is the 
auditing of users who need a shell with root privileges. They start 
rootsh through the sudo mechanism.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
make %{?smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/var/log/rootsh

%files
%doc README AUTHORS ChangeLog THANKS INSTALL COPYING
%{_bindir}/rootsh
%{_mandir}/man1/rootsh.1.gz
%attr(700, root, root) /var/log/rootsh/

%changelog
%autochangelog
