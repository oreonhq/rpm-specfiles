%global abi 8

Name:           libdvdread
Version:        7.0.1
Release:        1%{?dist}
Summary:        A library for reading DVD video discs based on Ogle code
# msvc/contrib/dirent/dirent.c is HPND-Kevlin-Henney, but is not included in the build
# src/logger.c and few other are LGPL-2.1-or-later
# part of src/md5.c is LicenseRef-Fedora-Public-Domain
# src/dvdread/nav_types.h and src/nav_print.c are GPL-2.0 or GPL-3.0 (no later versions)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Fedora-Public-Domain
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz
Source1:        https://download.videolan.org/pub/videolan/libdvdread/%{version}/libdvdread-%{version}.tar.xz.asc
Source2:        https://download.videolan.org/pub/keys/7180713BE58D1ADC.asc
# oreon url source checksums begin
%global source0_sha256 2e3e04a305c15c3963aa03ae1b9a83c1d239880003fcf3dde986d3943355d407
%global source0_file libdvdread-7.0.1.tar.xz
# oreon url source checksums end

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
Provides:       bundled(md5-gcc)

%description
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

%package        devel
Summary:        Development files for libdvdread
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.

This package contains development files for libdvdread.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libdvdread-7.0.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2e3e04a305c15c3963aa03ae1b9a83c1d239880003fcf3dde986d3943355d407" || { echo "oreon: Source0 SHA256 mismatch for libdvdread-7.0.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

%build
%meson \
  -Ddefault_library=shared \
  -Denable_docs=true \
  -Dlibdvdcss=disabled
%meson_build

%install
%meson_install
mv %{buildroot}%{_pkgdocdir}/ docdir/


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libdvdread.so.%{abi}*

%files devel
%doc docdir/*
%{_includedir}/dvdread
%{_libdir}/libdvdread.so
%{_libdir}/pkgconfig/dvdread.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.1-1
- Prepare for Oreon 11 (RP1)
