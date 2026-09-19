%global source0_hash c114e625b87fb06585484eb9f3ff868de165b3e61926fee55479d1bd3de09b99

Summary: A tool for gathering and displaying system information
Name: procinfo
Version: 18
Release: 60%{dist}
License: GPL-1.0-or-later
Source: ftp://ftp.cistron.nl/pub/people/00-OLD/svm/%{name}-%{version}.tar.gz
Patch0: procinfo-14-misc.patch
Patch3: procinfo-17-mandir.patch
Patch5: procinfo-17-uptime.patch
Patch6: procinfo-17-lsdev.patch
Patch7: procinfo-18-acct.patch
Patch8: procinfo-18-mharris-use-sysconf.patch
Patch9: procinfo-18-maxdev.patch
Patch10: procinfo-18-ranges.patch
Patch11: procinfo-18-cpu-steal.patch
Patch12: procinfo-18-intr.patch
Patch13: procinfo-18-intrprint.patch
Patch14: procinfo-18-version.patch
Patch15: procinfo-18-man-comment.patch
Patch16: procinfo-18-socklist.patch
Patch17: procinfo-18-idle-overflow.patch
Patch18: procinfo-strsignal.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: ncurses-devel

%description
The procinfo command gets system data from the /proc directory (the
kernel filesystem), formats it and displays it on standard output.
You can use procinfo to acquire information about your system from the
kernel as it is running.

Install procinfo if you'd like to use it to gather and display system
data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .misc
%patch -P3 -p1 -b .mandir
%patch -P5 -p1 -b .uptime
%patch -P6 -p1 -b .lsdev
%patch -P7 -p1 -b .acct
%patch -P8 -p1 -b .mharris-use-sysconf
%patch -P9 -p1 -b .maxdev
%patch -P10 -p1 -b .ranges
%patch -P11 -p1 -b .steal
%patch -P12 -p1 -b .intr
%patch -P13 -p1 -b .intrprint
%patch -P14 -p1 -b .version
%patch -P15 -p1 -b .mancomment
%patch -P16 -p0 -b .socklist
%patch -P17 -p1 -b .idle
%patch -P18 -p1 -b .strsignal

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS= LDLIBS=-lncurses

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
make install prefix=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/%{_mandir}

%files
%doc README CHANGES
%{_bindir}/procinfo
%{_bindir}/lsdev
%{_bindir}/socklist
%{_mandir}/man8/procinfo.8*
%{_mandir}/man8/lsdev.8*
%{_mandir}/man8/socklist.8*

%changelog
%autochangelog
