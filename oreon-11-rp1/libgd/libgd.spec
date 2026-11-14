# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3fe822ece20796060af63b7c60acb151e5844204d289da0ce08f8fdf131e5a61

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libgd
Version: 2.3.3
Release: 1%{?dist}
Summary: Graphics drawing library
License: GD
URL: https://libgd.github.io/
Source0: https://github.com/libgd/libgd/releases/download/gd-%{version}/libgd-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
%if %{without bootstrap}
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
%endif
BuildRequires: pkgconfig(zlib)

Provides: gd = %{version}-%{release}
Provides: pkgconfig(libgd) = %{version}
Provides: pkgconfig(gdlib) = %{version}

%description
GD is a graphics library for creating and manipulating raster images in
PNG, JPEG, GIF and other formats.

%package -n gd-devel
Summary: Development files for GD
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n gd-devel
Headers and development files for applications using GD.

%if %{without bootstrap}
%package -n gd-tools
Summary: Command-line tools for GD images
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n gd-tools
Command-line tools for creating and converting images with GD.
%endif

%prep
%oreon_sha256
%autosetup

%build
%if %{without bootstrap}
%configure --disable-static
%else
%configure \
  --disable-fontconfig \
  --disable-freetype \
  --disable-jpeg \
  --disable-png \
  --disable-static
%endif
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
%if %{with bootstrap}
rm -f %{buildroot}%{_bindir}/*
%endif

%check
TMPDIR=%{_builddir} %make_build check

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/libgd.so.3*

%files -n gd-devel
%{_includedir}/gd.h
%{_includedir}/gd_color_map.h
%{_includedir}/gd_errors.h
%{_includedir}/gd_io.h
%{_includedir}/gdcache.h
%{_includedir}/gdfontg.h
%{_includedir}/gdfontl.h
%{_includedir}/gdfontmb.h
%{_includedir}/gdfonts.h
%{_includedir}/gdfontt.h
%{_includedir}/gdfx.h
%{_includedir}/gdpp.h
%{_libdir}/libgd.so
%{_libdir}/pkgconfig/gdlib.pc

%if %{without bootstrap}
%files -n gd-tools
%{_bindir}/annotate
%{_bindir}/bdftogd
%{_bindir}/gd2copypal
%{_bindir}/gd2togif
%{_bindir}/gd2topng
%{_bindir}/gdcmpgif
%{_bindir}/gdparttopng
%{_bindir}/gdtopng
%{_bindir}/giftogd2
%{_bindir}/pngtogd
%{_bindir}/pngtogd2
%{_bindir}/webpng
%endif

%changelog
%autochangelog
