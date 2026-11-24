# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ff9aa641af180a59acedc7fc9e663543fb397ff758b5122093158fd628125ac1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{!?ruby_vendorlibdir: %global ruby_vendorlibdir %(ruby -r rbconfig -e 'print RbConfig::CONFIG["vendorlibdir"]')}
%{!?ruby_vendorarchdir: %global ruby_vendorarchdir %(ruby -r rbconfig -e 'print RbConfig::CONFIG["vendorarchdir"]')}

%if 0%{?el9}
%bcond_with    gl
%else
%bcond_without gl
%endif

%if 0%{?fedora} >= 40 || 0%{?rhel} > 9
%bcond_with    ruby
%else
%bcond_without ruby
%endif

%define beta beta20

Summary: Library for Colour AsCii Art, text mode graphics
Name: libcaca
Version: 0.99
Release: 0.86.%{beta}%{?dist}
License: WTFPL
URL: http://caca.zoy.org/wiki/libcaca

Source0: https://github.com/cacalabs/libcaca/releases/download/v%{version}.%{beta}/%{name}-%{version}.%{beta}.tar.bz2
Patch0: libcaca-0.99.beta16-multilib.patch
Patch1: libcaca-0.99.beta20-c99.patch
Patch2: libcaca-0.99.beta20-CVE-2022-0856.patch
Patch3: libcaca-0.99.beta20-CVE-2026-42046.patch
Patch4: libcaca-0.99.beta20-CVE-2026-42046_followup.patch

Buildrequires: doxygen
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: slang-devel
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig(imlib2)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%if %{with ruby}
BuildRequires: ruby
BuildRequires: ruby-devel
%endif
Buildrequires: texlive-dvips
Buildrequires: texlive-latex
%if %{with gl}
BuildRequires: freeglut-devel
BuildRequires: mesa-libGLU-devel
%endif

%description
libcaca is the Colour AsCii Art library. It provides high level functions for
color text drawing, simple primitives for line, polygon and ellipse drawing, as
well as powerful image to text conversion routines.

%package devel
Summary: Development files for libcaca, the library for Colour AsCii Art
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libcaca is the Colour AsCii Art library. It provides high level functions for
color text drawing, simple primitives for line, polygon and ellipse drawing, as
well as powerful image to text conversion routines.

This package contains the header files needed to compile applications or shared
objects that use libcaca.

%package -n caca-utils
Summary: Colour AsCii Art Text mode graphics utilities based on libcaca
Requires: toilet

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca, the
Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image formats
such as JPEG, PNG, GIF etc. and renders them on the terminal using ASCII art.
The user can zoom and scroll the image, set the dithering method or enable
anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII metaballs on the
screen, cacafire is a port of AALib's aafire and displays burning ASCII art
flames, and cacademo is a simple application that shows the libcaca rendering
features such as line and ellipses drawing, triangle filling and sprite
blitting.

%package -n python3-caca
Summary: Python bindings for libcaca

%description -n python3-caca
This package contains the python bindings for using libcaca from python.

%if %{with ruby}
%package -n ruby-caca
Summary: Ruby bindings for libcaca
Requires: ruby(release)
Provides: ruby(caca) = %{version}-%{release}

%description -n ruby-caca
This package contains the ruby bindings for using libcaca from ruby.
%endif

%prep
%oreon_sha256
%autosetup -p1 -n libcaca-%{version}.%{beta}

for file in python/examples/*.py; do
  sed -e 's|/usr/bin/env python$|%{__python3}|g' ${file} > ${file}.tmp
  touch -r ${file} ${file}.tmp
  mv -f ${file}.tmp ${file}
done

%build
%define _lto_cflags -flto=auto -ffat-lto-objects

export LDFLAGS="$(pkg-config --libs gio-2.0) $LDFLAGS"

sed -i -e 's/sitearchdir/vendorarchdir/g' -e 's/sitelibdir/vendorlibdir/g' configure

%configure \
  --disable-static \
  --disable-csharp \
  --disable-java

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

mv %{buildroot}%{_docdir}/libcaca-dev libcaca-dev-docs

%{?ldconfig_scriptlets}

%files
%license COPYING
%{_libdir}/*.so.0*

%files devel
%doc libcaca-dev-docs/html/
%{_bindir}/caca-config
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_mandir}/man1/caca-config.1*
%{_mandir}/man3/*

%files -n caca-utils
%license COPYING*
%doc AUTHORS NEWS NOTES README THANKS
%{_bindir}/cacaclock
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaplay
%{_bindir}/cacaserver
%{_bindir}/cacaview
%{_bindir}/img2txt
%{_datadir}/libcaca/
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaplay.1*
%{_mandir}/man1/cacaserver.1*
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2txt.1*

%files -n python3-caca
%doc python/examples
%{python3_sitelib}/caca/

%if %{with ruby}
%files -n ruby-caca
%doc ruby/README
%{ruby_vendorlibdir}/caca.rb
%{ruby_vendorarchdir}/caca.so
%endif

%changelog
%autochangelog
