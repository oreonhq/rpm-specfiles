%global source0_hash c1a552b6ff48ea3e4e10110a7c188861abc4750befc67c6caaba8eb3ecf67f46

Name:           bwm-ng
Version:        0.6.3
Release:        8%{?dist}
Summary:        Bandwidth Monitor NG
License:        GPL-2.0-or-later
URL:            https://github.com/vgropp/bwm-ng
Source0:        https://github.com/vgropp/%{name}/archive/v%{version}.tar.gz
Source1:        bwm-ng.conf
Patch0:         0001-fix-format-not-a-string-literal.patch
Patch1:         0002-fix-use-after-free-in-proc_diskstats-on-error.patch
Patch2:         0003-fix-missing-device-number-in-fbsd-devstat-input.patch
Patch3:         0004-fix-multiple-fflush-might-miss-some-branch-and-html-.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  make
Requires:       hostname
Requires:       procps

%description
A small and simple console-based live network and disk io bandwidth monitor.

Features:
- Supports /proc/net/dev, netstat, getifaddr, sysctl, kstat, /proc/diskstats 
/proc/partitions, IOKit, devstat and libstatgrab
- Unlimited number of interfaces/devices supported
- Interfaces/devices are added or removed dynamically from list
- White-/blacklist of interfaces/devices
- Output of KB/s, Kb/s, packets, errors, average, max and total sum
- Output in curses, plain console, CSV or HTML
- Configfile

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
./autogen.sh
%configure --enable-64bit \
           --enable-netstatbyte \
           --enable-netstatlink \
           --with-ncurses \
           --with-time \
           --with-getopt_long \
           --with-getifaddrs \
           --with-sysctl \
           --with-procnetdev \
           --with-netstatlinux \
           --without-strip
make %{?_smp_mflags}

%install
install -pDm755 src/bwm-ng %{buildroot}%{_bindir}/bwm-ng
install -pDm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bwm-ng.conf
install -pDm644 bwm-ng.1 %{buildroot}%{_mandir}/man1/bwm-ng.1

%files
%doc AUTHORS README ChangeLog bwm-ng.conf-example bwm-ng.css
%config(noreplace) %{_sysconfdir}/bwm-ng.conf
%{_bindir}/bwm-ng
%{_mandir}/man1/bwm-ng.1*

%changelog
%autochangelog
