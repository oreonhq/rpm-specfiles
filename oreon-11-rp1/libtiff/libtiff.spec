# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 672bd7d10aee4606171afb864f3570b83340f6a33e2c186dc0512f7145ffdf6a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libtiff
Version:        4.7.2
Release:        1%{?dist}
Summary:        Library of functions for manipulating TIFF format image files
License:        libtiff
URL:            https://libtiff.gitlab.io/libtiff/
Source0:        https://download.osgeo.org/libtiff/tiff-%{version}.tar.gz
Source1:        tiff-%{version}.tar.gz.sig
Source2:        gpgkey-B1FA7D81EEB8E66399178B9733EBBFC47B3DD87D.gpg

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  oreon-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
The libtiff package contains a library of functions for manipulating TIFF
(Tagged Image File Format) image format files. TIFF is a widely used file
format for bitmapped images. TIFF files usually end in the .tif extension
and they are often quite large.

%package        devel
Summary:        Development files for the libtiff library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libjpeg-turbo-devel%{?_isa}
Requires:       pkgconfig

%description    devel
This package contains the header files and shared libraries necessary for
developing programs which will manipulate TIFF format image files using the
libtiff library.

%package        tools
Summary:        Command line utilities for manipulating TIFF files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains command line programs for manipulating TIFF format
image files using the libtiff library.

%package        doc
Summary:        Documentation for the libtiff library
BuildArch:      noarch

%description    doc
This package contains the libtiff manual and the change log.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n tiff-%{version}

%build
%configure \
        --disable-static \
        --disable-rpath \
        --disable-sphinx \
        --disable-jbig \
        --disable-lerc \
        --disable-libdeflate \
        --disable-opengl \
        --disable-webp \
        --enable-cxx
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%check
%make_build check

%ldconfig_scriptlets

%files
%license LICENSE.md
%{_libdir}/libtiff.so.6*
%{_libdir}/libtiffxx.so.6*

%files devel
%{_includedir}/tiff.h
%{_includedir}/tiffconf.h
%{_includedir}/tiffio.h
%{_includedir}/tiffio.hxx
%{_includedir}/tiffvers.h
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%{_libdir}/pkgconfig/libtiff-4.pc
%{_mandir}/man3/*

%files tools
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%{_docdir}/tiff-%{version}

%changelog
%autochangelog
