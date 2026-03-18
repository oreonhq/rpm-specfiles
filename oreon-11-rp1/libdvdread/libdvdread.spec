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
