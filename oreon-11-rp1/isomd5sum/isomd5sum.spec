%global source0_hash b4ffe78a8277b28f7c4528989c55af3eec87d48245f362229c213c704b8c2b97
%global forgeurl https://github.com/rhinstaller/isomd5sum
Summary:        Utilities for working with md5sum implanted in ISO images
Name:    isomd5sum
Version: 1.2.5
Release:        1%{?dist}
Epoch: 1
License: GPL-2.0-or-later
%global tag %{version}
%forgemeta
Url:     %{forgeurl}
Source0:        https://github.com/rhinstaller/isomd5sum/archive/refs/tags/1.2.5.tar.gz#/isomd5sum-1.2.5.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary: Development headers and library for using isomd5sum 
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}-static = %{epoch}:%{version}-%{release}
%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%package -n python3-isomd5sum
Summary: Python bindings for isomd5sum
%description -n python3-isomd5sum
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgeautosetup

%build

CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"; export CFLAGS
LDFLAGS="$RPM_LD_FLAGS"; export LDFLAGS
PYTHON=%{__python3} make checkisomd5 implantisomd5 pyisomd5sum.so
%install
PYTHON=%{__python3} make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel install-python
%oreon_autofiles python3-isomd5sum usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n isomd5sum-devel -f %{oreon_filedir}/isomd5sum-devel.list
%files -n python3-isomd5sum -f %{oreon_filedir}/python3-isomd5sum.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-6
- Prepare for Oreon 11 (RP1)
