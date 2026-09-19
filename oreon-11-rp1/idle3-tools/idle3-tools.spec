%global source0_hash 9778060c7873ad2c9c40db3a7049d8ca22535427b982ff12f5bd519f703f2a02

Name:           idle3-tools
Version:        0.9.1
Release:        24%{?dist}
Summary:        Manipulate the value of the idle3 timer found on recent WD Hard Disk Drives
License:        GPLv3
URL:            http://idle3-tools.sourceforge.net/
Source0:        http://sourceforge.net/projects/idle3-tools/files/%{name}-%{version}.tgz
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires: make

%description
Idle3-tools provides a linux/unix utility that can disable, get and set the
value of the infamous idle3 timer found on recent Western Digital Hard Disk
Drives.  It can be used as an alternative to the official wdidle3.exe
proprietary utility, without the need to reboot in a DOS environement.  A power
off/on cycle of the drive will still be mandatory for new settings to be taken
into account.

Idle3-tools is an independant project, unrelated in any way to Western Digital Corp.
WARNING: THIS SOFTWARE IS EXPERIMENTAL AND NOT WELL TESTED. IT ACCESSES LOW
LEVEL INFORMATION OF YOUR HARDDRIVE. USE AT YOUR OWN RISK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
CFLAGS="${RPM_OPT_FLAGS}" make %{?_smp_mflags} \
    LDFLAGS="${RPM_LD_FLAGS}" STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
%make_install binprefix=/usr

%files
%doc COPYING
%{_sbindir}/idle3ctl
%{_mandir}/man8/idle3ctl*

%changelog
%autochangelog
