# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ee5e457d4cfebe566f94b99e5e3d3cc7f5c79ddb741c2ac2ba2e456f00329644
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define         _hardened_build 1

%if 0%{?el10} || 0%{?oreon}
%bcond_with inkscape
%else
%bcond_without inkscape
%endif

Summary: DjVu viewers, encoders, and utilities
Name: djvulibre
Version: 3.5.30
Release: 1%{?dist}
License: GPL-2.0-or-later
URL: http://djvu.sourceforge.net/
Source0: http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
Patch0: djvulibre-3.5.22-cdefs.patch
Patch6: djvulibre-3.5.27-export-file.patch
Patch11: djvulibre-3.5.27-djvuport-stack-overflow.patch
Patch14: djvulibre-3.5.27-out-of-bound-write-2.patch

Requires(post): xdg-utils
Requires(preun): xdg-utils
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: chrpath
BuildRequires: hicolor-icon-theme
%if %{with inkscape}
BuildRequires: inkscape
%endif
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtiff-devel
BuildRequires: make
BuildRequires: xdg-utils

Provides: %{name}-mozplugin = %{version}
Obsoletes: %{name}-mozplugin < 3.5.24

%description
DjVu is a web-centric format and software platform for distributing documents
and images. DjVu can advantageously replace PDF, PS, TIFF, JPEG, and GIF for
distributing scanned documents, digital documents, or high-resolution pictures.
DjVu content downloads faster, displays and renders faster, looks nicer on a
screen, and consume less client resources than competing formats. DjVu images
display instantly and can be smoothly zoomed and panned with no lengthy
re-rendering.

DjVuLibre is a free (GPL'ed) implementation of DjVu, including viewers,
decoders, simple encoders, and utilities. The browser plugin is in its own
separate sub-package.

%package libs
Summary: Library files for DjVuLibre

%description libs
Library files for DjVuLibre.

%package devel
Summary: Development files for DjVuLibre
Requires: %{name}-libs = %{version}-%{release}
Requires: pkgconfig

%description devel
Development files for DjVuLibre.

%prep
%oreon_sha256
%setup -q 
%patch -P0 -p1 -b .cdefs
%patch -P6 -p1 -b .export-file
%patch -P11 -p1 -b .djvuport-stack-overflow
%patch -P14 -p1 -b .out-of-bound-write-2

%build 
%configure --with-qt=%{_libdir}/qt-3.3 --enable-threads

%make_build

%install
%make_install

find %{buildroot}%{_libdir} -name '*.so*' | xargs %{__chmod} +x

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvutoxml
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvused
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/cjb2
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/csepdjvu
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvuserve
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvm
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvuxmlparser
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvutxt
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/ddjvu
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvumake
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/cpaldjvu
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvuextract
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/c44
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvups
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvudump
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/djvmcvt
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/bzz

rm -f $RPM_BUILD_ROOT%{_datadir}/mime/packages/djvulibre-mime.xml

pushd desktopfiles
for i in 22 32 48 64 ; do
    install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/
    cp -a ./prebuilt-hi${i}-djvu.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/image-vnd.djvu.mime.png
done
popd

%post
rm -f %{_datadir}/applications/djvulibre-djview3.desktop || :
rm -f %{_datadir}/icons/hicolor/32x32/apps/djvulibre-djview3.png || :

%preun
if [ $1 -eq 0 ]; then
    %{_datadir}/djvu/osi/desktop/register-djvu-mime uninstall || :
fi

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/djvu/
%{_datadir}/icons/hicolor/16x16/mimetypes/*
%{_datadir}/icons/hicolor/20x20/mimetypes/*
%{_datadir}/icons/hicolor/22x22/mimetypes/*
%{_datadir}/icons/hicolor/24x24/mimetypes/*
%{_datadir}/icons/hicolor/32x32/mimetypes/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/64x64/mimetypes/*
%{_datadir}/icons/hicolor/72x72/mimetypes/*
%{_datadir}/icons/hicolor/96x96/mimetypes/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%{_datadir}/icons/hicolor/256x256/mimetypes/*

%files libs
%license COPYING
%doc README COPYRIGHT NEWS
%{_libdir}/libdjvulibre.so.21*

%files devel
%doc doc/
%{_includedir}/libdjvu/
%{_libdir}/pkgconfig/ddjvuapi.pc
%{_libdir}/libdjvulibre.so

%changelog
%autochangelog
