%global source0_hash 67bea6fbc3a42a535a0230c9e891e5ddfb4d9d39422d46565a2990d1ace15216

# The testsuite is unsuitable for running on buildsystems
%global tests_enabled 0

Summary: System and process monitoring utilities
Name: procps-ng
Version: 4.0.6
Release: 1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://sourceforge.net/projects/procps-ng/

Source0:        https://downloads.sourceforge.net/procps-ng/procps-ng-4.0.6.tar.xz

BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: systemd-devel
BuildRequires: git
BuildRequires: po4a

%if %{tests_enabled}
BuildRequires: dejagnu
%endif

Provides: procps = %{version}-%{release}
Obsoletes: procps < 4.0.1-1

# usrmove hack - will be removed once initscripts are fixed
Provides: /sbin/sysctl
Provides: /bin/ps

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/sysctl
%endif

%description
The procps package contains a set of system utilities that provide
system information. Procps includes ps, free, skill, pkill, pgrep,
snice, tload, top, uptime, vmstat, pidof, pmap, slabtop, w, watch,
pwdx and pidwait.
The ps command displays a snapshot of running processes. The top command
provides a repetitive update of the statuses of running processes.
The free command displays the amounts of free and used memory on your
system. The skill command sends a terminate command (or another
specified signal) to a specified set of processes. The snice
command is used to change the scheduling priority of specified
processes. The tload command prints a graph of the current system
load average to a specified tty. The uptime command displays the
current time, how long the system has been running, how many users
are logged on, and system load averages for the past one, five,
and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they are running. The watch
program watches a running program. The vmstat command displays
virtual memory statistics about processes, memory, paging, block
I/O, traps, and CPU activity. The pwdx command reports the current
working directory of a process or processes. The pidwait command
waits for processes of specified names.

%package devel
Summary:  System and process monitoring utilities
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: procps-devel = %{version}-%{release}
Obsoletes: procps-devel < 3.3.17-8

%description devel
System and process monitoring utilities development headers

%package i18n
Summary:  Internationalization pack for procps-ng
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

# fortunately the same release number for f21 and f22
Conflicts: man-pages-de < 1.7-3
Conflicts: man-pages-fr < 3.66-3
Conflicts: man-pages-pl < 0.7-5

%description i18n
Internationalization pack for procps-ng

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

%build
# The following stuff is needed for git archives only
#echo "%%{version}" > .tarball-version
#./autogen.sh

autoreconf --verbose --force --install

%configure \
           --exec-prefix=/ \
           --disable-static \
           --disable-w-from \
           --disable-kill \
           --enable-watch8bit \
           --enable-skill \
           --enable-sigwinch \
           --enable-libselinux \
           --with-systemd \
           --disable-modern-top\
           --enable-pidwait

make CFLAGS="%{optflags}"


%if %{tests_enabled}
%check
make check
%endif


%install
%make_install

# these are created by make, yet empty. This causes rpmbuild errors.
rm -rf %{buildroot}%{_mandir}/{pl,fr,pt_BR}/man5
rm -rf %{buildroot}%{_mandir}/{fr,de,pt_BR,pl,zh_CN}/man3
# kill is delivered with util-linux pkg along with i18n manpage
rm -rf %{buildroot}%{_mandir}/{fr,de,pt_BR,ro,sv,uk}/man1/kill.1


%find_lang %{name} --all-name --with-man

%if "%{_sbindir}" != "%{_bindir}"
ln -s %{_bindir}/pidof %{buildroot}%{_sbindir}/pidof
%endif

%ldconfig_scriptlets

%files
%doc AUTHORS bugs.md FAQ NEWS README.md
%license COPYING COPYING.LIB
%{_libdir}/libproc2.so.1{,.*}
%{_bindir}/*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/pidof
%{_sbindir}/sysctl
%endif
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_mandir}/man5/*

%exclude %{_pkgdocdir}/libproc.supp

%files devel
%license COPYING COPYING.LIB
%{_libdir}/libproc2.so
%{_libdir}/pkgconfig/libproc2.pc
%{_includedir}/libproc2
%{_mandir}/man3/*

%files i18n -f %{name}.lang

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.6-1
- Prepare for Oreon 11 (RP1)
