%global source0_hash none

Name: fxload
Version: 2008_10_13
Release: 34%{?dist}
Summary: A helper program to download firmware into FX and FX2 EZ-USB devices

License: GPL-2.0-or-later
URL: http://linux-hotplug.sourceforge.net/
Source0: https://downloads.sourceforge.net/project/linux-hotplug/fxload/%{version}/fxload-%{version}.tar.gz
# This file contains code that is copyright Cypress Semiconductor Inc,
# and cannot be distributed. Therefore we use this script to remove the
# copyright code before shipping it. Download the upstream tarball and
# invoke this script while in the tarball's directory:
# ./fxload-generate-tarball.sh 2008_10_13
Source1: fxload-generate-tarball.sh
Patch0: fxload-noa3load.patch
Patch1: fxload-ldflags.patch

BuildRequires: curl
BuildRequires: gcc kernel-headers make
Requires: udev
Conflicts: hotplug-gtk hotplug

%description
This program is conveniently able to download firmware into FX and FX2
EZ-USB devices, as well as the original AnchorChips EZ-USB.  It is
intended to be invoked by udev scripts when the unprogrammed device
appears on the bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{SOURCE1} %{version} %{_sourcedir}
cd %{builddir}
tar -xf %{_sourcedir}/fxload-%{version}-noa3load.tar.gz
cd fxload-%{version}
%patch -P0 -p1 -b .fxload-noa3load
%patch -P1 -p1 -b .ldflags

%build
%{make_build} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS -pie"

%install
install -m 755 -Dt %{buildroot}%{_sbindir}/ fxload
install -m 644 -Dt %{buildroot}%{_mandir}/man8/ fxload.8

%files
%doc COPYING
%doc README.txt
%{_sbindir}/fxload
%{_mandir}/man8/fxload.8*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2008_10_13-34
- Import
