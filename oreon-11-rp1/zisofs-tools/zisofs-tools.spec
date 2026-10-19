%global source0_hash ae4e53e4914934d41660248fb59d3c8761f1f1fd180d5ec993c17ddb3afd04f3
Summary:        Utilities for creating compressed CD-ROM filesystems
Name: zisofs-tools
Version: 1.0.8
Release:        1%{?dist}
License: GPL-1.0-or-later
URL: http://www.kernel.org/pub/linux/utils/fs/zisofs/
Source0:        http://mirror.linux.org.au/linux/utils/fs/zisofs/zisofs-tools-%{version}.tar.bz2
Patch0: zisofs-tools-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
A utility which works in combination with an appropriately patched
version of mkisofs to allow the creation of compressed CD-ROM
filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make  %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install INSTALLROOT="$RPM_BUILD_ROOT"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
