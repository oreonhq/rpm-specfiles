%global source0_hash 40cf3bd506852942aa98f468c90ed4ea66dbd343b93efacd40d617b55caf3967

Summary: A tool which displays the status of serial port modem lines
Name: statserial
Version: 1.1
Release: 74%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: ftp://metalab.unc.edu/pub/Linux/system/serial/
Source: ftp://metalab.unc.edu/pub/Linux/system/serial/statserial-1.1.tar.gz
Patch0: statserial-1.1-config.patch
Patch1: statserial-1.1-dev.patch
Patch2: statserial-1.1--n.patch
Patch3: statserial-1.1-loop-fix.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel
ExcludeArch: s390 s390x

%description
The statserial utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines.  Statserial is useful for debugging serial port
and/or modem problems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .config
%patch -P1 -p1 -b .dev
%patch -P2 -p1 -b .-n
%patch -P3 -p1 -b .loop-fix

%build
make LDFLAGS= CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

install -m 755 statserial ${RPM_BUILD_ROOT}%{_bindir}/statserial
install -m 644 statserial.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/statserial.1

%files
%doc COPYING
%doc phone_log
%{_bindir}/statserial
%{_mandir}/man1/*

%changelog
%autochangelog
