# Must be kept in sync with xorg-x11-fonts !
%define _x11fontdir		%{_datadir}/X11/fonts

Summary: X.Org X11 libfontenc runtime library
Name: libfontenc
Version: 1.1.8
Release: 5%{?dist}
# SPDX
License: MIT
URL: http://www.x.org
Source0: https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: pkgconfig make
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel
BuildRequires: xorg-x11-font-utils

%description
X.Org X11 libfontenc runtime library

%package devel
Summary: X.Org X11 libfontenc development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libfontenc development package

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -Os"
%configure --disable-static --with-fontrootdir=%{_x11fontdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove all libtool archives (*.la)
find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :

%ldconfig_post
%ldconfig_postun

%files
%doc COPYING README.md ChangeLog
%{_libdir}/libfontenc.so.1
%{_libdir}/libfontenc.so.1.0.0

%files devel
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.8-5
- Prepare for Oreon 11 (RP1)
