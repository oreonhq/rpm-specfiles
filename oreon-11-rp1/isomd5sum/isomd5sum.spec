%global forgeurl https://github.com/rhinstaller/isomd5sum

Summary: Utilities for working with md5sum implanted in ISO images
Name:    isomd5sum
Version: 1.2.5
Release: 6%{?dist}
Epoch: 1
License: GPL-2.0-or-later

%global tag %{version}
%forgemeta
Url:     %{forgeurl}
Source0:        https://github.com/rhinstaller/isomd5sum/archive/1.2.5/isomd5sum-1.2.5.tar.gz
# oreon url source checksums begin
%global source0_sha256 b4ffe78a8277b28f7c4528989c55af3eec87d48245f362229c213c704b8c2b97
%global source0_file isomd5sum-1.2.5.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: popt-devel
BuildRequires: python3-devel
BuildRequires: make

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/isomd5sum-1.2.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b4ffe78a8277b28f7c4528989c55af3eec87d48245f362229c213c704b8c2b97" || { echo "oreon: Source0 SHA256 mismatch for isomd5sum-1.2.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%forgeautosetup


%build
CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"; export CFLAGS
LDFLAGS="$RPM_LD_FLAGS"; export LDFLAGS

PYTHON=%{__python3} make checkisomd5 implantisomd5 pyisomd5sum.so

%install

PYTHON=%{__python3} make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel install-python

%files
%license COPYING
%{_bindir}/implantisomd5
%{_bindir}/checkisomd5
%{_mandir}/man*/*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
/usr/share/pkgconfig/isomd5sum.pc

%files -n python3-isomd5sum
%{python3_sitearch}/pyisomd5sum.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.5-6
- Prepare for Oreon 11 (RP1)
